from dataclasses import dataclass

@dataclass(frozen=True)
class ToolContract:
    tool_id:str
    required_permission:str
    risk:str
    requires_confirmation:bool
    timeout_seconds:int=30
    idempotency_required:bool=True
    audit_required:bool=True

class ToolAuthorizer:
    def authorize(self,permission_store,subject,tool:ToolContract,scope="self"):
        return permission_store.check(subject,tool.tool_id,tool.required_permission,scope)
