MODULE_ID = "M46"
MODULE_NAME = "Payment"
DOMAIN = "commerce"

BOUNDARY_RULES = [
    "No direct cross-module database access",
    "Use interfaces/APIs/events for collaboration",
    "Permission is authoritative for access",
    "Critical actions are audited",
    "Safety must fail closed",
]
