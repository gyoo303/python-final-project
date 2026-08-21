from models.base_book import BaseBook

class PaperBook(BaseBook):
    def __init__(self, book_name, author, ISBN, page_num, page_size, is_checkout = False, dt_checkout = None, dt_return = None):
        super().__init__(book_name, author, ISBN, is_checkout, dt_checkout, dt_return)
        self.__page_num = page_num
        self.__page_size = page_size
        self.__checkout_available = "대여가능"
    
    def __str__(self):
        if not self.get_is_checkout():
            self.__checkout_available = "대여가능"
        else:
            self.__checkout_available = "대여불가"
        
        return f"[{self.__checkout_available}] {self.get_info()}-{self.__page_num}p"