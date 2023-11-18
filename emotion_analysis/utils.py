# sentiment_analysis/utils.py

from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options

from textblob import TextBlob

def get_youtube_comments(video_url, scroll_pause_time=2):
    # Chrome 웹 드라이버 실행
    options = Options()
    options.add_argument("--headless")  # GUI를 사용하지 않도록 설정 (옵션)

    # ChromeDriver를 PATH에 포함된 상태에서는 아래 코드로 바로 사용 가능
    driver = webdriver.Chrome(options=options)

    # 유튜브 댓글 페이지로 이동
    driver.get(video_url)

    # 페이지 스크롤 다운
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # 페이지 소스 가져오기
    page_source = driver.page_source

    # BeautifulSoup을 사용하여 댓글 추출
    soup = BeautifulSoup(page_source, 'html.parser')
    comments = [comment.text for comment in soup.find_all('yt-formatted-string', {'id': 'content-text'})]

    # 드라이버 종료
    driver.quit()

    return comments


def analyze_sentiment(comments):
    positive_count = 0
    negative_count = 0

    for comment in comments:
        analysis = TextBlob(comment)
        # 분석 결과의 감성 점수를 확인하여 긍정 또는 부정으로 분류
        if analysis.sentiment.polarity > 0:
            positive_count += 1
        elif analysis.sentiment.polarity < 0:
            negative_count += 1

    total_comments = len(comments)

    # 긍정, 부정 감성 비율 계산
    positive_percentage = (positive_count / total_comments) * 100
    negative_percentage = (negative_count / total_comments) * 100
    normal_percentage = (100 - positive_percentage - negative_percentage)

    result = {
        'total_comments': total_comments,
        'positive_count': positive_count,
        'negative_count': negative_count,
        'normal_count': total_comments - positive_count - negative_count,
        'positive_percentage': positive_percentage,
        'negative_percentage': negative_percentage,
        'normal_percentage': normal_percentage,
    }

    return result
