class SafetyEngine:
    def evaluate(self, action:str, risk:str="normal")->dict:
        blocked = action in {"change_owner_authority","disable_audit","bypass_permission"}
        return {"allowed":not blocked,"reason":"SAFETY_BLOCKED" if blocked else "OK"}
