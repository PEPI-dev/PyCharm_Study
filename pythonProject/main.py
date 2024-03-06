import os

wordList = [] # 단어 저장 변수
filename = 'words.txt'


class Words:
    def __init__(self, eng, kor, lev=1):
        self.eng = eng
        self.kor = kor
        self.lev = lev
    def setEng(self, eng):
        self.eng = eng
    def getEng(self):
        return self.eng
    def setKor(self, kor):
        self.kor = kor
    def getKor(self):
        return self.kor
    def setLev(self, lev):
        self.eng = lev
    def getLev(self):
        return self.lev

class WordsDao:
    def __init__(self):
        pass

    def insert(self,word):
        wordList.append(word)

    def selectAll(self):
        return wordList



class WordsService:
    def __init__(self):
        self.dao = WordsDao()
    def insertWord(self):
        eng = input('단어를 입력하세요: ')
        kor = input('뜻을 입력하세요: ')
        lev = input('레벨을 입력하세요: ')
        word = Words(eng, kor, lev)
        self.dao.insert(word)

    def removeWord(self):
        del_word = input('삭제할 단어 : ')

        found = False
        for word in wordList:
            if word.getEng() == del_word:
                wordList.remove(word)
                print(f'{del_word} 삭제 완료!')
                found = True
                break

        if not found:
            print(f'리스트에 {del_word} 라는단어는 없습니다.')

    def editWord(self):
        edit_word = input('수정할 단어 : ')  # 수정할 단어를 입력받아 edit_word 변수에 저장

        found = False   # found 변수를 False로 선언하는데 이 변수는 나중에 단어를 찾았는지 여부를 찾을때 씀
        for word in wordList:
            if word.getEng() == edit_word:  # word의 영어 단어를 가져와서 edit_word와 비교하고 만약 일치하는 단어를 찾으면 아래 코드실행
                new_meaning = input('업데이트 할 뜻을 입력하세요: ')
                word.setKor(new_meaning)

                new_level = input('업데이트 할 레벨을 입력하세요: ')
                word.setLev(new_level)

                found = True
                print(f'{word.getEng()}단어 업데이트 완료.')

                break

        if not found:
            print('찾는 단어가 없습니다.')

    def loadDataFromFile(self):
        if os.path.exists(filename):  # Check if the file exists
            with open(filename, 'r') as f:
                while True:
                    line = f.readline()
                    if line:
                        data = line.strip().split(',')  # 읽은 줄을 공백과 쉼표로 분리하여 데이터를 추출하고, data 변수 저장
                        word = Words(data[0], data[1], data[2]) # 추출된 데이터에 대한 Words 클래스의 객체를 생성하고 word 변수에 할당, data[0]은 단어의 영어 부분, data[1]은 뜻, data[2]는 레벨
                        self.dao.insert(word)
                    else:
                        break
            print('데이터를 불러왔습니다')

    def printAll(self):
        datas = self.dao.selectAll()
        for data in datas:
            # apple : 사과(레벨 1)
            print(data.getEng() + ' : ' + data.getKor() + '(레벨 ' + data.getLev() + ')')
    def saveAll(self):
        datas = self.dao.selectAll()
        with open(filename, 'w') as f:
            for data in datas:
                f.write(f'{data.getEng()},{data.getKor()},{data.getLev()}\n')
            print('파일에 저장했습니다')


class Menu:
    def __init__(self):
        self.service = WordsService()
        self.service.loadDataFromFile()

    def run(self):
        while True:
            try:
                menu = int(input('1. 등록 2. 출력 3. 저장 4. 수정6오기 5. 삭제하기 6. 종료'))
                if menu == 1:
                    self.service.insertWord()

                elif menu == 2:
                    self.service.printAll()

                elif menu == 3:
                    self.service.saveAll()

                elif menu == 4:
                    self.service.editWord()

                elif menu == 5:
                    self.service.removeWord()

                elif menu == 6:
                    print('종료')
                    break
            except Exception as e:
                print(e)
                print('다시 입력')

start = Menu()
start.run()