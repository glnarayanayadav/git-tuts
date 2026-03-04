from flask import Blueprint, render_template_string, current_app

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    # Minimal index page for scaffold
    html = '''
    <h1>ABC Company — ML App</h1>
    <p>Welcome to the scaffolded Flask app. Next: implement auth, upload, ML APIs.</p>
    '''
    return render_template_string(html)
