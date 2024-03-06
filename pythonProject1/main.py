# 컴퓨터가 생성한 난수를 맞히는 UpDown 게임을 실행하는 UpDown 클래스 구현해보기
# 1. UpDown 클래스의 인스턴스를 생성하면 1~100 사이의 난수가 인스턴스 변수 answer에 저장되고 인스턴스 생성 후에는 play()메소드만 호출됨
# 2. challenge() 메소드는 사용자의 입력을 처리함. 유효하지않은 정숫값을 입력하면 예외를 발생시키고 '1~100 사이만 입력하세요.' 라는 예외 메시지 출력
# 3. challenge() 메소드가 호출될때 마다 인스턴스 변수 count가 1씩 증가하고 최종적으로 count 변수값으로 몇번의 시도 끝에 성공한지 알수있다.
# 4. 생성된 난수를 맞히기 전까지 프로그램 종료되지 않음
# 5. 정수 대신 다른 자료형의 값은 입력되지 않는다고 가정
# * play()메소드는 challenge()메소드의 결과와 생성된 난수의 값이 일치할 때까지 계속 반복처리하고 난수 생성을 위해 random모듈 import 해야한다.

import random

class Game:
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
            elif int(user_input) == 101:
                self.play()

    def RspGame(self):
        print("가위 바위 보 게임")
        while True:
            computer = random.choice(['가위', '바위', '보'])  # choice()는 리스트 중에서 무작위로 하나의 요소를 추출함
            player = input('--- 가위 바위 보 중 하나를 입력하세요 --- (HOME : 돌아가기)')

            if computer == '가위':
                print('컴퓨터는 가위를 냈습니다.')
                if player == '가위':
                    print('플레이어는 가위를 냈습니다.')
                    print('무승부')
                elif player == '바위':
                    print('플레이어는 바위를 냈습니다.')
                    print('플레이어 승리')
                elif player == '보':
                    print('플레이어는 보를 냈습니다.')
                    print('컴퓨터 승리')
            elif computer == '바위':
                print('컴퓨터는 바위를 냈습니다.')
                if player == '가위':
                    print('플레이어는 가위를 냈습니다.')
                    print('컴퓨터 승리')
                elif player == '바위':
                    print('플레이어는 바위를 냈습니다.')
                    print('무승부')
                elif player == '보':
                    print('플레이어는 보를 냈습니다.')
                    print('플레이어 승리')
            elif computer == '보':
                print('컴퓨터는 보를 냈습니다.')
                if player == '가위':
                    print('플레이어는 가위를 냈습니다.')
                    print('플레이어 승리')
                elif player == '바위':
                    print('플레이어는 바위를 냈습니다.')
                    print('컴퓨터 승리')
                elif player == '보':
                    print('플레이어는 보를 냈습니다.')
                    print('무승부')
                elif player == "home":
                    self.play()

    def play(self):
        while True:
            select_game = int(input('--- 게임 선택 --- \n 1. UpDown \n 2. 가위바위보 \n 3. 종료 '))
            if select_game == 1:
                self.playUpDown()
            elif select_game == 2:
                self.RspGame()
            elif select_game == 3:
                break


game = Game()
game.play()


