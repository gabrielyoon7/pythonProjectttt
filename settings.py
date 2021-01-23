#각종 환경 설정을 위한 "값"을 모아놓는 곳.
#다른 파일에서 코드를 읽을 때 숫자가 무슨 의미를 하는지 이해하기 어려운 요소들은 전부 여기에 넣고 관리하기.
#예를들면 RGB값, 블럭 크기와 같은 것은 코드를 읽을 때 갑자기 숫자로 표현해서 읽는 것이 난해해짐
#다른 py에서 이 값을 불러오고싶으면 import settings를 해주고, settings.WHITE와 같은 방법으로 불러올 수 있음

#창 크기
SCREEN_SIZE=(700,700)

#게임 영역 관련

#난이도에 따른 맵 크기 설정 (가로축, 세로축, 지뢰수)
BEGINNER = (5,5,1) #5x5사이즈의 맵 크기에 지뢰 1개
INTERMEDIATE = (10,10,5)
ADVANCED = (20,10,10)

#색상
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
ORANGE = (255,69,0)
GOLD = (255,125,0)
PURPLE = (128,0,128)
CYAN = (0,255,255)
BLACK = (0,0,0)
GRAY = (128, 128, 128)