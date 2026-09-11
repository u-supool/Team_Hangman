from lllogin import Login
from menu import menu
from history import Nickname_save
from history import History
from game import Hangman


login_manager = Login()
game_menu = menu()
nickname_save = Nickname_save()
history = History()


# 로그인
if login_manager.login() == True:

    while True:

        # 메뉴 실행
        select = game_menu.finish()

        # 1. 게임 시작
        if select == "1":

            # 닉네임 입력
            name = nickname_save.nickname()

            # 행맨 게임 생성
            game = Hangman()

            # 행맨 게임 실행
            try_count, life = game.start_press()

            # 게임 기록 저장
            history.save_history(name, try_count, life)

        # 2. 랭킹 보기
        elif select == "2":

            history.find_leaderboard()

        # 3. 종료
        elif select == "3":

            break