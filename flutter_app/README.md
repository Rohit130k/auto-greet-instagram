# Auto Greet Instagram - Flutter App

Beautiful Android app for scheduling Instagram greeting messages.

## 🚀 Setup Instructions

### 1. Install Flutter

Make sure you have Flutter installed. Check with:

```bash
flutter --version
```

If not installed, download from: https://flutter.dev/docs/get-started/install

### 2. Install Dependencies

```bash
cd flutter_app
flutter pub get
```

### 3. Run the App

Connect your Android device or start an emulator, then:

```bash
flutter run
```

## 📱 Features

### Home Screen (Schedule)
- Enter recipient's Instagram username
- Choose from quick message templates
- Type custom greeting message
- Select date and time
- Enable daily repeat option
- Configure backend URL in settings

### History Screen
- View all scheduled messages
- See message status (Pending, Sent, Failed)
- Delete pending schedules
- Pull to refresh

## 🔧 Configuration

### Backend URL Setup

1. Tap the settings icon (⚙️) in the home screen
2. Enter your backend URL:
   - Local: `http://localhost:5000`
   - ngrok: `https://your-id.ngrok.io`
   - Render: `https://your-app.onrender.com`
3. Tap "Save"

The app will automatically check backend connection status.

## 🎨 UI Features

- **Material Design 3** with Instagram-inspired theme
- **Dark mode** support (follows system theme)
- **Bottom navigation** for easy screen switching
- **Status indicators** for backend connection
- **Quick templates** for common greetings
- **Pull to refresh** in history screen

## 📦 Dependencies

- `http` - API communication
- `intl` - Date/time formatting
- `shared_preferences` - Store backend URL
- `flutter_local_notifications` - Future notification support

## 🔐 Permissions

The app requires internet permission to communicate with the backend.

This is automatically added in `AndroidManifest.xml`.

## 🌐 Network Configuration

For Android to connect to localhost backend:

1. Use your PC's IP address instead of `localhost`
2. Find your IP: `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
3. Example: `http://192.168.1.100:5000`

Or use ngrok for easy tunneling:

```bash
ngrok http 5000
```

## 📱 Building APK

To build a release APK:

```bash
flutter build apk --release
```

The APK will be in: `build/app/outputs/flutter-apk/app-release.apk`

## 🎯 Usage Flow

1. **Configure Backend**: Set backend URL in settings
2. **Schedule Message**: Fill form and tap "Schedule Message"
3. **View History**: Switch to History tab to see all schedules
4. **Backend Handles**: Backend automatically sends at scheduled time

## 🐛 Troubleshooting

### Backend Not Reachable
- Check if backend is running
- Verify backend URL is correct
- Use PC's IP address instead of localhost
- Check firewall settings

### Message Not Sending
- Ensure backend is logged into Instagram
- Check backend logs for errors
- Verify recipient username is correct

## 🚀 Future Enhancements

- [ ] Push notifications when message is sent
- [ ] Message templates management
- [ ] Multiple recipients per schedule
- [ ] Analytics and statistics
- [ ] In-app backend status logs
