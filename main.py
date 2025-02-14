import streamlit as st
import pandas as pd
import joblib
import os

# 제목 설정
st.set_page_config(page_title="🎵 음악 사이트 이탈률 예측", layout="wide")


def load_model():
    model_paths = ["./model/xgb_model_over.joblib", "./model/rf_model_over.joblib"]
    
    for model_path in model_paths:
        if os.path.exists(model_path):
            try:
                model = joblib.load(model_path)
                return model
            except Exception as e:
                st.error(f"모델을 불러오는 중 오류 발생: {e}")
                return None
    st.error("모델 파일을 찾을 수 없습니다.")
    return None

# 최빈값 로드 함수
def load_mode_values():
    try:
        data = pd.read_csv("./model/final_data.csv")
        mode_values = data.mode().iloc[0].to_dict()
        return mode_values
    except Exception as e:
        st.error(f"최빈값을 불러오는 중 오류 발생: {e}")
        return {}
    
def compare_isChurn_isBack():
    # 데이터 불러오기
    df2 = pd.read_csv('./model/is_back+churn_Data.csv')

    # is_back == 1 또는 is_churn == 1 인 데이터만 남김
    df_filtered = df2[(df2["is_back"] == 1) | (df2["is_churn"] == 1)].copy()

    # is_back == 1인 데이터에서 is_back 컬럼 제외
    df_is_back = df_filtered[df_filtered["is_back"] == 1].drop(columns=["is_back",'is_churn','total_secs'])

    # is_churn == 1인 데이터에서 is_churn 컬럼 제외
    df_is_churn = df_filtered[df_filtered["is_churn"] == 1].drop(columns=["is_churn","is_back",'total_secs'])
    df_is_back = df_is_back.mean().astype(int)
    df_is_churn = df_is_churn.mean().astype(int)
    return df_is_back, df_is_churn

# 사용자 정보 입력
st.header("👤 사용자 정보")
col1, col2, col3 = st.columns(3)
with col1:
    gender = st.radio("성별", ["남성", "여성"], index=0, horizontal=True)
with col2:
    bd = st.slider("나이 (bd)", min_value=10, max_value=100, step=1, value=26)
with col3:
    payment_plan_sum = st.number_input("📅 멤버십 가입 기간", min_value=0, step=1, value=500) 

# 결제 정보 입력
st.header("💰 결제 정보")
col1, col2, col3 = st.columns(3)
with col1:
    plan_list_price = st.number_input("요금제 정가", min_value=0, step=1, value=2250)
with col2:
    actual_amount_paid = st.number_input("실제 지불 금액", min_value=0, step=1, value=2250)
with col3:
    is_auto_renew = st.slider('자동 갱신 비율(%)', min_value=0, step=1, value=20)

# 청취 패턴 입력
st.header("🎧 청취 패턴")
col1, col2, col3 = st.columns(3)
with col1:
    num_25 = st.number_input("🎵 25% 이하 청취 횟수", min_value=0, step=1, value=1200)
    num_50 = st.number_input("🎵 50% 이하 청취 횟수", min_value=0, step=1, value=500)
with col2:
    num_75 = st.number_input("🎵 75% 이하 청취 횟수", min_value=0, step=1, value=300)
    num_985 = st.number_input("🎵 98.5% 이하 청취 횟수", min_value=0, step=1, value=2000)
with col3:
    num_100 = st.number_input("🎵 100% 청취 횟수", min_value=0, step=1, value=2000)
    num_unq = st.number_input("📀 고유 청취 곡 수", min_value=1, step=1, value=5000)

# 활동 기간 입력
st.header("📆 활동 기간")
col1, col2 = st.columns(2)
with col1:
    total_secs = st.number_input("⏳ 총 청취 시간 (초)", min_value=0.0, step=1.0, value=900000.0)
    listening_duration = st.number_input("🎤 플랫폼 사용 기간", min_value=0, step=1, value=500)
with col2:
    registration_duration = st.number_input("📆 가입 후 경과일", min_value=0, step=1, value=700)
    

# 최빈값 가져오기
mode_values = load_mode_values()

feature_order = [
    "city", "bd", "gender", "registered_via", "payment_plan_sum",
    "plan_list_price", "actual_amount_paid", "discount_rate",
    "is_auto_renew", "is_cancel", "transaction_count",
    "num_25", "num_50", "num_75", "num_985", "num_100",
    "num_unq", "total_secs", "registration_duration", "listening_duration"
]

# 입력값을 데이터프레임으로 변환 (예측용)
input_data = pd.DataFrame({
    "city": [0],
    "bd": [bd],
    "gender": [1 if gender == "남성" else 0],
    "registered_via": [4],
    "payment_plan_sum": [payment_plan_sum],
    "plan_list_price": [plan_list_price],
    "actual_amount_paid": [actual_amount_paid],
    "discount_rate": [mode_values.get("discount_rate", 0.0)],
    "is_auto_renew": [is_auto_renew/100.0],
    "is_cancel": [0],
    # "transaction_count": [(mode_values.get("transaction_count", 0)) / 10],
    "transaction_count": [0],
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

input_data = input_data[feature_order]

# 예측 결과 상태를 session_state에 저장
if 'prediction_result' not in st.session_state:
    st.session_state.prediction_result = None

# 입력 데이터 확인 (사용자가 입력한 값만 표시)
show_data = pd.DataFrame({
    "성별": [gender],
    "나이": [bd],
    "멤버십 가입 기간": [payment_plan_sum],
    "요금제 정가": [plan_list_price],
    '자동 갱신 비율': [is_auto_renew],
    "실제 지불 금액": [actual_amount_paid],
    "25% 이하 청취 횟수": [num_25],
    "50% 이하 청취 횟수": [num_50],
    "75% 이하 청취 횟수": [num_75],
    "98.5% 이하 청취 횟수": [num_985],
    "100% 청취 횟수": [num_100],
    "고유 곡 수": [num_unq],
    "총 청취 시간(초)": [total_secs],
    "가입 후 경과일": [registration_duration],
    "플랫폼 사용 기간": [listening_duration]
})

st.write("### 📝 입력한 데이터")
st.dataframe(show_data)


# 예측 버튼 추가
if st.button("🚀 예측하기"):
    model = load_model()
    if model:
        prediction = model.predict(input_data)[0]
        prediction_proba = model.predict_proba(input_data)[0]

        # 예측 결과 저장
        st.session_state.prediction_result = {
            "prediction": prediction,
            "probability": prediction_proba
        }


is_back, is_churn = compare_isChurn_isBack()


# 예측 결과 표시
if st.session_state.prediction_result:
    prediction = st.session_state.prediction_result["prediction"]
    prediction_proba = st.session_state.prediction_result["probability"]
    
    st.write("### 🎯 예측 결과")
    if prediction == 1:
        st.error(f"사용자가 이탈할 가능성이 높습니다. (확률: {prediction_proba[1]:.2%})")
        if (is_back['is_auto_renew'] - is_auto_renew) < 0 :
            st.write(f'자동 갱신 비율이 일반 사용자에 낮습니다.')
        if ((num_unq)-is_back['num_unq']) > 0:
            st.write(f'고유 청취 곡수가 일반 사용자의 평균값에 비해 많이 청취했습니다.')
        elif ((num_unq)-is_back['num_unq']) < 0:
            st.write(f'고유 청취 곡수가 일반 사용자의 평균값에 비해 적게 청취했습니다.')
        else :
            st.writ('일반 사용자의 평균값과 같습니다.')
        
    else:
        st.success(f"사용자가 유지될 가능성이 높습니다. (확률: {prediction_proba[0]:.2%})")