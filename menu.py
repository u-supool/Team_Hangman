class menu:
    def __init__(self):
        pass

    def start(self):
        print('게임을 시작하겠습니다!')
        
    def rank(self):
        print('-------------------')
        print('    명예의 전당          ')
        print('-------------------')
        
    def stop(self):
        print('종료하겠습니다.')
        
    def finish (self):
        while True:
            m=input('1.게임 시작 2.랭킹 보기 3.종료하기>>>')
            if m=='1':
                self.start()
                return m
            elif m=='2':
                self.rank()    
                return m
            elif m=='3':
                self.stop()
                return m
