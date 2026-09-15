MODULE_ID = "M53"
MODULE_NAME = "KYC/Verification Adapter"
DOMAIN = "adapters"

BOUNDARY_RULES = [
    "No direct cross-module database access",
    "Use interfaces/APIs/events for collaboration",
    "Permission is authoritative for access",
    "Critical actions are audited",
    "Safety must fail closed",
]
