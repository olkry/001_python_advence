import contextlib


@contextlib.contextmanager
def saved_file(path, mode):
    try:
        f = open(path, mode)
        yield f
    finally:
        f.close()

with saved_file('some', 'w') as f:
    f.write('Hello')
    f.write('\nAnd bye bye')



