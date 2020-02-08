def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

if __name__ == '__main__':
    print(is_leap_year(2096))
    print(is_leap_year(2016))
    print(is_leap_year(2020))
    print(is_leap_year(2022))
    print(is_leap_year(1996))
    print(is_leap_year(1980))