import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def parse_hh(keyword, pages=1):
    ua = UserAgent()
    headers = {"User-Agent": ua.random}

    URL = 'https://hh.ru/search/vacancy'

    vacancies = []

    for page in range(pages):
        params = {
            "text": keyword,
            "page": page
        }

        response = requests.get(URL, params=params, headers=headers)
        if response.status_code != 200:
            print(f"Error {response.status_code}: couldn't load the page {page}")
            continue
        
        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.find_all("div", class_="magritte-card___bhGKz_6-2-0")

        for item in items:
            title_tag = item.find("a", class_="magritte-link___b4rEM_5-0-4")
            title = title_tag.text.strip() if title_tag else "Untitled"
            link = title_tag["href"] if title_tag else "#"

            company_tag = item.find("div", class_="company-name-badges-container--ofqQHaTYRFg0JM18")
            company_name = company_tag.text.strip() if company_tag else 'Not specified'
            

            salary_tag = item.find("span", class_="magritte-text___pbpft_3-0-27 magritte-text_style-primary___AQ7MW_3-0-27 magritte-text_typography-label-1-regular___pi3R-_3-0-27")
            salary = salary_tag.text.strip() if salary_tag else "Not specified"


            vacancies.append({
                "title": title,
                "company": company_name,
                "salary": salary,
                "link": link
            })

    return vacancies
    
vacancies = parse_hh("Вакансии", pages=1)

for i, vacancy in enumerate(vacancies, 1):
    print(f"{i}. {vacancy['title']} ({vacancy['company']}) - {vacancy['salary']}\n{vacancy['link']}\n")