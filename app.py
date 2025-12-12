from flask import Flask, render_template, jsonify, request
from datetime import datetime

app = Flask(__name__)

start_time = None  # store start time
end_time = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_sleep():
    global start_time, end_time
    start_time = datetime.now()
    end_time = None
    return jsonify({"message": "Sleep started", "start_time": start_time.strftime("%H:%M:%S")})

@app.route('/stop', methods=['POST'])
def stop_sleep():
    global start_time, end_time
    if start_time is None:
        return jsonify({"message": "Sleep not started yet!"})
    end_time = datetime.now()
    duration = end_time - start_time
    hours = round(duration.total_seconds() / 3600, 2)
    start_time = None
    return jsonify({"message": "You slept for", "hours": hours})

if __name__ == '__main__':
    app.run(debug=True)

# @app defines the URLs like /start and /stop which the webpage calls
