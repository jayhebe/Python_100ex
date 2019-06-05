# import datetime


# def day_in_year():
#     return int(datetime.date.today().strftime("%j"))


def day_of_the_year(year, month, day):
    if year % 4 == 0 and year % 400 != 0:
        year_list = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        year_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return sum(year_list[:month]) + day


if __name__ == '__main__':
    print(day_of_the_year(2019, 6, 4))
    # print(day_in_year())
