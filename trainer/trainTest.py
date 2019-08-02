# !/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'qiuzixian'  http://blog.csdn.net/qqzhuimengren/   1467288927@qq.com
# @time          :2018/1/29  10:39
# @abstract    :

from trainer.HtmlDownloader import HtmlDownloader
from headToDict.headToDict import headToDict
import requests, re, json

# headToDict('''
# leftTicketDTO.train_date:2018-02-01
# leftTicketDTO.from_station:FZS
# leftTicketDTO.to_station:HJS
# purpose_codes:ADULT''')

headers = {
'Cookie': 'JSESSIONID=2B5E11D97482C32A6856661D5492C623; _jc_save_detail=true; RAIL_EXPIRATION=1516645110723; RAIL_DEVICEID=ac77a5XG0O3U85_64X4kSeqiY-7S7_5Zb0Ue6z3EkSYY_7gRuKcSGZR1AE80n80Jk69KswYeTt27qK6pWixLI9hUgJ3nIFqdy7osXh8fPYKx83oavnPaArksFm9fqamfMR-N5iaRJacdhpV-Zu8et-jxYda7rFK9; route=495c805987d0f5c8c84b14f60212447d; BIGipServerotn=1373176074.64545.0000; BIGipServerpassport=937951498.50215.0000; current_captcha_type=Z; BIGipServerportal=3084124426.17183.0000; _jc_save_fromStation=%u798F%u5DDE%2CFZS; _jc_save_toStation=%u6DB5%u6C5F%2CHJS; _jc_save_fromDate=2018-02-01; _jc_save_toDate=2018-01-29; _jc_save_wfdc_flag=dc' ,
'X-Requested-With': 'XMLHttpRequest' ,
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML: like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER' ,
'Accept': '*/*' ,
'Host': 'kyfw.12306.cn' ,
'Cache-Control': 'no-cache' ,
'If-Modified-Since': '0' ,
'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init' ,
'Accept-Encoding': 'gzip: deflate: sdch: br' ,
'Accept-Language': 'zh-CN:zh;q=0.8' ,
'Connection': 'keep-alive' ,
}

datas = {
'leftTicketDTO.to_station': 'HJS' ,
'leftTicketDTO.train_date': '2018-02-03' ,
'purpose_codes': 'ADULT' ,
'leftTicketDTO.from_station': 'FZS' ,
}

url = "https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-02-03&leftTicketDTO.from_station=FZS&leftTicketDTO.to_station=HJS&purpose_codes=ADULT"
downloader = HtmlDownloader()

# url = "https://kyfw.12306.cn/otn/leftTicket/init"
# response = downloader.download(url)
# print(response)
stringData = '''
{"data":{"flag":"1","map":{"FYS":"福州南","FZS":"福州","HJS":"涵江","PTS":"莆田","XWS":"仙游"},"result":
["JvG2BRAivhr%2B5oeiRkVyaFWlfT5kZj0Yr%2FLvE4cwB0dKlt2j%2Bsnp%2FueVJRoAlpifSq27yQIOw8Sl%0AqKfxi%2BqurIISLqsr9
%2FoUkjebTKeVN%2BFiT84VykkPbM9Gt7wPcgNXOPGAhu7wmsgBWDdgRjp%2BM2uY%0AJ2JZEDeER3noY
%2BQQ1sSNi5Zyq4AF5zSLjYc5puyNdFTZ2YkNnBQ5kvl0B7e3sr85ls3ftTRq3k4y%0AtWfX82vUHjKoHUrRM6Gw3Lk
%3D|预订|58000D62010K|D6201|FZS|XMS|FZS|PTS|06:21|07:09|00:48|Y|%2BSXlTFtbYMj7bqL6IyD%2F2YfzNpQokixLVBN1Gw
%2BzU69MeQDe|20180201|3|G2|01|04|1|0|||||||有||||有|有|||O0M0O0|OMO|1","SOsJv87ZB%2BOU84ZOWVyHZvgo2K22sPKygpUrprcmHmfw
%2B4ObYHiEx95%2F%2BxvM74ENHtO7mTGMig%2FA%0AzPHesrAC9DecDpOQuJCQj9ZSWOJej
%2FdoqVCSk3fIgFN2lNhUzWZ6PxvHyqF5UzREaxJPiIjlszaF%0A9OhwQ7iTPp0bGTjf40cFiKkWHty66Jk7OvfqG5JlJGwhuhG3E9dlfliNt9xRoC7FtJZi%2FYxlnlqx%0A3u6KNl9D7XEM4VUT%2BNkolXg%3D|预订|58000D657105|D6571|FZS|GZG|FZS|PTS|06:44|07:32|00:48|Y|1Z%2FAC%2Fb92zfoLK%2BS0Ittan0WZxE71BEIdRuunO2aslPIBgdd|20180201|3|G2|01|04|1|0|||||||有||||有|无|||O0O0M0|OOM|0","GbCg2Ca%2BYIoqVR8VgfNz5ZY%2FEApQsClGCxd3Cj63t73kYUmfB%2FbJ3%2BtGpV6nrwuZe%2BN2PM8Q1Kjv%0A6rSNBbebCZR%2BB1GMRZLNVOtG0mjxpeEEDLYdvH%2FGJzPPgiPSi%2FVBbmQfGFvL%2BxUKqGlji1VBj2M3%0AQBrK%2FBqn6eAaDr19qbVzgKiN1c3kbOBGhEsMZOFYBRkvFzqv%2FKfR0JuKhobCU%2BeahCPiThvrArgd%0AJG90p24%2FD6ztRFrODKbdM9%2B7ZO54|预订|5n000D333309|D3333|FYS|IOQ|FYS|HJS|06:45|07:09|00:24|Y|%2Bal%2BhxGgt5Cigs3PtQJNljhKIJgnO47jCarz97b%2B4jqYxdO4|20180201|3|G2|01|02|1|0|||||||有||||有|有|||O0M0O0|OMO|0","Tuepl8wAOqWSH2JqydiUzzOCp%2B2%2BozHriSW9FE%2Fo3Ov5UlBvc5DCbh%2BaLiCHaKaBjHRjGg1vYoqf%0AT1ki89FS0KUDUiXT1V4wUFARGDTQuaZ8SIblOQhwo2ipvWMwx4lHk3FLnOSqXLIv2TQmnIHdZMsI%0AnNXBfiyWoJDGVHKNk%2FnPHmUuk5r0WJHd3xiRCo3tBhMDIXVLqJu7pO5kDnKmSZSWfsJBtgG0EdnG%0ACw4aMuNUuxt%2FGq1yYRCGz1i4Tu9k|预订|5n000D23270J|D2327|FYS|IOQ|FYS|PTS|07:10|07:47|00:37|Y|H436T3fCTJJiZj%2F%2BNgW2Wz3hk0oj5nzjj2gTHMdMvvEPGkk5|20180201|3|G1|01|03|1|0|||||||有||||有|有|||O0M0O0|OMO|0","mKCBYq6Wjrw4UySPy9Ev5A1WUyEnLtuRWeBVMJcsd8lEAusgBsAYEUUoasLMTUV1L2Se2Psb5c98%0A33otxeSOgDJ4bs%2BgBSlJzHIQf3SR3WTPKAou%2BBdaiF4C%2BQCHkjXEGjrqztW%2F0JFUz0AheHX1CdQc%0AtaAkh7OLhiQHiLijv7heo%2FiWUUVKDHNWpZ9mwKvK6Xb%2B5cv8nWW93jihzVbWn5d7eBqxLTFpYqyE%0AqqW36Eq0aScfrAQMfvM1RGQ%3D|预订|58000D62070G|D6207|FZS|XMS|FZS|PTS|07:25|08:13|00:48|Y|Ajac2vXIpQ%2FY7XCg9vGYrnNlcb9msi9iRVfNJgQ34nYhfHYd|20180201|3|G1|01|03|1|0|||||||有||||有|有|||O0M0O0|OMO|0","5donEcSq%2BA9evoEQ7No%2BnZmuBm8tT0eHLHWQB2FAFHqcGLVsVjq1oFqgpxNAQZ0yaAkJ31qGM4wD%0AHyyd0LfSdW60CmSTun2rX9Z4bjCUiLuUnH%2BP2UzBDkTFTXmg4jyCiZ0TobA2qJKOzXBbKl1IqeNC%0AgnUuw2YxtYoxhZfV8q9ElfpWN8iIcpHodmXpaHLR9xRg16e%2Fv8qmU2UhjY5jlaNmzr%2B5LTmWthDS%0AbbQ8ecAzfv%2FHXDHiXSc0wic%3D|预订|58000D64050F|D6405|FZS|LYS|FZS|HJS|07:32|08:14|00:42|Y|oJji9t6QOkevxCvQDgpT8lp7mdYsRq0nE9rGEkwpjAUij3oP|20180201|3|G2|01|03|1|0|||||||有||||16|有|||O0M0O0|OMO|1","uJYAQHa6j8LBn05IlaOHYC6Zbx8ThsvDM2cjmKgvDRxhOiWeJJJmxilqTubJUn9cOgz3xCwIdHot%0A7vG%2FdoTux0gE7McMFvhR5DzX0y%2Bx%2B7RAcnGUTx1MCl9SFOpqQIawFnMbCMqJtoWEIFAO%2FsFZr%2BFv%0APkXLDu8ftV9HZocOYxxRUalvyLr%2B6%2BVEviAM2gHzOEkamaHmAvzXgarOE3MzYUVvF07DPrkp8i%2B5%0AfiW10g15ZnCQlJM0Td5CPCMnYZNQ|预订|5n000D23110C|D2311|FYS|IOQ|FYS|PTS|07:57|08:27|00:30|Y|6vy2uO8XFboIGf3E3zNUx%2BasuHB%2Fl3%2B%2FMTnvrbYPcVtrnN0f|20180201|3|G2|01|02|1|0|||||||有||||有|有|||O0M0O0|OMO|0","Qc%2F1xnQnMw5e%2F6bJVIlRqpTVbhRKBY48bLDJ%2FrrWoZ3KctZwzA7yyeFazpOFlh3NYLcMOJZyhKl9%0AtXSs1dkysrh1hFdZY01mcf6AWT93fey3b79yQED3NeUZbPmhhediopxEf6l48A6vrrmv9PMsTmcO%0AuQl3KUgtRsKW5aHrqsncQc1MAsvvUZuvO%2BVZ9I0uCuJI2uF0sO70a1T9E%2BmQi6m0H0nj7UrbDb7z%0A5GzTUjxa%2FRgCQdQMuXaicJbxfozJ|预订|5n000D22950E|D2295|FYS|IOQ|FYS|HJS|08:13|08:37|00:24|Y|ih106CB4nRMdzszFFDbjKgOEK8RtvyBYXjqvbinxMAYIFZgF|20180201|3|G2|01|02|1|0|||||||有||||有|有|||O0M0O0|OMO|0","scmKZD1B%2BCOlZ7x89BiCNRBK0Y7s0oT%2FFoZkVudowwgZL9PJh%2FVbt2qPw0NUCgVbKaOueEIHQ5qw%0A%2B5NUWK53KCpA2Ykks18zUrvy8h0HXvlU0Er3%2FBqlaKtBLi4IFmFR1F1OwZrnRPP0u9g625pZK2Ow%0AVnU1yIlPWSjDKFhnJt4miqu4854NHQnXas7bbILCNX7%2Bo4KOg7z5DnclpqnOFhfmgm%2BZdEvVd8%2Fk%0AewFb5Gsp1kEJ6aRVAGr13KU%3D|预订|58000D64090G|D6409|FZS|CNS|FZS|HJS|08:20|09:02|00:42|Y|qB4iYVWxEQhmZOT0DKXpgzV0OGgCFxsW%2Fic2uLzBHqp72P9U|20180201|3|G2|01|03|1|0|||||||有||||有|有|||O0M0O0|OMO|0","niEpflXFwPDD2Z7ltl8XpQIdiZffAyu2DrnNhmeZJGwhBDCqhy8pjZzmzykkYgWpAL%2BkFmixc226%0AHEpkgqfOn8jgkDA%2FOWgzFD3ZyiKcLBI%2BtadqmXQexb4C%2F1fjP6h3%2Bqg5w2d%2FtqZ41XaJJ%2F6379nm%0AEA7u87VgsSgkLXz4qMDdTwtu2%2B00boarMt3ZNSX73oQI0xdizq4gOVKW%2F65WCT9qIABM2IihjhJO%0AZ6tTFiGHa5pp6hq9JokVDdkH17a1|预订|5n000D996112|D9961|FYS|GZG|FYS|PTS|08:22|08:58|00:36|Y|uagtsfdylbzlHE8DnwM0uVJPEPeeovNtJZzGbRWMjzvWqAVE|20180201|3|G1|01|03|1|0|||||||有||||有|有|||O0M0O0|OMO|0","qb7bPQMSkt1u0jz2T%2FC8n4OpDjHj8uNwIZSXTrBwT9ZB4lxsTdI%2FWNIy1yUQSLhOuyDhMpkjl54l%0A1%2F3KjaKFHAjvIc1naGcu%2F3Ps%2Bv7cmrC%2B2A3%2FqU0HSbmU%2BsMdd4Tsn6NNl%2BYnfTkX2nJIdqegE8PI%0AQ3g0KeGUH1rEQxIyg%2F8K2uJttQgV%2FpSWzl%2BC9uLDLEo8u29q5I96DW7uLoiC3wKJ1m7ibB97NDIa%0AIMGam4QTKScSBbeMqd3SU0E%3D|预订|58000D958118|D9581|FZS|GZG|FZS|HJS|08:40|09:22|00:42|Y|3SHUNh5XXK%2FHWz2aZFfV22NTwtsDAEVZ01g0dsgBSjCFD6ks|20180201|3|G1|01|04|1|0|||||||有||||无|无|||O0O0M0|OOM|0","hsFipI0HCnskVGyfbZY97qT0h2OllFkq1RqpSLHAmKjtHNnNWzjg4I4o5nMt1YuFzdMJwT3chA%2Fr%0AO7de49yaGMwSCDXYMErt0lRc0llGE2b4GhqSSnooGEB6p0Zb5mhChiOsgtH2MaMU%2B%2B9Fp7JFJ%2BeP%0ApFMhVZmJ4J3YpNbm6159%2FFFMIbFnq03AEAWxsZi3MJRa4Z0yoXCs2AWQzNZTBxuhl8GAHJn874SY%0AKI1DSGo3G3vdFQLdhYTTSnk%3D|预订|58000D62170Q|D6217|FZS|XMS|FZS|PTS|08:51|09:39|00:48|Y|kqJHMFGYf8%2FYxUA2qxkjkaAUftyc%2FIk3EsQV5bvGVh5Qu856|20180201|3|G1|01|05|1|0|||||||有||||有|有|||O0M0O0|OMO|0","LoodCOH%2FlNViX4dzZLshcp7IOLbfN%2BkFOMiAgB7AgOfCZZcjbOLYc8Zihy1yd19ACZeM1Kn0eBSh%0A9Y8RxnGFyQyy65Rd%2Fbxx87cTFzslJNo%2FK%2FIJ9iBtp3MEVpWRQpJsLD9cy1pgzSOYa9KHTcUOox2o%0AGiHtBbguh%2BBY7vbpcGEkzcKLTSJ7mvUSyutbH%2Bdhi%2FJnD6daUUGmXxR9EwJVawtDpuDpIyQGLfou%0Akk4V3gsKV%2BUZEyun47D2cg5Gy9RY|预订|5n000D23010D|D2301|FYS|IOQ|FYS|HJS|09:19|09:43|00:24|Y|ghTegwBvjzz6Jxwz0VMW%2BQWQ4fpSR5Uq1pNsgVvn%2BZCgaAVS|20180201|3|G2|01|02|1|0|||||||有||||有|有|||O0M0O0|OMO|0","XLdQukRmNRNhH%2F5LzJQmnaMyTlgUTDljOC1%2BvqsH%2BuSil4VzNG9s91AcNcBhf7HA5iLUWr9TGh8a%0AWerW2YDlzsI9mPLuxokxBsWmLRqwVoFSiNn%2FnA0%2BXPf8TZc6irpxPgXQNGABlAg3QQqHeRZGogEM%0AaaEkKKIdOUzURmeDit3S15p7iutBW2FmJnRD30Z963WZOiUdgoejJ5JMXBoRclmV5FF6hr2FFgg4%0AOqpEypLcsQjNo2G7ZMPxdVE%3D|预订|58000D64070J|D6407|FZS|LYS|FZS|PTS|09:25|10:13|00:48|Y|wG5hN45kpfVRc6Z8gRqf8DA84CHqbCp56pZb8RmwwwpMJO%2Fp|20180201|3|G1|01|04|1|0|||||||有||||无|2|||O0M0O0|OMO|0","5nfroNSa3XnYXxrWylB6JZSTTpFTtU2dOlBbB96kV5cAaUELUucwCJJbwFRLm%2FbhsYFV4JDbNhF6%0Ab%2B%2BTpB%2BhQFMApbi9ag25858OpCZ0N3IcZYtS7n8H6JdnV7pnsqHIbQSTmE9onDAinwZCGelNEwvr%0AoGm10ZK%2BaoURJPxD4kJAquXQFWOB1DiOsiFZc4OekJiwoTE6WAYsBGmessBMou34SVZrYLaP%2BAiy%0Ay7TTPCEz23oqfGOCgkJTNS7kdLK4|预订|5n000D23230B|D2323|FYS|IOQ|FYS|XWS|09:36|10:13|00:37|Y|0CGRzBVtT8OgMHxsIrfSLA632YuljxmlkV8bE%2Bqa8klHGkS6|20180201|3|G2|01|02|1|0|||||||有||||有|15|||O0M0O0|OMO|0","MPIFrUmy5icRWa2EPOiO8a7QcY2zhR%2Bt0mucuF2BvaDspbCfOXhLIjEV9DQIFNKMepqfD%2FWYqtb%2B%0A0zeWTO4C423vdCSYBF6MakOjiJ9YK2HKw3sPgZhPaLvI%2Bu574wepTOIAEjXmyM5XI4jJ4uXUU2Bd%0AzIKEJ%2BjMILclRIp0zwIznycK4hS9LtFErqlgFTYNIFR8mFW1%2BYf85ZqmiI3tILdnve5P2wRCM7cG%0ApQwxBuVBMTyJsm7CBRpJx5eya1b2|预订|5n000D333703|D3337|FYS|IOQ|FYS|PTS|09:56|10:26|00:30|Y|QqNVKxgYZ0mijQ73XkdJCXqn7NWSYzQLCW3IOYAeDWJY9UXs|20180201|3|G1|01|02|1|0|||||||有||||1|11|||O0M0O0|OMO|0","YMGMV5Hx5TPSP4BIqgHWDzcioa%2Bq5DYEKRHbd%2F2345ij1JvZ%2FLR7%2BcOoYUzerOTkKvnxhODUlYw8%0ATAh20azp%2Fy7qSN3uQYOW8HW%2Bu44qpCjqiAqWy8dqTROI3ZlQUAITHtxI8fjCqAn9TrPvKdqwahT%2B%0Am06UA2aNM%2BEce%2Fuf6%2BgcvFgV3O0OQC6jGR078koGAlR6J22tRkT2nTH9RY7TlpInGfBRhi2JBYCI%0ATnzh7mzbqyTcBBIa3k7X4OU%3D|预订|58000D62190I|D6219|FZS|XMS|FZS|HJS|10:04|10:55|00:51|Y|PFCdBY3OlK2J5xaOrOyIzcEdX9%2FNFST2RfFQIkkTqxdvvPN6|20180201|3|G2|01|04|1|0|||||||有||||有|6|||O0M0O0|OMO|0","qqCeR6FThBzTOMa9jhZ9obVLEUj%2BUTI8r4rpQzVwBvX96kApke5wqo3EUZAU5fbqO8aAjkC9384m%0AdwFk7vKe%2FwBW2On0tm96YC7pe%2BjzzLc54AeCPOVSyB%2FwiA1Idb8WMVlpbrPcoA6ft0n4G%2FouiY26%0A8nQUkUHJOnWtQO1o99mo%2FPSVIRhB2AnoKwa5e8GFEYHIy2e6Sa5USvRKgaHhxmRCjJ0OeqSMz3xL%0AqC9v5PPemd1hYcyQGfyGECNr%2Fc8z|预订|5n000D96211A|D9621|FYS|CNS|FYS|PTS|10:12|10:42|00:30|Y|zrOar%2F%2B26eiCCMSI%2FFDoWMuYlRJWFn24%2BDuor11ftDl%2BGn5e|20180201|3|G1|01|02|1|0|||||||有||||无|1|||O0O0M0|OOM|0","AfVTDI9VyNF%2F05NP0LmLbukfE2Zn36CdBz0nySeU1uvKBdtezrVg%2BpBrjEkfE8TpJafY2ir7AN0U%0AEq4qdru01qGlG3xkvKNXNpHBaJEvlCeX4bjSO99Cz%2FYqpmjfIcGhl0EW1mKIbt8lPyl7EzvmZIof%0AKrS2FcOmZ9dOs3hhSjAC1sF%2BhhMcp7l5FeggoIrOxh2KaPP0zOsTYOIMFp0HN1x2jdgzs9rcfu5E%0AMpoBmkWgJUOIO4ck9jK%2Bo1R1SlLp|预订|5n000D23030H|D2303|FYS|IOQ|FYS|HJS|10:17|10:42|00:25|Y|qR1f1TZElsOVXfzLeiIAxyZCrUoh1dqp8INf9UwhYpgK8ajN|20180201|3|G2|01|02|1|0|||||||有||||12|有|||O0M0O0|OMO|0","WJhp%2FNZyg8Hf0Z%2BfwAl83qAr%2B6zjVHJ05MD%2BiFPtKa10Y5YzSfFwe5sSI7UuaUejJ%2Fcj4BS8Slub%0ARQ6Dje%2FVHzz%2BC7qhiIpAFCgNxrdKAFPSDLK%2FmN1F%2FYzxQiDsQrUlzlAKiFFc5mbU4ejeVKi8HTVv%0ALeJFVfHUxbClW28ymGFlix9jlGczIDN3WDc4%2Bo6Hsq1O%2FP5LDTrUzdJadEl4zi0jLzQlm%2B4M07Cg%0AcLNySFXd8IvRXOym2hx5ehY%3D|预订|57000D232505|D2325|SRG|IOQ|FZS|PTS|10:22|11:11|00:49|Y|WtNcQsOxbS64I7evm5Gc5G1frHT8iotRG0StSP556ebKUY9X|20180201|3|G2|09|11|1|0|||||||有||||1|无|||O0M0O0|OMO|0","DdjgyomgcF0CquZwWhDBiVzs4KLpPXRzPD0jtyjivnzUkw3v2lKB2Fv80M%2FMk5b7TxicKOmV77sh%0AVg%2FvM3WPjmDHSI0Qxdq3JhqZuDlA8TaYycDxjyuJ1syUxfaLOYoBTZjLFJF8VHCNplFxZJT%2BzxO6%0AZfgGK8%2B1Ee7kY3svr65aqEjRa1av4tkU7RlZd3k0WKaJP5weScv3Lf5CKhmuGpi7vIR6dr2u3ctF%0AfKNR8W2lrPDIaOSf3CDUyH9q3VeT|预订|5n000D33390E|D3339|FYS|IOQ|FYS|PTS|10:51|11:27|00:36|Y|7kJITBzG21zAGAdsAOx7KNgQUu8wXsiVxC6qP3LJ6z82Floa|20180201|3|G2|01|03|1|0|||||||有||||无|3|||O0M0O0|OMO|0","TjMKgIkQ8DfyR8uPmSR%2FS1UBQKp%2Fki6whpeb%2FNb3nDFfJ%2F7xyLzkW65RpUvdj1mMpOwsMugSqxU6%0A1juz1%2BPlAiBb26Knombnj%2FLDHlNok72S9L%2FN5OLD1w4RzKVMIQYMj%2B7TvBH5tUELPPORukuiIz2t%0APa3bR7gw%2BxLlmZwzIZcW1B5N3mjuvbceMGeBb8jKAnOV1ZlAR4BNMxS9x3IlbNhWOVNIbK8cPnur%0A%2BFhdU4TtCvKPN%2BBubwq68Ms%3D|预订|58000D62210J|D6221|FZS|ZUS|FZS|XWS|11:01|11:56|00:55|Y|fo5hjsozO%2FZ4VMPeUEGOIyioy7mCfYPBIyoCCMBrnT6gOIRa|20180201|3|G2|01|03|1|0|||||||15||||无|无|||O0M0O0|OMO|0","DqpM1QD5WC5IDqbzWjUS%2FEkhl2zAdz9jS5191YKbGedMuTm%2Fl8Jo1JUIsDMF7yGsDWfEmkPUdU86%0AgT0qN7tN%2Bs5LluV%2F5FIfQzZQaoxFaWwsUCx99ovgrGWOO51xeS5ZtfyoWi1mU3TifG%2B36TQfuEaY%0Atx2hvFAzatixA%2BnuNLeJ87KT4D7TzcAb4HaOOqcc3Jand%2BepdZqN2bmXuhv1bkMkMckQAZYl2XUO%0AfoXkZH3K%2FcvN5mNKvhOYzdjI3uRf|预订|5e000D321931|D3219|NGH|XKS|FYS|PTS|11:02|11:32|00:30|Y|%2BgkzoMWhyMMRt6IVBpV%2BQ5OK0RLn2Las9m%2FLPFoWWXneB7Pa|20180201|3|H2|10|11|1|0|||||||无||||3|无|||O0M0O0|OMO|0","lGNT%2BJLnBkiEZIXi6saVOz2iztvH7G%2BZfCj7Cv8QMA%2BExpHdj8Bu%2BaXIB%2F1WK9GB3opOXoYcmihM%0A0g%2BOTFutskjJL5ctst1w97rEbRJwSk%2FoxLyk%2F6aoESgKFAE6GB0naev5fYfkW1VPUfwrgihlOvy9%0AK2ScOqEn1MrkgoBp1N%2Fwp5LsY6zPl4sPZIQXEuQ6fUPupV%2BXLWj9lRSguC2oa3WQrUO0mLwguL2k%0AWjT45GQBh6r0SoCKpMdXH3o%3D|预订|5u000G530801|G5305|NXG|XKS|FZS|PTS|11:30|12:20|00:50|Y|AbLUlSk%2B5kycKg%2FMxQfsXqjz7xkFOUQp5jBzO0%2BnrN1bK0fg|20180201|3|G1|14|16|1|0|||||||||||1|无|无||O0M090|OM9|1","|预订|5e000D321122|D3211|NGH|XKS|FYS|PTS|11:38|12:08|00:30|N|c7t%2BygKokbsEPDLEAwUiSOnPo7NHodIw12HLIm3NNWYREEA%2B|20180201|3|H3|10|11|1|0|||||||无||||无|无|||O0M0O0|OMO|1","HVBNJdZHZiQCYNC2MVe4WQS3sK9xdCoul17gTO7x%2Biwfe28qbBM%2BNQTxPA%2BTq1Nbolezz3wUqTAq%0AkG6zAuNrpHVgLCZ3CRwdPfqAPisfA2HHZK4p3btceVFukaaGK4GnMetyoasDcgdOnhjjISznJgQK%0AknSZY8yIH0PM0zwdhWvzfuAEcTEvt0V73HjGRNEBkv0sS%2BglqA2TgjfoEb5RVqmt5hZrUG7pHNFf%0AiMFAJLc0No5GTtT8foT0z2A%3D|预订|5l000G165120|G1651|AOH|XKS|FZS|HJS|11:46|12:30|00:44|Y|sl2IAxvpkz6Ms%2FH6FAkKvKkfpjGQAwt8jUuuOyi8xlJBkz3v|20180201|3|H3|12|14|1|0|||||||||||1|无|无||O0M090|OM9|0","|预订|5i000G161120|G1611|ENH|XKS|FZS|PTS|11:59|12:47|00:48|N|0g9SHLdcnFi4DdvKIbehkg%2Fj10F7GVNOUcOR7YJRkUSpm81m|20180201|3|H3|12|14|1|0|||||||||||无|无|无||O0M090|OM9|0","65g8DligINa%2BS6YLNGTJIpHwC7Twq1s2rwaCC1Wb0Dz4MYNHOc%2BN9o0OLiKpMeKQQKuNPMZS3uUM%0Awblf9dv4x5QgwyBtMp1E5h4IEuW9LZB8vHbS%2Bqw979rJPxCdkNGFXZ9%2BHDCy7%2B5ml%2BRJlVhk7vLV%0AyVTwfQLb8YLiiOM9VaiRJcPKEV6NNdHvUi1uLavCePrDp4rIcy3WQGdqlye%2BD3vk940BK812xgR1%0AHJoEYGGwaYIqpU%2FDCk%2FsnZQ%3D|预订|58000D62230S|D6223|FZS|XMS|FZS|PTS|12:10|12:52|00:42|Y|JoZyUSnhAtWEZnvOCWChCB6CaaukCYallYGp4tLoVYcnNoHm|20180201|3|G2|01|02|1|0|||||||有||||有|有|||O0M0O0|OMO|0","ZiZiGbouK7ocxk7UR46kZXIwHYk%2F9iFXuOJ93%2FnG5%2FgituYLUmFhjAsKQcpY14iK0Va0Uj%2B%2FAV8N%0AShFjfwjo5lSe4BCl2V1kSZ0%2FA%2FmvWT2BFXxtgn61TYFsBdMSW5EduJjMcIn0cKsbyWCa1b85NWi1%0AeaIZAr419wzfxglRzRNnYghkqYtckDo7pdIINaHSbkXKlfst79jPEiXeS8BRLXTXFhCEnB9oLD2U%0A7Sl9VyaXxXfW2S0gEyaB7No%3D|预订|58000D23310A|D2331|FZS|IOQ|FZS|PTS|12:25|13:13|00:48|Y|muFPgSOvB7%2Ft9otk4c2t7mhT6OFJLWSQSupx9LZRHeLed2D8|20180201|3|G2|01|03|1|0|||||||有||||有|8|||O0M0O0|OMO|0","nqLPP0%2F3qrbzB0WK87vpfGSbiiecH1o%2F2TdCjoKNTk2TWx6xd1Ru6WQeqz4wOKztox%2Bhk3OGJqB1%0AJEEpKfssGwbEDOW2RMUqDt9hugSQoWOt4o9%2F692%2BehYpupWoGyIlBTRH6cK9K6PZcrbzKAh6EKvE%0AbVITJmMvkzinBdMoWW3ImwI%2B9F%2FIJrAxJWGbcwEJ%2FSY9Tb9EQPHTPf3rI8rEVPbKuNknwhDZzQz7%0A1uLr%2FSQLDc69bsF7ejkqroatAXld|预订|56000D323162|D3231|HGH|XKS|FYS|PTS|12:36|13:06|00:30|Y|fWvuHExhhOYZuafQCMNKlGWngQBmliQ%2B3%2FRli%2FE2n1V9hVdV|20180201|3|H3|14|15|1|0|||||||1||||无|无|||O0O0M0|OOM|0","H6UduBss3TYRoqUWtCdJ87ryALR6T7677dhQ5%2BDVWum%2F%2F%2B8P%2Fi1dNj1EzldFMyazFVMncAoxJgru%0Ardp%2FljR%2B8w2sxklsmKmro7s4rYv0UaFYgrcir5E3wtBDZTS6lK2WhoFG2EqoFAfUyU6qeNIypzY4%0AW3ftMXbzA2yCt6P0W%2BTtDOtraRM16ZjmiOaxRnQobzF7z7MvSep9x9j6VXY4KT1peBWmIw6uJCUF%0APTl%2B%2FlZBcWlWEu11Yn8UDyM%3D|预订|58000D62250S|D6225|FZS|XMS|FZS|PTS|12:40|13:35|00:55|Y|QA6WhVKXOIIjxaMB%2FPebJiEx2uucHx%2BZQMfN5rKDf5pawt1x|20180201|3|G2|01|05|1|0|||||||有||||有|有|||O0M0O0|OMO|0","aUVOrmfoA1g6GK%2Bgom2HHOzXXA3MoG%2BxYy3%2Betw7P%2FR1PhrwoOynQje59B8u2ZCEYCWVw3WF8fiG%0AI3ArmBqdYMKoKQkmY6vW47kPhJ3QG3CBFQP0o%2Bd1JCo2y6LJLvGaUSONGvMRMJhA1%2BJGh2eodc1z%0A87SXZLevHMQAoaA7s6ZCD472pu0uzztTjKPGhsj%2Fhfwhi4Tm7A5Xtzepj54wcIz8P0K%2Bp6rLwJuH%0A18rjtrzPr1E4G0TYEQeN6U4%3D|预订|5l000G166700|G1667|NKH|XKS|FZS|PTS|12:46|13:29|00:43|Y|F%2BXQ62I7OUGIR8LpomXw8uQwejGrwaUvc31DOsChL%2FiImFPD|20180201|3|HY|14|15|1|0|||||||||||有|无|无||O0M090|OM9|0","dMw4D1tIvsPeGY2NcxAUdfysoY2gvMooILF2ZYFhNxYxERKOjy%2FRz88pLj8tD1vlYUN2w0TWT6B1%0AlLyrxxW8WKpCz2UXnS6PtO2vsbdzfw1mFyICFHEP%2FoOOOlGb3D6A8%2Buh4srmBQGo8tZHOT%2F%2Blrod%0Ah2dX3xYQklGtYefHRYS3RvpVqPBUk09X%2Br7tb81L4qcbZ7%2BMjbIhkCJU2XptpC7WOXz%2FfTd1m5wT%0ATEMvZ3gdQ9BscDIDFWvTUcE3UeFa|预订|56000D3111B0|D3111|HGH|IOQ|FYS|PTS|12:53|13:23|00:30|Y|95AzOuMAoOfjsHkWq%2B0cadmeajsD8HuqCLSf7WDzBNrVtT%2B1|20180201|3|H3|13|14|1|0|||||||无||||9|有|||O0M0O0|OMO|0","7he1WkNR69Vgrq4ouZ%2BDyWpgBpg7SRsVu9uzxnDxGY5Ik8qRAm26YL71JCBzjFiCIdjs%2F3dcnVOB%0A%2FIDTXFYk4VLxPBmpJ2TUYOzbFm9%2Bz%2BA5JgAEgaHHGWq2TnkBbLZZOqvjh361ZgMfm0MkJ6jd5a17%0AAbl4jpoMn6fH4DzITtt1822YjIjhUbobkFaGt6XUC2nM1XtdLHYO7tQOtv7g0zXD%2FopoRYgQyVp7%0AxobTJUk0qi%2FUuaTD3cx%2BuCg%3D|预订|5l000G165340|G1653|AOH|XKS|FZS|PTS|12:58|13:40|00:42|Y|LRORbRpnolijKfZiMYJI%2BUI1vFAsgU%2BTiTKUOaeDTD3eQu3V|20180201|3|H3|11|12|1|0|||||||||||有|无|无||O0M090|OM9|0","|预订|5l000D314540|D3145|AOH|GZG|FYS|PTS|13:16|13:46|00:30|N|c7t%2BygKokbsEPDLEAwUiSOnPo7NHodIw12HLIm3NNWYREEA%2B|20180201|3|H2|17|18|1|0|||||||无||||无|无|||O0M0O0|OMO|0","|预订|5l000G166900|G1669|UUH|XKS|FZS|PTS|13:17|14:00|00:43|N|0g9SHLdcnFi4DdvKIbehkg%2Fj10F7GVNOUcOR7YJRkUSpm81m|20180201|3|H1|17|18|1|0|||||||||||无|无|无||O0M090|OM9|0","%2B1EIIrHCPKRJ8UIrqKe63uqxbbpO1uppFw1ByJLpSgt5FAT8FXc1UsRQhW%2BR7KzoKOkMocD61bK%2F%0As%2FRmsI%2FrTAE7CZAUUvB1N%2FTlJV4ULo2hbr40WduA4gDwr677n18vmJPQhfC5SfNotBB2qOakF19A%0AoibgarTUYUDwLY05ernxXuaTffL8v8SHQ3RAqP1jtvSApuDSlTyUsZnzBo71i9%2Fdgq32Ss1LnbMs%0AOfpg7Pj6a9VyZVuS6vMs9z0%3D|预订|6c000G169205|G1693|CWQ|XKS|FZS|PTS|13:23|14:06|00:43|Y|LUH%2Fzt%2BbyC%2BnNNFUpa0H6OireG460VPOvHJSbFFkTYJQihdv|20180201|3|Q6|13|14|1|0||||||4|||||6|无|||O0P0M0|OPM|0","tjqtThAy%2FWVp3OgYVnH9GwIbHo9Ztf3nCOsXwX3ULQ%2BPYA%2F%2FOKDg5B70SUo%2BOj2VEc7t5a%2B4phND%0A%2BulfNtmspw%2BQueG7901kuzaKij11PuR836sj%2Ft3DGG7Y%2BtwngstmNjxI5d2UhAD2I4YlSsE7wDn6%0Aq7Jjg4ipFgQOL1oygPEgpzALeuOH9ztOp%2F2d%2Fh7%2B6E9mrcyU8FzBvJ4caQWbpe%2B3URoKJ7nFv3s3%0ArC1S1kqSjYO7DXchwBTigs8%3D|预订|5l0000D37962|D379|AOH|XKS|FYS|PTS|13:24|13:54|00:30|Y|55Tq8FtwzfcKrcXj7Rj6panGqg%2FPzN2Q%2FZ8yFDpjKy0Vcjov|20180201|3|H2|16|17|1|0|||||||无||||7|无|||O0M0O0|OMO|0","|预订|5l000G166130|G1661|NKH|LYS|FZS|PTS|13:40|14:31|00:51|N|0g9SHLdcnFi4DdvKIbehkg%2Fj10F7GVNOUcOR7YJRkUSpm81m|20180201|3|H3|14|16|1|0|||||||||||无|无|无||O0M090|OM9|0","3o%2F0Dko9LvfsJuENtmecDStG%2FPJ1w3vuahw48Q8dA2TR7PUzu%2Bn8JlUgjUrbC8gekr%2FhhxdUn8fl%0AgzjJEp4PDvZMa8XyZiWokzASYswRGNlI%2FqKolL%2Bt5wPU8qWXkgzSA%2BXTiqgh7kIuQxNs1iAfWq2J%0AvOrKdQm36B%2B7m1hvyWXj2zwl1ZyAORPeYrQPP%2BF4euswqdhTittzhPyzThoKneWa0y%2BuZQ7pKE4X%0AcaiBiB4yHAVAevm%2F6Zr4%2Fnaad5lp|预订|5n000D63810B|D6381|FES|LYS|FYS|PTS|13:42|14:12|00:30|Y|2nLiN1lnW5qyDCFZA1gQVBscrMhdP7vULkxwcCup5j8mMtR9|20180201|3|G2|06|08|1|0|||||||有||||有|有|||O0M0O0|OMO|0","in2YVkPsCUVAxrS6oGXuydupH69ukl2UiZ6VAyJ4D9xblVFsLSAigZ%2B872GSZh1eT4E0sMi0bZsE%0AooUwOnWAhOkj0BXQT9byuvKprEmyq9XUGwQnzfIuvIL1HoTPandiD4HCK%2BqCffBF6IJrInrdVjs%2F%0AKMpN279MmQIPIQdAk1%2Fe9B%2Fjg%2F1yzXIDNYnBUbdNh4Smq9JAPKqg5XNGCKV3EusS2uEz2gmZUo1s%0ACpMqLHy44eDgrR%2F0ISxyocVxJquV|预订|5l000D313150|D3131|AOH|LYS|FYS|PTS|13:55|14:25|00:30|Y|5gN%2Fuqynn1P4Tef3GV7Kc7HohDprhHNEYDzlQobeDCePKy%2B7|20180201|3|H2|16|17|1|0|||||||1||||1|9|||O0M0O0|OMO|0","%2BhaYbgYLBcxR27SxJk6mncOmLLS%2Bu%2F0%2BnuuTj8wWw9ECVIKvRBfOGbTljMJDuNMxGI5DoSV%2BZ4pP%0A1lhWwz2BrzT9FRU9HEFKP4V%2BXDIStEfNjsO%2FW%2FvvIMWPGGXFehcDZFVo0cl2RjTjXLwRBH%2FHhBm0%0Av%2Bihbs5%2FE8iI62UkYPxmhmlQLe3g5P9pgHlxS3jptMNiObRp6RFTbzpDV3yh8ptzThc%2F3Db3mO4r%0ATMsY5ckJELfKH214bQmVa1U%3D|预订|5l000G165521|G1655|AOH|XKS|FZS|PTS|14:07|14:49|00:42|Y|vSxbG%2F7B7eVT3RZQkdLnG2DvYwlfVgEjdCCf%2BkB0w5uupHoZ|20180201|3|H3|11|12|1|0|||||||||||有|1|无||O0M090|OM9|0","rDFHxzWr2EUQNIWcrqy2D8bIdtxX1wYouLH7N2Td8DbpKs5oueM1PGYY98NZH0B%2BOB%2FBkiMhvLWF%0A3cs3s7B3bPdqmkIcO6Q9iv0bkem99uUESrLq7IEQ5Hd8Y%2Fc5%2FmLCGh4Jgzir1o1Fo%2FkCoutZt%2Bid%0A%2FaO6%2FE8C7P5LXVyZBXFEHuTCkFHzGDlXvP7I55c3WRyO9uTZNYRgiR25LHTbkSnAzs4vmqWhq9rr%0AbVeHQtmpvdOb%2Fv9d5b2WKhA4FhAm|预订|5n000D63310J|D6331|FES|XMS|FYS|PTS|14:08|14:38|00:30|Y|YvWqKBDtqpa%2FT%2BVmTT%2FnMilKOVUKDgosigxjOFO7v4Y2%2Fkss|20180201|3|G2|04|06|1|0|||||||有||||4|13|||O0M0O0|OMO|0","tJV1fsvgMytJ08FGx%2BkQcOqcW47qbwsNIPjEIk85MwFFq8cANU8QlMEJKKaMfoo4FSacFuMLyklD%0AbP5RbbjaP87YNDv8CbnJtpbvf4YnTFlCulIGv%2BMqEy5LIGdNZBhQ7AnETlJBs8qhQ1h9MADTaUdY%0AaHw%2BhooyPypniSXziIUGbnpWfRaprmSWz04V0MyC2ZnH3%2BKsqSuPxAkJnZX0h3aNkVV%2B%2FDf1sPQy%0A7qH%2BrM36yeyfW%2BPXQ6Wy5rI%3D|预订|5i000G160122|G1601|ENH|IOQ|FZS|PTS|14:13|14:55|00:42|Y|AbLUlSk%2B5kycKg%2FMxQfsXqjz7xkFOUQp5jBzO0%2BnrN1bK0fg|20180201|3|H3|15|16|1|0|||||||||||1|无|无||O0M090|OM9|0","vq4FUhdpbwrGmODf1cziTxwjkD7eoC7%2FQu9VuJwqlM0nTls0mHERPzASFnyC88stB%2BKEziKG%2FxdM%0Aolgzkih0PiSHkRH3Rxsegqv4pdTE38F%2B09KUm9q9SBoyzI4MH72kC8wRs2PfFjEs6cpVEidFrH9D%0ATkCkaF8V0vgl2AHB%2F735mYjfElavCU9ekG4o6IXwe4MfT14i8rZyp1dJ9UcPDqYXqxEKaFqhTIwM%0AVCqoPeXrI%2F8ub%2BvBnw%2BVEuK4tlsE|预订|5l000D228732|D2287|AOH|IOQ|FYS|PTS|14:14|14:44|00:30|Y|4OapOiUYYtZOOF7rLgoJ7w4B3pngQ97o3w3bRZftTI7mZL60|20180201|3|H2|15|16|1|0|||||||无||||5|3|||O0M0O0|OMO|0","5j7xxazCX%2Bt7ton0wN5ph81g3LBYf%2FTsGwQD3hxAyyR7NwQPFM1qm6oOUqtCUhbpjOqbR%2F2cks0Y%0AvoaBv0eYYGku92nxScMSFl7qsvoFm0r2Qg3asvnUGtuJCOrrSkhr%2BNCpa9943F2KR9ifTtEMQ7sW%0AEL03a1gaHqrdwSib3ED%2FelvQGABUTmkSeBpSCy%2Ba%2F%2BfCvVlrZWItawDbIQk4MW2vO8EyJXxsvs2O%0AyiMQTjQs6ujlBG3fVBfnb%2Bk%3D|预订|58000D62270Q|D6227|FZS|XMS|FZS|PTS|14:19|15:01|00:42|Y|ivZG0K8WFTMbCWdd92clE%2F3xVnv6S%2F6zqquUOeVUN9mVNEyP|20180201|3|G1|01|03|1|0|||||||有||||有|有|||O0M0O0|OMO|0","BC9xtNKWtE9Rfmwf1JH0rwRyUkZLHGKiMBsVs57mHeW0%2FtEA9dC4ljRMiM5mg%2BFZMWXPDwecaL54%0AJUpQGiTp5WWQn1H2AwGUULtJwS2XUW6bIUL%2BlJWnTJZpQKsqrgpKp3Be2QnW6ngISW3vYjzZStJ%2B%0APCxdk8%2BHrbDjCWsCdTq0wvOiE4GSqBAc2rGhdZob4P%2B3qe3ofGg87sy6ZYwLo%2FwknSM6vvvaf9%2Fw%0Astd5t%2Fn00tj31LO%2FDH8aZEw%3D|预订|58000D657504|D6575|FZS|GZG|FZS|HJS|14:25|15:01|00:36|Y|yQWN8fDSBF4bqKcwWZz5eKYQVTiu6kR2QuWZa1tEYpH5TMsv|20180201|3|G2|01|03|1|0|||||||有||||无|无|||O0M0O0|OMO|0","gljY9opzEWJhfaoOFvn4Y4Tj3klGd09ad3YucFe2j3LF5i00%2FL8B1HlFYSTmWRR2B1jfvY7vnKSa%0ARi2nF%2F9UrL%2BiX8t6hynoQS966SfUSvjIWdx3iKetqa%2BfKujMBh5AJ3x0zeT9jHBy%2FyWQ2lj%2BgoE4%0A%2Bu1vt2SUmxDR3IxEgF7FWBMYuNVMc6m6DPelv9A2jYo2K%2FDxE9qcNlaN9lV%2BD9A0fkUQ1R66UXql%0AdJSS2dX5V16AL0i7qPnlttvRAQ4n|预订|5l000D320192|D3201|AOH|XKS|FYS|PTS|14:50|15:20|00:30|Y|WezRX%2Bm8iDPxWc0M6gTScWdmxy%2Bpw2kL8zZQJ42J0nmrDoz2|20180201|3|H3|17|18|1|0|||||||7||||9|无|||O0M0O0|OMO|0","x6YLGSIjvIFWU99jVKgPP1zc%2FpsiZcaYFiIGgl9u4CeMYmkebWVCrn11YB9tA3ssrHoc7sRdfUt2%0A3ZPd8WNcJJz0dt7xv4%2B7RKI5UFhxKUJAKLNEtRBaXLVQb5t%2BA4hNWlaJ5RuoFm%2BNk8F8Tlk5Z%2Fw7%0AKZ%2BF086mnTbrbOqhnjPNY55ewL0RDwocMFXEHfMW5tpKJHXdOALJ%2FFJXhPIdadn%2BdbNq624Uo61Y%0A3lFCfqWRWyc6QcfETRNVrDI%3D|预订|58000D62310R|D6231|FZS|XMS|FZS|PTS|14:52|15:40|00:48|Y|GGuM6CmRJk4giNRwfUVnuzMr%2Fb2n%2B3TwNIRe7hlnMglB7jM5|20180201|3|G2|01|04|1|0|||||||有||||7|有|||O0M0O0|OMO|0","UrDI8%2BQ4zW2Xmlg1Haa5YqEv9Uew2DkAmh6BbrdkktcDVI1h250B5ie2ErIllyAMkQX7Jd4vBRjz%0AGrAbW%2Fp2VK8%2F%2F37NLX%2BMBotu5CH4aigaJ8Qs0v6fIBX21nbfyON8PRhOr93vlh4GQn52eSMPjFrj%0AoEQ3dIB4H4%2FWnf%2FSwKOykTaRI9VWvrM2GvAJ1XFKRWfIImSafwCo%2B059si3EEnlBFLjzTz5%2BZDlf%0AxHLkQ%2FSXN%2BUGVh6i1SARh4jgeX3K|预订|5n000D23070D|D2307|FYS|IOQ|FYS|PTS|14:56|15:26|00:30|Y|20YxFB%2BWjcuOmboJFnWBIk4YRSwy3U0zfg8lX96hiSb69MtK|20180201|3|G1|01|02|1|0|||||||有||||有|有|||O0M0O0|OMO|0","|预订|5l000G165721|G1657|AOH|XKS|FZS|PTS|15:02|15:51|00:49|N|0g9SHLdcnFi4DdvKIbehkg%2Fj10F7GVNOUcOR7YJRkUSpm81m|20180201|3|H3|12|14|1|0|||||||||||无|无|无||O0M090|OM9|0","tpn7kLyQa%2B1NSZoiCDbYVAmBKZ32gsiCDi6P63%2FtU0tkzGGBT19ZaO8OLKK25DdB%2FhhytMmt5W7G%0A2J3B25L4FFdIh9%2FUbsjjzEbPN7OAQ0GfL5lY3rpLnuUEXjv8TPta1y6H1gyQVF%2B89uLiy8Na6fod%0A8Ydm1361LMarXyXU6ELJYcl7887gVweCOuKmQ%2B%2FJhc1vPwkvCGEotSW9G4iSModfhRgc8HBEMYgE%0ARMbZzr3VRILT4Con2v53ur0ARvuy|预订|5l000D329540|D3295|NKH|LYS|FYS|HJS|15:02|15:26|00:24|Y|5EGLaSmXMCGF5MXGscUzdYwoBd0IhSei6%2BTnaNDRKqXnaVOl|20180201|3|HY|20|21|1|0|||||||无||||3|1|||O0M0O0|OMO|0","%2BOLBuREFcz1zuAd9ygEfK%2FuSxVntocPmuLD7Yr4lG2t%2BRdE65PUEhrRCi7wdw6aXuGAsydRIDvqr%0AbUuilH281vFspYvG%2FF92XUdUx7IVoAjlKUL%2FW1CEfhyDTN5wbK4%2B2s%2BRBgmpnsY6UhAkTYGwFq8d%0AjPPp51%2Fxpqkng9tkCuJYPL1%2FSFs5e%2FTUSCu8DV40ARdJlD%2FsmgDpHHIYYTVY7DsrEEChkeZ0VcxN%0AzTczjZLLd0i%2FRYOA4pAL1Ls%3D|预订|58000D62330Q|D6233|FZS|XMS|FZS|PTS|15:28|16:10|00:42|Y|x8Ivv3z0YXqUkXYIV8gu8GyBTPzKo%2BIuooY7N7H3PJdTa1VK|20180201|3|G2|01|05|1|0|||||||有||||有|20|||O0M0O0|OMO|0","nzpGaGQH8zMjam4w1m0zQ%2BPbjpoTZcXG%2BG0QQf4CKZSFfrKKAWW4csX6%2FNMuiRdrRbxjdmqma4d2%0A4hCTUvV6uDazofQRFyiXaiIMZEwD23N7s1xdzX%2FnqUmnOao%2BxiWYjk4rnUl6j868Hvql529N121x%0AL735RGqwKYhO8gVxmGA%2B3GXTGF94qv3WPwzDsGYsR%2BFD4VAqCgV8lR7OxKBn%2BU5v0ikkjfFYNjWY%0AQw7M2DwwWQAZBp6Nqn4xP8u%2BFaTZ|预订|54000D312520|D3125|NJH|IOQ|FYS|PTS|15:29|15:59|00:30|Y|6U2iJtYdHS0QISiHMN4X7nClpuUxE%2BTNsoNwyxwcL0%2F8oodV|20180201|3|HZ|22|23|1|0|||||||无||||6|7|||O0M0O0|OMO|0","blAE6yIPPyXZ9D3U2DuyhC%2F1kQ2ckYpvfQlKLfwxNYi%2FfLiq5ODDe%2BadLOVU9dAfA1OSTjefU%2FQx%0AdOvpWgM75qfaycY0T2HCK5dCa9dlgbRyqL4eQDADgaWvKwBiqyFoJFmAomNadUnv3DmQ%2FF7JyoRz%0AsYF4ru1q%2BBENz3l1gonXKAFts2GxsnhxFSSHk0hwGeup2loYQ%2BC60%2FJHc9COE0UtXXhue77KPN1Q%0AiMFussoxNCPQ%2FxSrBM0M7zKq%2FyAD|预订|5l000D228521|D2285|AOH|IOQ|FYS|PTS|15:35|16:05|00:30|Y|gwPYnC5Wq%2BVYFZ1b01nL8FPlxL2Hy3aWzyC%2FiIP85Y6TLykO|20180201|3|H2|17|18|1|0|||||||1||||无|无|||O0M0O0|OMO|0","aM1AHMceAYWW0RojK8ZhzHlhissTn6s9vHKZB9WIpemQS1YXrYKPO7S9iycmST7MLFXbjE7fDMey%0AbM0Q7upCxKVk75F6mDnpi0CDCX%2B5PpxIDYx9L2kvt3Rb%2B4%2BaTtyC1jlHYlHJMkHlIMVVrYAaW3NF%0AUO2cRjhWc9QO3aIO%2F%2FOlDHQuXBWPk57uv1j8vs5oZYTtizxglpQ3W6aCGr8ovvcHQlIrux4ASDII%0Ao5erZ55Vr5hubucRpxDQoE%2FqSmTt|预订|5n000D23090D|D2309|FYS|IOQ|FYS|PTS|15:48|16:18|00:30|Y|%2BrC63qJOCtO4I01ugSkhI16WHExaKRDE3eBAutwf7zCS4kJg|20180201|3|G2|01|02|1|0|||||||有||||有|有|||O0M0O0|OMO|0","p5E1p7WFc4qdjeSWj%2FwE27T20rCPN7v4EkETLsixSuHT9ugWmuePK4YTXNZf%2BjThoSMFetZ4AKR7%0ANO3XxYk%2FsZAvczFcZ%2BTG6UbtpDnrkHrMp3pYTqjljIOotnjxZmWiQu4JF7qvvPctkSBag8JFE8z9%0AP9BYWbJ21RwfX9ooEZHz%2FYH7%2Btb6v6FHuFkpeXK02XcMMbFP8M%2B6PZAJW2mTJFHKxTt3o2G9hAp%2B%0A2HyBpDP65TKs6FfFQZz6WeU%3D|预订|5y000D624100|D6241|WCS|XMS|FZS|HJS|16:10|16:58|00:48|Y|DQ9yxM5kaI6pxf0S8YR%2FTCrWgXnyelAtaSuEVJjWQymc%2Fgz0|20180201|3|G2|03|06|1|0|||||||有||||3|无|||O0M0O0|OMO|0","|预订|5l000D3107C0|D3107|AOH|IOQ|FYS|HJS|16:22|16:46|00:24|N|H1P3jd1fNkG%2FerAhpspadQrSjA8r4Q8O5mFBUY1SAm51dGIY|20180201|3|H6|16|17|1|0|||||||无||||无|无|||O0M0O0|OMO|0","1iQ9qJK%2BB6JqWQlK0dPaD1oyUGpN3chth1mMKlI%2FhH7a15lR%2F4ZzjZbAXQX7oVJMG%2BOBSb4iKR%2Bv%0AzAN%2F2P4E2AK%2BJVT6NdAZ4a%2B0NoksliksJ99nME5FCaLZgOkBqtr6xBDtZQnuzSGogY7QsdCZkQD%2F%0Ax3HtUxc3urPdLHcgwgEe%2Fe7d6sgqBTozC4XBCBvqn3eQmNN3LQ3NA4rhdLHNfwwbR77PHvTPYYsr%0Ay3G8%2BUKLKsttcwRyw5%2FIPxY%3D|预订|58000D64150G|D6415|FZS|LYS|FZS|HJS|16:30|17:15|00:45|Y|ZiS0rpSj%2FgGxvnHg3ve9cRnCYdr%2FcI3PlFUmGnhSYlTefpO8|20180201|3|G2|01|04|1|0|||||||有||||1|1|||O0M0O0|OMO|0","03eiGKzNccKeXqHiX5Mg837mmdrn8HRKzYbEo6pFqKsGqWDXCvnM8AISkN411yJ2XmOX6yvZKUoP%0AkgAnnMDNhbPkmvYs5TzNonfbufe8fQ%2BDffa7aDeFQlkZvQ%2BP4Evcqb1py6Wk0Tb8VoxOoTy4ZIuj%0ANvprfk8cZmwxAW5z%2FCmY0GAxjiLOJ3SyHBztp99hO%2BzZZuA%2FU0E8Ujbzk1avo5ciPEmxDHt9%2FzEh%0AwVnHI7yGDjDOw65V8uJaF4U%3D|预订|38000G204501|G2045|ZAF|XKS|FZS|PTS|16:36|17:45|01:09|Y|Rgg6YHpsowuDV4zWECIbl%2BRccTcVDQZEvtIorZ4LXqZsYgAj|20180201|3|F1|21|24|1|0|||||||||||有|无|无||O0M090|OM9|0","|预订|54000D228140|D2281|NJH|IOQ|FYS|XWS|16:40|17:23|00:43|N|mTm9CNIfvRqzMjEKH1E99PrDnGUKNkQvK2Sg5PdULKRj%2FHWD|20180201|3|H1|23|25|1|0|||||||无||||无|无|||O0M0O0|OMO|0","x2vocdzOTVGHoKsgSoxyDXCUOSuOoKvSGMBTCBQmi4QURwbYzB9xN%2Fs8F%2BL5%2B0aydtIyZLJb7EHf%0A%2BpFRJhybeKpuaywohIeR9Ev%2FPS2I9XIRBOdr%2FBm4pzdGn5akIhMJlpbLd%2FZ2nZL3o14swtbDAQ7l%0Azv4HCxNm91ITyvdZCYCMdFQVmVNXTvAjlMn2rB6CxGf8YMDDZeCiwGwKXpyDG2ZB5eRBZljjCM7E%0ACECfqHtVZcNksB47Anoyozw%3D|预订|5u000G52080F|G5205|NXG|XMS|FZS|PTS|16:42|17:33|00:51|Y|GTNBCFLW%2FKGp0YgsDVRbn24%2Bhun89%2BuktrKfCpKvlY9qAU3%2F|20180201|3|G1|12|15|1|0|||||||||||有|4|无||O0M090|OM9|1","r0DlOA0uTiv1%2Bvq7l0scNeL1q1CB8s01QQHpGX5MahEzFNTup7eMezOAllCHilbp3beGVwTY3Tt6%0AZUolc8qgFaS00nm%2FVDoeGMlwGvko%2FapAs57f89kDYZ8RXq4fPGYP8xQ9FWMIOkwi%2B1JlfRDb1ttE%0Am%2Bh42OvKmdtjJ4UTNrBh0H0AWGHB%2BknnwbqrUEL7B5sosCy1OYXqG2vrvsiUA4DGhLFoKKtOtdN%2B%0ArYkygPlTehEvPUuqMbPyW%2BM%3D|预订|5y000D235305|D2353|WCS|IOQ|FZS|PTS|16:50|17:39|00:49|Y|tCwj3%2BP0ismmc%2Flv3uFfCrYSdgrqMGJ55Rb%2B00r8u8n%2BrLyf|20180201|3|G2|03|05|1|0|||||||有||||4|2|||O0O0M0|OOM|0","xV2LdFYV%2BIkvEVOTNnV9rGS8I2WozTC8IkmvVvkGJ6Ode3%2F%2FVIkA0ox3euAqbBA1QOxLZ1KoEljE%0A43wOH9di5FrA1hOG3vOq%2F56ikE1MaSY0DhOKm%2BtT4ehkcpvxbkjg3IFUHV5XuzRMYfFpjV6PzaAi%0AxZhLEx3VZRIgIy4svsF%2F3kOEJ69ptSBchVUv15DvTmOI%2FyZdR4pmNoU17zH5zlwY8UVR0P8fk3Ce%0A%2BsW9QRSht5S%2F96qHH3PSYK9JD58X|预订|5n000D63330M|D6333|FES|XMS|FYS|PTS|17:20|17:50|00:30|Y|oRA13wsXkAbWUOK0rLoU%2F8EjsVq02IK5fnE%2BKZAJjU5gA2ia|20180201|3|G2|06|08|1|0|||||||有||||有|有|||O0M0O0|OMO|0","uvEoXnWau1PPUj4%2Fh4JURY0u4DRx0z0LZSxJkTvLZqxNbzYCSj4njHJ5NHBfUPhR0DtbkSmRBVTW%0ABQyfsSZ83riuDP4qKWkBeszxcBWx1Xc%2BqvjA%2F%2Fe0U2lCgjr4nHOJYUQbAM6ZcHkbuCIsp8P%2Fuey0%0AAd9Xq4519EDk1dBLED7VfpfDplmthbz0kpE1RGhYoGjdilL%2BC0oHm83QTEqKRy7BTVPl0U5rGXOX%0AcHJ4cQNNrTO4Uh2w7nZY8Yv7z2BO|预订|54000D313582|D3135|NJH|GZG|FYS|PTS|17:29|17:59|00:30|Y|DyVd7EcATLKBHP%2BTvKay2FvSLEW3IoHoF4qbrOVec7AJGOR6|20180201|3|H2|26|27|1|0|||||||无||||14|有|||O0M0O0|OMO|0","BLJaweAy8H6%2BWErwsFVErxr%2FJ7Bz1Ut%2FG1KZ0lAQeSu3QMEJQRA4sgGi%2Fp1N0aC%2BymIDPLh%2B1d7B%0AN%2FHew3Us%2FGvht%2FQoa1Sdk%2Bxwfjcg2u7gAeOB0pPTG1FrvQs0j1gBbdExrH%2BSkNUJ%2FfrFIRlMWYow%0AygSmD9wc%2FjRUpVkitY12ErxrOFZVk0w0UEWhGdRmutjK4QvAT%2Fc3C%2BtuMFTOIEISWCnbRD8Jurdx%0AeI2o8AuUhnj1fsoKnJBHE6xRG4O2|预订|56000D316510|D3165|HGH|LYS|FYS|PTS|17:34|18:04|00:30|Y|sIh3GhN16Ra%2FESooy02iikiId3kCmE4%2FL3zwHiF03Zh7WIob|20180201|3|H1|12|13|1|0|||||||5||||1|无|||O0M0O0|OMO|0","LCh4aaOJJMJrxhptkw1AWp4t%2BqUi%2BtDij7oxXF5aOAMrpuRipFzflzN0JyPvPLZRF165n3sonzpB%0A%2Bw3GzYqkaAYwBKThddM42bAG40hM3qgiJXPK2xW60mjj2Gt70tVCv5uPix6bug6r3QWjiN1V%2F1ZI%0AH%2BP%2F6AlKGj%2BYiDGJOMQEZ7b5f3mQ8m0gI%2B2%2BkHoF6JInQV82lXDHpRGuXBP7cUwM%2FeqsH5zWJ2%2BR%0AmB1K9HGae1PphnzEiZT8Ces%3D|预订|5l000G165921|G1659|AOH|XKS|FZS|PTS|17:43|18:34|00:51|Y|uRUAB6st06VW1odtgECQQwnYKepqslmjayP7DNuyr1P8sr0X|20180201|3|H3|11|13|1|0|||||||||||有|15|3||O0M090|OM9|0","|暂售至<br/>01月31日|56000G167921|G1679|HGH|XMS|FZS|PTS|17:50|18:39|00:49|IS_TIME_NOT_BUY|ZGkMju%2FoZu23IItNSsUYWECNf8Ys1I7BYKTI6LH3XAB7JahH|20180201|3|H6|07|09|1|0||||||*|||||*|*|||O0M0P0|OMP|0","tAJ6HhPMstk6wWM0riWp13%2FU0HS0uCoN6ohv%2FGDfvkDFL%2F5h4qIqQ6sHB7%2BW4%2Ftv5mdg0Eg%2FEkJI%0A3ougx8%2BXu32aS7Ft1P4OyDbPH7s10HruW1XMp9E76litF1ik%2BVne%2FoPQkydxw8wDGx35Tfg%2FMi21%0ANxxNHMfLINmha7nVTdSgKhqsHssz2DolxDZLgPafrus8O%2B%2FWPqUV1pHW4qkIZhKZmICcJkLeYl2F%0Ah%2BGURJa%2FXwWhpTalTWwrU30%3D|预订|240000G3550A|G355|VNP|XKS|FZS|PTS|18:16|19:04|00:48|Y|%2FF%2F7mvL2T5aH8MSxRJ0hLfzDSjT0ru9QCMNRoN6AYe3Mf%2FbF|20180201|3|P4|20|22|1|0|||||||||||有|3|无||O0M090|OM9|0","SpOFNlA5L5RkEoOL8MEkDxaUUdJHxOIrNTrfhBCqOJ4rWqbBBXo%2B1nlwBDIhtGp8WM2IIqSLofGo%0ARcOnIdF4CSGzcEC%2FPPfVzYd7nTw28AOZyI%2Bs4uYfRCo73YuWTcJqJ%2Buk7%2BNVzxzEH2Lu9nIHLkr7%0AqM%2FjXk4v8VeuVylbcAjow9NftJgHXfXpvhMUWgeClAbh4P%2FZqhWkiYmwTpCilOgV2QE4z6QVbUSf%0AiAySfYRFEc%2FDQp0uTxcVWhE%3D|预订|5n0000D6710F|D671|FYS|IOQ|FYS|PTS|18:16|18:46|00:30|Y|zpjnM8WFZbOQu7FmmYFsF6nxIPpv6aTDOi2JVgBkv%2BSVYco8|20180201|3|G1|01|03|1|0|||||||有||||有|有|||O0M0O0|OMO|0","mLT%2F8p%2F4NAPOmN9L9fOZeiJIz569OhNQAN4%2FYTSjnZ6vArzf80jhdznRqCa1ge8Fll9%2FqeXMoBSS%0AQwvY0OUncHTg1r%2FKiGaUt6GMphszcVTtjOrNTO2sQyC2IqZA5mAw3uG6QKU406zJxpmlOJ%2BQo4TJ%0AZN%2BxGruSZ7nMhAFhzKrSOnRUn0HY5qdVzf%2FM5QxzyCGARa3eiuge0l%2FhXQhchmvTehUmZ4xmQWEQ%0AXYE7mBBPiiKwZOaZl6vg4LrMz1eo|预订|5e000D321522|D3215|NGH|XKS|FYS|HJS|18:22|18:46|00:24|Y|2WquynXs9%2BiZsGQ6Ch5M52Z6xGLNeAvdk6pX87waGJ%2F880q7|20180201|3|H6|10|11|1|0|||||||无||||无|2|||O0M0O0|OMO|0","NLhRpvLAT85qyINvGUnqd6H1OkmPUSt1rj%2F7vG6dRzaCIxWYYfTCXdlVE0y596EUMajgTAeexgG8%0AFVDpRC753O6e7iWKYpomUxpez6Juwb5rFvib7qvnVEhGBwAd875eU6IzAe2GIn%2BZVogHmnbvk2ol%0AQCIw%2FDMPzJHATLcJxNRt37FoJ8%2BaPpBgniEL8jOlX3x3FBbTQpnZP4ZLxy6j9EjAaH%2BQw2JVfLAB%0A%2BfNMLLnKJNa1Z5d5nxHn3xQ%3D|预订|58000D64170A|D6417|FZS|RJG|FZS|HJS|18:29|19:14|00:45|Y|nwQCv%2BxlSBEyCCzcEod44bmXub2bvAL4qEWiKa9ACdEB%2FvWX|20180201|3|G1|01|03|1|0|||||||有||||无|1|||O0M0O0|OMO|0","Gqq1JpO1EhgJQzCiHe5Flut1%2F1y8o5SQWwSJRdPSG6Icxa5Xjz%2Bko1AX2dDQYxvfQX7kobJRqaMg%0AZEby%2Fc8ihxh6a4ubjMIjxshLyGYXZW3asfGB3%2FL3iso9X6w8Qw%2Bv1eeUOt5ZJbVt7WNpZrNQYj3p%0A6UXiFtGDSrUDuQKhnsBW9P96Q0VGTalOHWcuKKsNcUClmuvCSTObyyEh5iO8CxWBw25f72wLc5au%0AbsAKZWh3%2FKNkJh9pUEY5LtkHJNyK|预订|5l000D3207A3|D3207|AOH|XKS|FYS|PTS|18:39|19:09|00:30|Y|z8BEGDpJw554fbZk2ifzvVVL5FA0Ja4lmpluo71T8AY7%2B%2BzF|20180201|3|H2|17|18|1|0|||||||1||||有|19|||O0M0O0|OMO|0","sFeo68uT2izoTxOaq94VEbMKDzrMxzCk3YBHooEquvqjrzSSFgLecrJEyvVhET8l0hrdvGgqKVaf%0A55Mi%2FwkKq8i8Hys%2BNw8e4S75iXFPZGT0SzHsqp8R8IN2gKVSVkyQiL9bxaAhWaMU%2Fj1HJZeC7Rt0%0A3Knl5zXA%2BGPtZfkp7RfdaAJyhiWq55k33%2F56gKe6ic66DQdhEuk3Fb6INNgObeNhjpz3M2lF4Ohz%0AlcgaLsTi7hxKZX%2BrEJR%2BVJw%3D|预订|78000G168603|G1687|KQW|XKS|FZS|PTS|18:42|19:26|00:44|Y|ZX96XEPINHjZc0xzJQGPpGcl0F3%2BaRmqFvWvk5veEJubFANh|20180201|3|W2|22|24|1|0|||||||||||有|3|无||O0M090|OM9|0","59KX3MD2bOAM9JKgxtqPfSr6FbsmmH43hi8d7jigM57wojcrgF2sxUtupsX44Wx%2BH0h5nyow0dOJ%0A%2BVnIf5f2QiXH3yw6QLhI2ewQwNi%2BYKrl79Ei5MsCGpypColW%2B8%2FR4LnUQwOceL5%2BkkiJORcasBO%2F%0AX1cPxknjRc85wAWqfFwXhqZpg61aDnIz70CkM%2FzqIdVi1MshGfnRf6JKcLZ7yjtA2bOhvCRHQzng%0ALJoUO3v54AuSFtkx2eSYOFP2XBUd|预订|5l000D329130|D3291|AOH|LYS|FYS|PTS|18:45|19:17|00:32|Y|gwPYnC5Wq%2BVYFZ1b01nL8FPlxL2Hy3aWzyC%2FiIP85Y6TLykO|20180201|3|H6|17|18|1|0|||||||1||||无|无|||O0M0O0|OMO|0","ROFj5ORtjpPAvrvsA8hWqacgrNn2P7vsom2fCgB6jKditZq0vi8WCBI11entB1bKPMVi4l1Imnw6%0AArU%2Fv7lEbzeJJzn3fbVTHaVvTl87IWfquJCKYXPpbTuXDmswdUGxDjddw253Mq8T0pDqRw%2BJtutq%0A0q6Dn9V%2FV4yFZrdGXSWEkQVKGIIyTBtnF01ACwdIO70TAuLvdTLHboGhRVl%2FyfBCeyZy4UvWOMbh%0AgktiZKkD2pqd4m7lhcE7%2BxpaHzWpkh430w%3D%3D|预订|490000G2440E|G241|QDK|XKS|FZS|PTS|18:59|19:45|00:46|Y|3KL9BD3DimXFyjw3EGW0VqMv0ojtka0tVmFFT8GBNdvmZRZ8ZerfXJZ92cc%3D|20180201|3|K1|25|26|1|0||||||1|||||有|有|无||O090M0P0|O9MP|0","YupAr7tf4YEcIcayhwuUwC%2FaWjidbVKyPJiAnb7gNmt9cChxqey6PKjYtSydykJ%2FF5R2W24TRd%2Fq%0Aw6LkFurxwU2aDEx4TSq1%2B6t6Ky1N2pHFspMoRiTQzQsBc9XfesIprjueG3eXNZRO5jHxgsS95z2W%0AFFihcDRuoCYEcHTJjs3abUfO37JOsDbaFXpWFB51tAKqB9%2Bs9htnQs0ubHJdnm%2FCle%2BkevsKtZCo%0AfSFWhtKK78ZGagVsZg5qAcM%3D|预订|5l000G167530|G1675|NKH|XKS|FZS|PTS|19:05|19:53|00:48|Y|%2F1aucznvwLW6T8%2B96RLbTVDXknnjUS77zx8W2Zxg1i9q8ZnD|20180201|3|H6|14|16|1|0|||||||||||无|1|无||O0M090|OM9|0","yhdIHnJ6U111EYkcQ9tJEZEF77kNziipc4SOsFcHypm1UShloWLdaBqzdy4259epPtpHy5Zrimcm%0ATRW4KdRBXnc46IC8%2FjLxTYlUhbSoE72YBK50%2FtxWKD28hVR8Ov9GQIYDIIaCq9tUomJcU%2FcsryDu%0AWszA8szwHCXN1X17dhBDd6yAdm3yyXxzt07LDSTEaJR9dRaKwhv8a2l4tKxjl9SVd5vjWzmNiEAg%0AWNPVPTXV3lBLtwbhD61uIzVQjPb2|预订|54000D314120|D3141|NJH|LYS|FYS|PTS|19:33|20:03|00:30|Y|LWyp23GrFLn6BZ%2B2SX3s3i9TyknWmMZJh5hcwcQSbUs7QLqL|20180201|3|H2|21|22|1|0|||||||无||||无|2|||O0M0O0|OMO|0","029oMYTnkTL3l0%2B%2BFVpGG8FJFBC%2BJ%2BGnaFluaFnmNjPT8eaTWUxkEnG68opaHqeVWHXB0NEziRgt%0ATSmeBttFjjcUEHndN%2FUxUbYVAkJSOGQFYpQro7GwYGcfULmmljcHcG59rZmkS%2B3M6QVzOHVBY0fM%0A%2FM2HnVHhCRHisTNZsRyoJ4OHgZo2texe4RdJHE%2FNsEcTHpUgem6x6RR1PY8UL5E5TtuEeqActEqj%0ASVoYz%2BfV8w%2FvZxP96fWaLKc%3D|预订|240000G3230D|G323|VNP|XKS|FZS|HJS|19:37|20:26|00:49|Y|fAblC5xkOZIBEvdAa2eVvAD3sR6fN2yr4ReXxg0Vq2n4ypBa|20180201|3|P3|23|26|1|0|||||||||||有|8|2||O0M090|OM9|0","qQdlJOwgUM5yQCdYzJBP%2BHGb0Oqdzbc9ejxgFHfqot54ryitya6WmCCIdPTi87ceu%2ByujDOw5x6a%0AG036WHOIfrbAJz4yo5FKBFvP1peuCN5fBKweIK9nI%2B6zGJD6x%2BWwpuC4bru1YJ1CrAAv9td9I4KB%0AGx5GJ6yE%2B6MAA38YeJoZfsP8V%2FTeATYgRf4a2m0C6BKFWQEfGSpAtQ%2FxlCbWBs%2FB7jInFvEWAW8B%0AWGumHhEmJzVkfX%2F%2Fg4jBae4%3D|预订|58000D64190D|D6419|FZS|LYS|FZS|PTS|20:05|20:55|00:50|Y|I5y%2F2glFgmYNRmoDmfMbXX6fMuBoBXjUz%2ByFVbeSGCmrUXAw|20180201|3|G2|01|03|1|0|||||||有||||无|无|||O0M0O0|OMO|0","|预订|56000D323320|D3233|HGH|XMS|FYS|PTS|20:06|20:46|00:40|N|c7t%2BygKokbsEPDLEAwUiSOnPo7NHodIw12HLIm3NNWYREEA%2B|20180201|3|H6|11|13|1|0|||||||无||||无|无|||O0M0O0|OMO|0","j4Oi6LZLmtVNJ02F0R4lyK0CqwPC1PWmYQ5yFX%2F%2F9BT4%2Fim9P2avSgCdBePpyzQoBeu%2BdGc25A3J%0AyNVIDM%2FYcrKSbVIKPsN2ZTKZ9Nr%2FGLTRVoQt5J8YdQIJPkRPSp6uGrX3vqadosv%2Bm2QDZQq3LUqF%0ANGRESDFhc8ILB4LzCgY%2FGWRk3rR0DMfisthZc6pFwocY07b2X0MnCF%2FE9zTJflMUzRafGbR%2BGYrY%0AGr4cI9YHhURy1pjOfyGpwUQ%3D|预订|5y000G53030A|G5303|WCS|XMS|FZS|HJS|20:18|21:02|00:44|Y|DfpubYxFBIwsS3XS50yeeLugorNuX7rled92NfaWdGYAXLHm|20180201|3|G1|04|06|1|0||||||3|||||无|无|||O0M0P0|OMP|0","5sVT9EjXY4FR0cSwbLvkk21t0DpDp794ugrzePfREjltL6PAiqYVL6ClWKdiWaOHRcRsIkXO%2FMdp%0AbD40atOf2kDYivFdk3CQIVWWb334US4jz%2BQzaBcFI37rQAk57n%2FiDHhWxywuDEks%2Fv5rRJCdlTPP%0AV%2FT3r0mnnM1AvGWpuBSi%2F4S%2FbqGERFMULOwnOP8k4FutOm%2FJnknloSFqB9qlP8%2FuFIr3B4psQAQR%0ANxoGxf%2BUKW1eCGeRM8G2hNc%3D|预订|58000D62390C|D6239|FZS|XKS|FZS|HJS|20:30|21:14|00:44|Y|N%2FPJJCzcp2fVDNvgS45q2u%2BtIOoEE2lsuU6TWWJQ1cq3pPSb|20180201|3|G2|01|04|1|0|||||||有||||有|20|||O0M0O0|OMO|0","yetLblHWWGzebLXhKZ9Af8pXf2h2mnlNPPQDAFVIFlh5fI%2BFEndlEFp2wdEh76ca6%2BL862DTWe0f%0AnXo203q27sPTcwWsPd5kZMRghjOlVrGTJoFOxuRgFcq7hUaKZ3GRHX1aqREb5fL2jrNuMOMFrJ0v%0AH%2BAjJqsJaa9F8lr9Ny97fmaiW7uwDaeYEkHnHeUfrxc0Yxj%2FBTT0xZvTDGKo3a13vRt24aNvBQsr%0AUGnzxUdLX%2FkEyE6zTT18EW0%3D|预订|240000G32509|G325|VNP|XKS|FZS|PTS|21:00|22:06|01:06|Y|mFAMNTZmc%2B2BORP24AYfdEz1R8rKjltpEQAkmmJz%2BLh2tpMm|20180201|3|P4|18|20|1|0|||||||||||有|有|2||O0M090|OM9|0","jOrvmeTe4suNH3YqjNnifKKHb22lMk2VY%2FHjYZ%2BhzcIQq4oeQfcRJ34%2FsR2lFuI%2FhzA46CuZI7PZ%0AwXJcf07FYqbMLqumCgQbhS1IyzernNyqq%2BOmiCp4xtRaae4Un7nUK7X2w%2F%2FizJZAAGtXKRdSFqTd%0AEbaePYtGKRa97SpSVNUsm5xvTYNFJ19f6ixLvSGdHPIxqFJDLqhjJdgl3Mcdt6UpxHJKYyDWr9eH%0Anvqh4OETXIvvd3TH9%2FdMXpHC2A7L|预订|5e000D330555|D3305|NGH|XKS|FYS|PTS|21:10|21:40|00:30|Y|Gx2FiRoL6PWQLvNuuyeBm2745l4UFRZ6Bgy16dA3GueXd7wF|20180201|3|H2|10|11|1|0|||||||无||||有|7|||O0M0O0|OMO|0","LK%2F2F32tzfMjFl3gINHKc40p%2BDeCN44bEeKidAWYgvC7zYFdDfVqEPUR4Q2nHdk2of%2Bbs2jVB4ji%0A7cxcGifC%2BiaGr1VqBxz2SkJkOLtlz%2B7mhdsR5dE1pO3W%2Bjp2A%2FkBAaMQ3wZk1gt%2Fg5Bexb0BJNkL%0AozWg9PyH7pBWaLywFabXEH57p39pGRF%2FOf7k6Bmgnr9kmbnI0pUYy7XJrxlAIXMn4a%2BWqUZx4ax2%0AfnEFKB1uXt801QDEZtgv7%2FGBdxXQ|预订|56000D321760|D3217|HGH|XKS|FYS|XWS|21:16|21:53|00:37|Y|6Ti5TIej1WVWJYv%2FG%2BwzKXSi0yw3a9NytAbQ0G4YyKjnE3vD|20180201|3|H2|13|14|1|0|||||||无||||有|1|||O0M0O0|OMO|0","N50VyZwQQI85hj3eaMLa3v1VEQQiCyF23NIZGB0u2t87pdoXBxkwMMZzioUsuiNCKjU8RI8AJTVA%0AIszyLUoLmk3ng44gUBdii4jNi6pi0H1SV7F%2BSN6tNOrloy7sixehYGm2036WBnzQsyIUdZ40RTRz%0A57phYwXalpdNChZoQQsCR%2Ftb56A%2FNBqJlywjaYQPokOq98TCrprNWoek7sP%2F4vucN6kuu4oUwtfV%0Af6ECRBQQk60MpJ7waqGmIBo%3D|预订|5l0000D38190|D381|AOH|PTS|FYS|PTS|21:47|22:26|00:39|Y|ZZPeIRLFj5D9gOH9nEN7Guampjkst1uXzKCcTD0wyT89ywxQ|20180201|3|H3|17|19|1|0|||||||无||||有|有|||O0O0M0|OOM|0"]},"httpstatus":200,"messages":"","status":true}
'''
response = requests.get(url, headers=headers)
result = json.loads(response.text)
print(result)
# print(response.text)
# reCom = re.compile(r'\|预订\|.*?\|(.*?)\|.*?\|(\d{2}:\d{2})\|(\d{2}:\d{2})\|(\d{2}:\d{2})\|Y\|.*?\|+([有无]{1}|\d*?)\|+([有无]{1}|\d*?)\|([有无]{1}|\d*?)\|+O0M0O0\|OMO\|')
# data = re.findall(reCom, stringData)
# print(data,  len(data))