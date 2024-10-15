
from typing import List, Optional

from flask import Flask, request

app = Flask(__name__)


# @app.route("/search/<path:args>")
# /search/3/12/2/1/1/999*/2G/4G/1/-100
@app.route("/search/", methods=["GET"])
def search():
    cell_tower_ids: List[int] = request.args.getlist("cell_tower_id", type=int)
    if not cell_tower_ids:
        return f"You must specify at least one cell_tower_id", 400

    phone_prefixes: List[str] = request.args.getlist("phone_prefix")
    protocols: List[str] = request.args.getlist("protocol")
    signal_level: Optional[float] = request.args.get("signal_level", type=float, default=None)

    return (
        f"Search for {cell_tower_ids} cell tower. Search criteria: "
        f"phone_prefix={phone_prefixes}, "
        f"protocols={protocols}, "
        f"signal_level={signal_level}"
    )


# Реализуйте flask endpoint, который принимает на вход массив чисел, и возвращает их сумму и произведение. Проверьте его работу.
@app.route("/calculate", methods=["GET"])
def calculate():
    numbers: List[int] = request.args.getlist("num", type=int)

    if not numbers:
        return f"error: Input any numbers", 400

    sum_num = sum(numbers)
    prod_num = 1
    for numb in numbers:
        prod_num *= numb

    return (
        f'Сумма всех введенных чисел = {sum_num}'
        f'\nПроизведение всех введенных чисел = {prod_num}'
    )


# Реализуйте flask endpoint, который принимает на вход 2 массива A и B и возвращает все возможные комбинации пар чисел a и b, где a — число из массива A, а b — число из массива B.
@app.route("/combinations", methods=["GET"])
def combinations():
    array_a = request.args.getlist("A", type=int)
    array_b = request.args.getlist("B", type=int)

    if not array_a or not array_b:
        return "error: Both arrays A and B must be provided with numbers", 400

    combinations_list = []
    for a in array_a:
        for b in array_b:
            combinations_list.append((a, b))

    result = "\n".join(f"({a},{b})" for a, b in combinations_list)

    return f"<pre>Список всех пар: \n{result}</pre>"


#Реализуйте flask endpoint, принимающий на вход отсортированный массив A и число X, и возвращающий число из массива A, максимально близкое к числу X.
@app.route('/closest', methods=['GET'])
def closest_number():
    array_a: List[int] = request.args.getlist("A", type=int)
    x: int = request.args.get("X", type=int)

    if not array_a or x is None:
        return "Введите данные", 400

    closest = min(array_a, key=lambda num: abs(num - x))
    return f'Ближайшее число в списке: {closest}'



if __name__ == '__main__':
    # /search/?cell_tower_id=1&cell_tower_id=2&cell_tower_id=3&phone_prefix=999*&phone_prefix=921*&signal_level=-100
    app.run(debug=True)
    # /calculate?num=1&num=2&num=3&num=4&num=5&num=6&num=7&num=1&num=8&num=9&num=10
    # /combinations?A=1&A=2&A=3&A=4&A=5&B=6&B=7&B=8&B=9&B=10
    # /closest?A=10&A=20&A=30&A=40&A=50&X=26
