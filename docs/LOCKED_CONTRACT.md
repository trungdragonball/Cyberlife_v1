# Locked V1 Logic & Test Contract

## Authority
Owner -> Identity -> Authentication -> Permission -> Trust/Risk -> Safety ->
Tool Authorization -> Execution -> Validation -> Audit

## Data
DATA -> OWNER -> CLASSIFICATION -> SCOPE -> PERMISSION -> ACCESS

## AI
AI OUTPUT -> INTENT -> TOOL REQUEST -> AUTHORIZATION -> SAFETY -> EXECUTION

## Evolution
SIGNAL -> CANDIDATE -> EXPERIMENT -> BENCHMARK -> POLICY -> APPROVAL ->
DEPLOY -> MONITOR -> ROLLBACK

## Recovery
FAILURE -> DETECT -> ISOLATE -> PRESERVE STATE -> RECOVER -> VERIFY ->
HEALTH CHECK -> RESUME

## Invariants
- No Identity -> no action.
- No Authentication -> sensitive action blocked.
- No Permission -> blocked.
- Expired/revoked permission -> capability invalid.
- Trust does not grant permission.
- Safety unavailable -> fail-safe.
- AI output is not authority.
- Cross-user/private Memory access requires permission.
- External AI cannot directly access Core/DB/private Memory.
- Cache/Vector/Object Storage is not authority source.
- Worker cannot change permission.
- Evolution cannot self-escalate.
- Restart cannot duplicate side effects.
- Payment must be idempotent.
- Critical action is audited.
- Deletion covers primary and derived data according to policy.
- Device is not authority.
- Capability cannot live longer than authorization.
- Safety/Permission failure never fails open.
- Critical actions reauthorize immediately before execution.
