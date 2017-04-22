def outer():
    a = 20

    def inner():
        a = 30
        print('a = ',a)

    inner()
    print('a = ',a)

a = 10
outer()
print('a = ',a)
