from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

st = time.time()
print('start time', st)
for i in range(3):      #3 times run chesthunnam
    driver = webdriver.Chrome()
    url = 'https://www.imdb.com/find/?q=telugu&ref_=nv_sr_sm'
    driver.get(url)
    driver.maximize_window()
    page_source = driver.page_source
    driver.close()


    jsoup = BeautifulSoup(page_source)

    body = jsoup.find('ul', attrs={'class':'ipc-metadata-list ipc-metadata-list--dividers-after sc-17bafbdb-3 gAWnDM ipc-metadata-list--base'})
    # print(jsoup)
    # print(body)
    result = body.find_all('li', attrs={'class':'ipc-metadata-list-summary-item ipc-metadata-list-summary-item--click find-result-item find-title-result'})
    # print(result)
    finla_result = []
    for li in result:
        dummy = dict()
        # print(li)
        a = li.find('a', attrs={'class':'ipc-metadata-list-summary-item__t'})
        # span = li.find('span',attrs={'class':'ipc-metadata-list-summary-item__li'})
        span = li.find_all('span',attrs={'class':'ipc-metadata-list-summary-item__li'})
        # print(actor_span)
        name = a.text
        link = a['href']
        year = span[0].text

        actor = span[-1].get_text()

        # print('Name: ', name)
        # print('Link: ', link)
        dummy['Movie Name'] = name
        dummy['Link'] = link
        dummy['Year'] = year
        dummy['Actor'] = actor
        finla_result.append(dummy)
        # break
    print(finla_result)
    df = pd.DataFrame(finla_result)

    def remove(x):
        return x.replace('–','')

    df['Year'] = df['Year'].apply(remove)
    # print(df['Year'])
    print(df)
    # df.to_csv('D:\\$PYTHON\\selenium sample imdb.csv', index=False)


et = time.time()
print('end time', et)