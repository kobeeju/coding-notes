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


# 사용자로부터 3개의 추측 숫자를 입력받음
def take_guess():
    guesses = []

    i = 1
    while i <= 3:
        guess = int(input(f"{i}번째 숫자를 입력하세요: "))
        if guess < 0 or guess > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif guess in guesses:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            guesses.append(guess)
            i += 1

    return guesses


print(take_guess())
