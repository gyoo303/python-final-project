# 📚 Library Management System (도서 관리 시스템)

> **KANT AX 과정 - 파이썬 기초 최종 프로젝트**  
> CLI 환경에서 동작하는 직관적이고 효율적인 간단 도서 관리 프로그램입니다.

---

## 📌 프로젝트 소개 (Overview)

본 프로젝트는 파이썬(Python) 기초 문법, 자료구조(List, Dict), 함수형 프로그래밍 및 제어 흐름을 활용하여 도서관의 핵심 업무를 CLI(Command Line Interface) 기반으로 구현한 도서 관리 시스템입니다.

사용자는 터미널 메뉴를 통해 도서의 등록부터 대여/반납, 검색, 통계 확인까지 손쉽게 처리할 수 있습니다.

---

## 🛠️ 기술 스택 (Tech Stack)

- **Language:** Python 3.x
- **Environment:** CLI / Terminal
- **Dependencies:** Built-in Modules (별도 외부 패키지 설치 불필요)

---

## ✨ 주요 기능 (Key Features)

| 기능 | 설명 |
|:---|:---|
| **1. 도서 등록** | 도서명, 저자, 출판연도 등의 정보를 입력받아 신규 도서 등록 |
| **2. 도서 조회** | 전체 등록된 도서의 목록 및 현재 대여 가능 여부 출력 |
| **3. 도서 검색** | 도서명 또는 저자 키워드 검색을 통한 도서 정보 조회 |
| **4. 도서 대여 / 반납** | 도서 대여 상태 전환 (`대여 가능` ↔ `대여 중`) |
| **5. 통계 조회** | 전체 도서 수, 대여 중인 도서 수, 대여 가능 도서 수 등 요약 통계 확인 |
| **6. 프로그램 종료** | 시스템 안전 종료 |

---

## 📂 프로젝트 구조 (Project Structure)

```text
python-final-project/
└── models
    ├── base_book.py           # 기본 책 클래스 (부모 클래스)
    └── specialized_book.py    # 특수 책 클래스 (자식 클래스)
└── utils
    └── helpers.py             # 사용자 입력 예외처리 등 보조 함수
├── main.py        # 메인 실행 파일 및 도서 관리 로직
└── README.md      # 프로젝트 문서