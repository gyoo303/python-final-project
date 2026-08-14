from models.base_book import base_book

class paper_book(base_book):
    def __init__(self, book_name, author, ISBN, page_num, page_size, is_checkout = False, dt_checkout = None, dt_return = None):
        super().__init__(book_name, author, ISBN, is_checkout, dt_checkout, dt_return)
        self.page_num = page_num
        self.page_size = page_size
    
    def __str__(self):
        checkout_available = ""
        if not self.is_checkout:
            checkout_available = "대여가능"
        else:
            checkout_available = "대여불가"
        
        return f"[{checkout_available}] {self.info}-{self.page_num}p"