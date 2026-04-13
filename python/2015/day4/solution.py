import hashlib
import math

def main():
    text = get_input()
    print(f'Part 1: {search_hash(text, "00000")}')
    print(f'Part 2: {search_hash(text, "000000")}')

def search_hash(text, prefix):
    i = 0
    while True:
        hash = hashlib.md5(f'{text}{i}'.encode()).hexdigest()
        if hash.startswith(prefix):
            return i
        i += 1

def get_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


if __name__ == '__main__':
    main()