def mobile_biling(call,data):
    call_rate = call * 2
    data_rate = data * 50
    return call_rate + data_rate
def discount(amount):
    if amount <= 500:
        return amount * 0.03
    elif amount <= 800:
        return amount * 0.04
    elif amount <= 1000:
        return amount * 0.05
    elif amount > 1000:
        return amount * 0.06
def vatable(amount):
    vat = amount * 0.07
    return vat + amount
