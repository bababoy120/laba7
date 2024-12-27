def replace_negative_with_zeros_map(data):
    """Заменяет отрицательные элементы списка на нули и возвращает их количество."""
    new_list = list(map(lambda x: 0 if x < 0 else x, data))
    replaced_count = sum(1 for x in data if x < 0)  #Подсчет замен
    return new_list, replaced_count


my_list = [1, -2, 3, -4, 5, -6, 0, 7, -8, 9]
modified_list, replaced_count = replace_negative_with_zeros_map(my_list)
print("Измененный список:", modified_list)
print("Количество замененных элементов:", replaced_count)
