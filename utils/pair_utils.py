class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


def create_pair(f, s):
    return Pair(first=f, second=s)
