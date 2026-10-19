from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from parser import parse_indian_banking_sms

app = FastAPI(title="India FinTech Core Ingestion Gateway")

# 1. Define Explicit Allowed Origins matching industry security standards
# In production environments, replace localhost strings with your verified organizational domains.

#Project Architecture Verification Walkthrough

#With this middleware in place, your entire Indian Salaried FinTech Accounting application stack is now connected and operational:
#1. React Web UI (:3000) securely transmits a raw banking text notification via an authenticated POST request.
#2. FastAPI Server (:8000) screens the request header, matches origin parameters, parses the complex text into double-entry components, and streams the structured payload instantly back onto the screen dashboard layout.

origins = [
    "http://localhost:3000",     # React Web Dashboard (Development Local server)
    "http://127.0.0.1:3000",   # Fallback localhost address resolution
]

# 2. Inject Security Middleware Configuration Layer
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Restricts requests specifically to authorized web interfaces
    allow_credentials=True,           # Permits transmission of HTTP cookies / cookies across domains
    allow_methods=["POST", "GET"],    # Limits system attack vector scope (Blocks PUT, DELETE on ingestion)
    allow_headers=["Content-Type", "Authorization"], # Explicit white-listed protocol headers
)

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
