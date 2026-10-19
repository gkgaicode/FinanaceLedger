import { SmsTransactionInput, IngestionResponse } from './types';

export class SmsSyncService {
  private baseUrl: string;

  constructor(baseUrl: string) {
    this.baseUrl = baseUrl;
  }

  /**
   * Pushes a manual transaction string to the FastAPI validation engine
   */
  async triggerSmsSync(payload: SmsTransactionInput, token: string): Promise<IngestionResponse> {
    const response = await fetch(`${this.baseUrl}/api/v1/transactions/sms-sync`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`Sync failed: ${response.status} - ${errorText}`);
    }

    return response.json();
  }
}
