import streamlit as st
import pandas as pd

# 제목
st.title("🎵 음악 사이트 이탈률 예측")

# 📌 [1] 사용자 정보
st.header("👤 사용자 정보")
col1, col2, col3 = st.columns(3)
with col1:
    gender = st.radio("성별", ["남성", "여성"], index=0, horizontal=True)
with col2:
    bd = st.slider("나이 (bd)", min_value=10, max_value=100, step=1, value=29)
with col3:
    payment_plan_sum = st.number_input("📅 멤버십 가입 기간", min_value=0, step=1, value=1)

# 📌 [2] 결제 정보
st.header("💰 결제 정보")
col1, col2 = st.columns(2)
with col1:
    plan_list_price = st.number_input("요금제 정가", min_value=0, step=1, value=2500)
with col2:
    actual_amount_paid = st.number_input("실제 지불 금액", min_value=0, step=1, value=2500)

# 📌 [3] 청취 패턴
st.header("🎧 청취 패턴")
col1, col2, col3 = st.columns(3)
with col1:
    num_25 = st.number_input("🎵 25% 이하 청취 횟수", min_value=0, step=1, value=100)
    num_50 = st.number_input("🎵 50% 이하 청취 횟수", min_value=0, step=1, value=50)
with col2:
    num_75 = st.number_input("🎵 75% 이하 청취 횟수", min_value=0, step=1, value=30)
    num_985 = st.number_input("🎵 98.5% 이하 청취 횟수", min_value=0, step=1, value=20)
with col3:
    num_100 = st.number_input("🎵 100% 청취 횟수", min_value=0, step=1, value=10)
    num_unq = st.number_input("📀 고유 곡 수", min_value=1, step=1, value=500)

# 📌 [4] 활동 기간
st.header("📆 활동 기간")
col1, col2 = st.columns(2)
with col1:
    total_secs = st.number_input("⏳ 총 청취 시간 (초)", min_value=0.0, step=1.0, value=100000.0)
with col2:
    registration_duration = st.number_input("📆 가입 후 경과일", min_value=0, step=1, value=365)
    listening_duration = st.number_input("🎤 청취 지속 일수", min_value=0, step=1, value=30)

# 입력값을 데이터프레임으로 변환
input_data = pd.DataFrame({
    "gender": [1 if gender == "남성" else 0],  # 남성은 1, 여성은 0
    "bd": [bd],
    "payment_plan_sum": [payment_plan_sum],
    "plan_list_price": [plan_list_price],
    "actual_amount_paid": [actual_amount_paid],
    "num_25": [num_25],
    "num_50": [num_50],
    "num_75": [num_75],
    "num_985": [num_985],
    "num_100": [num_100],
    "num_unq": [num_unq],
    "total_secs": [total_secs],
    "registration_duration": [registration_duration],
    "listening_duration": [listening_duration]
}, index=[0])

# 한글 컬럼명 변환 및 성별 표시
show_data = input_data.copy()
show_data.columns = ["성별", "나이", "멤버십 가입 기간", "요금제 정가", "실제 지불 금액", "25% 이하 청취 횟수", "50% 이하 청취 횟수", "75% 이하 청취 횟수", "98.5% 이하 청취 횟수", "100% 청취 횟수", "고유 곡 수", "총 청취 시간(초)", "가입 후 경과일", "청취 지속 일수"]
show_data["성별"] = show_data["성별"].map({1: "남성", 0: "여성"})

# 입력 데이터 확인
st.write("### 📝 입력한 데이터")
st.dataframe(show_data)

# 예측 버튼 추가
if st.button("🚀 예측하기"):
    st.write("📢 모델을 로드하여 예측하는 코드를 추가하세요.")