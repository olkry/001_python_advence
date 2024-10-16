import shlex

# Клас помогающий распарсить команду юникс для метода subprocess.run пайтона
command_line = 'python test_program.py'
command_line2 = 'python block_005_Linux_02/simple_app.py &>/dev/null &'

args = shlex.split(command_line)
args2 = shlex.split(command_line2)


if __name__ == '__main__':
    print(args)
    print(args2)