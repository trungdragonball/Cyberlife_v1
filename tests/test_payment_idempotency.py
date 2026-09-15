from core.commerce.payment import IdempotencyLedger

def test_payment_idempotency():
    l=IdempotencyLedger()
    ok,_=l.accept("k1",{"amount":100})
    again,payload=l.accept("k1",{"amount":100})
    assert ok is True
    assert again is False
    assert payload["amount"]==100
