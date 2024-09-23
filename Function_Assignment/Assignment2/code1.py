# code1
def add(X):
    def inner(Y):
        return X*Y
    return inner
if __name__ == '__main__':
    add_3 = add(3)
    result = add_3(7)
    print(result)
