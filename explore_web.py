import requests,os
from bs4 import BeautifulSoup

def get_link(url):
    link_list = []
    root = url[0:url.rfind("/")+1]

    htmlfile = requests.get(url)
    soup = BeautifulSoup(htmlfile.text, 'html.parser')

    # 所有的超連結
    a_tags = soup.find_all("a")
    for tag in a_tags:
        # 輸出超連結的文字
        if tag.get("href")[0:4]=="http":
            http_url = tag.get("href")
        else:
            http_url = root + tag.get("href")
        #print(http_url)
        if http_url != url:
            link_list.append(http_url)
    return link_list

def explore_web(url,layers,file_type):
    link_reserve = []
    links = get_link(url)
    for i in range(0,layers):
        temp = []
        for j in links:
            if j.find("."+file_type) > 0:
                link_reserve.append(j)
            temp += get_link(j)
        links = temp
    return link_reserve


#參數設定(url:網址，layers:要搜尋幾層，file_type:檔案類型(副檔名))
url = "https://storage.googleapis.com/gimyweb/index.html"
layers = 3
file_type = "jpg"

links = explore_web(url,layers,file_type)

for i in links:
    print(i)
print("共找到",len(links),"筆")
