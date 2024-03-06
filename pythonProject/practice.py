import os

wordList = []
filename = 'words.txt'

# CLASS 1
class Words:
  def __init__(self, eng, kor, lev = 1):
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
    self.lev = lev

  def getLev(self):
    return self.lev

# CLASS 2
class WordsDao:
  def __init__(self):
    pass

  def insert(self, word):
    wordList.append(word)

  def selectAll(self):
    return wordList

  def delete(self, word):
    wordList.remove(word)

# CLASS 3
class WordsService:
  def __init__(self):
    self.dao = WordsDao()

  def insertWord(self):
    eng = input('단어를 입력하세요: ')
    kor = input('뜻을 입력하세요: ')
    lev = input('레벨을 입력하세요: ')
    word = Words(eng, kor, lev)
    self.dao.insert(word)
    print("등록되었습니다")

  def printAll(self):
    datas = self.dao.selectAll()
    for data in datas:
      print(f'{data.getEng()} {data.getKor()} {data.getLev()}')
    print('출력을 완료했습니다')

  def saveAll(self):
    datas = self.dao.selectAll()
    with open(filename, 'w') as f:
      for data in datas:
        f.write(f'{data.getEng()}, {data.getKor()}, {data.getLev()}\n')
      print('파일에 저장했습니다')

  def loadData(self):

    if os.path.exists(filename):
      with open(filename, 'r') as f:
        while True:
          line = f.readline()
          if line:
            data = line.strip().split(',')
            word = Words(data[0], data[1], data[2])
            self.dao.insert(word)

          else:
            break
        print('기존 데이터를 불러왔습니다')
        print('='*30)
    else:
      print("파일이 존재하지 않습니다. 새롭게 영어단어들을 저장해서 영어단어장을 만드시오!")

    return self.dao.selectAll()

  def fixData(self):
    word_fix = input('수정할 단어를 선택하세요: ')
    for w in self.dao.selectAll():
      if w.getEng().strip() == word_fix.strip():
        word_fix_meaning = input('수정될 뜻을 입력하세요: ')
        word_fix_level = input('수정될 레벨을 입력하세요: ')
        w.setKor(word_fix_meaning)
        w.setLev(word_fix_level)

        print("수정을 완료했습니다")
        break


  def deleteData(self):
    word_delete = input('삭제할 단어를 선택하세요: ')

    for word in self.dao.selectAll():
      if word.getEng().strip() == word_delete.strip():
        self.dao.delete(word)
        print("위 단어를 리스트에서 삭제했습니다")
        break


# CLASS 4
class Menu:
  def __init__(self):
    self.service = WordsService()
    self.data_loaded = False  # Initialize a flag to track data loading


  def run(self):
    while True:
      try:
        if not self.data_loaded:
          participate = input('영어 단어 만들기를 시작하겠습니까? Y /N \n')
          if participate == 'Y':
            self.service.loadData()
            self.data_loaded = True
          else:
            print('프로그램을 종료합니다')
            break

        menu = int(input('\n 메뉴를 선택하세요: \n1. 등록하기 \n2. 출력하기 \n3. 저장하기 \n4. 수정하기 \n5. 삭제하기  \n6. 종료하기\n'))
        if menu == 1:
          self.service.insertWord()
          print("="*30)
        elif menu == 2:
          self.service.printAll()
          print("="*30)
        elif menu == 3:
          self.service.saveAll()
          print("="*30)
        elif menu == 4:
          self.service.fixData()
          print("="*30)
        elif menu == 5:
          self.service.deleteData()
          print("="*30)
        elif menu == 6:
          print('프로그램을 종료합니다')
          break

      except Exception as e:
        print(e)
        print('다시 입력하세요')

# RUN
start = Menu()
start.run()
