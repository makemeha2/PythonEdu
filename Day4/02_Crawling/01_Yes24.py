import sqlite3
import urllib.request
from bs4 import BeautifulSoup


def getGoodsInfoDic(goodsTag) :
    # goods_nameTag = goodsTag.find("div", class_="goods_name")
    # bookTitle = goods_nameTag.find("a").text
    goods_nameTag = goodsTag.select("div.goods_name > a")[0]
    bookTitle = goods_nameTag.text

    goods_pubGrpTag = goodsTag.find("div", class_="goods_pubGrp")
    goods_authTag = goods_pubGrpTag.find("span", class_="goods_auth")
    author = goods_authTag.find("a").text

    goods_dateTag = goods_pubGrpTag.find("span", class_="goods_date")
    goods_date = goods_dateTag.text

    d = {'bookTitle' : bookTitle, 'author' : author, 'goods_date' : goods_date}
    return d

if __name__ == "__main__" :
    CONST_CATE = "001001003022"     #IT>프로그래밍
    url = "http://www.yes24.com/24/Category/Display/{0}?PageNumber={1}".format(CONST_CATE, str(1))
    data = urllib.request.urlopen(url)

    soup = BeautifulSoup(data, 'html.parser')
    cCont_goodsSet = soup.find_all('div', class_='cCont_goodsSet')

    lst = []
    for goodsTag in cCont_goodsSet:
        lst.append(getGoodsInfoDic(goodsTag))

    """
    con = sqlite3.connect(r"C:\examples\Day4\01_DataBase\test.db")
    cur = con.cursor()
    for item in lst :
        cur.execute("INSERT INTO Books(book_name, author, pub_date) VALUES(:book_name, :author, :pub_date)", 
        {"book_name":item["bookTitle"], "author":item["author"], "pub_date":item["goods_date"]})
    con.rollback()
    """


    try :
        con = sqlite3.connect(r"C:\examples\Day4\01_DataBase\test.db")
        cur = con.cursor()
        for item in lst :
            cur.execute("INSERT INTO Books(book_name, author, pub_date) VALUES(:book_name, :author, :pub_date)", 
            {"book_name":item["bookTitle"], "author":item["author"], "pub_date":item["goods_date"]})
    except Exception :
        print("error ocurred.")
        con.rollback()
    else :
        print("saved.")
        con.commit()
    finally :
        con.close()



