from flask import Flask, request, jsonify
from instagrapi import Client
import json
import os
from datetime import datetime, time
import threading
import time as time_module
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# File to store scheduled messages
SCHEDULE_FILE = 'schedule.json'

# Instagram client
cl = None
is_logged_in = False
login_attempted = False

def load_schedule():
    """Load scheduled messages from JSON file"""
    if os.path.exists(SCHEDULE_FILE):
        with open(SCHEDULE_FILE, 'r') as f:
            return json.load(f)
    return []

def save_schedule(schedule_data):
    """Save scheduled messages to JSON file"""
    with open(SCHEDULE_FILE, 'w') as f:
        json.dump(schedule_data, f, indent=2)

def login_instagram():
    """Login to Instagram"""
    global cl, is_logged_in
    username = os.getenv('INSTAGRAM_USERNAME')
    password = os.getenv('INSTAGRAM_PASSWORD')
    
    if not username or not password:
        print("⚠️ Instagram credentials not found in .env file")
        return False
    
    try:
        cl = Client()
        cl.login(username, password)
        is_logged_in = True
        print(f"✅ Logged in as @{username}")
        return True
    except Exception as e:
        print(f"❌ Login failed: {str(e)}")
        is_logged_in = False
        return False

def send_instagram_message(recipient_username, message):
    """Send a direct message on Instagram"""
    global cl, is_logged_in
    
    if not is_logged_in:
        if not login_instagram():
            return False, "Not logged in to Instagram"
    
    try:
        user_id = cl.user_id_from_username(recipient_username)
        cl.direct_send(message, [user_id])
        print(f"✅ Message sent to @{recipient_username}")
        return True, "Message sent successfully"
    except Exception as e:
        error_msg = f"Failed to send message: {str(e)}"
        print(f"❌ {error_msg}")
        return False, error_msg

def check_and_send_scheduled_messages():
    """Background thread to check and send scheduled messages"""
    while True:
        try:
            schedule_data = load_schedule()
            current_time = datetime.now().strftime("%H:%M")
            current_date = datetime.now().strftime("%Y-%m-%d")
            
            for item in schedule_data:
                if item['status'] == 'pending':
                    scheduled_time = item['time']
                    scheduled_date = item.get('date', current_date)
                    
                    # Check if it's time to send
                    if scheduled_date == current_date and scheduled_time == current_time:
                        success, msg = send_instagram_message(
                            item['recipient'],
                            item['message']
                        )
                        
                        # Update status
                        item['status'] = 'sent' if success else 'failed'
                        item['sent_at'] = datetime.now().isoformat()
                        item['error'] = None if success else msg
                        
                        save_schedule(schedule_data)
                        
                        # Add delay to prevent spam detection
                        time_module.sleep(30)
            
            # Check every 30 seconds
            time_module.sleep(30)
            
        except Exception as e:
            print(f"❌ Scheduler error: {str(e)}")
            time_module.sleep(60)

@app.route('/login', methods=['POST'])
def login():
    """Login to Instagram"""
    success = login_instagram()
    if success:
        return jsonify({
            'success': True,
            'message': 'Logged in successfully'
        }), 200
    else:
        return jsonify({
            'success': False,
            'message': 'Login failed. Check credentials in .env file'
        }), 401

@app.route('/schedule', methods=['POST'])
def schedule_message():
    """Schedule a new greeting message"""
    data = request.json
    
    # Validate input
    required_fields = ['recipient', 'message', 'time']
    for field in required_fields:
        if field not in data:
            return jsonify({
                'success': False,
                'message': f'Missing required field: {field}'
            }), 400
    
    # Load existing schedule
    schedule_data = load_schedule()
    
    # Create new schedule entry
    new_entry = {
        'id': len(schedule_data) + 1,
        'recipient': data['recipient'],
        'message': data['message'],
        'time': data['time'],
        'date': data.get('date', datetime.now().strftime("%Y-%m-%d")),
        'repeat_daily': data.get('repeat_daily', False),
        'status': 'pending',
        'created_at': datetime.now().isoformat(),
        'sent_at': None,
        'error': None
    }
    
    schedule_data.append(new_entry)
    save_schedule(schedule_data)
    
    return jsonify({
        'success': True,
        'message': 'Message scheduled successfully',
        'data': new_entry
    }), 201

@app.route('/list', methods=['GET'])
def list_schedules():
    """Get all scheduled messages"""
    schedule_data = load_schedule()
    return jsonify({
        'success': True,
        'data': schedule_data,
        'count': len(schedule_data)
    }), 200

@app.route('/delete/<int:schedule_id>', methods=['DELETE'])
def delete_schedule(schedule_id):
    """Delete a scheduled message"""
    schedule_data = load_schedule()
    
    # Find and remove the schedule
    updated_schedule = [item for item in schedule_data if item['id'] != schedule_id]
    
    if len(updated_schedule) == len(schedule_data):
        return jsonify({
            'success': False,
            'message': 'Schedule not found'
        }), 404
    
    save_schedule(updated_schedule)
    
    return jsonify({
        'success': True,
        'message': 'Schedule deleted successfully'
    }), 200

@app.route('/status', methods=['GET'])
def status():
    """Check backend status"""
    global is_logged_in, login_attempted
    
    # Auto-login on first status check if not attempted yet
    if not login_attempted:
        print("🔐 First status check - attempting login...")
        login_instagram()
        login_attempted = True
    
    print(f"📊 Status check - is_logged_in: {is_logged_in}")
    return jsonify({
        'success': True,
        'status': 'running',
        'logged_in': is_logged_in,
        'timestamp': datetime.now().isoformat()
    }), 200

@app.route('/send-now', methods=['POST'])
def send_now():
    """Send a message immediately (for testing)"""
    data = request.json
    
    if 'recipient' not in data or 'message' not in data:
        return jsonify({
            'success': False,
            'message': 'Missing recipient or message'
        }), 400
    
    success, msg = send_instagram_message(data['recipient'], data['message'])
    
    return jsonify({
        'success': success,
        'message': msg
    }), 200 if success else 500

@app.route('/update-credentials', methods=['POST'])
def update_credentials():
    """Update Instagram credentials"""
    global is_logged_in, login_attempted
    data = request.json
    
    if 'username' not in data or 'password' not in data:
        return jsonify({
            'success': False,
            'message': 'Missing username or password'
        }), 400
    
    try:
        # Update .env file
        env_path = '.env'
        with open(env_path, 'w') as f:
            f.write(f"INSTAGRAM_USERNAME={data['username']}\n")
            f.write(f"INSTAGRAM_PASSWORD={data['password']}\n")
            f.write(f"FLASK_ENV=development\n")
        
        # Reload environment variables
        load_dotenv(override=True)
        
        # Force re-login
        is_logged_in = False
        login_attempted = False
        
        # Attempt login with new credentials
        if login_instagram():
            return jsonify({
                'success': True,
                'message': 'Credentials updated and logged in successfully'
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': 'Credentials updated but login failed'
            }), 401
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Failed to update credentials: {str(e)}'
        }), 500

@app.route('/logout', methods=['POST'])
def logout():
    """Logout from Instagram"""
    global is_logged_in, login_attempted
    
    try:
        is_logged_in = False
        login_attempted = False
        
        return jsonify({
            'success': True,
            'message': 'Logged out successfully'
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Logout failed: {str(e)}'
        }), 500

@app.route('/update/<int:schedule_id>', methods=['PUT'])
def update_schedule(schedule_id):
    """Update a scheduled message"""
    data = request.json
    
    # Validate input
    required_fields = ['recipient', 'message', 'time']
    for field in required_fields:
        if field not in data:
            return jsonify({
                'success': False,
                'message': f'Missing required field: {field}'
            }), 400
    
    # Load existing schedule
    schedule_data = load_schedule()
    
    # Find and update the schedule
    updated = False
    for item in schedule_data:
        if item['id'] == schedule_id:
            item['recipient'] = data['recipient']
            item['message'] = data['message']
            item['time'] = data['time']
            item['date'] = data.get('date', item.get('date'))
            item['repeat_daily'] = data.get('repeat_daily', item.get('repeat_daily', False))
            item['status'] = 'pending'  # Reset status to pending
            updated = True
            break
    
    if not updated:
        return jsonify({
            'success': False,
            'message': 'Schedule not found'
        }), 404
    
    save_schedule(schedule_data)
    
    return jsonify({
        'success': True,
        'message': 'Schedule updated successfully'
    }), 200

if __name__ == '__main__':
    print("🚀 Auto Greet Instagram Backend Started")
    print("⏳ Login will happen on first API request...")
    
    # Start the scheduler thread
    scheduler_thread = threading.Thread(target=check_and_send_scheduled_messages, daemon=True)
    scheduler_thread.start()
    print("📱 Scheduler thread running in background")
    
    # Get port from environment variable (for cloud hosting) or use 5000
    port = int(os.getenv('PORT', 5000))
    
    # Run Flask app (debug=False to prevent reloader issues)
    app.run(host='0.0.0.0', port=port, debug=False)
