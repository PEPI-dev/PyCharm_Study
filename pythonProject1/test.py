import random

class UpDown:
    def __init__(self):
        self.answer = random.randint(1, 100) # pc가 가지고있는 1~100까지의 무작위 난수값
        self.count = 0 # 몇번째 시도인지 알기위해 0부터 저장

    def challenge(self, guess):
        try:    # 입력값이 1미만 100초과일경우 에러메시지 발생
            guess = int(guess)
        except ValueError:
            raise ValueError('1~100 사이만 입력하세요.')

        if guess < 1 or guess > 100:
            raise ValueError('1~100 사이만 입력하세요.')

        self.count += 1 # 이 함수가 실행될때마다 count 값이 1씩 증가

        if guess < self.answer:  # 난수 값이 플레이어가 입력한 값보다 클경우 아래 메시지
            print('Up!')
        elif guess > self.answer:
            print('Down!')
        else:
            print(f'{self.count}번만의 정답입니다.')

    def playUpDown(self):
        print("UpDown 게임을 시작합니다.")
        while True:
            user_input = input("입력(1~100): ")
            try:
                self.challenge(user_input)
            except ValueError as e:
                print(e)
                continue
            if self.answer == int(user_input):
                break

play = UpDown()
play.playUpDown()