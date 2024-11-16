import requests
from bs4 import BeautifulSoup
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 상수로 URL 정의
NAVER_EXCHANGE_RATE_URL = "https://finance.naver.com/marketindex/"

def get_usd_to_krw_exchange_rate():
    """
    네이버 환율 페이지에서 달러-원 환율을 가져오는 함수
    :return: USD-KRW 환율 (float)
    """
    try:
        # HTTP 요청
        response = requests.get(NAVER_EXCHANGE_RATE_URL)
        response.raise_for_status()

        # BeautifulSoup으로 HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # 달러-원 환율 데이터 추출
        rate_element = soup.select_one('div.market1 div.head_info > span.value')
        if rate_element is None:
            logging.error("환율 정보를 찾을 수 없습니다. HTML 구조를 확인하세요.")
            return None

        usd_krw = float(rate_element.text.replace(',', ''))
        logging.info(f"현재 달러-원 환율: {usd_krw}")
        return usd_krw

    except requests.exceptions.RequestException as e:
        logging.error(f"HTTP 요청 중 오류 발생: {e}")
        return None
    except ValueError as e:
        logging.error(f"환율 값 파싱 중 오류 발생: {e}")
        return None