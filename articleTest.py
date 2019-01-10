from XiaoMi import requestUrl
from bs4 import BeautifulSoup
import re

# from postsTest import types_re
#re.compile objects


def articleParser(index):
    result = list()
    soup = BeautifulSoup(requestUrl(index),'html.parser')
    all_articles = soup.find_all('td', attrs={'class':'t_f'})

    for article_item in all_articles:
        article_item_content = article_item.get_text()
        article_item_content_1 = re.sub('\n|\r','',article_item_content)
        article_item_content_2 = re.sub(r'[\000-\010]|[\013-\014]|[\016-\037]','',article_item_content_1)
        result.append(article_item_content_2)
        # print(article_item_content)
    # print(result)

    return result


def timeParser(index):
    soup = BeautifulSoup(requestUrl(index),'html.parser')
    try:
        all_times = soup.find("em",id =re.compile('authorposton\d{7,9}'))
        all_times_content = all_times.get_text()
    except AttributeError:
        all_times_content = "-"
    return all_times_content

def uidParser(index):
    result = list()
    soup = BeautifulSoup(requestUrl(index), 'html.parser')
    all_uids = soup.find_all('a', attrs={'target':'_blank','class': 'xw1'})
    for uid_item in all_uids:
        uid_item_content = uid_item.get_text()
        result.append(uid_item_content)
    # print(result)
    return result
# def commentParser(index):
#     result = list()
#     soup = BeautifulSoup(requestUrl(index),'html.parser')
#     all_comment_uid = soup.find()
def typeParser(index):
    result = list()
    soup = BeautifulSoup(requestUrl(index), 'html.parser')
    all_types = soup.find_all('a', href = re.compile('home.php\?mod=spacecp&ac=usergroup&gid=\d{1,2}'))
    for type_item in all_types:
        type_item_content = type_item.get_text()
        result.append(type_item_content)
    # print(result)
    return result

#
# if __name__ == "__main__":
#     article_url = "http://www.miui.com/thread-17412678-1-1.html";
#     uidParser(article_url)


