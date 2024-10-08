from get_social_status import get_social_status

# def test_check_social_status():
#     age = 8
#     correct_answer = 'ребенок'
#     function_answer = get_social_status(age)
#
#     if correct_answer == function_answer:
#         print('Всё верно')
#     else:
#         print('Не проходит')

def test_check_baby_status():
    age = 12
    correct_answer = 'ребенок'
    function_answer = get_social_status(age)
    assert correct_answer == function_answer, 'Not matched'

def test_check_adult_status():
    age = 33
    correct_answer = 'взрослый'
    function_answer = get_social_status(age)
    assert correct_answer == function_answer, 'Not matched'


if __name__ == '__main__':
    test_check_baby_status()
    test_check_adult_status()