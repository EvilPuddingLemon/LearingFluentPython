class LookingGlass:

    def __enter__(self):  # 除了self外不穿如其它参数
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        # 为 sys.stdout.write 打猴子补丁，替换成自己编写的方法。
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys
        sys.stdout.write = self.original_write
        # 还原成原来的 sys.stdout.write 方法。
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True

if __name__ == '__main__':
    with open('s15_1.py') as fp:
        src = fp.read(60)

    print(len(src))
    print(fp)
    print(fp.closed, fp.encoding)
    try:
        fp.read(60)
    except ValueError as e:
        print("\033[31;1m"+str(e)+"\033[0m")

    with LookingGlass() as what:
        print('Alice, Kitty and Snowdrop')
        print(what)
    print(what)
    print('Back to normal.')

    # 在 with 块之外使用 LookingGlass 类
    manager = LookingGlass()
    print(manager)
    monster = manager.__enter__()
    print(monster == 'JABBERWOCKY')
    print(monster)
    print(manager)
    manager.__exit__(None, None, None)
    print(monster)