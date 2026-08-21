
class BaseBook:
    def __init__(self, book_name, author, ISBN, is_checkout= False, dt_checkout = None, dt_return = None):
        self.__book_name = book_name
        self.__author = author
        self.__ISBN = ISBN
        self.__is_checkout = is_checkout
        self.__dt_checkout = dt_checkout
        self.__dt_return = dt_return

        self.__checkout_history = []
        self.__return_history = []

        self.__info = f"{self.__book_name} ({self.__author} 저)(ISBN: {self.__ISBN})"

    def checkout_book(self, dt_checkout):
        self.__is_checkout = True
        self.__dt_checkout = dt_checkout
        self.__checkout_history.append((self.get_ISBN(), dt_checkout))

    def calc_checkout_count(self, dt_condition = ""):
        if dt_condition:
            return len(self.__checkout_history)
        else:
            return len([(isbn, dt) for (isbn, dt) in self.__checkout_history if dt.startswith(dt_condition)])

    def return_book(self, dt_return):
        self.__is_checkout = False
        self.__dt_return = dt_return
        self.__return_history.append((self.get_ISBN(), dt_return))

    def __str__(self):
        checkout_available = ""
        checkout_available = "대여 불가" if self.__is_checkout else "대여 가능"            
        return f"[{checkout_available}] {self.__info}\n{self.__book_name}"

    def get_is_checkout(self):
        return self.__is_checkout

    def get_book_name(self):
        return self.__book_name

    def get_info(self):
        return self.__info

    def get_ISBN(self):
        return self.__ISBN