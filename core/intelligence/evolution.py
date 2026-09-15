from enum import Enum

class EvolutionState(str,Enum):
    SIGNAL="SIGNAL"; CANDIDATE="CANDIDATE"; EXPERIMENT="EXPERIMENT"
    BENCHMARK="BENCHMARK"; POLICY="POLICY"; APPROVAL="APPROVAL"
    DEPLOY="DEPLOY"; MONITOR="MONITOR"; ROLLBACK="ROLLBACK"

class EvolutionEngine:
    def propose(self,signal:str)->dict:
        return {"state":EvolutionState.CANDIDATE.value,"signal":signal,"requires_approval":True}
    def can_deploy(self,approved:bool,benchmark_passed:bool)->bool:
        return approved and benchmark_passed
