import urllib.request
import pymysql
from bs4 import BeautifulSoup

url = "https://movie.douban.com/top250"
moveList = []


# 获取html
def get_html(url):
    res = urllib.request.urlopen(url)
    html = res.read().decode()
    return html


# 解析html
def parse_html(htmlfile):
    # 使用html.parser解析器
    mysoup = BeautifulSoup(htmlfile, "html.parser")
    # 找到所有的ol标签
    movie_zone = mysoup.find('ol')
    # 取出其中的li标签及其数据
    movie_list = movie_zone.find_all('li')
    for movie in movie_list:
        movie_name = movie.find('span', attrs={'class': 'title'}).getText()
        moveList.append(movie_name)
    next_page = mysoup.find('span', attrs={'class': 'next'})
    if next_page.find('a'):
        if next_page:
            new_url = "" + url + next_page.find('a')['href']
            parse_html(get_html(new_url))


# 保存数据
def save_data(moveList):
    connect = pymysql.Connect(host='xx.xx.xx.xx', port=3306, user='root', passwd='xxx', db='xxx', charset='utf8')
    # 获取游标
    cursor = connect.cursor()
    sql = "insert into movie_name(id,name) values ('%s','%s')"
    i = 0
    for movie in moveList:
        data = (++i, movie)
        cursor.execute(sql % data)
        connect.commit()
    cursor.close()
    connect.close()


parse_html(get_html(url))
save_data(moveList)

