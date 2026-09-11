class Login:

    def __init__(self):
        self.correct_id = "admin"
        self.correct_pw = "1234"
        self.count = 0

    def login(self):

        while self.count < 3:

            user_id = input("ID를 입력하세요: ")
            user_pw = input("PASSWORD를 입력하세요: ")

            if user_id == self.correct_id and user_pw == self.correct_pw:
                print("로그인 되었습니다.")
                return True

            else:
                self.count = self.count + 1
                print("ID 또는 PASSWORD가 일치하지 않습니다.")

        print("3회 실패하여 프로그램을 종료합니다.")
        return False