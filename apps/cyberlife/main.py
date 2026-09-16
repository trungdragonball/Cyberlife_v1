from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from core.intelligence.runtime import AIRuntime
from core.intelligence.memory import MemoryService
from core.platform.security import InMemoryPermissionStore, SafetyGate
from core.safety.engine import SafetyEngine

app=FastAPI(title="CyberLife V1",version="1.0.0")
ai=AIRuntime()
memory=MemoryService()
permissions=InMemoryPermissionStore()
safety=SafetyEngine()

class ChatIn(BaseModel):
    owner_id:str
    message:str

class MemoryIn(BaseModel):
    owner_id:str
    content:str
    classification:str="private"
    scope:str="private"

class PermissionIn(BaseModel):
    subject:str
    resource:str
    action:str
    scope:str="self"
    purpose:str=""

@app.get("/health")
def health(): return {"status":"RUNNING","system":"CyberLife V1","architecture":"modular-monolith"}

@app.post("/api/v1/chat")
def chat(body:ChatIn):
    return {"reply":ai.run(body.message),"owner_id":body.owner_id}

@app.post("/api/v1/memory")
def create_memory(body:MemoryIn):
    return memory.create(body.owner_id,body.content,body.classification,body.scope).__dict__

@app.get("/api/v1/memory/{memory_id}")
def get_memory(memory_id:str, owner_id:str):
    try: return memory.get(owner_id,memory_id).__dict__
    except PermissionError: raise HTTPException(403,"PERMISSION_DENIED")

@app.post("/api/v1/permissions/grant")
def grant(body:PermissionIn):
    pid=permissions.grant(body.subject,body.resource,body.action,body.scope,body.purpose)
    return {"permission_id":pid,"active":True}

@app.post("/api/v1/tools/authorize")
def authorize(subject:str,tool_id:str,required_permission:str,scope:str="self"):
    allowed=permissions.check(subject,tool_id,required_permission,scope)
    if not allowed: raise HTTPException(403,"PERMISSION_DENIED")
    safe=safety.evaluate(required_permission)
    if not safe["allowed"]: raise HTTPException(403,safe["reason"])
    return {"authorized":True}
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
