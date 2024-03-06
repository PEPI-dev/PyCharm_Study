import MySQLdb


class ShoppingProgram:
    def __init__(self):
        self.limit = 5000000
        self.spent = 0
        self.db = MySQLdb.connect('localhost', 'root', '1234', 'mall')
        self.cursor = self.db.cursor()

    def run(self):
        print('얏호 엄카를 맘껏 사용할 수 있다니 사고싶은 거 다 사야징 ㅎㅎ')

        while True:
            try:
                print('1. 쇼핑하기 2. 남은 한도 확인 3. 집 가기')
                choice = input('행동 선택: ')

                if choice == '1':
                    self.shopping()
                elif choice == '2':
                    self.check_limit()
                elif choice == '3':
                    self.go_home()
                else:
                    print('잘못된 선택입니다. 다시 입력하세요.')
            except ValueError:
                print('잘못된 입력입니다. 숫자를 입력하세요.')

    def shopping(self):
        print('어느 매장에 방문하실 겁니까? (의류, 가구, 전자기기, 생필품)')
        category = input('매장 선택: ')

        if category not in ['의류', '가구', '전자기기', '생필품']:
            print('잘못된 매장 선택입니다.')
            return

        print(f'{category} 매장에 오셨습니다. 상품을 선택해주세요.')

        if category == '의류':
            self.buy_clothes()
        elif category == '가구':
            self.buy_furniture()
        elif category == '전자기기':
            self.buy_electronics()
        elif category == '생필품':
            self.buy_living()


    def check_limit(self):
        print(f'남은 한도: {self.limit - self.spent}원')

    def go_home(self):
        print('집갈게')
        exit()

    def buy_product(self, product_name, price):
        category = 'item'
        print(f'{product_name} 상품을 선택하셨습니다. 가격: {price}원')
        confirm = input('구입하시겠습니까? (Y/N): ')

        if confirm.upper() == 'Y':
            if self.spent + price > self.limit:
                print('카드 한도를 초과하여 구매할 수 없습니다. 다른 상품을 선택하세요.')
            else:
                try:

                    self.cursor.execute(f"SELECT count FROM {category} WHERE product = '{product_name}'")
                    result = self.cursor.fetchone()
                    if result and result[0] > 0:

                        self.cursor.execute(f"UPDATE {category} SET count = count - 1 WHERE product = '{product_name}'")
                        self.spent += price
                        print(f'{product_name} 상품을 구입했습니다. 남은 한도: {self.limit - self.spent}원')
                        self.db.commit()
                    else:
                        print(f'{product_name} 상품은 품절되었습니다.')

                except MySQLdb.Error as e:
                    self.db.rollback()
                    print(f'Error: {str(e)}')
        else:
            print(f'{product_name} 상품을 구매하지 않았습니다.')

    def buy_clothes(self):
        try:
            self.cursor.execute("SELECT product, price, count FROM clothes")
            products = self.cursor.fetchall()
            for product in products:
                product_name, price, count = product
                print(f'{product_name} - 가격: {price}원, 재고: {count}개')

            product_name = input('상품 이름을 입력하세요: ')

            selected_product = next((p for p in products if p[0] == product_name), None)
            if selected_product:
                product_name, price, count = selected_product
                self.buy_product(product_name, price)
            else:
                print('잘못된 상품 이름을 입력했습니다.')

        except MySQLdb.Error as e:
            print(f'Error: {str(e)}')


    def buy_furniture(self):
        try:
            self.cursor.execute("SELECT product, price, count FROM furniture")
            products = self.cursor.fetchall()
            for product in products:
                product_name, price, count = product
                print(f'{product_name} - 가격: {price}원, 재고: {count}개')

            product_name = input('상품 이름을 입력하세요: ')

            selected_product = next((p for p in products if p[0] == product_name), None)
            if selected_product:
                product_name, price, count = selected_product
                self.buy_product(product_name, price)
            else:
                print('잘못된 상품 이름을 입력했습니다.')

        except MySQLdb.Error as e:
            print(f'Error: {str(e)}')

    def buy_electronics(self):
        try:
            self.cursor.execute("SELECT product, price, count FROM it_shop")
            products = self.cursor.fetchall()
            for product in products:
                product_name, price, count = product
                print(f'{product_name} - 가격: {price}원, 재고: {count}개')

            product_name = input('상품 이름을 입력하세요: ')


            selected_product = next((p for p in products if p[0] == product_name), None)
            if selected_product:
                product_name, price, count = selected_product
                self.buy_product(product_name, price)
            else:
                print('잘못된 상품 이름을 입력했습니다.')

        except MySQLdb.Error as e:
            print(f'Error: {str(e)}')

    def buy_living(self):
        try:
            self.cursor.execute("SELECT product, price, count FROM living")
            products = self.cursor.fetchall()
            for product in products:
                product_name, price, count = product
                print(f'{product_name} - 가격: {price}원, 재고: {count}개')

            product_name = input('상품 이름을 입력하세요: ')


            selected_product = next((p for p in products if p[0] == product_name), None)
            if selected_product:
                product_name, price, count = selected_product
                self.buy_product(product_name, price)
            else:
                print('잘못된 상품 이름을 입력했습니다.')

        except MySQLdb.Error as e:
            print(f'Error: {str(e)}')



shopping_program = ShoppingProgram()
shopping_program.run()
