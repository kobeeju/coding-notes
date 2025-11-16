from random import randint


# 1~45 사이의 무작위 번호 n개 생성
def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        number = randint(1, 45)
        if number not in numbers:
            numbers.append(number)

    return numbers


# 일반 당첨 번호 6개와 보너스 번호 1개 리스트 리턴
def draw_winning_numbers():
    winning_numbers = sorted(generate_numbers(6))

    bonus_number = 0
    while True:
        bonus_number = generate_numbers(1)
        if bonus_number not in winning_numbers:
            winning_numbers += bonus_number
            break

    return winning_numbers


# 테스트 코드
print(draw_winning_numbers())
