class FlatIterator:

    def __init__(self, main_list):
        self.main_list = main_list
        self.lens = len(self.main_list)
        self.cursor = -1

    def __iter__(self):
        self.cursor += 1
        self.cursor_next = 0
        return self

    def __next__(self):
        if self.cursor_next == len(self.main_list[self.cursor]):
            iter(self)
        if self.cursor == self.lens:
            raise StopIteration
        self.cursor_next += 1
        return self.main_list[self.cursor][self.cursor_next - 1]


def generation(main_list):
    for part in main_list:
        for i in part:
            yield i


class FlatIterator2:

    def __init__(self, multi_list):
        self.multi_list = multi_list

    def __iter__(self):
        self.iterators_queue = []
        self.current_iterator = iter(self.multi_list)
        return self

    def __next__(self):
        while True:
            try:
                self.current_element = next(self.current_iterator)
            except StopIteration:
                if not self.iterators_queue:
                    raise StopIteration
                else:
                    self.current_iterator = self.iterators_queue.pop()
                    continue
            if isinstance(self.current_element, list):
                self.iterators_queue.append(self.current_iterator)
                self.current_iterator = iter(self.current_element)
            else:
                return self.current_element


def generation_hard(o, tree_types=(list, tuple)):
    if isinstance(o, tree_types):
        for value in o:
            for sub in generation_hard(value, tree_types):
                yield sub
    else:
        yield o


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
nested_list2 = [
    [[[[[['a']]]]], 'b', 'c'],
    [[[['d', 'e']]], 'f', 'h', False],
    [1, 2, None],
]

print("Задача 1")
for item in FlatIterator(nested_list):
    print(item)
print()
print("List comprehension")
print()
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
print()
print("Задача 2")
for item in generation(nested_list):
    print(item)
print()
print("Задача 3")
for item in FlatIterator2(nested_list2):
    print(item)
print()
print("Задача 4")
for item in generation_hard(nested_list2):
    print(item)
