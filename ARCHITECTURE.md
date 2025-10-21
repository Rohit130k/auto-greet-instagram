# 🏗️ System Architecture - Auto Greet Instagram

## 📊 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                  │
│                        USER LAYER                                │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │                                                         │    │
│  │           📱 Flutter Android App                        │    │
│  │                                                         │    │
│  │  ┌──────────────┐        ┌──────────────┐            │    │
│  │  │              │        │              │            │    │
│  │  │ Home Screen  │        │   History    │            │    │
│  │  │  (Schedule)  │◄──────►│   Screen     │            │    │
│  │  │              │        │              │            │    │
│  │  └──────┬───────┘        └──────┬───────┘            │    │
│  │         │                       │                     │    │
│  │         └───────────┬───────────┘                     │    │
│  │                     │                                 │    │
│  │                     ▼                                 │    │
│  │            ┌─────────────────┐                        │    │
│  │            │   API Service   │                        │    │
│  │            │  (HTTP Client)  │                        │    │
│  │            └────────┬────────┘                        │    │
│  │                     │                                 │    │
│  └─────────────────────┼─────────────────────────────────┘    │
│                        │                                       │
└────────────────────────┼───────────────────────────────────────┘
                         │
                         │ HTTP/JSON
                         │ REST API
                         │
┌────────────────────────▼───────────────────────────────────────┐
│                                                                 │
│                      BACKEND LAYER                              │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │                                                           │ │
│  │              🐍 Python Flask Backend                      │ │
│  │                                                           │ │
│  │  ┌─────────────────────────────────────────────────┐    │ │
│  │  │                                                  │    │ │
│  │  │           Flask Web Server                       │    │ │
│  │  │                                                  │    │ │
│  │  │  ┌──────────┐  ┌──────────┐  ┌──────────┐     │    │ │
│  │  │  │  /status │  │/schedule │  │  /list   │     │    │ │
│  │  │  └──────────┘  └──────────┘  └──────────┘     │    │ │
│  │  │  ┌──────────┐  ┌──────────┐  ┌──────────┐     │    │ │
│  │  │  │  /login  │  │ /delete  │  │/send-now │     │    │ │
│  │  │  └──────────┘  └──────────┘  └──────────┘     │    │ │
│  │  │                                                  │    │ │
│  │  └──────────────────┬───────────────────────────────┘    │ │
│  │                     │                                     │ │
│  │  ┌──────────────────▼───────────────────────────────┐    │ │
│  │  │                                                   │    │ │
│  │  │         Background Scheduler Thread              │    │ │
│  │  │                                                   │    │ │
│  │  │  • Checks time every 30 seconds                  │    │ │
│  │  │  • Matches scheduled messages                    │    │ │
│  │  │  • Triggers message sending                      │    │ │
│  │  │  • Updates status                                │    │ │
│  │  │                                                   │    │ │
│  │  └──────────────────┬───────────────────────────────┘    │ │
│  │                     │                                     │ │
│  │  ┌──────────────────▼───────────────────────────────┐    │ │
│  │  │                                                   │    │ │
│  │  │          Instagram Client (instagrapi)           │    │ │
│  │  │                                                   │    │ │
│  │  │  • Login to Instagram                            │    │ │
│  │  │  • Get user ID from username                     │    │ │
│  │  │  • Send direct messages                          │    │ │
│  │  │                                                   │    │ │
│  │  └──────────────────┬───────────────────────────────┘    │ │
│  │                     │                                     │ │
│  └─────────────────────┼─────────────────────────────────────┘ │
│                        │                                       │
│  ┌─────────────────────▼─────────────────────────────────┐   │
│  │                                                        │   │
│  │              📄 schedule.json                          │   │
│  │                                                        │   │
│  │  [                                                     │   │
│  │    {                                                   │   │
│  │      "id": 1,                                          │   │
│  │      "recipient": "friend",                            │   │
│  │      "message": "Good Morning",                        │   │
│  │      "time": "08:00",                                  │   │
│  │      "status": "pending"                               │   │
│  │    }                                                   │   │
│  │  ]                                                     │   │
│  │                                                        │   │
│  └────────────────────────────────────────────────────────┘   │
│                                                                │
└────────────────────────┬───────────────────────────────────────┘
                         │
                         │ Instagram API
                         │
┌────────────────────────▼───────────────────────────────────────┐
│                                                                 │
│                    INSTAGRAM LAYER                              │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │                                                           │ │
│  │              📷 Instagram Servers                         │ │
│  │                                                           │ │
│  │  • Authenticate user                                     │ │
│  │  • Process direct messages                              │ │
│  │  • Deliver to recipients                                │ │
│  │                                                           │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 🔄 Data Flow Diagrams

### 1. Scheduling a Message

```
┌─────────┐
│  User   │
└────┬────┘
     │ 1. Fill form (recipient, message, time)
     ▼
┌─────────────────┐
│  Home Screen    │
└────┬────────────┘
     │ 2. Tap "Schedule Message"
     ▼
┌─────────────────┐
│  API Service    │
└────┬────────────┘
     │ 3. POST /schedule
     │    {recipient, message, time, date}
     ▼
┌─────────────────┐
│ Flask Backend   │
└────┬────────────┘
     │ 4. Validate input
     ▼
┌─────────────────┐
│ schedule.json   │
└────┬────────────┘
     │ 5. Save schedule
     ▼
┌─────────────────┐
│ Flask Backend   │
└────┬────────────┘
     │ 6. Return success
     ▼
┌─────────────────┐
│  Home Screen    │
└────┬────────────┘
     │ 7. Show confirmation
     ▼
┌─────────┐
│  User   │
└─────────┘
```

### 2. Automatic Message Sending

```
┌──────────────────────┐
│ Background Scheduler │
│     (Every 30s)      │
└──────────┬───────────┘
           │ 1. Check current time
           ▼
┌──────────────────────┐
│   schedule.json      │
└──────────┬───────────┘
           │ 2. Find matching schedules
           ▼
┌──────────────────────┐
│  Time Match Found?   │
└──────────┬───────────┘
           │ Yes
           ▼
┌──────────────────────┐
│ Instagram Client     │
└──────────┬───────────┘
           │ 3. Login (if needed)
           ▼
┌──────────────────────┐
│ Instagram Client     │
└──────────┬───────────┘
           │ 4. Get user_id from username
           ▼
┌──────────────────────┐
│ Instagram Client     │
└──────────┬───────────┘
           │ 5. Send direct message
           ▼
┌──────────────────────┐
│ Instagram Servers    │
└──────────┬───────────┘
           │ 6. Deliver message
           ▼
┌──────────────────────┐
│   Recipient          │
└──────────────────────┘
           │
           ▼
┌──────────────────────┐
│ Background Scheduler │
└──────────┬───────────┘
           │ 7. Update status to 'sent'
           ▼
┌──────────────────────┐
│   schedule.json      │
└──────────────────────┘
```

### 3. Viewing History

```
┌─────────┐
│  User   │
└────┬────┘
     │ 1. Tap "History" tab
     ▼
┌─────────────────┐
│ History Screen  │
└────┬────────────┘
     │ 2. Request schedules
     ▼
┌─────────────────┐
│  API Service    │
└────┬────────────┘
     │ 3. GET /list
     ▼
┌─────────────────┐
│ Flask Backend   │
└────┬────────────┘
     │ 4. Read schedule.json
     ▼
┌─────────────────┐
│ schedule.json   │
└────┬────────────┘
     │ 5. Return all schedules
     ▼
┌─────────────────┐
│ Flask Backend   │
└────┬────────────┘
     │ 6. JSON response
     ▼
┌─────────────────┐
│ History Screen  │
└────┬────────────┘
     │ 7. Display list
     ▼
┌─────────┐
│  User   │
└─────────┘
```

## 🧩 Component Details

### Flutter App Components

```
flutter_app/
│
├── main.dart
│   └── AutoGreetApp (MaterialApp)
│       └── MainScreen (StatefulWidget)
│           ├── NavigationBar
│           └── Screen Switcher
│               ├── HomeScreen
│               └── HistoryScreen
│
├── screens/
│   ├── home_screen.dart
│   │   ├── Form (recipient, message, time)
│   │   ├── Time Picker
│   │   ├── Date Picker
│   │   ├── Template Chips
│   │   └── Schedule Button
│   │
│   └── history_screen.dart
│       ├── Schedule List
│       ├── Status Badges
│       ├── Delete Button
│       └── Pull to Refresh
│
└── services/
    └── api_service.dart
        ├── checkStatus()
        ├── login()
        ├── scheduleMessage()
        ├── getScheduledMessages()
        ├── deleteSchedule()
        └── sendNow()
```

### Backend Components

```
backend/
│
├── app.py
│   ├── Flask App
│   │   ├── Routes
│   │   │   ├── /status
│   │   │   ├── /login
│   │   │   ├── /schedule
│   │   │   ├── /list
│   │   │   ├── /delete/<id>
│   │   │   └── /send-now
│   │   │
│   │   └── Functions
│   │       ├── load_schedule()
│   │       ├── save_schedule()
│   │       ├── login_instagram()
│   │       └── send_instagram_message()
│   │
│   └── Background Thread
│       └── check_and_send_scheduled_messages()
│           ├── Check time (every 30s)
│           ├── Find matches
│           ├── Send messages
│           └── Update status
│
└── schedule.json
    └── Array of schedule objects
```

## 🔐 Security Architecture

```
┌─────────────────────────────────────────────┐
│          Security Layers                     │
├─────────────────────────────────────────────┤
│                                              │
│  1. Environment Variables (.env)            │
│     • Instagram credentials                 │
│     • Never committed to Git                │
│                                              │
│  2. Input Validation                        │
│     • Backend validates all inputs          │
│     • Frontend form validation              │
│                                              │
│  3. Rate Limiting                           │
│     • 30s delay between messages            │
│     • Prevents spam detection               │
│                                              │
│  4. HTTPS (Production)                      │
│     • Encrypted communication               │
│     • Secure data transfer                  │
│                                              │
│  5. Local Storage                           │
│     • Backend URL in SharedPreferences      │
│     • No sensitive data in app              │
│                                              │
└─────────────────────────────────────────────┘
```

## 📡 API Communication

### Request/Response Flow

```
Flutter App                    Flask Backend
    │                               │
    │  POST /schedule               │
    ├──────────────────────────────►│
    │  {                            │
    │    "recipient": "user",       │
    │    "message": "Hello",        │
    │    "time": "08:00"            │
    │  }                            │
    │                               │
    │                          ┌────┴────┐
    │                          │ Validate│
    │                          └────┬────┘
    │                               │
    │                          ┌────┴────┐
    │                          │  Save   │
    │                          └────┬────┘
    │                               │
    │  200 OK                       │
    │◄──────────────────────────────┤
    │  {                            │
    │    "success": true,           │
    │    "message": "Scheduled",    │
    │    "data": {...}              │
    │  }                            │
    │                               │
```

## 🔄 State Management

### Flutter App State

```
┌─────────────────────────────────────┐
│         App State                    │
├─────────────────────────────────────┤
│                                      │
│  • Selected Time (TimeOfDay)        │
│  • Selected Date (DateTime)         │
│  • Repeat Daily (bool)              │
│  • Backend URL (String)             │
│  • Backend Status (String)          │
│  • Schedules List (List<dynamic>)   │
│  • Loading State (bool)             │
│                                      │
└─────────────────────────────────────┘
```

### Backend State

```
┌─────────────────────────────────────┐
│       Backend State                  │
├─────────────────────────────────────┤
│                                      │
│  • Instagram Client (Client)        │
│  • Login Status (bool)              │
│  • Schedules (JSON file)            │
│  • Scheduler Thread (Thread)        │
│                                      │
└─────────────────────────────────────┘
```

## 🎯 Deployment Architecture

### Local Development

```
┌──────────────┐         ┌──────────────┐
│              │         │              │
│  Android     │  WiFi   │   PC/Laptop  │
│  Device      │◄───────►│              │
│              │         │  • Backend   │
│  Flutter App │         │  • Port 5000 │
│              │         │              │
└──────────────┘         └──────────────┘
```

### Production (Cloud)

```
┌──────────────┐         ┌──────────────┐
│              │         │              │
│  Android     │ Internet│  Cloud Server│
│  Device      │◄───────►│  (Render)    │
│              │         │              │
│  Flutter App │         │  • Backend   │
│              │         │  • Port 443  │
│              │         │  • HTTPS     │
└──────────────┘         └──────────────┘
```

## 📊 Performance Considerations

### Backend Performance

- **Memory**: ~50-100 MB
- **CPU**: <5% idle, ~10% active
- **Network**: Minimal (only when sending)
- **Disk**: <1 MB (schedule.json)

### App Performance

- **APK Size**: ~20-30 MB
- **Memory**: ~100-150 MB
- **Battery**: Minimal (no background service)
- **Network**: <1 MB/day

## 🔧 Technology Stack Details

```
┌─────────────────────────────────────────────┐
│           Technology Stack                   │
├─────────────────────────────────────────────┤
│                                              │
│  Frontend                                    │
│  ├── Flutter 3.0+                           │
│  ├── Dart                                   │
│  ├── Material Design 3                      │
│  └── Packages:                              │
│      ├── http (API calls)                   │
│      ├── intl (Date/Time)                   │
│      └── shared_preferences (Storage)       │
│                                              │
│  Backend                                     │
│  ├── Python 3.8+                            │
│  ├── Flask 3.0.0                            │
│  ├── instagrapi 2.1.2                       │
│  └── python-dotenv 1.0.0                    │
│                                              │
│  Database                                    │
│  └── JSON file (schedule.json)              │
│                                              │
│  Deployment                                  │
│  ├── Local (Development)                    │
│  ├── ngrok (Tunneling)                      │
│  ├── Render.com (Cloud)                     │
│  └── Replit (Cloud)                         │
│                                              │
└─────────────────────────────────────────────┘
```

---

**This architecture is designed for:**
- ✅ Simplicity and ease of use
- ✅ Minimal dependencies
- ✅ Easy deployment
- ✅ Scalability
- ✅ Maintainability

**Built with ❤️ for efficient Instagram automation!**
