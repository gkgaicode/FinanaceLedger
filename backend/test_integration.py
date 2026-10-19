import pytest
import httpx
from datetime import datetime

BASE_URL = "http://localhost:8000"
MOCK_TOKEN = "Bearer MOCK_JWT_ACCESS_TOKEN"

@pytest.mark.asyncio
async def test_cors_handshake_headers():
    """
    Simulates the Preflight OPTIONS handshake request fired by web browsers
    running our React Dashboard layer at port 3000.
    """
    async with httpx.AsyncClient() as client:
        headers = {
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "content-type,authorization",
        }
        
        response = await client.options(f"{BASE_URL}/api/v1/transactions/sms-sync", headers=headers)
        
        assert response.statusCode == 200
        assert response.headers.get("access-control-allow-origin") == "http://localhost:3000"
        assert "POST" in response.headers.get("access-control-allow-methods", "")

@pytest.mark.asyncio
async def test_valid_upi_ingestion_pipeline():
    """
    Simulates a successful real-time ingestion flow matching an Indian banking UPI push message.
    Ensures data matches our double-entry target outputs.
    """
    payload = {
        "sender": "AD-HDFCBK",
        "body": "Your A/c XX4321 has been Debited for Rs. 1,250.50 via UPI to SWIGGY@HDFCBANK on 19-10-2026.",
        "timestamp": datetime.utcnow().isoformat(),
        "sim_slot": 0
    }
    
    headers = {
        "Authorization": MOCK_TOKEN,
        "Content-Type": "application/json",
        "Origin": "http://localhost:3000"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/api/v1/transactions/sms-sync", json=payload, headers=headers)
        
        assert response.statusCode == 201
        res_data = response.json()
        assert res_data["status"] == "queued"
        
        # Validate that the inner parser properly structured the raw text nodes
        parsed_fields = res_data["data"]
        assert parsed_fields["amount"] == 1250.50
        assert parsed_fields["action"] == "DEBIT"
        assert parsed_fields["account_source"] == "ACC_TAIL_4321"
        assert "SWIGGY" in parsed_fields["merchant_ref"]

@pytest.mark.asyncio
async def test_spam_sms_filtering():
    """
    Ensures that generic text messages or non-financial updates (OTP updates, ads)
    are caught and filtered out by the gateway with a 422 processing boundary state.
    """
    payload = {
        "sender": "9876543210",
        "body": "Hey, are we still meeting for coffee at Starbucks at 4 PM today?",
        "timestamp": datetime.utcnow().isoformat(),
        "sim_slot": 0
    }
    
    headers = {"Authorization": MOCK_TOKEN, "Content-Type": "application/json"}

    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/api/v1/transactions/sms-sync", json=payload, headers=headers)
        assert response.statusCode == 422
