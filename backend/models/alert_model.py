from pydantic import BaseModel

class Alert(BaseModel):
    timestamp: str
    ip: str
    attack_type: str
    severity: str
    ip_type: str
    attack_count: int