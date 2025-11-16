from random import randint


# 서로 다른 3개의 숫자 뽑기
def generate_numbers():
    numbers = []

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")

    while len(numbers) < 3:
        new_number = randint(0, 9)
        if new_number not in numbers:
            numbers.append(new_number)

    return numbers


print(generate_numbers())
