import requests
import urllib.parse
from bs4 import BeautifulSoup

cookies = {
    '_ga': 'GA1.1.1729020262.1713994291',
    '_ym_uid': '1668333867978722429',
    '_ym_d': '1713994291',
    'PHPSESSID': '2lniriiq310dmvhjqqr0h3aa3h',
    '_ga_QM6KN23Y0N': 'GS1.1.1725121708.3.0.1725121708.0.0.0',
    '_ym_isad': '1',
    'sess_cookie': '66297a2e866013.89587670',
    'sess_counter': '18',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': '_ga=GA1.1.1729020262.1713994291; _ym_uid=1668333867978722429; _ym_d=1713994291; PHPSESSID=2lniriiq310dmvhjqqr0h3aa3h; _ga_QM6KN23Y0N=GS1.1.1725121708.3.0.1725121708.0.0.0; _ym_isad=1; sess_cookie=66297a2e866013.89587670; sess_counter=18',
    'priority': 'u=0, i',
    'referer': 'https://kartaslov.ru/%D0%BF%D0%BE%D0%B4%D0%BE%D0%B1%D1%80%D0%B0%D1%82%D1%8C-%D1%81%D0%B8%D0%BD%D0%BE%D0%BD%D0%B8%D0%BC%D1%8B-%D0%BE%D0%BD%D0%BB%D0%B0%D0%B9%D0%BD',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "YaBrowser";v="24.7", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 YaBrowser/24.7.0.0 Safari/537.36',
}

def get_synonyms(word):
    try:
        response = requests.get(
            f'https://kartaslov.ru/%D1%81%D0%B8%D0%BD%D0%BE%D0%BD%D0%B8%D0%BC%D1%8B-%D0%BA-%D1%81%D0%BB%D0%BE%D0%B2%D1%83/{urllib.parse.quote(word)}',
            cookies=cookies,
            headers=headers,
        )


        soup = BeautifulSoup(response.text, 'lxml')

        links = soup.find_all('a', class_="syn synRepeat")

        result = {}
        res = []

        for link in links:
            res.append(link.text)

        if not res:
            raise Exception('Слово не найдено')

        result = {
            'status': 'ok',
            'word': word,
            'synonyms': res
        }
    except Exception as ex:
        result = {
            'status': 'error',
            'message': str(ex)
        }

    return result

print(get_synonyms('слово'))