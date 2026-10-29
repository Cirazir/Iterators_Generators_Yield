class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.outer_cursor = 0   # индекс текущего вложенного списка
        self.inner_cursor = 0   # индекс элемента внутри вложенного списка

    def __iter__(self):
        self.outer_cursor = 0   # сбрасываем состояние, чтобы объект
        self.inner_cursor = 0   # можно было итерировать повторно
        return self

    def __next__(self):
        # Пока не перебрали все вложенные списки
        while self.outer_cursor < len(self.list_of_list):
            inner_list = self.list_of_list[self.outer_cursor]
            # Если во вложенном списке ещё есть элементы — возвращаем следующий
            if self.inner_cursor < len(inner_list):
                item = inner_list[self.inner_cursor]
                self.inner_cursor += 1
                return item
            # Вложенный список закончился — переходим к следующему
            self.outer_cursor += 1
            self.inner_cursor = 0
        # Все элементы перебраны
        raise StopIteration


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
    print('test_1 — OK')