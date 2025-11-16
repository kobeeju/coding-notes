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
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


# 일치하는 당첨 번호의 개수 리턴
def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for number in numbers:
        if number in winning_numbers:
            count += 1

    return count


# 당첨금 확인
def check(numbers, winning_numbers):
    normal_winning_numbers = winning_numbers[:6]
    bonus_winning_numbers = winning_numbers[6]
    prize = 0

    count = 0
    for number in numbers:
        if number in normal_winning_numbers:
            count += 1

    if count == 6:
        prize = 1000000000
    elif count == 5 and bonus_winning_numbers in numbers:
        prize = 50000000
    elif count == 5:
        prize = 1000000
    elif count == 4:
        prize = 50000
    elif count == 3:
        prize = 5000

    return prize


# 테스트 코드
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))
