def check_safe_int(user_input):
    """
    사용자 입력이 정수값이 아니면 오류 텍스트를 출력하고 None을 반환한다.
    """
    try:
        if int(user_input):
            return int(user_input)
    except ValueError:
        print("숫자를 입력해 주세요.")
        return

# 신규 서적 등록시 예외처리 - 1. ISBN 중복 2. 유효하지 않은 입력
# def check_safe_ISBN(user_input, ISBN_list):
#     if (user_input in ISBN_list):
#         print("중복된 ISBN 입니다.")
#         return
#     elif (not user_input.startswith("ISBN")):
#         print("올바른 형식의 ISBN 입력이 아닙니다.")
#         return
#     else:
#         return user_input


def generate_dict(data):
    """
    대용량 데이터 조회를 전제하여, 딕셔너리를 생성자 방식으로 조회한다.
    """
    for key, value in data.items():
        yield key, value

# 메뉴 출력 시 구분선 삽입 (데코레이션)
def deco_border(callback):
    """
    각 메뉴 실행 시 구분선을 출력한다.
    """
    def wrapper(*args, **kwargs):
        print('=' * 10)
        callback(*args, **kwargs)
        print('=' * 10)
    return wrapper