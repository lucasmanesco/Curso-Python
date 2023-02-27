# try, except, else, finally

try:
    print('Open file.')
    8/0

except ZeroDivisionError:
    print('Divison by zero.')

else:
    print('No error.')

finally: # sempre será executado independente das exceções
    print('Close file.')
