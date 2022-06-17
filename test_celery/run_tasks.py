from .tasks import longtime_add
import time

if __name__ == '__main__':

    print('Inside Task Worker')

    with open('files/million.txt', 'r') as source:
        for line in source:
            url = 'https://' + line.rstrip()
            print(url)
            result = longtime_add.delay(url)
            print('Task Result: %s', result.result)
