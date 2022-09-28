from datetime import date
import application.salary
import application.db.people


def main():
    current_date = date.today()
    print(f'Сегодня {current_date}')


if __name__ == '__main__':
    main()
    application.salary.calculate_salary()
    application.db.people.get_employees()
    # application.db.people.sieve_of_Eratosthenes()