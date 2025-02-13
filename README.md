# [SKN09-2nd-2Team]
✅ SKN AI FAMILY CAMP 9기<br>

---
# 💗Contents
### 1. 팀 소개
- **팀명**
- **팀원 소개**

### 2. 프로젝트 소개
- **프로젝트 기간**
- **WBS**
- **프로젝트 주제**
- **프로젝트 진행배경**
 
### 3. 데이터 소개
- **데이터 소개**
- **사용 컬럼 소개**
- **info**

### 4. ML 절차
- **데이터 이상치 및 결측치 처리**
- **EDA**
- **데이터 전처리**
- **모델 선정**
- **평가**
- **피드백**

### 5. 기대효과

---

# 💗Team Introduce
### 🎃팀명: Fade Out 🍀<br>
### 🐱팀원

| 이름      | GitHub ID                          |
|-----------|------------------------------------|
| 🧑‍💻 김우중  | [@kwj9942](https://github.com/kwj9942)      |
| 👩‍💻 이다인  | [@daainn](https://github.com/daainn)        |
| 👩‍💻 이재혁  | [@ohdyo](https://github.com/ohdyo)          |
| 👨‍💻 전성원  | [@Hack012](https://github.com/Hack012)      |

<br>


---

# 💗프로젝트 소개
✅ **프로젝트 기간: 2025.02.04 - 2025. 02.14**
## WBS
- 이미지 들어갈 예정

## 프로젝트 주제
#### **음악 사이트 이탈률 분석**

## 프로젝트 진행 배경
모바일 음악 스트리밍 시장의 경쟁이 치열해지면서, AI 기반 추천 시스템과 독점 콘텐츠 확보가 핵심 전략으로 부상함 <br>
`Spotify`, `Apple Music` 등은 AI 알고리즘을 활용한 맞춤형 추천과 큐레이션 기능을 강화하며 사용자를 확보하고 있으며, `멜론`, `지니뮤직`, `플로` 등도 유사한 전략을 통해 경쟁력을 높임
이러한 환경에서 **사용자 이탈**을 **예측**하고 **방지**하는 것은 음악 앱의 생존과 직결되는 핵심 요소가 되었음 <br>

출처
- https://www.yna.co.kr/view/AKR20190213143851017 **진격의 플로**
- https://news.mtn.co.kr/news-detail/2019022809241139855 **인공지능&킬러콘텐츠**
- https://www.chosun.com/economy/tech_it/2023/09/06/QJFPBWMJP5C2BDEGYSBEFXU4UQ/ **주요 업체의 이용자 확보**

# 💗 데이터 소개
## 데이터 소개
- <a href="https://www.kaggle.com/competitions/kkbox-churn-prediction-challenge/data">대만 음원 사이트KKBox</a>
## 사용 컬럼 소개
- **msno**: 사용자 고유 식별자
- **city**: 사용자의 도시 코드
- **bd**: 사용자의 연령
- **gender**: 사용자의 성별 (남성/여성/미입력)
  - female: 0
  - male: 1
- **registered_via**: 사용자의 등록 경로 (예: Facebook, Google 등)
- **registration_init_time**: 사용자의 최초 가입 날짜
- **is_churn**: 이탈 여부 (1: 이탈, 0: 유지)
- **is_back**: 사용자가 다시 돌아왔는지 여부
- **payment_plan_sum**: 사용자가 구독한 결제 플랜 개수
- **plan_list_price**: 구독 요금제 원가
- **actual_amount_paid**: 실제 결제된 금액
- **discount_rate**: 할인율
- **is_auto_renew**: 자동 갱신 여부 (1: 자동 갱신, 0: 수동 갱신)
- **membership_expire_date**: 멤버십 만료일
- **is_cancel**: 구독 취소 여부
- **transaction_count**: 결제 내역 횟수
- **num_25**: 전체 노래 길이 중 25% 이하로 청취된 곡 수
- **num_50**: 전체 노래 길이 중 50% 이하로 청취된 곡 수
- **num_75**: 전체 노래 길이 중 75% 이하로 청취된 곡 수
- **num_985**: 전체 노래 길이 중 98.5% 이하로 청취된 곡 수
- **num_100**: 전체 노래 길이 중 100% 청취된 곡 수
- **num_unq**: 고유한 곡 청취 수
- **total_secs**: 총 청취 시간(초)
- **log_start**: 사용자의 첫 로그 기록
- **log_end**: 사용자의 마지막 로그 기록

# 💗 ML 절차
## 데이터 이상치 및 결측치 처리
**이상치 및 결측치 컬럼**
   - bd
   - gender<br><br>
  **이상치 시각화: `bd`, `payment_plan_sum`, `plan_list_price`, `actual_amount_paid`, `discount_rate`, `transaction_count`**
  [사진]<br>
  → 이상치 컬럼을 봤을 때, `bd` 컬럼의 이상치가 무의미하다고 판단<br><br>
  - `bd` 컬럼 이상치 처리 전
  [사진] [사진] <br>
  - 처리 공정
    1. 음수 데이터 절댓값 처리
    2. 10 ~ 100 사이 데이터 외 삭제
  - `bd` 컬럼 이상치 처리 후
  [사진] <br><br>
  **결측치**
  - `gender` 컬럼 결측치 처리 전
  [사진] <br>
  - 처리 공정
    1. 결측치 삭제
    2. 범주형으로 Label Encoding 진행
  - `gender` 컬럼 결측치 처리 후
  [사진]

## EDA
- `is_churn` 컬럼과 전체 컬럼의 상관계수
- 

## 데이터 전처리
1. 불필요한 컬럼 삭제
    - msno
    - membership_expire_date
    - registration_init_time
    - log_start
    - log_end
    - is_back
2. to datetime 변환
   - membership_expire_date
   - registration_init_time
   - log_start
   - log_end
3. 파생변수 생성
   - 등록기간 (`registration_duration`): [`membership_expire_date`column] - [`registration_init_time`column]
   - 음악 청취 기간 (`listening_duration`): ([`log_end`column] - [`log_start`column]) 후 day 추출

## 모델 선정

## 평가

## 피드백

# 💗 기대효과
- 본 프로젝트를 통해 **음악 사이트의 이탈 요인을 보다 명확하게 이해**하고, 이를 기반으로 맞춤형 마케팅 및 운영 전략을 수립할 수 있다.
- **이탈 예측 모델을 활용하여 사전 대응 전략을 강화**하고, 궁극적으로 사용자 유지율을 높이는 데 도움을 줄수 있다.
