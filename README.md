# [SKN09-2nd-2Team]
✅ SKN AI FAMILY CAMP 9기<br>

<div align="center">
  <img src="./readme_images/team.png" height="70%" width="70%">
</div>


---
# 🔊Contents


| 1. 팀 소개 | 2. 프로젝트 소개 | 3. 데이터 소개 | 4. ML 절차 | 5.기대효과 |
|------------|----------------|----------------|------------|------------|
| 팀명 | 프로젝트 기간, WBS | 데이터 소개, 사용 컬럼 소개 | 데이터 정제, 이상치,결측치 처리, EDA | 기대효과 및 결론 |
|팀원 소개 | 프로젝트 주제, 진행배경 | info | 데이터 전처리, 모델 선정 | |
| | | | 평가, 피드백 | | 

---

# 🎙️Team Introduce
### 🎃팀명: StayTuned 🍀<br>
### 🐱팀원


| 김우중 | 이다인 | 이재혁 | 전성원 |
|------|------|------|------|
| <img src="./readme_images/포비.png"> | <img src="./readme_images/루피.png"> | <img src="./readme_images/뽀로로.png"> | <img src="./readme_images/패티.png"> |
| [@kwj9942](https://github.com/kwj9942) | [@daainn](https://github.com/daainn) | [@ohdyo](https://github.com/ohdyo) | [@Hack012](https://github.com/Hack012) |

---

# 🎼Project Overview
✅ **프로젝트 기간: 2025.02.04 - 2025. 02.14**
## WBS
- 이미지 들어갈 예정

## 프로젝트 주제
#### **음악 사이트 이탈률 분석**

## 프로젝트 진행 배경
최근 음악 스트리밍 서비스 시장이 급격히 성장함에 따라, 사용자 확보뿐만 아니라 사용자 유지율이 중요한 경쟁 요소가 되고 있다.하지만 많은 사용자들이 일정 기간 사용 후 서비스를 이탈하는 문제(churn)가 발생하며, 이러한 현상은 서비스 운영 측면에서 큰 도전 과제로 남은 상태다.
이번 프로젝트에선 이용자 이탈 패턴을 탐색하고, 이를 최소화할 수 있는 전략을 도출하는데 도움을 주고자 기획됐다.

# 🪗 Dataset Description

## 데이터 소개
- <a href="https://www.kaggle.com/competitions/kkbox-churn-prediction-challenge/data">대만 음원 사이트KKBox</a>
## 사용 컬럼 소개

### 원본 데이터
`train.csv`
>*사용자의 이탈 여부를 확인할 수 있는 데이터*
- **msno**: 사용자 고유 식별자
- **is_churn**: 이탈 여부 (1: 이탈, 0: 유지)

`members.csv`
> *사용자의 고유 특성과 관련된 데이터*
- **msno**: 사용자 고유 식별자
- **city**: 사용자의 도시 코드
- **bd**: 사용자의 연령
- **gender**: 사용자의 성별 (남성/여성/미입력)
- **registered_via**: 사용자의 등록 경로 (예: Facebook, Google 등)
- **registration_init_time**: 사용자의 최초 가입 날짜


`transactions.csv`
> *사용자의 거래와 관련된 데이터*
- **msno**: 사용자 고유 식별자
- **payment_plan_id** : 지불 방법
- **payment_plan_days** : 멤버심 플랜 기간 (일)
- **plan_list_price** : 요금제 가격
- **actual_amount_paid** : 실제 지불한 가격
- **is_auto_renew** : 자동갱신 여부
- **transaction_date** : 구독 거래 날짜
- **membership_expire_date** : 구독 만료 날짜
- **is_cancel**: 구독 취소 여부

`user_logs.csv`
> *사용자의 노래 청취와 관련된 데이터*
- **msno**: 사용자 고유 식별자
- **날짜**: 노래를 청취한 날짜(로그에 기록된 날짜)
- **num_25**: 전체 노래 길이 중 25% 이하로 청취된 곡 수
- **num_50**: 전체 노래 길이 중 50% 이하로 청취된 곡 수
- **num_75**: 전체 노래 길이 중 75% 이하로 청취된 곡 수
- **num_985**: 전체 노래 길이 중 98.5% 이하로 청취된 곡 수
- **num_100**: 전체 노래 길이 중 100% 청취된 곡 수
- **num_unq**: 고유한 곡 청취 수
- **total_secs**: 총 청취 시간(초)

### 최종 데이터

`final_data.csv`
> *데이터 정제 및 파생변수 생성을 마친 최종 데이터*
- **city**: 사용자의 도시 코드
- **bd**: 사용자의 연령
- **gender**: 사용자의 성별 (남성/여성/미입력)
- **registered_via**: 사용자의 등록 경로 (예: Facebook, Google 등)
- **is_churn**: 이탈 여부 (1: 이탈, 0: 유지)
 **payment_plan_sum**: 사용자가 구독한 결제 플랜 개수
**plan_list_price**: 구독 요금제 원가 합
- **actual_amount_paid**: 실제 결제된 금액 합
- **discount_rate**: 구독 요금제 원가와 실제 결제된 금액을 토대로 계산된 할인율
- **is_auto_renew** : 자동갱신 여부 비율
- **is_cancel**: 구독 취소 여부 비율
- **transaction_count**: 총 거래 횟수
- **num_25**: 전체 노래 길이 중 25% 이하로 청취된 곡 수
- **num_50**: 전체 노래 길이 중 50% 이하로 청취된 곡 수
- **num_75**: 전체 노래 길이 중 75% 이하로 청취된 곡 수
- **num_985**: 전체 노래 길이 중 98.5% 이하로 청취된 곡 수
- **num_100**: 전체 노래 길이 중 100% 청취된 곡 수
- **num_unq**: 고유한 곡 청취 수
- **total_secs**: 총 청취 시간(초)
- **registration_duration**: 총 가입 기간
- **listening_duration**:
총 노래 청취 기간
- **is_back**: 사용자가 다시 돌아왔는지 여부

# 🎧Tech Stack
| **분류**         | **기술/도구**                                                                            |
|------------------|------------------------------------------------------------------------------------------|
| **언어**         | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python)     |
| **라이브러리**   | ![NumPy](https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy)       ![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas)   ![Matplotlib](https://img.shields.io/badge/Matplotlib-ffffff?style=for-the-badge&logo=Matplotlib) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) |
| **협업 툴**      | ![GitHub](https://img.shields.io/badge/github-121011?style=for-the-badge&logo=github)   ![Git](https://img.shields.io/badge/git-F05033?style=for-the-badge&logo=git) ![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)         |


# 🥁 데이터 전처리 결과서 (EDA)

## 데이터 정제 및 파생변수 생성
> 사용자를 식별하는  `MSNO`컬럼값이 `Rb9UwLQTrxzBVwCB6+bCcSQWZ9JiNLC9dXtM1oEsZA8=`와 같이 매우 길게 구성되어 있어 데이터의 크기를 불필요하게 증가시키는 문제가 있었다. 이를 해결하기 위해 각 값을 고유한 숫자로 변환하는 인코딩을 적용하여 데이터의 효율성을 높였다.

#### 거래 데이터
> 음원 스트리밍 서비스에서 사용자가 구독을 종료한 후 다시 재구독하면, 하나의 사용자에 대해 여러 개의 거래 데이터가 기록될 수 있다. 이를 해결하기 위해, 사용자별로 하나의 행만 유지하도록 데이터를 재구성하였다.
* `is_back` : 사용자가 재구독을 한 경우 1의 값, 사용자가 재구독을 하지 않았을 경우 0의 값을 가지도록 구성.
* `payment_plan_sum` : 사용자가 구독한 결제 플랜 개수의 총함.
* `plan_list_price` : 사용자가 구매한 요금제 가격의 총합.
* `actual_amount_paid ` : 사용자가 실제 지불한 금액의 총합.
* `discount_rate` : 구독한 결제 플랜과 구매한 요금제 가격을 통해 계산된 할인율의 평균.
* `is_auto_renew` : 자동갱신여부의 비율.
* `is_cancle` : 구독 만료 여부의 비율.
* `membership_expire_date` : 가장 최근 구독 만료 날짜.
* `transaction_count` : 총 거래 횟수.

#### 로그 데이터

* 로그 데이터의 경우 파일의 크기가 다른 파일에 비해 공간을 많이 차지하기에 파일을 판다스가 읽을수 있는 크기로 분할

* `member.csv`에 없는 `msno` 드랍

* 모든 데이터가 사용 횟수 및 갯수에 대한 컬럼이기에 음수가 존재하면 안된다 판단하여 음수값이 들어간 행 드랍

* msno별 누적 횟수를 파악하도록 값을 누적시켜 압축
    * 최종적으로 고유한 유저 마다 이용별 기록 횟수 확인 가능 



>* 데이터 정제 및 파생변수 생성을 마친 후 거래 데이터와 로그 데이터 및 타 데이터를 `msno`를 기준으로 merge해주었다.
* 이 과정에서 로그 데이터에만 존재하는 `msno`는 드롭해주었다.

## 데이터 이상치 및 결측치 처리


## EDA

## 데이터 전처리


# 🎹인공지능 학습 결과서 

## 모델 선정 및 학습

## 최종 모델 선정



# 🎶수행 결과

## Streamlit



## Expected Outcomes
- 본 프로젝트를 통해 **음악 사이트의 이탈 요인을 보다 명확하게 이해**하고, 이를 기반으로 맞춤형 마케팅 및 운영 전략을 수립할 수 있다.
- **이탈 예측 모델을 활용하여 사전 대응 전략을 강화**하고, 궁극적으로 사용자 유지율을 높이는 데 도움을 줄수 있다.

# 🎧한 줄 회고