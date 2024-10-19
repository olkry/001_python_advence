

def naive_approach():
    f = open('file.txt', 'w')
    f.write('Ping')
    f.close()

def try_finally_approach():
    f = open('file.txt', 'w')
    try:
        f.write('Ping')
    finally:
        f.close()

def with_approach():
    with open('file.txt', 'w') as f:
        f.write('Ping')

if __name__ == '__main__':
    with_approach()