export interface SmsTransactionInput {
  sender: string;
  body: string;
  timestamp: string;
  sim_slot?: number;
}

export interface IngestionResponse {
  status: string;
  data: {
    amount: number;
    action: 'DEBIT' | 'CREDIT';
    account_source: string;
    merchant_ref: string;
  };
}
