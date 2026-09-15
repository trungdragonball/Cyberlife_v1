from dataclasses import dataclass
from typing import Protocol

class AIProvider(Protocol):
    def generate(self, prompt:str, context:dict|None=None)->str: ...

class MockProvider:
    def generate(self,prompt,context=None):
        return f"[MOCK CYBER] {prompt}"

class ModelRouter:
    def __init__(self,providers=None):
        self.providers=providers or {"mock":MockProvider()}
    def route(self,preferred="mock")->AIProvider:
        return self.providers.get(preferred,self.providers["mock"])

class AIRuntime:
    def __init__(self,router=None): self.router=router or ModelRouter()
    def run(self,prompt,preferred="mock",context=None):
        return self.router.route(preferred).generate(prompt,context)
