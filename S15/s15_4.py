import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    orignial_wirte = sys.stdout.write

    def reverse_write(text):
        orignial_wirte(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = orignial_wirte
        if msg:
            print(msg)

if __name__ == '__main__':
    with looking_glass() as what:
        print('Alice, Kitty and Snowdrop')
        print(what)
    print(what)

    manager = looking_glass()
    print(manager)
    monster = manager.__enter__()
    print(monster == 'JABBERWOCKY')
    print(monster)
    print(manager)
    manager.__exit__(None, None, None)
    print(monster)

    import csv
    from PythonTest.S15.inplace_file_rewriting import inplace

    with inplace('test.txt', 'r', newline='') as (infh, outfh):
        reader = csv.reader(infh)
        writer = csv.writer(outfh)

        for row in reader:
            row += ['new', 'columns']
            writer.writerow(row)