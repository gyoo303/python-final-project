
def check_safe_int(user_input):
    try:
        if int(user_input):
            return int(user_input)
    except ValueError:
        print("숫자를 입력해 주세요.")
        return

# 신규 서적 등록시 예외처리 - 1. ISBN 중복 2. 유효하지 않은 입력
def check_safe_ISBN(user_input, ISBN_list):
    if (user_input in ISBN_list):
        print("중복된 ISBN 입니다.")
        return
    elif (not user_input.startswith("ISBN")):
        print("올바른 형식의 ISBN 입력이 아닙니다.")
        return
    else:
        return user_input

# 메뉴 출력 시 구분선 삽입 (데코레이션)
def deco_border(callback):
    def wrapper(*args, **kwargs):
        print('=' * 10)
        callback(*args, **kwargs)
        print('=' * 10)
    return wrapper