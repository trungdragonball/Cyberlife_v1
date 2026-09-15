MODULE_ID = "M10"
MODULE_NAME = "Event"
DOMAIN = "platform"

BOUNDARY_RULES = [
    "No direct cross-module database access",
    "Use interfaces/APIs/events for collaboration",
    "Permission is authoritative for access",
    "Critical actions are audited",
    "Safety must fail closed",
]
