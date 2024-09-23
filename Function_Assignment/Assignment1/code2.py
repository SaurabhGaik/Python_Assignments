# 2. What is the output of the following function? (dry run compulsor)
def outer():
    def inner():
        return "Hello, I'm the inner function!"

    return inner

retObj = outer()
retInner = retObj()
print(retInner)