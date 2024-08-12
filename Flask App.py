from flask import Flask, request
import os

app = Flask(__name__)

def vibrate_phone(duration_ms=500):
    os.system('termux-wake-lock')
    os.system(f'termux-vibrate -d {duration_ms}')
    os.system('termux-wake-unlock')  # Optional: to release the wake lock after the vibration


@app.route('/command', methods=['POST'])
def command():
    cmd = request.form.get('cmd')
    if cmd == "vibrate":
        duration = int(request.form.get('duration', 500))  # Get duration from request or default to 500ms
        vibrate_phone(duration)
        return f"Phone vibrated for {duration} milliseconds"
    else:
        return "Unknown command", 400


print("Verson 4")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
