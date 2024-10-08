from flask import Flask, request
import sys

app = Flask(__name__)
file_path = '../test/output_file.txt'
units = ['Б', 'Кб', 'Мб', 'Гб', 'Тб']


def get_mean_size(file_data):
    lines = file_data.splitlines()[1:]  # Пропускаем первую строку

    total_size = 0
    file_count = 0

    for line in lines:
        columns = line.split()
        if len(columns) > 8 and columns[0][0] == '-':  # Проверяем, что это файл
            try:
                size = int(columns[4])  # 5-й столбец - это размер файла
                total_size += size
                file_count += 1
            except ValueError:
                continue  # Пропускаем строки с некорректными данными

    if file_count > 0:
        mean_size = total_size / file_count
        return f"Средний размер файла: {mean_size:.2f} байт"
    else:
        return "Нет файлов для обработки."


@app.route('/summary')
def get_summary_rss():
    with open(file_path, 'r') as f:
        lines = f.readlines()[1:]

    total_rss = 0

    for line in lines:
        columns = line.split()
        total_rss += int(columns[5])

    size = total_rss
    unit_index = 0

    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1

    size = round(size, 2)

    return f'Размер = {str(size)} {units[unit_index]}'


@app.route("/mean-size")
def index():
    file_data = request.args.get('data')  # Получаем данные из параметров URL
    if file_data:
        result = get_mean_size(file_data)
    else:
        result = "Нет данных для обработки."
    return result


if __name__ == '__main__':
    app.run(debug=True)
