import subprocess

from colorama.win32 import STDERR


def run_program():
    # res = subprocess.run(['python', 'test_program.py']) # поток ошибки печатается
    # res = subprocess.run(['python', 'test_program.py'], capture_output=True) без вывода в консоль, как делает программа
    # res = subprocess.run(['python', 'test_program.py'], stderr=subprocess.STDOUT) # поток ошибки перенаправляется в вывод
    res = subprocess.run(['python', 'test_program.py'], input=b'some input\nother input') # передача инпута

    print(res)

if __name__ == '__main__':
    run_program()