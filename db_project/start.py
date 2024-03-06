import MySQLdb
import self

import dao
import main

# 엄카 사용하기 프로그램
#
#  1. 철수는 자취를 시작했다. 철수의 어머니는 철수가 독립을 한게 대견스러워 자취방좀 꾸미라고 철수에게 카드를 주었다.
#  2. 한도는 500만원 철수는 백화점에 달려갔다.
#  3. 백화점에는 여러가지 상품들이 있다.
#  4. 하지만 함정매장에서 물건을 살경우 어머니에게 문자가서 카드가 정지됩니다.
#  5. 함정 물건을 피해서 사고싶은 물건을 사시오
#  6. 500만원 이상 넘어가면 프로그램 종료
#
#
#  -------- 출력 -------------
#  1. print(' 얏호 엄카를 맘껏 사용할수있다니 사고싶은거 다사야징 ㅎㅎ')
#  2. input(' 행동 선택 1. 쇼핑하기 2. 남은한도 확인 3. 집가기')
#  3. input(' 어느 매장에 방문하실겁니까? (의류, 가구, 전자기기, 생필품,명품)
#  4. ex) input ( 의류매장에 오셨습니다. 상품을 선택해주세요 (톰브라운 가디건, 구찌 모자, 아디다스 신발 ......)
#  5. ex) print ( oo상품을 선택하셨습니다. 가격 : n원, 남은 한도 : n원 - 구입(Y/N) 사는지 마는지 출력메시지도 출력 ) -> 3번으로 돌아감
#  6. 함정 매장 ex) input ( 전자기기 매장에 오셨습니다. 상품을 선택해주세요 ( 닌텐도스위치, 노트북, ps5 ....)
#  7. ex) print ( oo상품을 구입했습니다. 남은 한도 n원)
#  8. print(' 어머니에게 전화가 와서 엄청 혼이나고 카드가 정지됩니다....')  프로그램 종료

import MySQLdb


class ShoppingProgram:
    def __init__(self):
        self.remaining_limit = 5000000
        self.connect()  # 데이터베이스 연결을 초기화

    def connect(self):
        self.conn = MySQLdb.connect('localhost', 'root', '1234', 'mall')
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def get_remaining_limit(self):
        return self.remaining_limit

    def set_remaining_limit(self, limit):
        self.remaining_limit = limit

    def select_store(self):
        print('1. 의류 매장')
        print('2. 가구 매장')
        print('3. 전자기기 매장')
        print('4. 생필품 매장')
        print('5. 명품 매장')

        choice = input('어느 매장에 방문하시겠습니까? (번호를 입력하세요): ')

        if choice == '1':
            self.shop('clothes')
        elif choice == '2':
            self.shop('furniture')
        elif choice == '3':
            self.shop('it_shop')
        elif choice == '4':
            self.shop('living')
        elif choice == '5':
            self.shop('luxury')
        else:
            print('잘못된 선택입니다. 다시 시도하세요.')

    def shop(self, category):
        self.cursor.execute(f"SELECT product, price, count FROM {category} WHERE count > 0")
        products = self.cursor.fetchall()

        if not products:
            print('해당 카테고리에 상품이 없거나 품절되었습니다.')
            return

        print(f'{category} 매장에서 판매 중인 상품 목록:')
        for i, (product, price, _) in enumerate(products, start=1):
            print(f'{i}. {product} - 가격: {price}원')

        choice = input('상품을 선택해주세요 (번호 또는 "뒤로"): ')

        if choice == '뒤로':
            return

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(products):
                selected_product, selected_price, remaining_count = products[choice - 1]

                print(f'{selected_product} 상품을 선택하셨습니다. 가격: {selected_price}원')

                buy_choice = input('구입하시겠습니까? (Y/N): ')
                if buy_choice.lower() == 'y':
                    if self.remaining_limit >= selected_price:
                        self.set_remaining_limit(self.remaining_limit - selected_price)
                        print(f'{selected_product} 상품을 구입했습니다. 남은 한도: {self.get_remaining_limit()}원')
                        self.cursor.execute(f"UPDATE {category} SET count = count - 1 WHERE product = %s",
                                            (selected_product,))
                        self.conn.commit()
                    else:
                        print('한도를 초과하여 구매할 수 없습니다.')
                else:
                    print('구입하지 않았습니다.')
            else:
                print('유효한 번호를 입력하세요.')
        else:
            print('잘못된 입력입니다.')

    def run(self):
        while True:
            print('-------- 출력 -------------')
            print('1. 얏호 엄카를 맘껏 사용할수있다니 사고싶은거 다사야징 ㅎㅎ')
            print('2. 행동 선택')
            print('3. 남은 한도 확인')
            print('4. 집가기')
            print('---------------------------')

            choice = input('선택: ')

            if choice == '1':
                pass  # 이미 출력되었으므로 아무 작업도 하지 않음
            elif choice == '2':
                self.select_store()
            elif choice == '3':
                print(f'남은 한도: {self.get_remaining_limit()}원')
            elif choice == '4':
                print('어머니에게 전화가 와서 엄청 혼이 나고 카드가 정지됩니다.... 프로그램 종료')
                break
            else:
                print('잘못된 선택입니다. 다시 시도하세요.')



if __name__ == "__main__":
    program = ShoppingProgram()
    program.run()
    program.close()
