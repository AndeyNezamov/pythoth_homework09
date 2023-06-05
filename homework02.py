import numpy

array = numpy.random.randint(0,2, size=(5,5))
print(array)

uniq_rows = numpy.unique(array, axis=0)
uniq_rows_len = uniq_rows.shape[0]
array_len = array.shape[0]
if array_len == uniq_rows_len:
    print('одинаковых строк нет')
else:
    print('Есть одинаковые строки')