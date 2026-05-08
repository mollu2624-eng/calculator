# main.py

import streamlit as st
import math
import random
from collections import Counter
import plotly.express as px
import pandas as pd

# -----------------------------
# 기본 설정
# -----------------------------
st.set_page_config(
    page_title="다기능 웹앱",
    page_icon="🧮",
    layout="centered"
)

# -----------------------------
# 사이드바 메뉴
# -----------------------------
st.sidebar.title("📂 메뉴")
menu = st.sidebar.radio(
    "앱 선택",
    ["계산기", "확률 시뮬레이터"]
)

# =====================================================
# 계산기 앱
# =====================================================
if menu == "계산기":

    st.title("🧮 계산기 웹앱")

    st.write("원하는 연산을 선택하고 값을 입력하세요.")

    # 연산 선택
    operation = st.selectbox(
        "연산 선택",
        ["덧셈", "뺄셈", "곱셈", "나눗셈", "모듈러(나머지)", "지수", "로그"]
    )

    # 입력값
    num1 = st.number_input("첫 번째 값", value=0.0)

    # 로그는 입력 방식 다름
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

# =====================================================
# 확률 시뮬레이터 앱
# =====================================================
elif menu == "확률 시뮬레이터":

    st.title("🎲 확률 시뮬레이터")

    st.write("주사위 또는 동전 시뮬레이션을 실행해보세요.")

    sim_type = st.selectbox(
        "시뮬레이션 선택",
        ["주사위", "동전"]
    )

    trials = st.number_input(
        "시행 횟수",
        min_value=1,
        max_value=100000,
        value=100,
        step=1
    )

    if st.button("시뮬레이션 실행"):

        # -------------------------
        # 주사위 시뮬레이션
        # -------------------------
        if sim_type == "주사위":

            results = [random.randint(1, 6) for _ in range(trials)]

            counts = Counter(results)

            df = pd.DataFrame({
                "숫자": list(counts.keys()),
                "횟수": list(counts.values())
            })

            df = df.sort_values("숫자")

            st.subheader("🎲 주사위 결과")

            fig = px.bar(
                df,
                x="숫자",
                y="횟수",
                text="횟수",
                title=f"주사위 {trials}회 시행 결과"
            )

            st.plotly_chart(fig, use_container_width=True)

            st.dataframe(df)

        # -------------------------
        # 동전 시뮬레이션
        # -------------------------
        elif sim_type == "동전":

            results = [
                random.choice(["앞면", "뒷면"])
                for _ in range(trials)
            ]

            counts = Counter(results)

            df = pd.DataFrame({
                "결과": list(counts.keys()),
                "횟수": list(counts.values())
            })

            st.subheader("🪙 동전 결과")

            fig = px.pie(
                df,
                names="결과",
                values="횟수",
                title=f"동전 {trials}회 시행 결과"
            )

            st.plotly_chart(fig, use_container_width=True)

            st.dataframe(df)
