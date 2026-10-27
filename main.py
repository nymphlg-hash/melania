print("Hello, World, My Honey!")

import random


def play_game(max_number=100, max_tries=7):
    answer = random.randint(1, max_number)
    print(f"1부터 {max_number} 사이의 숫자를 맞혀 보세요! (기회: {max_tries}번)")

    for attempt in range(1, max_tries + 1):
        try:
            guess = int(input(f"[{attempt}/{max_tries}] 숫자 입력: "))
        except ValueError:
            print("숫자만 입력해 주세요.")
            continue

        if guess < answer:
            print("더 큰 숫자예요.")
        elif guess > answer:
            print("더 작은 숫자예요.")
        else:
            print(f"정답! {attempt}번 만에 맞혔어요.")
            return

    print(f"아쉬워요. 정답은 {answer}였어요.")


if __name__ == "__main__":
    play_game()
