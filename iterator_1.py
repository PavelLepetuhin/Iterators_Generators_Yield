class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.flatten_list = self.flatten()

    def flatten(self):
        for sublist in self.list_of_list:
            for item in sublist:
                yield item

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.flatten_list)
        except StopIteration:
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
    print('All tests passed!')
