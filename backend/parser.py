import re
from typing import Optional

def parse_indian_banking_sms(text: str) -> Optional[dict]:
    amt_match = re.search(r'(?:RS|INR|RS\.)\s*([\d,]+\.?\d*)', text)
    if not amt_match:
        return None
    amount = float(amt_match.group(1).replace(',', ''))

    action = "DEBIT" if any(x in text for x in ["DEBITED", "SPENT", "PAID"]) else "CREDIT"

    acc_match = re.search(r'(?:A/C|A\s*/\s*C|CARD|ACC)\s*(?:ENDING|XX|X)*\s*(\d{3,4})', text)
    account_source = f"ACC_TAIL_{acc_match.group(1)}" if acc_match else "UNKNOWN_BANK_SOURCE"

    merchant_ref = "General Marketplace Outflow"
    merchant_match = re.search(r'(?:TO|INFO|VPA|AT)\s+([A-Z0-9\s\.\-\_\@\/]+?)(?:\s+ON|\s+BALANCE|\s+LINKED|$)', text)
    
    if merchant_match:
        merchant_ref = merchant_match.group(1).strip()
        merchant_ref = re.sub(r'(USING UPI|REF\s*\d+|FOR).*$', '', merchant_ref).strip()

    return {
        "amount": amount,
        "action": action,
        "account_source": account_source,
        "merchant_ref": merchant_ref
    }
