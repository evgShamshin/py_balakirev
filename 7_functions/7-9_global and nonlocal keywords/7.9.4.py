def func1():
    msg = input()


    def func2():
        nonlocal msg
        msg = input()
        print(msg)


    func2()
    print(msg)


func1()