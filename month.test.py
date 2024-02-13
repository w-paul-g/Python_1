# Months
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# month = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
month = 0
while not month:
    month = (input('Enter a month: '))
    if month == '1':
        print('January')
    elif month == '2':
        print('February')
    elif month == '3':
        print('March')
    elif month == '4':
        print('April')
    elif month == '5':
        print('May')
    elif month == '6':
        print('June')
    elif month == '7':
        print('July')
    elif month == '8':
        print('August')
    elif month == '9':
        print('September')
    elif month == '10':
        print('October')
    elif month == '11':
        print('November')
    elif month == '12':
        print('December')
    else:
        print('Please enter any number between 1 and 12')

