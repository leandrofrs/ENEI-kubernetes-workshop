from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    app_name = os.getenv("APP_NAME", "Unknown")
    api_key = os.getenv("API_KEY", "No API Key Found")
    return f"Hello from {app_name}! API Key: {api_key}"

@app.route('/log')
def log():
    with open("/data/log.txt", "a") as f:
        f.write("Visited /log endpoint\n" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    return "Logged to persistent volume!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)