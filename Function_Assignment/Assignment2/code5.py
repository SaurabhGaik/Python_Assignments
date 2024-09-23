def outer():
    def inner(outer):
        print(outer)
        return inner
    return inner(outer)
if __name__ == "__main__":
    retobj = outer()
    print(retobj)