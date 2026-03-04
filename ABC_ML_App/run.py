from app import create_app

app = create_app()

if __name__ == "__main__":
    # Use Flask dev server for local development
    app.run(host="127.0.0.1", port=5000, debug=True)
