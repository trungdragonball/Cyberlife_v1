from dataclasses import dataclass
from typing import Protocol

class PermissionStore(Protocol):
    def check(self, subject:str, resource:str, action:str, scope:str="self", purpose:str="")->bool: ...
    def grant(self, subject:str, resource:str, action:str, scope:str="self", purpose:str="")->str: ...
    def revoke(self, permission_id:str)->None: ...

@dataclass
class Permission:
    id:str
    subject:str
    resource:str
    action:str
    scope:str
    purpose:str
    active:bool=True

class InMemoryPermissionStore:
    def __init__(self): self.items={}
    def grant(self,subject,resource,action,scope="self",purpose=""):
        import uuid
        pid=str(uuid.uuid4()); self.items[pid]=Permission(pid,subject,resource,action,scope,purpose)
        return pid
    def revoke(self,permission_id):
        if permission_id in self.items: self.items[permission_id].active=False
    def check(self,subject,resource,action,scope="self",purpose=""):
        return any(p.active and p.subject==subject and p.resource==resource and
                   p.action==action and (p.scope==scope or p.scope=="*") and
                   (not p.purpose or p.purpose==purpose) for p in self.items.values())

class SafetyGate:
    def allow(self, action:str, risk:str="normal")->bool:
        return action not in {"bypass_security","change_owner_authority"}
