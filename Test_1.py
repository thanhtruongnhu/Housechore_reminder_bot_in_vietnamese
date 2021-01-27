

class Person:
    def __init__(self, name, service):
        self.name = name
        self.service = service


def initialize():
    global array
    array[0] = Person(['t', 'o', 'a', '2', 'n'], 1)
    array[1] = Person(['v', 'y', '4'], 2)
    array[2] = Person(['t', 'r', 'u', 'o', '7', '2', 'n', 'g'], 3)
    array[3] = Person(['t', 'i', 'e', '6', '1', 'n'], 4)
    array[4] = Person(['n', 'h', 'u', '7'], 5)


if __name__ =="__main__":
    array = [0] * 5
    initialize()
    print(array[0].name)
