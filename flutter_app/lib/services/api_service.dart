import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

class ApiService {
  static String _baseUrl = 'http://localhost:5000';

  // Get base URL from shared preferences
  static Future<String> getBaseUrl() async {
    final prefs = await SharedPreferences.getInstance();
    _baseUrl = prefs.getString('backend_url') ?? 'http://localhost:5000';
    return _baseUrl;
  }

  // Set base URL
  static Future<void> setBaseUrl(String url) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('backend_url', url);
    _baseUrl = url;
  }

  // Check backend status
  static Future<Map<String, dynamic>> checkStatus() async {
    try {
      await getBaseUrl();
      final response = await http.get(
        Uri.parse('$_baseUrl/status'),
      ).timeout(const Duration(seconds: 5));

      if (response.statusCode == 200) {
        return json.decode(response.body);
      } else {
        throw Exception('Failed to connect to backend');
      }
    } catch (e) {
      throw Exception('Backend not reachable: $e');
    }
  }

  // Login to Instagram
  static Future<Map<String, dynamic>> login() async {
    try {
      await getBaseUrl();
      final response = await http.post(
        Uri.parse('$_baseUrl/login'),
        headers: {'Content-Type': 'application/json'},
      ).timeout(const Duration(seconds: 10));

      return json.decode(response.body);
    } catch (e) {
      throw Exception('Login failed: $e');
    }
  }

  // Schedule a message
  static Future<Map<String, dynamic>> scheduleMessage({
    required String recipient,
    required String message,
    required String time,
    String? date,
    bool repeatDaily = false,
  }) async {
    try {
      await getBaseUrl();
      final response = await http.post(
        Uri.parse('$_baseUrl/schedule'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({
          'recipient': recipient,
          'message': message,
          'time': time,
          'date': date,
          'repeat_daily': repeatDaily,
        }),
      ).timeout(const Duration(seconds: 10));

      return json.decode(response.body);
    } catch (e) {
      throw Exception('Failed to schedule message: $e');
    }
  }

  // Get all scheduled messages
  static Future<List<dynamic>> getScheduledMessages() async {
    try {
      await getBaseUrl();
      final response = await http.get(
        Uri.parse('$_baseUrl/list'),
      ).timeout(const Duration(seconds: 10));

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        return data['data'] ?? [];
      } else {
        throw Exception('Failed to load schedules');
      }
    } catch (e) {
      throw Exception('Failed to load schedules: $e');
    }
  }

  // Delete a scheduled message
  static Future<Map<String, dynamic>> deleteSchedule(int id) async {
    try {
      await getBaseUrl();
      final response = await http.delete(
        Uri.parse('$_baseUrl/delete/$id'),
      ).timeout(const Duration(seconds: 10));

      return json.decode(response.body);
    } catch (e) {
      throw Exception('Failed to delete schedule: $e');
    }
  }

  // Send message now (for testing)
  static Future<Map<String, dynamic>> sendNow({
    required String recipient,
    required String message,
  }) async {
    try {
      await getBaseUrl();
      final response = await http.post(
        Uri.parse('$_baseUrl/send-now'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({
          'recipient': recipient,
          'message': message,
        }),
      ).timeout(const Duration(seconds: 15));

      return json.decode(response.body);
    } catch (e) {
      throw Exception('Failed to send message: $e');
    }
  }

  // Update Instagram credentials
  static Future<Map<String, dynamic>> updateCredentials({
    required String username,
    required String password,
  }) async {
    try {
      await getBaseUrl();
      final response = await http.post(
        Uri.parse('$_baseUrl/update-credentials'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({
          'username': username,
          'password': password,
        }),
      ).timeout(const Duration(seconds: 15));

      // Check if response is HTML (error page)
      if (response.body.trim().startsWith('<!') || response.body.trim().startsWith('<html')) {
        throw Exception('Backend endpoint not found. Please restart the backend server.');
      }

      // Check for non-200 status codes
      if (response.statusCode != 200 && response.statusCode != 201) {
        try {
          final errorData = json.decode(response.body);
          throw Exception(errorData['message'] ?? 'Server error: ${response.statusCode}');
        } catch (e) {
          throw Exception('Server error: ${response.statusCode}');
        }
      }

      return json.decode(response.body);
    } catch (e) {
      if (e.toString().contains('Backend endpoint not found')) {
        rethrow;
      }
      throw Exception('Failed to update credentials: $e');
    }
  }

  // Logout Instagram account
  static Future<Map<String, dynamic>> logout() async {
    try {
      await getBaseUrl();
      final response = await http.post(
        Uri.parse('$_baseUrl/logout'),
        headers: {'Content-Type': 'application/json'},
      ).timeout(const Duration(seconds: 10));

      if (response.statusCode == 200 || response.statusCode == 201) {
        return json.decode(response.body);
      } else {
        throw Exception('Logout failed: ${response.statusCode}');
      }
    } catch (e) {
      throw Exception('Failed to logout: $e');
    }
  }

  // Update a scheduled message
  static Future<Map<String, dynamic>> updateSchedule({
    required int id,
    required String recipient,
    required String message,
    required String time,
    String? date,
    bool repeatDaily = false,
  }) async {
    try {
      await getBaseUrl();
      final response = await http.put(
        Uri.parse('$_baseUrl/update/$id'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode({
          'recipient': recipient,
          'message': message,
          'time': time,
          'date': date,
          'repeat_daily': repeatDaily,
        }),
      ).timeout(const Duration(seconds: 10));

      return json.decode(response.body);
    } catch (e) {
      throw Exception('Failed to update schedule: $e');
    }
  }
}
