class SavedFile:
    def __init__(self, path, mode='r'):
        self.name = path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, type, value, traceback):
        # if self.file:
        #     self.file.close()  #стандартное закрытие без ошибки
        print(f'Exception {type} has been handled')  # Выкинет сообщение ошибки и продолжит работу
        self.file.close()
        return True


if __name__ == '__main__':
    with SavedFile('some', 'w') as f:
        f.undefind('hello')
