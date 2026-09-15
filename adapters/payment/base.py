class PaymentAdapter:
    def create_payment(self,amount:int,currency:str,reference:str)->dict: raise NotImplementedError
    def verify_callback(self,payload:dict)->bool: return False
