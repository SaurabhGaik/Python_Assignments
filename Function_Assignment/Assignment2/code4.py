def outer():
    def innner():
        return outer
    return innner
if __name__ == "__main__":
    retobj = outer()
    retinner = retobj()
    print(retinner)
    