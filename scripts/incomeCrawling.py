import re
import requests  
from bs4 import BeautifulSoup as bs

money = []

url = "https://www.jobplanet.co.kr/companies/by_industry/700"
a = requests.get(url).text
soup = bs(a,'lxml')
nums=soup.select('#listCompaniesTitle > span')
for i in nums:
    print("총"+i.get_text()+"개의 정보가 있습니다.")
for i in range(1,300):
    url = "https://www.jobplanet.co.kr/companies/by_industry/700?page="+str(i)
    a = requests.get(url).text
    soup = bs(a,'lxml')
    income = soup.select('#listCompanies > div > div.section_group > section \
    > div > div > dl.content_col2_4 > dd:nth-child(3) > a > strong')
    for j in income:
        if j.get_text() != "0":
            money.append(int(re.sub(',','',j.get_text())))
print(money," ",len(money))
print("평균: ",round((sum(money)/len(money)),2)," 만원")