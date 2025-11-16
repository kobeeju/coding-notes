from random import randint


def generate_numbers():
    numbers = []

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")

    while len(numbers) < 3:
        number = randint(0, 9)
        if number in numbers:
            continue
        else:
            numbers.append(number)

    return numbers


print(generate_numbers())
