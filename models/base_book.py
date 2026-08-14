
class base_book:
    def __init__(self, book_name, author, ISBN, is_checkout = False, dt_checkout = None, dt_return = None):
        self.book_name = book_name
        self.author = author
        self.ISBN = ISBN
        self.is_checkout = is_checkout
        self.dt_checkout = dt_checkout
        self.dt_return = dt_return

        self.checkout_history = []
        self.return_history = []

        self.info = f"{self.book_name} ({self.author} 저)(ISBN: {self.ISBN})"

    def checkout_book(self, dt_checkout):
        self.is_checkout = True
        self.dt_checkout = dt_checkout
        self.checkout_history.append((self.ISBN, dt_checkout))


        # 저장소 구현 패턴으로 다시 짜보기??
        # https://app.notion.com/p/5-3-208566040df88286aae90100c3e4bfee

        # def message_store():
        #   storage = ""
        #   def add_message
        #       nonlocal storage
        #       storage += f"\n{message}"
        #   return add_message
        # my_storage = message_store()
        # my_storage("새로운 알림이 도착했습니다")
        # my_storage("출석 체크가 완료되었습니다")

    def return_book(self, dt_return):
        self.is_checkout = False
        self.dt_return = dt_return
        self.return_history.append((self.ISBN, dt_return))

    def __str__(self):
        checkout_available = ""
        if not self.is_checkout:
            checkout_available = "대여 가능"
        else:
            checkout_available = "대여 불가"
            
        return f"[{checkout_available}] {self.info}\n{self.book_name}"