import time

def print_name():
    print(f'__name__ == {__name__}')

def print_time():
    print(f'Now is {time.ctime()}')


if __name__ == '__main__':
    print_name()
    print_time()

