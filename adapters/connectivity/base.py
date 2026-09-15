class ConnectivityAdapter:
    def connect(self,target:str)->bool: return False
    def status(self,target:str)->dict: return {"target":target,"online":False}
