from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Channel Access Token ของคุณ
CHANNEL_ACCESS_TOKEN = '69Jnv/dRH4+bUJcKUpAnSL7Tvl81KNGl2w5KHc8EQCJJ2MoudxsQOj7mlE8GcQZBsb/Igk/SQoFWnfQrbBvfymkWfSnk3Lt01t8wLHe51LVprBS4VwJ+pp9TVITMgkaY8V6n92jHQEussNRq/HTQcQdB04t89/1O/w1cDnyilFU='

@app.route('/get_user_profile', methods=['GET'])
def get_user_profile():
    # รับ UID ไลน์จากอาร์กิวเมนต์ของ URL
    user_id = request.args.get('user_id')
    
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400
    
    # ขอข้อมูลโปรไฟล์ของผู้ใช้จาก LINE Messaging API
    profile_url = f'https://api.line.me/v2/bot/profile/{user_id}'
    headers = {
        'Authorization': f'Bearer {CHANNEL_ACCESS_TOKEN}'
    }
    response = requests.get(profile_url, headers=headers)
    
    if response.status_code != 200:
        return jsonify({'error': 'Failed to get user profile'}), 400
    
    profile_data = response.json()
    
    # คืนค่ารูปโปรไฟล์และชื่อของผู้ใช้เป็น JSON พร้อมกับ UID ไลน์
    result = {
        'userId': user_id,
        'displayName': profile_data['displayName'],
        'pictureUrl': profile_data['pictureUrl']
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
