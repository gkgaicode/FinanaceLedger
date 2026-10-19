class SmsPayload {
  final String sender;
  final String body;
  final DateTime timestamp;
  final int simSlot;

  SmsPayload({
    required this.sender,
    required this.body,
    required this.timestamp,
    this.simSlot = 0,
  });

  Map<String, dynamic> toJson() {
    return {
      'sender': sender,
      'body': body,
      'timestamp': timestamp.toUtc().toIso8601String(),
      'sim_slot': simSlot,
    };
  }
}
