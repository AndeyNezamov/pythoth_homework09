import numpy as np

size = np.random.randint(1,10, size=2)
array = np.random.randint(1,20, size=(size[0], size[1]))
print(array)
max_index = np.unravel_index(np.argmax(array), array.shape)
min_index = np.unravel_index(np.argmin(array), array.shape)
print(f"Индексы максимального элемента: {max_index}")
print(f"Индексы минимального элемента: {min_index}")
print(f"Главная диагональ массива:\n {np.diag(array)}" )