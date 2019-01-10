from urllib import request
from bs4 import BeautifulSoup
import re

#Request the url and return the url
def requestUrl(index):
    response = request.urlopen(index)
    html = response.read()
    html = html.decode("utf-8")

    # print(html)
    return html

# #parse the blog
# def classParser(index):
#     miui_prefix = "www.miui.com/"
#     result = {}
#     soup = BeautifulSoup(requestUrl(index),'html.parser');
#     all_classes = soup.find_all(title=re.compile(".*：.*"))
#
#     for class_item in all_classes:
#         class_href = class_item.get('href')
#         a = class_item.get_text()
#         print(miui_prefix + class_href)
#         print(a)

# def titleParser(index):
#
# if __name__ == "__main__":
#     extract_index = "http://www.miui.com/forum-38-2.html"
#     classParser(extract_index);
