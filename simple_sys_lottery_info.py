import json
import re
import time

import requests
from numpy import around

import utils.globalvar as gl

url = 'https://share.egame.qq.com/cgi-bin/pgg_live_async_fcgi'


def lottery_related_function(room_id: str):
    try:
        timestamp = int(time.time())
        data = {
            '_t': timestamp,
            'g_tk': room_id,
            'p_tk': '',
            'param': '{"key":{"module":"pgg_anchor_interact_area_mt_svr","method":"get_interact_area_list","param":{'
                     '"anchor_id":' + room_id + '}}}',
            'app_info': '{"platform":4,"terminal_type":2,"egame_id":"egame_official","version_code":"9.9.9",'
                        '"version_name":"9.9.9"}',
            'tt': '1'
        }
        response = requests.get(url, params=data)
        response = response.text
        msg_list = json.loads(response)
        # lottery_all_info 包含了所有抽奖的信息，是个父list
        lottery_all_info = msg_list['data']['key']['retBody']['data']['list']
        try:
            lottery_all_info = lottery_all_info[0]['event_item']['info']['lottery_info']
        except:
            lottery_all_info = lottery_all_info[1]['event_item']['info']['lottery_info']
        print(lottery_all_info)
        # 获取主播名称
        gift_nick = lottery_all_info['creater']['nick']
        gl.set_value('gift_nick', gift_nick)
        # 获取此次抽奖红包的ID
        lottery_id = lottery_all_info['lottery_id']
        print("红包ID: ", lottery_id)
        gl.set_value('lottery_id', lottery_id)
        # 获取抽奖的时间
        lottery_time = lottery_all_info['lottery_tm']
        gl.set_value('lottery_time',lottery_time)
        # 在此判断是否多礼物抽奖
        queue_conds = lottery_all_info['queue_conds']
        # print(queue_conds)
        # 拿到List长度，判断有几个礼物
        multi_gift = len(queue_conds)
        # lottery_id = ''
        if multi_gift:
            # print('List不空有东西，多礼物抽奖')
            # print('礼物个数为',multi_gift)
            multi_gift_name = ''
            gift_color = ''
            for gift in queue_conds.values():
                # print(gift[0]['info']['desc'])
                multi_gift_name = multi_gift_name + gift[0]['info']['desc'] + "|"
                gift_color = gift_color + gift[0]['info']['tips_color'] + "|"
            # print(gift_color)
            gl.set_value('gift_name', multi_gift_name)
            # print(multi_gift_name)
            stat = lottery_all_info['stat']
            # print(stat)
            # 获取礼物总数，参与人的总数
            user_total = stat['user_total']
            gift_total = stat['gift_total']
            # 获取红包信息
            prize_info = lottery_all_info['prize']
            name = prize_info['name']
            name = re.findall(r"\d+\.?\d*", name)
            prize_per_copy = name[0]
            # print("红包金额: ", name[0], '元')
            copies_total = prize_info['copies_total']
            print("红包的个数: ", copies_total)

            # prize_per_copy = 0
            # copies_total = 0

            total_lottery_value = float(prize_per_copy) * float(copies_total)
            print(multi_gift_name)
            gl.set_value('gift_name', multi_gift_name)
            gl.set_value('total_lottery_value', total_lottery_value)
        else:
            # print('List空，单礼物抽奖')
            # 获取此次抽奖红包的ID
            lottery_id = lottery_all_info['lottery_id']
            # print("红包ID: ", lottery_id)
            # 获取此次抽奖每个红包的金额
            prize_info = lottery_all_info['prize']
            # print(prize_info)
            # prize_per_copy = prize_info['prize_per_copy']
            # prize_per_copy = int(prize_per_copy) / 100
            # if prize_per_copy <=0 :
            name = prize_info['name']
            name = re.findall(r"\d+\.?\d*", name)
            # print("红包金额: ", name[0], '元')
            # else:
            # print("红包金额: ", name[0], '元')
            # 获取此次抽奖的红包个数
            print(name)
            copies_total = prize_info['copies_total']
            print("红包的个数: ", copies_total)
            # 下面是获取送礼信息
            stat = lottery_all_info['stat']
            # print(stat)
            # 获取礼物总数，参与人的总数
            user_total = stat['user_total']
            gift_total = stat['gift_total']
            # lucky_total = stat['lucky_total']
            # print("参与人数: ", user_total)
            # print("礼物总数: ", gift_total)
            # print("红包个数: ", lucky_total)
            # 获取主播的姓名
            gift_nick = lottery_all_info['creater']['nick']
            # print(gift_nick)
            # 获取礼物的名称
            gift_info = lottery_all_info['conds']
            print(gift_info)
            gift_info = gift_info[1]['info']
            gift_name = gift_info['gift_name']
            print(gift_name)
            # ("礼物名称: ", gift_name)
            # 获取抽奖的ID，礼物名称，参与人数，红包总额，礼物总数
            prize_per_copy = name[0]
            total_lottery_value = float(prize_per_copy) * float(copies_total)
            gl.set_value('lottery_id', lottery_id)
            gl.set_value('total_lottery_value', total_lottery_value)
            gl.set_value('gift_name', gift_name)
            gl.set_value('gift_nick', gift_nick)

    except Exception as e:
        print("抓取抽奖后台数据出错，请将错误提示保存，并反馈")
        print(e)
        gl.set_value('gift_name', '当前无抽奖')
        # i = 1
