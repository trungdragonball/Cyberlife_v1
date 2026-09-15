import pytest
from core.intelligence.memory import MemoryService

def test_cross_owner_memory_blocked():
    m=MemoryService()
    item=m.create("A","secret")
    with pytest.raises(PermissionError):
        m.get("B",item.id)
