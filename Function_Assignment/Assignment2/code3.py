def outer():
    def inner():
        return outer
    return inner
if __name__ =="__main__":
    retobj = outer()
    retinner = retobj()
    print(retinner)