import random
import time

arr = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z',
    '!', '@', '#', '$', '%', '&', '*'
]

def pass_gen(size):
    random.seed(int(time.time()))
    password = ''.join(random.choice(arr) for _ in range(size))
    print(password)

def main():
    pass_size = int(input("Введите размер пароля: "))
    pass_gen(pass_size)

if __name__ == "__main__":
    main()
