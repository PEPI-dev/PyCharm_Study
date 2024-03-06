import MySQLdb
import cursor

# MySQL 연결 설정
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="1234",
    db="BitcoinTransactions"
)

cursor = db.cursor()

# 비트코인 클래스 정의
class Bitcoin:
    def __init__(self, coin_id, coin_name, price, count):
        self.coin_id = coin_id
        self.coin_name = coin_name
        self.price = price
        self.count = count

    def __str__(self):
        return f"ID: {self.coin_id}, 코인 이름: {self.coin_name}, 가격: {self.price}, 재고: {self.count}"

# 비트코인 관리자 모드
def admin_mode():
    coin_name = input("새로운 비트코인 이름을 입력하세요: ")
    price = float(input("비트코인 가격을 입력하세요: "))
    count = int(input("비트코인의 갯수를 입력하세요: "))

    # MySQL 테이블에 데이터 추가
    cursor = db.cursor()
    cursor.execute("INSERT INTO Trade (coin, price, count) VALUES (%s, %s, %s)",
                   (coin_name, price, count))
    db.commit()

    print(f"{coin_name}이(가) 추가되었습니다.")

def show_owned_bitcoins():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Trade")
    transactions = cursor.fetchall()

    if not transactions:
        print("보유한 비트코인이 없습니다.")
    else:
        print("보유한 비트코인 목록:")
        for transaction in transactions:
            coin = Bitcoin(*transaction)
            print(coin)

# 비트코인 구매 함수
def buy_bitcoin(user_balance, transactions):
    print("가능한 비트코인 거래:")
    for i, transaction in enumerate(transactions):
        coin = Bitcoin(*transaction)
        print(f"{i + 1}. {coin}")

    while True:
        try:
            coin_id = int(input("구매할 비트코인의 번호를 입력하세요 (0을 입력하여 종료): "))
            if coin_id == 0:
                break
            elif coin_id < 1 or coin_id > len(transactions):
                print("유효하지 않은 번호입니다.")
                continue

            selected_transaction = transactions[coin_id - 1]
            coin = Bitcoin(*selected_transaction)

            if coin.price <= 0:
                print(f"{coin.coin_name}의 가격이 0 이하입니다.")
                continue

            total_cost = coin.price
            if total_cost > user_balance:
                print("잔액이 부족합니다.")
            else:
                user_balance -= total_cost
                coin.count -= 1
                print(f"{coin.coin_name}을(를) 1개 구매하였습니다. 잔액: {user_balance}원")
                cursor.execute("UPDATE Trade SET count = %s WHERE coin = %s", (coin.count, coin.coin_id))
                db.commit()

        except ValueError:
            print("유효하지 않은 입력입니다. 숫자를 입력하세요.")

# 비트코인 판매 함수
def sell_bitcoin(user_balance, transactions):
    show_owned_bitcoins()

    try:
        coin_id = int(input("판매할 비트코인의 번호를 입력하세요 (0을 입력하여 종료): "))
        if coin_id == 0:
            return
        elif coin_id < 1 or coin_id > len(transactions):
            print("유효하지 않은 번호입니다.")
            return

        selected_transaction = transactions[coin_id - 1]
        coin = Bitcoin(*selected_transaction)

        if coin.count <= 0:
            print(f"{coin.coin_name}의 재고가 부족합니다.")
            return

        sell_amount = int(input(f"{coin.coin_name}을(를) 판매할 수량을 입력하세요: "))
        if sell_amount <= 0:
            print("유효하지 않은 수량입니다. 수량은 1 이상이어야 합니다.")
            return

        if sell_amount > coin.count:
            print(f"{coin.coin_name}의 재고보다 많은 수량을 판매할 수 없습니다.")
            return

        total_sell_price = coin.price * sell_amount
        coin.count -= sell_amount

        cursor.execute("UPDATE Trade SET count = %s WHERE coin = %s", (coin.count, coin.coin_id))
        db.commit()

        user_balance += total_sell_price
        print(f"{coin.coin_name}을(를) {sell_amount}개 판매하였습니다. 판매 금액: {total_sell_price}원, 잔액: {user_balance}원")

    except ValueError:
        print("유효하지 않은 입력입니다. 숫자를 입력하세요.")


def trade_mode():
    user_balance = 1000000000

    while True:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Trade")
        transactions = cursor.fetchall()

        print("\n1. 비트코인 구매")
        print("2. 비트코인 판매")
        print("3. 보유한 비트코인 목록 조회")
        print("4. 종료")
        choice = input("원하는 메뉴를 선택하세요 (1/2/3/4): ")

        if choice == "1":
            if not transactions:
                print("구매할 비트코인이 없습니다.")
            else:
                buy_bitcoin(user_balance, transactions)

        elif choice == "2":
            if not transactions:
                print("보유한 비트코인이 없습니다.")
            else:
                sell_bitcoin(user_balance, transactions)

        elif choice == "3":
            show_owned_bitcoins()

        elif choice == "4":
            print("프로그램을 종료합니다.")
            db.close()
            break

        else:
            print("유효하지 않은 선택입니다.")

if __name__ == "__main__":
    while True:
        print("\n1. 비트코인 관리자 모드")
        print("2. 비트코인 거래 모드")
        print("3. 종료")
        mode_choice = input("원하는 모드를 선택하세요 (1/2/3): ")

        if mode_choice == "1":
            admin_mode()
        elif mode_choice == "2":
            trade_mode()
        elif mode_choice == "3":
            print("프로그램을 종료합니다.")
            db.close()
            break
        else:
            print("유효하지 않은 선택입니다.")
