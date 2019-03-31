def adder(x):
    def wrapper(y):
        return x+y
    return wrapper


def adder2(function):
    print("hello")
    return function

@adder2
def test():
    print("Hello")


def test2(x):
    number=lambda x:x+2
    print (number(3))


if __name__ =="__main__":
    adder5=adder(5)
    adder5(10)
    adder5(6)

    # test()
    test2(3)