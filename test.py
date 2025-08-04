import time


def odlicz_do_5():
    for i in range(1, 6):
        yield i

for liczba in odlicz_do_5():
    print(liczba)
    time.sleep(1)
