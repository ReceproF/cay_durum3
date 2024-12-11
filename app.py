import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Global Variables
tea_status = "Çay Hazır Değil"
tea_timer = 0
water_timer = 0
tea_stock = "10"
tea_times = "10:00, 14:00, 16:00"
tea_money = "50 TL - 01.01.2024"

@app.route('/')
def index():
    global tea_status, tea_timer, water_timer, tea_stock, tea_times, tea_money
    return render_template('index.html', tea_status=tea_status, tea_timer=tea_timer, water_timer=water_timer,
                           tea_stock=tea_stock, tea_times=tea_times, tea_money=tea_money)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/status', methods=['GET'])
def get_status():
    global tea_status, tea_timer, water_timer, tea_stock, tea_times, tea_money
    return jsonify({
        "tea_status": tea_status,
        "tea_timer": tea_timer,
        "water_timer": water_timer,
        "tea_stock": tea_stock,
        "tea_times": tea_times,
        "tea_money": tea_money
    })

@app.route('/update-tea-status', methods=['POST'])
def update_tea_status():
    global tea_status
    tea_status = request.json['tea_status']
    return jsonify({"message": "Çay durumu güncellendi!"})

@app.route('/update-tea-timer', methods=['POST'])
def update_tea_timer():
    global tea_timer
    tea_timer = request.json['tea_timer']
    return jsonify({"message": "Çay sayacı güncellendi!"})

@app.route('/update-water-status', methods=['POST'])
def update_water_status():
    global water_timer
    water_timer = request.json['water_timer']
    return jsonify({"message": "Su kaynama durumu güncellendi!"})

@app.route('/decrease-timer', methods=['POST'])
def decrease_timer():
    global tea_timer, water_timer
    if tea_timer > 0:
        tea_timer -= 1
    if water_timer > 0:
        water_timer -= 1
    return jsonify({"tea_timer": tea_timer, "water_timer": water_timer})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Default to 5000 in local, use PORT from environment in Heroku
    app.run(host='0.0.0.0', port=port)  # Listen on all IPs and specified port
