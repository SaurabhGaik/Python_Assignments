# 1. what is the outer of the following function?

def outer():
    def inner():
        return "Hello,I'm the inner function!"
    return inner
retobj = outer()
retinner = retobj()