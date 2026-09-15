class StorageAdapter:
    def put(self,key:str,data:bytes)->str: raise NotImplementedError
    def get(self,key:str)->bytes: raise NotImplementedError
    def delete(self,key:str)->None: raise NotImplementedError
