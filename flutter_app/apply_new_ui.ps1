# Apply New UI Design
# This script replaces old screen files with the new redesigned versions

Write-Host "🎨 Applying New UI Design..." -ForegroundColor Cyan
Write-Host ""

$screensPath = "lib\screens"

# Remove old files
Write-Host "📝 Removing old screen files..." -ForegroundColor Yellow
Remove-Item "$screensPath\home_screen.dart" -Force -ErrorAction SilentlyContinue
Remove-Item "$screensPath\history_screen.dart" -Force -ErrorAction SilentlyContinue
Remove-Item "$screensPath\settings_screen.dart" -Force -ErrorAction SilentlyContinue

# Rename new files
Write-Host "✨ Installing new screen files..." -ForegroundColor Yellow
Rename-Item "$screensPath\home_screen_new.dart" "home_screen.dart" -ErrorAction SilentlyContinue
Rename-Item "$screensPath\history_screen_new.dart" "history_screen.dart" -ErrorAction SilentlyContinue
Rename-Item "$screensPath\settings_screen_new.dart" "settings_screen.dart" -ErrorAction SilentlyContinue

Write-Host ""
Write-Host "✅ New UI applied successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "🚀 Next steps:" -ForegroundColor Cyan
Write-Host "   1. Run: flutter clean" -ForegroundColor White
Write-Host "   2. Run: flutter pub get" -ForegroundColor White
Write-Host "   3. Run: flutter run" -ForegroundColor White
Write-Host ""
Write-Host "🎨 Your app now has a beautiful new design!" -ForegroundColor Magenta
