import pyautogui
import time
import schedule

# First run (Need to determine the first run,
# because we only assign people tasks
# in the first run)

# toan = vy = truong = tien = nhu = []
# array = [toan, vy, truong, tien, nhu]


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


def print_name(obj):
    # PRINT NAME
    for x_id, x in enumerate(obj):
        if x_id == 0:
            pyautogui.keyDown('shift')
            pyautogui.press(x)
            pyautogui.keyUp('shift')
        else:
            pyautogui.press(x)


def text(obj):
    for x in obj:
        pyautogui.press(x)


def print_full_text():
    size = 6
    data = [0] * size
    default_filename = 'text_'
    suffix = '.txt'

    # INSERT & PARSE TEXT FROM TXT FILES
    for i in range(1, size+1):
        j = str(i)
        filename = default_filename + j + suffix
        ray = []
        with open(filename, 'r') as file:
            temp = file.read().replace('\n', '')
        for k in temp:
            ray.append(k)
        ray = tuple(ray)
        data[i - 1] = ray

    # COMBINE ALL TEXT AND NAME
    for i in range(0, size):
        if i == 0:
            text(data[i])
        else:
            print_name(array[i-1].name)
            text(data[i])

    pyautogui.press('enter')


def main():
    global run, array
    if run == 0:
        initialize()
    else:
        array = array[-1:] + array[:-1]

    print_full_text()
    run += 1


if __name__ == "__main__":
    run = 0
    array = [0] * 5
    schedule.every().wednesday.at("09:17").do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)



