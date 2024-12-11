import os
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Global değişkenler: Çay ve su durumu, sayaçlar ve diğer bilgiler burada saklanıyor
tea_status = "Çay Hazır Değil"  # Çayın mevcut durumu
tea_timer = 0  # Çay hazır olmasına kalan süre (dakika)
water_timer = 0  # Su kaynama süresi (dakika)
tea_stock = "2"  # Mevcut çay paket sayısı
tea_times = "08.45, 13.35"  # Gün içindeki çay saatleri
tea_money = "0 TL - 01.01.2025"  # Toplanan çay parası ve tarihi

# Ana sayfa: Çay durumu, sayaçlar ve stok bilgilerini gösterir
@app.route('/')
def index():
    global tea_status, tea_timer, water_timer, tea_stock, tea_times, tea_money
    return render_template('index.html', tea_status=tea_status, tea_timer=tea_timer, water_timer=water_timer,
                           tea_stock=tea_stock, tea_times=tea_times, tea_money=tea_money)

# Admin paneli sayfası
@app.route('/admin')
def admin():
    return render_template('admin.html')

# Durum bilgisini JSON formatında döndürür
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

# Çay durumu güncelleme
@app.route('/update-tea-status', methods=['POST'])
def update_tea_status():
    global tea_status
    tea_status = request.json['tea_status']
    return jsonify({"message": "Çay durumu güncellendi!"})

# Çay sayacı güncelleme
@app.route('/update-tea-timer', methods=['POST'])
def update_tea_timer():
    global tea_timer
    tea_timer = request.json['tea_timer']
    return jsonify({"message": "Çay sayacı güncellendi!"})

# Su kaynama durumu güncelleme
@app.route('/update-water-status', methods=['POST'])
def update_water_status():
    global water_timer
    water_timer = request.json['water_timer']
    return jsonify({"message": "Su kaynama durumu güncellendi!"})

# Sayaçları her dakika bir azaltır
@app.route('/decrease-timer', methods=['POST'])
def decrease_timer():
    global tea_timer, water_timer
    if tea_timer > 0:
        tea_timer -= 1
    if water_timer > 0:
        water_timer -= 1
    return jsonify({"tea_timer": tea_timer, "water_timer": water_timer})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Varsayılan olarak 5000 portunu kullanır, Heroku gibi ortamlarda PORT değişkeni alınır
    app.run(host='0.0.0.0', port=port)  # Tüm IP adreslerinden gelen bağlantıları dinler ve belirtilen portu kullanır
