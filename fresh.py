from bs4 import BeautifulSoup
from lxml import html
import xml
import requests
from scrapy.selector import Selector


def getHtml(filename,url,headers):
    f = requests.get(url,headers=headers)
    soup = str(BeautifulSoup(f.content, "lxml") )
    file=open(filename,"w")
    for i in soup:
        file.write(i)
    file.close()

def scrapyContent(filename):
    body=open(filename,'r').read()
    class1=Selector(text=body).xpath('//img/@alt').extract()
    imageUrlList=Selector(text=body).xpath('//img/@data-ks-lazyload').extract()
    for i in class1:
        print(i.replace('\\"',""))
    j=0
    for i in imageUrlList:
        filename=i.replace('\\"',"")[2:]
        print("http://"+filename)
        saveImage("http://"+filename,str(j)+".jpg")
        j+=1


def saveImage(ImageUrl,ImageName):
    r = requests.get(ImageUrl,stream=True)
    fd=open(ImageName, 'wb')
    for chunk in r.iter_content():
            fd.write(chunk)
    fd.close()

if __name__ == "__main__":
    #所有页面对应的无图片html文件，其中有image的链接
    urlList=[
        "https://freshchina.world.tmall.com/i/asynSearch.htm?_ksTS=1592938579782_367&callback=jsonp368&mid=w-15900500889-0&wid=15900500889&path=/category.htm",
        "https://freshchina.world.tmall.com/i/asynSearch.htm?_ksTS=1592940782483_363&callback=jsonp364&mid=w-15900500889-0&wid=15900500889&path=/category.htm&pageNo=2",
        "https://freshchina.world.tmall.com/i/asynSearch.htm?_ksTS=1592940782483_363&callback=jsonp364&mid=w-15900500889-0&wid=15900500889&path=/category.htm&pageNo=3"
    ]
    #cookie，每次使用都需要从浏览器中截取，但是注意使用次数（小心封ip）
    mycookie="hng=GLOBAL%7Czh-CN%7CUSD%7C999; cna=Ty3tFSuTtHICATogBTKkU+s7; isg=BNbWf2s1lFMZzaD3Wm5Eo3qxJIXYdxqxZZ5nUEA_wrlUA3adqAdqwTzxmx_vsBLJ; l=eBM7l-QIQd6Ym-QDKOfahurza77OSIOYYuPzaNbMiOCP9vfp5JaVWZY4rlY9C31Vhs_MR3z8h5yyBeYBYIbTawcWQ577IRDmn; _m_h5_tk=13b1d31d1dec3c5ff50542da24e89412_1592937617924; _m_h5_tk_enc=840c4166b0b1e2dc93915602322597d4; lid=%E9%87%8C%E6%98%82%E7%83%A4%E9%B8%A1%E8%85%BF%E5%A0%A1; pnm_cku822=; dnk=%5Cu91CC%5Cu6602%5Cu70E4%5Cu9E21%5Cu817F%5Cu5821; uc1=pas=0&cookie21=UIHiLt3xThH8t7YQoFNq&cookie15=W5iHLLyFOGW7aA%3D%3D&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&existShop=false&cookie14=UoTV7giIqHQd4w%3D%3D; uc3=vt3=F8dBxGGSzmgnzwCzFXI%3D&nk2=o%2FI20XrO4PHNB9vF&lg2=UIHiLt3xD8xYTw%3D%3D&id2=UNGTrHlIbWjrXQ%3D%3D; tracknick=%5Cu91CC%5Cu6602%5Cu70E4%5Cu9E21%5Cu817F%5Cu5821; _l_g_=Ug%3D%3D; uc4=id4=0%40UgbrAkDrNhsWIRRniEcWrBq7LTpY&nk4=0%40oaRKnB4qsTg1wMTUrFEolu5GngBEY8E%3D; unb=3155670772; lgc=%5Cu91CC%5Cu6602%5Cu70E4%5Cu9E21%5Cu817F%5Cu5821; cookie1=VAcMZDYOGaGaqXc7egWQsxP8nSHuhA5EB6SGq1fHLWg%3D; login=true; cookie17=UNGTrHlIbWjrXQ%3D%3D; cookie2=18fd33cecc13cbdd4f5869de5ec62bd3; _nk_=%5Cu91CC%5Cu6602%5Cu70E4%5Cu9E21%5Cu817F%5Cu5821; sgcookie=E1mVpJgWQgxX1TXrvRthG; sg=%E5%A0%A12c; t=af99a3391dd924e014bbe0e77a46b7f7; csg=5a0e0f17; _tb_token_=ee5ebe5373b37"
    #使用火狐浏览器，如果使用其他浏览器，需要换user-agent
    headers = {
            'cookie':mycookie,
            'user-agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0",
            'referer': 'https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.6.77f65d5c5Awoik&id=613110434906&skuId=4352166796016&areaId=500100&user_id=2206943654630&cat_id=2&is_b=1&rn=74e1dcbd42307c1199e6fb4d70c6ae1b',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9'
    }
    #分别对应三页内容，如有需要，可以伴随urlList修改
    filenameList=["fresh1.xml","fresh2.xml","fresh3.xml"]
    #for i in range(len(filenameList)):
    #    getHtml(filenameList[i],urlList[i],headers)
    scrapyContent(filenameList[0])

