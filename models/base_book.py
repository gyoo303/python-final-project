
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

    def calc_checkout_count(self, dt_condition = ""):
        if dt_condition:
            return len(self.checkout_history)
        else:
            return len([(isbn, dt) for (isbn, dt) in self.checkout_history if dt.startswith(dt_condition)])

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