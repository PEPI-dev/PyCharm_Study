import os

# 캐릭터 그룹
groups = {
    "모험가": ["전사", "궁수", "마법사", "도적", "해적", "듀얼블레이드", "패스파인더", "캐논슈터"],
    "시그너스": ["소울마스터", "플레임위자드", "나이트워커", "스트라이커", "윈드브레이커", "미하일"],
    "영웅": ["아란", "에반", "메르세데스", "루미너스", "팬텀", "은월"],
    "레지스탕스": ["블래스터", "배틀메이저", "와일드헌터", "메카닉", "제논"],
    "데몬": ["데몬슬레이어", "데몬어벤져"],
    "노바": ["카이저", "카데나", "엔젤릭버스터", "카인"],
    "레프": ["아델", "아크", "칼리", "일리움"],
    "아니마": ["라라", "호영"],
    "초월자": ["제로"]
}


def create_character():

    print("--- 다음 중 하나의 그룹을 선택해주세요 ---")
    print(", ".join(groups.keys()))

    group = input(": ")
    if group not in groups:      # 사용자가 입력한 그룹명이 딕셔너리에 포함하는지 검사하고 포함 하지않으면 종료
        print("유효한 그룹을 선택해주세요.")
        return


    print(f"--- {group} 소속의 캐릭터 리스트 ---")
    print(", ".join(groups[group]))

    character = input(f"--- {group}에 속한 하나의 캐릭터를 선택해주세요 --- ")
    if character not in groups[group]:
        print("유효한 캐릭터를 선택해주세요.")
        return


    directory_name = group  # 선택한 캐릭터 그룹을 기반으로 폴더이름 생성. 예를 들어 "모험가" 그룹을 선택했다면, directory_name 변수에 "모험가"라는 문자열 저장


    os.makedirs(directory_name, exist_ok=True) # directory_name 에 저장된 폴더 이름사용해서 폴더 생성 하고
    # 'exist_ok=True 옵션은 이미 해당 디렉토리가 존재하는 경우에도 오류를 발생시키지 않고 계속 진행하도록 허용.


    file_name = f"{group}_{character}.txt" # 캐릭터 정보 저장할 그룹_캐릭터명.txt 파일생성


    with open(os.path.join(directory_name, file_name), "w") as character_file:
        character_file.write(f"소속: {group}\n")
        character_file.write(f"캐릭터: {character}\n")

    print("캐릭터가 생성되었습니다.")


def delete_character():

    print("--- 생성된 캐릭터 목록 ---")
    for group, characters in groups.items():
        for character in characters:
            file_name = f"{group}_{character}.txt"
            if os.path.exists(os.path.join(group, file_name)):
                print(f"{group} - {character}")

    # 삭제할 캐릭 선택
    target_character = input("삭제할 캐릭터를 입력해주세요 (예: 모험가 - 전사): ")

    # 입력 형식 검사
    if " - " not in target_character:
        print("올바른 형식으로 입력해주세요 (소속 - 캐릭터).")
        return

    group, character = target_character.split(" - ")

    if group not in groups or character not in groups[group]:
        print("유효한 캐릭터를 선택해주세요.")
        return

    file_path = os.path.join(group, f"{group}_{character}.txt")

    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{target_character}(이)가 삭제되었습니다.")
    else:
        print("해당 파일이 존재하지 않습니다.")


# 실행문
while True:
    choice = input("메이플 월드에 오신 것을 환영합니다!\n1. 캐릭터 생성\n2. 캐릭터 삭제\n3. 종료\n선택하세요 (1/2/3): ")

    if choice == "1":
        create_character()
    elif choice == "2":
        delete_character()
    elif choice == "3":
        print("프로그램 종료")
        break
    else:
        print("유효한 옵션을 선택하세요.")
