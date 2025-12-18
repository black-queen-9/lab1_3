# test.py
from lib import count_common_elements

# Тест 1: Обычный случай
list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5]
list3 = [3, 4, 5, 6]
# Общие элементы: 3, 4. Количество: 2
assert count_common_elements(list1, list2, list3) == 2, "Тест 1 не пройден"
print("Тест 1 пройден!")

# Тест 2: Нет общих элементов
list4 = [1, 2, 3]
list5 = [4, 5, 6]
assert count_common_elements(list4, list5) == 0, "Тест 2 не пройден"
print("Тест 2 пройден!")

# Тест 3: Все элементы общие
list6 = ['a', 'b']
list7 = ['a', 'b']
assert count_common_elements(list6, list7) == 2, "Тест 3 не пройден"
print("Тест 3 пройден!")

# Тест 4: Передаётся один список
list8 = [10, 20, 30]
assert count_common_elements(list8) == 3, "Тест 4 не пройден"  # Все 3 элемента "общие" для одного списка
print("Тест 4 пройден!")

# Тест 5: Пустые списки
list9 = []
list10 = [1, 2]
# Общих элементов с пустым списком нет -> 0
assert count_common_elements(list9, list10) == 0, "Тест 5 не пройден"
print("Тест 5 пройден!")

print("\nВсе тесты успешно пройдены!")
