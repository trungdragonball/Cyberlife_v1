from core.platform.security import InMemoryPermissionStore
from core.safety.engine import SafetyEngine
from core.intelligence.evolution import EvolutionEngine

def test_permission_required():
    p=InMemoryPermissionStore()
    assert not p.check("u","camera","view")
    p.grant("u","camera","view")
    assert p.check("u","camera","view")

def test_revoke_invalidates_capability():
    p=InMemoryPermissionStore()
    pid=p.grant("u","camera","view")
    assert p.check("u","camera","view")
    p.revoke(pid)
    assert not p.check("u","camera","view")

def test_safety_fail_closed():
    assert SafetyEngine().evaluate("bypass_permission")["allowed"] is False

def test_evolution_requires_approval_and_benchmark():
    e=EvolutionEngine()
    assert not e.can_deploy(False,True)
    assert not e.can_deploy(True,False)
    assert e.can_deploy(True,True)
