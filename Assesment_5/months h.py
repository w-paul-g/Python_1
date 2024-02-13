# Months
month = 0
# while 1 <= month <= 12:
while month == 0:
    try:
        month = int(input('Enter a month: '))
        if month == 1:
            print('January')
        elif month == 2:
            print('February')
        elif month == 3:
            print('March')
        elif month == 4:
            print('April')
        elif month == 5:
            print('May')
        elif month == 6:
            print('June')
        elif month == 7:
            print('July')
        elif month == 8:
            print('August')
        elif month == 9:
            print('September')
        elif month == 10:
            print('October')
        elif month == 11:
            print('November')
        elif month == 12:
            print('December')
        else:
            print('Please enter any number between 1 and 12')
    except ValueError:
        print('Please enter any number between 1 and 12')
