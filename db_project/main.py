import MySQLdb

class Products:
    def __init__(self, product, price, count):
        self.product = product
        self.price = price
        self.count = count

    def getProduct(self):
        return self.product

    def getPrice(self):
        return self.price

    def getCount(self):
        return self.count


class Dao:
    def __init__(self):
        self.db = None

    def connect(self):
        self.db = MySQLdb.connect('localhost', 'root', '1234', 'mall')
        self.cur = self.db.cursor()

    def disconnect(self):
        self.db.close()

    def selectAll(self, category):
        self.connect()
        cur = self.db.cursor(MySQLdb.cursors.DictCursor)
        sql = f'select product, price, count from {category}'
        cur.execute(sql)
        row = cur.fetchall()
        cur.close()
        self.disconnect()
        return row

    def search(self, product_name, category):
        self.connect()
        cur = self.db.cursor(MySQLdb.cursors.DictCursor)
        sql = f'select product, price, count from {category} where product like %s'
        data = ('%' + product_name + '%',)
        cur.execute(sql, data)
        row = cur.fetchall()
        cur.close()
        self.disconnect()
        return row

    def buy_product(self, product_name, price, category):
        self.connect()
        cur = self.db.cursor()
        sql = f"SELECT count FROM {category} WHERE product = %s"
        data = (product_name,)
        cur.execute(sql, data)
        result = cur.fetchone()
        if result and result[0] > 0:
            new_count = result[0] - 1
            sql = f"UPDATE {category} SET count = %s WHERE product = %s"
            data = (new_count, product_name)
            cur.execute(sql, data)
            self.db.commit()
            print(f"{product_name} 상품을 구입했습니다. 남은 개수: {new_count}")
        else:
            print(f"{product_name} 상품은 품절되었습니다.")
        cur.close()
        self.disconnect()

    def get_category(self, product_name):
        # 여기에 상품명을 기반으로 카테고리를 조회하는 로직 추가
        # 예를 들어, product_name을 가지고 카테고리를 판단하는 로직을 구현합니다.
        # 이 부분은 실제로 카테고리를 어떻게 판단할지에 따라 다를 수 있습니다.
        # 여기에서는 간단한 예시로 카테고리를 하드코딩으로 지정하겠습니다.
        if "의류" in product_name:
            return "clothes"
        elif "가구" in product_name:
            return "furniture"
        elif "전자기기" in product_name:
            return "it_shop"
        elif "생필품" in product_name:
            return "living"
        elif "명품" in product_name:
            return "luxury"
        else:
            return None

class Service:
    def __init__(self):
        self.dao = Dao()

    def printAll(self, category):
        datas = self.dao.selectAll(category)
        for data in datas:
            print(f"{data['product']}, 가격: {data['price']}, 개수: {data['count']}")

    def searchProduct(self, category):
        product_name = input(f'{category} 카테고리에서 사고싶은 상품 : ')
        products = self.dao.search(product_name, category)

        if products:
            for product in products:
                print(product)
        else:
            print('찾는 상품이 없습니다')

    def buyProduct(self, category):
        product_name = input(f'{category} 카테고리에서 구매할 상품 : ')
        price = int(input(f'{product_name} 상품의 가격 : '))
        self.dao.buy_product(product_name, price, category)

    def shopping(self):
        while True:
            try:
                category = input('어느 매장에 방문하실겁니까? (의류, 가구, 전자기기, 생필품, 명품, 종료): ')
                if category == "종료":
                    print('프로그램을 종료합니다.')
                    break
                elif category not in ["의류", "가구", "전자기기", "생필품", "명품"]:
                    print('유효한 매장을 선택하세요.')
                    continue

                action = input(f'행동 선택 1. {category} 쇼핑하기 2. {category} 남은 개수 확인 3. 종료: ')
                if action == '1':
                    self.buyProduct(category)
                elif action == '2':
                    self.printAll(category)
                elif action == '3':
                    print(f'{category} 매장에서 나갑니다.')
                else:
                    print('유효한 행동을 선택하세요.')

            except Exception as e:
                print(e)
                print('다시 입력')

class Menu:
    def __init__(self):
        self.service = Service()

    def run(self):
        while True:
            try:
                menu = input('1. 매장 방문 2. 종료: ')
                if menu == '1':
                    self.service.shopping()
                elif menu == '2':
                    print('프로그램을 종료합니다.')
                    break
                else:
                    print('유효한 메뉴를 선택하세요.')

            except Exception as e:
                print(e)
                print('다시 입력')

if __name__ == "__main__":
    start = Menu()
    start.run()
