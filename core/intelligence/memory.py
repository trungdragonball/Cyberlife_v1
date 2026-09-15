from dataclasses import dataclass
from datetime import datetime, timezone
import uuid

@dataclass
class MemoryItem:
    id:str
    owner_id:str
    content:str
    classification:str
    scope:str="private"
    version:int=1
    created_at:str=""

class MemoryService:
    allowed={"important","temporary","private","shareable"}
    def __init__(self): self.items={}
    def create(self,owner_id,content,classification="private",scope="private"):
        if classification not in self.allowed: raise ValueError("VALIDATION_FAILED")
        mid=str(uuid.uuid4())
        item=MemoryItem(mid,owner_id,content,classification,scope,1,datetime.now(timezone.utc).isoformat())
        self.items[mid]=item; return item
    def get(self,requester_id,memory_id):
        item=self.items.get(memory_id)
        if not item or item.owner_id!=requester_id: raise PermissionError("PERMISSION_DENIED")
        return item
    def delete(self,requester_id,memory_id):
        self.get(requester_id,memory_id); del self.items[memory_id]
