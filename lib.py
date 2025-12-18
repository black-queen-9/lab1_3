# lib.py
def count_common_elements(*lists):
    """
    Принимает произвольное количество списков.
    Возвращает количество элементов, которые присутствуют во всех переданных списках.
    """
    if not lists:
        return 0

    # Находим пересечение множеств всех списков
    common_set = set(lists[0])
    for current_list in lists[1:]:
        common_set.intersection_update(current_list)

    # Возвращаем количество элементов в пересечении
    return len(common_set)
