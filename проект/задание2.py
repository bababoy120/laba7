def process_list(data, a, b):

    if not data:
        return None

    max_element = max(data)

    last_positive_index = -1
    for i, x in enumerate(data):
        if x > 0:
            last_positive_index = i

    sum_before_last_positive = 0
    if last_positive_index != -1:
        sum_before_last_positive = sum(data[:last_positive_index])
    else:
        return None #нет положительных элементов

   
    new_list = [x for x in data if not (a <= abs(x) <= b)]
    num_zeros_to_add = len(data) - len(new_list)
    new_list.extend([0] * num_zeros_to_add)


    return max_element, sum_before_last_positive, new_list

my_list = [1.5, -2.3, 0.8, 5.2, -1.1, 0, 3.7, 2.1, -0.5, 4.9, -3.2]
a = 1
b = 4

result = process_list(my_list, a, b)

if result:
    max_element, sum_before_last_positive, modified_list = result
    print("Максимальный элемент:", max_element)
    print("Сумма элементов до последнего положительного:", sum_before_last_positive)
    print("Измененный список:", modified_list)
else:
    print("Список пуст или не содержит положительных элементов.")


