MODULE_ID = "M47"
MODULE_NAME = "Dispute"
DOMAIN = "commerce"

BOUNDARY_RULES = [
    "No direct cross-module database access",
    "Use interfaces/APIs/events for collaboration",
    "Permission is authoritative for access",
    "Critical actions are audited",
    "Safety must fail closed",
]
