# 행맨 실행
import random

from rule import Rule # 규칙 써먹기 위해서 !

class Hangman:
    def __init__(self):
        self.country = ["korea", "japan", "china", "canada", "mexico", "france", "italy"]
        self.words = random.choice(self.country)
        self.guess_list = []
        self.life = 6
        self.try_count = 0 
        self.rule = Rule()

    def start_press(self):
        
        press = int(input("행맨을 시작하겠습니다. 1을 입력하세요."))
        if press == 1:  # 게임 시작
            print("_ " * len(self.words))
            return self.game()     

    def game(self):
        while True:
            guess = self.rule.note()

            self.try_count += 1

            if guess in self.words:
                self.guess_list.append(guess)
                print("맞혔습니다.")

            else:
                print("틀렸습니다.")
                self.life -= 1
                print(f"남은 기회 {self.life}")

            for letter in self.words:
                if letter in self.guess_list:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
            print()
            if set(self.guess_list) == set(self.words):
                print("정답입니다!")
                #return True
                return self.try_count, self.life 

            if self.life == 0:
                print("패배")
                #return False
                return self.try_count, self.life
