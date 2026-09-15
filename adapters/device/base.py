class DeviceAdapter:
    def capabilities(self)->dict: return {}
    def connect(self,device_id:str)->bool: return False
    def execute(self,device_id:str,action:str,payload:dict|None=None)->dict:
        raise NotImplementedError
