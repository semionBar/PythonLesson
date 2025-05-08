def check_leap_year(year):
    try:
        year = int(year)  # Преобразуем входные данные в целое число
        if year < 0:  # Отрицательные годы считаем некорректными
            return 3
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 1  # Год високосный
        else:
            return 2  # Год невисокосный
    except ValueError:
        return 3  # Некорректный ввод (нечисловое значение)

def test_check_leap_year():
    # Тесты для годов, которые являются високосными
    assert check_leap_year(2020) == 1, "Error: 2020 is a leap year"
    assert check_leap_year(2000) == 1, "Error: 2000 is a leap year"
    assert check_leap_year(1600) == 1, "Error: 1600 is a leap year"
    assert check_leap_year(2400) == 1, "Error: 2400 is a leap year"

    # Тесты для годов, которые не являются високосными
    assert check_leap_year(1900) == 2, "Error: 1900 is not a leap year"
    assert check_leap_year(2100) == 2, "Error: 2100 is not a leap year"
    assert check_leap_year(2021) == 2, "Error: 2021 is not a leap year"
    assert check_leap_year(2019) == 2, "Error: 2019 is not a leap year"

    # Тесты для крайних случаев
    assert check_leap_year(0) == 1, "Error: Year 0 is a leap year (by definition)"
    assert check_leap_year(-4) == 3, "Error: Year -4 is a leap year"
    assert check_leap_year(-100) == 3, "Error: Year -100 is not a leap year"
    assert check_leap_year(-400) == 3, "Error: Year -400 is a leap year"    
    assert check_leap_year("тест") == 3, "Error: String cannot be leap or non leap"

    print("All tests passed!")


test_check_leap_year()