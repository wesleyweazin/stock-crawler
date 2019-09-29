co_ids = ['1101', '1102', '1216', '1301', '1303', '1326', '1402', '2002', '2105', '2207',
          '2227', '2301', '2303', '2308', '2317', '2327', '2330', '2352', '2357', '2382',
          '2395', '2408', '2409', '2412', '2454', '2474', '2609', '2610', '2633', '2801',
          '2823', '2880', '2881', '2882', '2883', '2884', '2885', '2886', '2887', '2890',
          '2891', '2892', '2912', '3008', '3045', '3711', '4904', '4938', '5871', '5876',
          '5880', '6505', '9904', '9910']


# http://pchome.megatime.com.tw/group/mkt5/cidE002.html
# https://www.cnyes.com/twstock/Etfingredient/0050.html
# https://web.archive.org/web/20100208100742/http://www.twse.com.tw/ch/trading/indices/twco/tai50i.php
# https://www.taiwanindex.com.tw/index/index/TW50
# https://www.twse.com.tw/zh/

def get_co_ids():
    # return ['2330']
    return ['2801']
    # return co_ids

def get_co_ids2():
    # end: inclusive
    l = [
        # {'begin': 1101, 'end': 1110, 'skip': [1105, 1106, 1107]},
        # {'begin': 1201, 'end': 1240, 'skip': [1202, 1204, 1205, 1206, 1207, 1208, 1209, 1211, 1214, 1221, 1222, 1223, 1224, 1226, 1228, 1230, 1237, 1238, 1239]},
        {'begin': 2801, 'end': 2823, 'skip': []},
    ]

    for category in l:
        for i in range(category['begin'], category['end'] + 1):
            if i not in category['skip']:
                yield str(i)


if __name__ == '__main__':
    print(list(get_co_ids()))
