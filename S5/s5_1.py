def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)
fact = factorial
if __name__ == '__main__':
    print(factorial(42))
    print(factorial.__doc__)
    print(factorial)

    # 通过别的名称使用函数，再把函数作为参数传递
    print(fact)
    print(fact(5))
    print(map(factorial, range(11)))
    print(list(map(fact, range(11))))