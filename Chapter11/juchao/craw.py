'''
模擬巨潮資訊的網路爬蟲
'''

import requests


def get_one_page_data(key, date_start='', date_end='', fulltext_str_flag='false', page_num=1, pageSize=30,sortName='nothing',sortType='desc'):
    '''
    :param key: 搜索的關鍵字
    :param date_start:起始時間 
    :param date_end: 終止時間
    :param fulltext_str_flag:是否為內容搜索，預設false，亦即標題搜索 
    :param page_num: 要搜索的頁碼
    :param pageSize: 每頁的數量
    :param sortName: 排序名稱，對應關係為：'相關度': 'nothing', '時間': 'pubdate', '代碼': 'stockcode_cat'，預設為相關度
    :param sortType: 排序類型，對應關係為：'昇冪': 'asc', '降冪': 'desc'，預設為降冪
    :return: 總頁碼和目前頁碼
    '''
    params = {'searchkey': key,
              'sdate': date_start,
              'edate': date_end,
              'isfulltext': fulltext_str_flag,
              'sortName': sortName,
              'sortType': sortType,
              'pageNum': str(page_num),
              'pageSize': str(pageSize)}
    key_encode = requests.models.urlencode({'a': key}).split('=')[1]

    url = 'http://www.cninfo.com.cn/cninfo-new/fulltextSearch/full'
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Accept-Encoding': 'gzip, deflate, sdch',
               'Accept-Language': 'zh-TW,zh;q=0.8',
               'Connection': 'keep-alive',
               'Cookie': 'JSESSIONID=7DF993E8D803E8672C6069F48399F60D; cninfo_search_record_cookie=%s' % key_encode,
               'Host': 'www.cninfo.com.cn',
               'Referer': 'http://www.cninfo.com.cn/cninfo-new/fulltextSearch?code=&notautosubmit=&keyWord=%s' % key_encode,
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36 Qiyu/2.1.0.0',
               'X-Requested-With': 'XMLHttpRequest'}
    try:
        r = requests.get(url, headers=headers, params=params, timeout=20)
        # r.encoding = 'utf-8'
        page_content = r.json()
        page_value = page_content['announcements']
        total_page_num = page_content['totalpages']
        return total_page_num, page_value
    except:
        return None, None


if __name__ == '__main__':
    total_num, page_value = get_one_page_data('台北', date_start='2015-01-05', date_end='2015-07-03')
