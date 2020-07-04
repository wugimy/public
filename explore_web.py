import requests,os
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

#參數設定(url:網址, layers:要搜尋幾層, file_type:檔案類型(副檔名), to_disk:存放下載檔案的位置)
url = "http://10.88.172.86:8080/data/images/B8MOR10/14H14A04-P5-ADI/20200511/4F0559K900/"
layers = 2
file_type = "jpg"
to_disk = "D:/python_download/20200704"

def get_link(url):
    link_list = []
    root = url[0:url.find("/",url.find("//")+2)]
    path = url[0:url.rfind("/")+1]

    htmlfile = requests.get(url)
    soup = BeautifulSoup(htmlfile.text, 'html.parser')

    # 所有的超連結
    a_tags = soup.find_all("a")
    for tag in a_tags:
        # 輸出超連結的文字
        if tag.get("href") == None:
            http_url = url
        elif tag.get("href")[0:4]=="http":
            http_url = tag.get("href")
        elif tag.get("href")[0:1]=="/":
            http_url = root + tag.get("href")
        else:
            http_url = path + tag.get("href")

        if http_url not in url:
            link_list.append(http_url)
            
    return link_list

def explore_web(url,layers,file_type):
    link_reserve = []
    links = get_link(url)
    for i in range(0,layers):
        temp = []
        for j in links:
            print("*",end="")
            if j.find("."+file_type) > 0 or file_type == "":
                link_reserve.append(j)
            temp += get_link(j)
        links = temp
        print("第",i,"層搜尋完成")
    return link_reserve


links = explore_web(url,layers,file_type)

for i in links:
    print(i)
print("共找到",len(links),"筆")

#轉成集合，避免重複
link_set = set(links)
for i in link_set:
    #針對不想要的資料夾過濾
    if i.find("/icon/") < 0: 
        link = i
        file_name = link[link.rfind('/'):]
        local = os.path.join(to_disk + file_name)  #檔案儲存位置
        urlretrieve(link,local)
print("下載到",to_disk,"完成")
