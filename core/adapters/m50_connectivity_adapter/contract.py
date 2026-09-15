MODULE_ID = "M50"
MODULE_NAME = "Connectivity Adapter"
DOMAIN = "adapters"

BOUNDARY_RULES = [
    "No direct cross-module database access",
    "Use interfaces/APIs/events for collaboration",
    "Permission is authoritative for access",
    "Critical actions are audited",
    "Safety must fail closed",
]
