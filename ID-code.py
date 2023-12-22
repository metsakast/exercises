"""ID code."""


def is_valid_birth_number(year_number: int):
    """Check if given value is correct for birth number in ID code."""
    if 0 <= year_number <= 99:
        return True
    else:
        return False


def is_valid_gender_number(gender_number: int):
    """Check if given value is correct for birth number in ID code."""
    if 0 < gender_number < 7:
        return True
    else:
        return False


def get_gender(gender_number: int):
    """Check if given value is correct for birth number in ID code."""
    if gender_number == 1 or gender_number == 3 or gender_number == 5:
        return "male"
    else:
        return "female"


def is_valid_year_number(year_number: int) -> bool:
    """Check if given value is correct for year number in ID code."""
    # Write your code here
    if 0 <= year_number < 100:
        return True
    else:
        return False


def is_valid_month_number(month_number: int) -> bool:
    """Check if given value is correct for month number in ID code."""
    # Write your code here
    if 0 < month_number < 13:
        return True
    else:
        return False


def is_valid_serial_number(serial_number: int) -> bool:
    """Check if given value is correct for birth number in ID code."""
    # Write your code here
    if 0 < serial_number:
        return True
    else:
        return False


def get_full_year(gender_number: int, year_number: int) -> int:
    """Define the 4-digit year when given person was born."""
    # Write your code here
    if gender_number == 1 or gender_number == 2:
        full_year_number = year_number + 1800
    elif gender_number == 3 or gender_number == 4:
        full_year_number = year_number + 1900
    elif gender_number == 5 or gender_number == 6:
        full_year_number = year_number + 2000
    return full_year_number


def is_leap_year(full_year_number: int):
    """Find the place where the person was born."""
    if full_year_number % 400 == 0:
        return True
    elif full_year_number % 4 == 0 and full_year_number % 100 != 0:
        return True
    else:
        return False


def get_birth_place(birth_number: int) -> str:
    """Find the place where the person was born."""
    # Write your code here
    if birth_number == 0:
        return "Wrong input!"
    elif 1 <= birth_number <= 10:
        return "Kuressaare"
    elif 11 <= birth_number <= 20:
        return "Tartu"
    elif 21 <= birth_number <= 220:
        return "Tallinn"
    elif 221 <= birth_number <= 270:
        return "Kohtla-Järve"
    elif 271 <= birth_number <= 370:
        return "Tartu"
    elif 371 <= birth_number <= 420:
        return "Narva"
    elif 421 <= birth_number <= 470:
        return "Pärnu"
    elif 471 <= birth_number <= 710:
        return "Tallinn"
    else:
        return "undefined"


if __name__ == '__main__':
    print("\nGender number:")
    for i in range(9):
        print(f"{i} {is_valid_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False

    print("\nGet gender:")
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"

    print("\nYear number:")
    print(is_valid_year_number(100))  # -> False
    print(is_valid_year_number(50))  # -> True

    print("\nMonth number:")
    print(is_valid_month_number(2))  # -> True
    print(is_valid_month_number(15))  # -> False

    print("\nBorn order number:")
    print(is_valid_serial_number(0))  # -> False
    print(is_valid_serial_number(1))  # -> True
    print(is_valid_serial_number(850))  # -> True

    print("\nLeap year:")
    print(is_leap_year(1804))  # -> True
    print(is_leap_year(1800))  # -> False

    print("\nGet full year:")
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001

    print("\nChecking where the person was born")
    print(get_birth_place(0))  # -> "Wrong input!"
    print(get_birth_place(1))  # -> "Kuressaare"
    print(get_birth_place(273))  # -> "Tartu"
    print(get_birth_place(220))  # -> "Tallinn"
