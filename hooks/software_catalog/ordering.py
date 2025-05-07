from math import inf


class Order:
    def __init__(self, values):
        self.__ranks = {value.lower(): rank
                        for rank, value
                        in enumerate(values)}

    def __rank(self, value):
        return self.__ranks.get(str(value).lower(), inf)

    def less_than(self, this, that):
        return self.__rank(this) < self.__rank(that)


class OrderedValue:
    def __init__(self, value, sequence: [str]):
        self.__value = value
        self.__order = Order(sequence)

    def __lt__(self, other):
        return self.__order.less_than(self, other)

    def __str__(self):
        return self.__value
