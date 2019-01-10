from urllib import request
from bs4 import BeautifulSoup
from postsTest import postParser
import re

from XiaoMi import requestUrl

#********************* parse the page Urls
def pageParser(index):
    result = {}
    soup = BeautifulSoup(requestUrl(index),'html.parser');
    all_classes = soup.find("a", href=re.compile("forum.php?.*page=.*"))
    href1 = all_classes.get('href')

    # print(href1[:-1])
    return href1[:-1]

#find the last page number
def requestPages(index):
    soup = BeautifulSoup(requestUrl(index), 'html.parser')
    last_page = soup.find("a", attrs={'class': 'last'})
    page_string = last_page.get_text()
    page_num = re.sub("\D","",page_string)
    # print(page_num)
    return int(page_num)

# def titleParser(index):

if __name__ == "__main__":
    extract_index = "http://www.miui.com/type-38-287.html"
    # pageParser(extract_index);

    for i in range(1656, requestPages(extract_index) + 1):
        page_href_suffix = pageParser(extract_index) + str(i)
        page_href = "http://www.miui.com/" + page_href_suffix
        postParser(page_href,i)
        # requestUrl(page_href)
        # print(page_href)
