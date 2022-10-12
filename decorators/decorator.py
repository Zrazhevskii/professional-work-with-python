from datetime import datetime


def decorator(some_function):
    def new_function(some_list):
        log_date = datetime.now().strftime("%d %B %Y  time %H:%M:%S")
        function = some_function(some_list)
        result = f'Вызвана функция {some_function.__name__}, время вызова функции {log_date}.\n' \
                 f'Вводные данные: {some_list}\n' \
                 f'Результат выполнения функции {some_function.__name__} - {function}\n'

        with open('date_log.txt', 'a', encoding='utf-8') as f:
            f.write(result)
        return some_function

    return new_function
