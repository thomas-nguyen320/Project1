def add(values):
    ans = values[0]
    for i in values[1::]:
        ans +=i
    return ans
def subtract(values):
    ans = values[0]
    for i in values[1::]:
        ans -=i
    return ans
def multiply(values):
    ans = values[0]
    for i in values[1::]:
        ans *=i
    return ans
def divide(values):
    ans = values[0]
    for i in values[1::]:
        ans /=i
    return ans