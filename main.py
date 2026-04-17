import streamlit as st
import math

st.title("🧮 계산기 웹앱")

st.write("원하는 연산을 선택하고 값을 입력하세요.")

# 연산 선택
operation = st.selectbox(
    "연산 선택",
    ["덧셈", "뺄셈", "곱셈", "나눗셈", "모듈러(나머지)", "지수", "로그"]
)

# 입력값
num1 = st.number_input("첫 번째 값", value=0.0)

# 로그는 입력이 다름
if operation == "로그":
    base = st.number_input("밑 (base)", value=10.0)
    num2 = None
else:
    num2 = st.number_input("두 번째 값", value=0.0)

# 계산 버튼
if st.button("계산하기"):
    try:
        if operation == "덧셈":
            result = num1 + num2

        elif operation == "뺄셈":
            result = num1 - num2

        elif operation == "곱셈":
            result = num1 * num2

        elif operation == "나눗셈":
            if num2 == 0:
                st.error("0으로 나눌 수 없습니다.")
                result = None
            else:
                result = num1 / num2

        elif operation == "모듈러(나머지)":
            result = num1 % num2

        elif operation == "지수":
            result = num1 ** num2

        elif operation == "로그":
            if num1 <= 0 or base <= 0 or base == 1:
                st.error("로그 계산 조건을 확인하세요 (값 > 0, 밑 > 0, 밑 ≠ 1)")
                result = None
            else:
                result = math.log(num1, base)

        # 결과 출력
        if result is not None:
            st.success(f"결과: {result}")

    except Exception as e:
        st.error(f"오류 발생: {e}")
