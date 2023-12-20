# Вопрос №1
#
# На языке Python написать алгоритм (функцию) определения четности целого числа,
# который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути.
# Объяснить плюсы и минусы обеих реализаций.

def is_even(item: int) -> bool:
    return True if bin(item)[-1] == '0' else False


# Вопрос №2
#
# На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO.
# Объяснить плюсы и минусы каждой реализации.

class FifoByList:
    """
    FIFO реализованный через список
    """
    def __init__(self):
        self.queue = []

    def put_(self, item):
        self.queue.append(item)

    def get_(self):
        try:
            return self.queue.pop(0)
        except IndexError:
            pass  # Просто глушу, поскольку нет ясности как реагировать. Писать сообщение "Очередь пуста"?


class FifoByDict:
    """
    FIFO реализованный через словарь.
    """
    def __init__(self):
        self.add_counter = 0
        self.del_counter = 0
        self.queue = {}

    def put_(self, item):
        self.queue[self.add_counter] = item
        self.add_counter += 1

    def get_(self):
        try:
            item = self.queue.pop(self.del_counter)
            self.del_counter += 1
            return item
        except KeyError:
            pass  # Просто глушу, поскольку нет ясности как реагировать. Писать сообщение "Очередь пуста"?


# Вопрос №3
#
# На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам)
# отсортирует данный ей массив чисел.
# Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным).
# Объяснить, почему вы считаете, что функция соответствует заданным критериям.

def quick_sort(list_):
    """
    Реализация алгоритма быстрой сортировки
    """
    if len(list_) <= 1:
        return list_
    else:
        base_item = len(list_) // 2
        lesser = [num for num in list_ if num < list_[base_item]]
        equal = [num for num in list_ if num == list_[base_item]]
        greater = [num for num in list_ if num > list_[base_item]]
        return quick_sort(lesser) + equal + quick_sort(greater)
