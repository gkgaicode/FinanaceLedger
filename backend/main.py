from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from parser import parse_indian_banking_sms

app = FastAPI(title="India FinTech Core Ingestion Gateway")

class IncomingSMS(BaseModel):
    sender: str
    body: str
    timestamp: datetime
    sim_slot: Optional[int] = 0

@app.post("/api/v1/transactions/sms-sync", status_code=status.HTTP_201_CREATED)
async def process_android_sms(payload: IncomingSMS):
    clean_body = payload.body.upper()
    
    if not any(kwd in clean_body for kwd in ["DEBITED", "CREDITED", "SPENT", "CHARGED", "SUCCESSFULLY PAID"]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
            detail="Non-transactional text content filtered out"
        )
    
    result = parse_indian_banking_sms(clean_body)
    if result:
        return {"status": "queued", "data": result}
        
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Failed to parse financial text components"
    )
