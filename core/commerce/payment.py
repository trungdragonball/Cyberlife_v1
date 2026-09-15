class IdempotencyLedger:
    def __init__(self): self.keys={}
    def accept(self,key,payload):
        if key in self.keys:
            return False,self.keys[key]
        self.keys[key]=payload
        return True,payload

class TransactionState:
    ORDER=("INITIATED","NEGOTIATING","AGREED","CONTRACTED","PAYMENT_PENDING",
           "PAID","DELIVERING","CONFIRMED","SETTLED")
