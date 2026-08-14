from models.base_book import base_book
from models.specialized_books import paper_book
from utils.helpers import check_safe_int, check_safe_ISBN, deco_border

from datetime import datetime

BOOK_ISBN = set(["ISBN%04d" % num for num in range(10)])
BOOK_DATA = {
    "ISBN0004" : paper_book("채식주의자", "한강", "ISBN0004", 247, "130x195"),
    "ISBN0003" : paper_book("소년이 온다", "한강", "ISBN0003", 216, "145x210"),
    "ISBN0000" : paper_book("아몬드", "손원평", "ISBN0000", 264, "135x200"),
    "ISBN0008" : paper_book("달러구트 꿈 백화점", "이미예", "ISBN0008", 300, "134x200"),
    "ISBN0001" : paper_book("불편한 편의점", "김호연", "ISBN0001", 268, "135x200"),
    "ISBN0005" : paper_book("82년생 김지영", "조남주", "ISBN0005", 192, "130x195"),
    "ISBN0009" : paper_book("피프티 피플", "정세랑", "ISBN0009", 396, "140x205"),
    "ISBN0006" : paper_book("구의 증명", "최진영", "ISBN0006", 172, "128x188"),
    "ISBN0002" : paper_book("우리가 빛의 속도로 갈 수 없다면", "김초엽", "ISBN0002", 330, "137x197"),
    "ISBN0007" : paper_book("시선으로부터,", "정세랑", "ISBN0007", 340, "145x210")
}

NAME_TO_ISBN = {value.book_name:key for (key, value) in BOOK_DATA.items()}

# BOOK_NAMES = [book.book_name for book in BOOK_DATA.values()]

# 1. 도서 등록
@deco_border
def add_book():
    # book_name, author, ISBN, page_num, page_size

    ISBN = check_safe_ISBN(input("ISBN을 입력하세요(ex. ISBN0035): "))
    if not ISBN:
        return

    # ISBN 중복 예외처리 - 1. 중복 2. 유효하지 않은 입력

    book_name = input("책 이름을 입력하세요: ") 
    author = input("저자 이름을 입력하세요: ")
    page_num = check_safe_int(input("페이지 수를 입력하세요: "))
    page_size = input("페이지 사이즈를 입력하세요(ex. 145x210): ")

    BOOK_DATA[ISBN] = paper_book(book_name, author, ISBN, page_num, page_size)

    # 갱신
    NAME_TO_ISBN[book_name] = ISBN
    BOOK_ISBN = BOOK_ISBN.union({ISBN})

    print(f"{book_name}({ISBN}) 서적이 정상적으로 등록되었습니다.")

    return

# 2. 전체 도서 조회
@deco_border
def print_book_list():
    for book in BOOK_DATA.values():
        print(book)
    return

# 3. 도서 검색
@deco_border
def search_book():
    # ISBN
    user_input = ""
    while user_input not in NAME_TO_ISBN.keys():
        user_input = input("검색하고자 하는 서적의 이름을 입력하세요: ")
        if user_input in NAME_TO_ISBN.keys():
            print(BOOK_DATA[NAME_TO_ISBN[user_input]])
        else:
            print("입력하신 서적을 찾을 수 없습니다.")

# 4. 대여/반납 처리
def borrow_return_book():
    # ISBN

    dt = datetime.now.strftime('%Y-%m-%d %H:%M:%S')

    pass

# 5. 통계 조회
def query_stats():
    """
     '통계 조회' 기능을 추가하여, 저장된 이력 데이터를 바탕으로 월간 대
    여 통계나 가장 많이 대여된 도서 목록을 콘솔 화면에 출력
    """

    
    pass


def menu_select():
    user_input = check_safe_int(input("\n원하시는 서비스의 번호를 입력해 주세요:\n[ 1. 도서 등록 ]\n[ 2. 전체 도서 조회 ]\n[ 3. 도서 검색 ]\n[ 4. 대여/반납 처리 ]\n[ 5. 통계 조회 ]\n[ 6. 종료 ]\n"))

    # if user_input == None:
    #     run_library_system()
    if user_input == 1: # 도서 등록
        add_book()
        return
    elif user_input == 2: # 전체 도서 조회
        print_book_list()
        return
    elif user_input == 3: # 도서 검색
        search_book()
        return
    elif user_input == 4: # 대여/반납 처리            
        borrow_return_book()
        return
    elif user_input == 5: # 통계 조회
        query_stats()
        return
    elif user_input == 6: # 종료
        print("도서 관리 시스템을 종료합니다.")
        return 'quit'
    else: # 잘못된 입력
        return

def run_library_system():

    user_input = ""

    while user_input != 'quit':
        user_input = menu_select()
        # if user_input == 'wrong':
        #     continue

# def run_library_system():

#     while True:
#         user_input = check_safe_int(input("\n원하시는 서비스의 번호를 입력해 주세요:\n1. 도서 등록\n2. 전체 도서 조회\n3. 도서 검색\n4. 대여/반납 처리\n5. 통계 조회\n6.종료\n"))

#         if user_input == None:
#             run_library_system()

#         if user_input == 1: # 도서 등록
#             add_book()
#         elif user_input == 2: # 전체 도서 조회
#             print_book_list()
#         elif user_input == 3: # 도서 검색
#             search_book()
#         elif user_input == 4: # 대여/반납 처리            
#             borrow_return_book()
#         elif user_input == 5: # 통계 조회
#             query_stats()
#         else: # 종료
#             print("도서 관리 시스템을 종료합니다.")
#             return    

if __name__ == "__main__":

        run_library_system()


           

