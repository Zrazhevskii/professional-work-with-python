from datetime import datetime


def parametrized_decor(params):
    def decorator(some_function):
        def new_function(*args, **kwars):
            log_date = datetime.now().strftime("%d %B %Y  time %H:%M:%S")
            function = some_function(*args, **kwars)
            result = f'Вызвана функция {some_function.__name__}, время вызова функции {log_date}.\n' \
                     f'Вводные данные: {args}, {kwars}\n' \
                     f'Результат выполнения функции {some_function.__name__} - {function}\n'

            with open('date_log.txt', 'w', encoding='utf-8') as f:
                f.write(result)
            return function

        return new_function

    return decorator