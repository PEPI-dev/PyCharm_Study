# 메이플 캐릭터 생성 프로그램

# -------- 프로그램 실행 ------------
# 1. input() 캐릭터를 생성하시겠습니까? (Y/N) N누를시 '프로그램을 종료합니다.'
# 2. input() 원하시는 소속을 선택하시오 (모험가,시그너스 기사단,레지스탕스,영웅,노바,레프,아니마,제로)
# 3. input() ex ) {영웅}을 선택하셨군요! 그럼 직업을 선택해주세요! (아란,에반,메르세데스,팬텀,은월)
# 4. print() {선택 직업}을 생성 하였습니다.
# 5. 바탕화면의 소속 폴더안에 직업폴더가 생성되고 해당 하는 직업폴더에 (소속명)_(직업명).txt 파일이 생성. copy 형식 사용


import os
import glob
import zipfile
import shutil
import fnmatch

os.getcwd()

target_path = ['.바탕 화면/directory_management/메이플직업군']

directory_path = []
for dir_name in glob.glob(os.path.join(target_path, '******/*.zip'), recursive = True):
    directory_path.append(dir_name)
    print(directory_path)