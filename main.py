from models.specialized_books import paper_book
from utils.helpers import check_safe_int, deco_border, generate_dict
from datetime import datetime

# 고유값인 ISBN 넘버로 책 정보에 접근할 수 있도록,
# ISBN 넘버를 key, 책 class를 value로 갖는 딕셔너리 자료형 선택
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

# 효율적인 데이터 접근을 위한 별도의 변수들
# 데이터 양이 크게 늘어나도 안전한 실행을 보장하도록 generator 사용

# 중복 체크 용도로만 사용하므로 순서 의미 없음 -> 집합 자료형 선택
BOOK_ISBN = set(["ISBN%04d" % num for num in range(len(BOOK_DATA))])

# 사용자가 책 이름을 입력할 경우 빠르게 ISBN 넘버를 찾을 수 있도록 딕셔너리 자료형 선택
NAME_TO_ISBN = {book.book_name:isbn for isbn, book in generate_dict(BOOK_DATA)}

# 1. 도서 등록
@deco_border
def add_book():
    """
    책 이름, 저자, 페이지 수, 페이지 사이즈를 입력받아 신규서적을 등록한다.
    페이지 수의 경우 정수가 입력되지 않으면 재입력을 요청한다.
    정보 입력이 완료되면 신규 ISBN 넘버를 발급하여 BOOK_DATA에 클래스 인스턴스를 추가한다.
    """
    
    book_name, author, page_num, page_size = "", "", 0, ""

    book_name = input("책 이름을 입력하세요: ")
    author = input("저자 이름을 입력하세요: ")
    page_size = input("페이지 사이즈를 입력하세요(ex. 145x210): ")
    while not page_num:
        page_num = check_safe_int(input("페이지 수를 입력하세요: "))
    
    # 신규 ISBN 발급
    new_ISBN = "ISBN%04d" % len(BOOK_DATA)
    BOOK_DATA[new_ISBN] = paper_book(book_name, author, new_ISBN, page_num, page_size)

    # 갱신
    NAME_TO_ISBN[book_name] = new_ISBN
    BOOK_ISBN.update([new_ISBN])

    print(f"{book_name}({new_ISBN}) 서적이 정상적으로 등록되었습니다.")

    return

# 2. 전체 도서 조회 - 가나다 순
@deco_border
def print_book_list():
    """
    전체 도서 목록을 가나다 순으로 출력한다.
    """
    
    print("*** 전체 도서 목록 (가나다 순) ***")
    for _, book in iter(sorted(BOOK_DATA.items(), key=lambda item: item[1].book_name)):
        print(book)
    return

# 3. 도서 검색
@deco_border
def search_book():
    """
    책 이름으로 도서 정보를 검색한다.
    """
    
    user_input = input("검색하고자 하는 서적의 이름을 입력하세요: ")
    if user_input in iter(NAME_TO_ISBN.keys()):
        print(BOOK_DATA[NAME_TO_ISBN[user_input]])
    else:
        print("입력하신 서적을 찾을 수 없습니다.")

# 4. 대여/반납 처리
@deco_border
def borrow_return_book():
    """
    사용자로부터 ISBN 넘버 또는 책 이름을 입력받아, BOOK_DATA에 존재할 경우 대출 또는 반납한다. 
    책이 현재 '대출 중' 상태면 반납 처리하고, '대출 가능' 상태면 대출 처리한다.
    """
    
    def check_checkout_and_process(user_input, check_target, dt):        
        if user_input in check_target:
            
            if not user_input.startswith("ISBN"):
                user_input = NAME_TO_ISBN[user_input]
            
            user_book = BOOK_DATA[user_input]
            
            if user_book.is_checkout: # 대여가 된 책
                print(f"<{user_book.book_name}> 반납이 완료되었습니다.")
                user_book.return_book(dt)
            else:
                print(f"<{user_book.book_name}> 대여가 완료되었습니다.")
                user_book.checkout_book(dt)
        else:
            print("입력하신 서적을 찾을 수 없습니다.")
        return
    
    user_input = input("대여 또는 반납하시려는 책의 이름 또는 ISBN 번호를 입력하세요.\n")
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    if user_input.startswith("ISBN"):
        check_checkout_and_process(user_input, set(NAME_TO_ISBN.values()), dt)
    else:
        check_checkout_and_process(user_input, set(NAME_TO_ISBN.keys()), dt)
    return

# 5. 통계 조회
@deco_border
def query_stats():
    """
    저장된 이력 데이터를 바탕으로 월간 대여 통계 또는 최다 대여 도서 통계값을 출력한다.
    """
    
    user_input = check_safe_int(input("조회하고자 하는 통계의 번호를 입력해 주세요:\n[ 1. 월간 대여 통계 ]\n[ 2. 가장 많이 대여된 도서 목록 ]\n"))
    if user_input == None:
        return

    if user_input == 1: # 월간 대여 통계
        stat_result = dict()
        current_year_month = datetime.now().strftime('%Y-%m')
        
        for isbn, book in generate_dict(BOOK_DATA):
            stat_result[BOOK_DATA[isbn].book_name] = book.calc_checkout_count(dt_condition = current_year_month)
        
        stat_result_top5 = sorted(stat_result.items(), key=lambda item: item[1], reverse=True)[:5]

        print(f"[ {current_year_month}: 이번 달 가장 많이 대여된 서적 TOP 5 ]\n")
        for i, (book_name, checkout_count) in enumerate(stat_result_top5):
            print(f"{i+1}위 : {book_name} (누적 대여 {checkout_count}회)")

        return
            
    elif user_input == 2:  # 가장 많이 대여된 도서
        stat_result = {"max_checkout_book_name":"", "max_checkout_count":0}
        
        for isbn, book in generate_dict(BOOK_DATA):
            checkout_count = book.calc_checkout_count()
            if stat_result["max_checkout_count"] < checkout_count:
                stat_result["max_checkout_book_name"] = book.book_name
                stat_result["max_checkout_count"] = checkout_count
        
        print(f"가장 많이 대여된 서적: <{stat_result['max_checkout_book_name']}> (누적 대여 {stat_result['max_checkout_count']}회)")
        return
        
    else:
        print("잘못된 입력입니다.")
        return

def menu_select():
    """
    도서관 시스템 전체 메뉴를 출력하고, 사용자 입력에 따라 해당 메뉴를 실행한다.
    메뉴를 1회 실행 완료 또는 잘못된 입력이 들어오면 반환값 없이 종료한다.
    """
    
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
    """
    사용자가 종료를 선택할 때까지 반복하여 [메뉴 선택 - 메뉴 실행]을 이용 가능하도록 한다.
    """
        
    user_input = ""
    while user_input != 'quit':
        user_input = menu_select()


if __name__ == "__main__":
    run_library_system()


           

