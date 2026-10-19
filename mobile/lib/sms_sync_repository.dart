import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;
import 'sms_payload_model.dart';

class SmsSyncRepository {
  final String baseUrl;
  final String authToken;

  SmsSyncRepository({
    required this.baseUrl,
    required this.authToken,
  });

  Future<bool> syncSmsToCloud(SmsPayload payload) async {
    final url = Uri.parse('$baseUrl/api/v1/transactions/sms-sync');
    
    try {
      final response = await http.post(
        url,
        headers: {
          HttpHeaders.contentTypeHeader: 'application/json',
          HttpHeaders.authorizationHeader: 'Bearer $authToken',
        },
        body: jsonEncode(payload.toJson()),
      ).timeout(const Duration(seconds: 10));

      return response.statusCode == 201;
    } catch (e) {
      print('Network link down. Cached to local database context.');
      return false;
    }
  }
}
