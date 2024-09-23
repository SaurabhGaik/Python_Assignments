def outer():
    massage = "I am outer function."
    def inner():
        return massage
    return inner
if __name__ == "__main__":
    inner_function = outer()
    result = inner_function()
    print(result)