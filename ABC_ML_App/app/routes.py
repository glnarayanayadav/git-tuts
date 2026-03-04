from flask import Blueprint, render_template_string, current_app, request, jsonify
import statistics
import os
from . import ml

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    # Minimal index page for scaffold
    html = '''
    <h1>ABC Company — ML App</h1>
    <p>Welcome to the scaffolded Flask app. Next: implement auth, upload, ML APIs.</p>
    '''
    return render_template_string(html)


@main_bp.route('/health')
def health():
    """Simple healthcheck endpoint."""
    return jsonify(status='ok')


@main_bp.route('/predict', methods=['POST'])
def predict():
    """Simple test prediction endpoint.

    Expects JSON body: {"features": [num, ...]}
    Returns the mean and sum as a placeholder "prediction".
    """
    # Use a trained model saved in the instance folder if available.
    model_path = os.path.join(current_app.instance_path, 'model.joblib')
    if not os.path.exists(model_path):
        return jsonify(error='Model not found. Train the model via /train first.'), 400

    if not request.is_json:
        return jsonify(error='Expected JSON'), 400
    data = request.get_json()
    features = data.get('features')
    if features is None:
        return jsonify(error='`features` field required'), 400

    # Accept single sample [a,b,c] or multiple samples [[a,b,c], ...]
    try:
        if all(not isinstance(x, (list, tuple)) for x in features):
            X = [[float(x) for x in features]]
        else:
            X = [[float(v) for v in row] for row in features]
    except Exception:
        return jsonify(error='All features must be numeric and shaped correctly'), 400

    try:
        model = ml.load_model(model_path)
    except FileNotFoundError:
        return jsonify(error='Model file missing'), 500

    preds = ml.predict_with_model(model, X)
    return jsonify(predictions=preds, n=len(preds))


@main_bp.route('/train', methods=['POST'])
def train():
    """Train a simple LinearRegression model.

    Expects JSON: {"X": [[...], ...], "y": [...]} . If omitted, trains on a
    small synthetic dataset for demonstration.
    """
    model_path = os.path.join(current_app.instance_path, 'model.joblib')

    if request.is_json:
        data = request.get_json()
        X = data.get('X')
        y = data.get('y')
    else:
        X = None
        y = None

    if X is None or y is None:
        # create tiny synthetic dataset: y = sum(features) + noise
        X = [[1.0, 2.0], [2.0, 1.0], [3.0, 0.5], [4.0, 1.0]]
        y = [sum(x) for x in X]

    try:
        model = ml.train_regressor(X, y)
        ml.save_model(model, model_path)
    except Exception as e:
        return jsonify(error=f'Training failed: {e}'), 500

    return jsonify(status='trained', model_path=model_path, n_samples=len(y))
