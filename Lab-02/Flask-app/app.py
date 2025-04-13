from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    app_name = os.getenv("APP_NAME", "Unknown")
    api_key = os.getenv("API_KEY", "No API Key Found")
    return f"Hello from {app_name}! API Key: {api_key}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)