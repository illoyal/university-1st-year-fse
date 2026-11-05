print('Ввод координат первой точки:')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))

print('\nВвод координат второй точки:')
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))
print('')

if x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0:
    print('Yes, 1')
elif x1 < 0 and y1 > 0 and x2 < 0 and y2 > 0:
    print('Yes, 2')
elif x1 < 0 and y1 < 0 and x2 < 0 and y2 < 0:
    print('Yes, 3')
elif x1 < 0 and y1 < 0 and x2 < 0 and y2 < 0:
    print('Yes, 4')
else:
    print('No')