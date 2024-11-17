# Stock Price Forecasting with Regression Models

이 프로젝트는 머신러닝과 다양한 데이터 소스를 활용하여 주식 시장 데이터를 분석하고 예측하는 시스템을 제공합니다. `Flask`를 사용한 RESTful API, `Gradio` 기반의 사용자 인터페이스, 그리고 `LightGBM` 모델을 활용하여 종가 예측 및 데이터 시각화를 수행합니다.

---

## 주요 기능

### 1. 데이터 수집 및 전처리
- **주식 데이터**:
  - `yfinance`를 활용하여 Open, High, Low, Close, Volume 데이터를 수집.
  - 추가적으로 환율, 금, 유가 데이터를 수집하여 분석에 활용.
- **거시 경제 지표**:
  - `FRED API`를 통해 Interest Rate, VIX, TEDSpread 등의 데이터를 수집.
  - 수집된 데이터를 결측치 처리 및 전처리하여 학습 데이터로 병합.
- **실시간 데이터**:
  - `TradingView`에서 실시간 상승률 상위 종목 및 거래량 상위 종목 데이터를 수집.

### 2. 머신러닝 기반 예측
- **모델 사용**: `LightGBM` 모델을 활용하여 주식 종가를 예측.
- **분석 지표 추가**:
  - Daily_Return, Rolling_Mean_Close, 상관계수 등 특성 추가.
  - 이동평균과 이동표준편차를 사용해 시계열적 특성을 반영.

### 3. API 제공
- **Flask RESTful API**:
  - `backend/stock_backend.py`에서 Flask 서버를 실행하여 `/predict` 엔드포인트를 제공합니다.
  - JSON 응답 예시:
    ```json
    {
      "Open": 135.67,
      "Predicted Close": 140.45,
      "Prediction": "UP",
      "Max_diff": 2.5,
      "Min_diff": -1.3
    }
    ```

### 4. 시각화 및 사용자 인터페이스
- **Gradio 기반 웹 UI**:
  - `frontend/index.py`를 통해 종목을 검색하여 예측 결과와 차트를 확인 가능.
  - 상승/하락 여부에 따라 시각적 표시.
- **Plotly 및 Matplotlib 차트**:
  - 주식 종가 및 변동성 차트를 생성하여 사용자에게 제공.

---

## 프로젝트 구조

```plaintext
STOCKPRICEFORECAST_REGRESSION_ML/
│
├── .gradio/                    # Gradio 설정 파일
├── .vscode/                    # VS Code 디버깅 설정
│   └── launch.json             # Flask와 Gradio를 동시에 실행하기 위한 설정
├── backend/                    # 백엔드 모듈
│   ├── exchangerate.py         # 네이버 환율 데이터 크롤러
│   ├── stockchart.py           # TradingView 데이터 크롤러
│   └── stock_backend.py        # Flask 서버 및 데이터 처리
│
├── data/                       # 데이터 디렉터리
│   └── available_tickers.csv   # 사용 가능한 주식 티커 목록
│
├── frontend/                   # 프론트엔드 리소스
│   ├── images/                 # UI 이미지 리소스
│   └── index.py                # Gradio 인터페이스 및 실행 파일
│
├── project_common/             # 공통 모듈
│   ├── my_yfinance.py          # 주식 데이터 수집 및 전처리
│
├── requirements.txt            # Python 패키지 목록
└── README.md                   # 프로젝트 설명 파일
```

---

## 설치 및 실행

### 1. 필수 패키지 설치
다음 명령어를 사용하여 필요한 라이브러리를 설치하세요:
```bash
pip install -r requirements.txt
```

### 2. VS Code를 사용한 실행
`launch.json` 설정을 사용하여 `stock_backend.py`와 `index.py`를 동시에 실행합니다:
1. `.vscode/launch.json` 파일을 열어 설정을 확인합니다.
2. VS Code 디버그 탭(▶️)에서 실행 구성을 선택한 뒤 실행합니다.

### 3. Flask 백엔드 수동 실행
`stock_backend.py`를 실행하여 Flask 서버를 활성화합니다:
```bash
python backend/stock_backend.py
```

### 4. Gradio UI 실행
`index.py`를 실행하여 Gradio 기반의 사용자 인터페이스를 실행합니다:
```bash
python frontend/index.py
```

---

## 사용 기술 및 라이브러리

- **데이터 수집 및 전처리**:
  - `yfinance`, `pandas`, `pandas_datareader`
- **머신러닝 모델**:
  - `LightGBM`, `scikit-learn`
- **백엔드**:
  - `Flask`, `BeautifulSoup`, `requests`
- **시각화**:
  - `Matplotlib`, `Plotly`, `Seaborn`

---

## 예측 API 사용 예시

### 1. API 요청
`curl`, Postman, 또는 기타 HTTP 클라이언트를 사용하여 `/predict` 엔드포인트에 요청을 보냅니다:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"ticker": "AAPL"}' http://127.0.0.1:5000/predict
```

### 2. API 응답
```json
{
  "Open": 135.67,
  "Predicted Close": 140.45,
  "Prediction": "UP",
  "Max_diff": 2.5,
  "Min_diff": -1.3
}
```
