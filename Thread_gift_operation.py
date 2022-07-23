import time

import utils.globalvar as gl
from Dream_Box_Calculation import caldiamond, caldiamond_buff
from Dream_Box_Judgment import Dream_Box_Judgment
from First_Judgement import Judgment_Contain_Diamond_Gift_Name
from Normal_Gift_Cal import normal_gift_cal
from Normal_Gift_Get_Gift_name import get_normal_gift_name
from Normal_Gift_Judgment import Normal_Gift_Judgement
from monitor_player_function import operation_function
from simple_sys_lottery_info import lottery_related_function

time_stamp_list = []
id_list = []
total_gift_value_diamond = 0
local_gift_value_diamond = 0
total_rmb_value = 0
cal_total_gift_value_diamond = 0
other_gift_total_diamond = 0
money_give_out = 0
final_balance = 0
this_time_RMB_total = 0  # 本次直播抽奖的总收益
refresh_time = 0
cal_local_gift_value_diamond = 0
gl.set_value('refresh_time', 0)
local_money_back = 0
local_total_rmb_value = 0
every_local_money_back = 0
RMB_balance = 0
Dict_user = {"用户统计": 1}
Dict_id = {'用户ID': 1}
Dict_time_stamp = {'时间戳': 1}
Dict_selected_gift = {}  # 记录选中的礼物格式为 user_id : gift_number 每轮清空
Dict_total_user = {}
Dict_pdk = {}  # 记录超跑派对卡
gl.set_value("dict_pdk", Dict_pdk)

Dict_every_mdx = {}  # 记录每轮的迷迭香
Dict_every_mtl = {}  # 记录每轮的摩天轮
Dict_every_pdk = {}  # 记录每轮的超跑派对卡
Dict_every_rqq = {}  # 记录每轮的热气球
Dict_every_xjzj = {}  # 记录每轮的星际战舰
balance_list = {}  # 每十分钟记录一次balance

gl.set_value("dict_every_pdk", Dict_every_pdk)
gl.set_value("dict_every_mtl", Dict_every_mtl)
gl.set_value("dict_every_mdx", Dict_every_mdx)
ini_time = 1
iii = 1
Dict_system_mention = {}

gift_total = 0
bln_TimeStamp_ext = False
bln_msgId_ext = False
bln_mention_ext = True
bln_current_lottery = 0


def gift_operation(agrs):
    Mdx_price_small = float(gl.get_value('Mdx_price_small'))
    Mtl_price_small = float(gl.get_value('Mtl_price_small'))
    double_mdx_price = float(gl.get_value('double_mdx_price'))
    Three_mdx_price = float(gl.get_value('Three_mdx_price'))
    Mtl_price = float(gl.get_value('Mtl_price'))
    Mdx_price = float(gl.get_value('Mdx_price'))
    Rqq_price = float(gl.get_value('Rqq_price'))
    Xjzj_price = float(gl.get_value('Xjzj_price'))
    Pdk_price = float(gl.get_value('Pdk_price'))
    Rmb_back = float(gl.get_value('Rmb_back'))
    Three_mtl_price = float(gl.get_value('Three_mtl_price'))
    Double_mtl_price = float(gl.get_value('Double_mtl_price'))
    room_id = gl.get_value('room_id')

    global time_stamp_list
    global id_list
    global total_gift_value_diamond
    global total_rmb_value
    global cal_total_gift_value_diamond
    global this_time_RMB_total
    global refresh_time
    global local_gift_value_diamond
    global cal_local_gift_value_diamond
    global local_money_back
    global every_local_money_back
    global RMB_balance
    global Dict_user
    global gift_total
    global Dict_id
    global Dict_time_stamp
    global bln_TimeStamp_ext
    global bln_msgId_ext
    global bln_mention_ext
    global ini_time
    global iii
    global Dict_selected_gift
    global Dict_system_mention
    global Dict_total_user
    global Dict_every_mdx
    global Dict_every_mtl
    global Dict_every_pdk
    global other_gift_total_diamond
    global money_give_out
    global local_total_rmb_value
    global final_balance
    global bln_current_lottery

    selected_gift = gl.get_value('selected_gift')
    temp_info = agrs.split("$$$")
    username = temp_info[0]
    content = temp_info[1]
    msg_id = temp_info[2]
    time_stamp = int(temp_info[3])
    lottery_gift_name = gl.get_value('gift_name')  # 拿到当前抽奖的礼物名称
    lottery_time = gl.get_value('lottery_time')  # 拿到抽奖的时间
    current_time = int(time.time())
    gap_time = current_time - int(lottery_time)
    if gap_time <= 900 and bln_current_lottery == 0:
        lottery_related_function(room_id)
        bln_current_lottery += 1
        money_give_out = gl.get_value('total_lottery_value')
        print('执行性了一次')
    # 第一遍过滤弹幕

    # 这个判断的原因是，一是抓取弹幕的时候，系统提示有可能会被重复抓取，所以需要根据msg_id,和time_stamp
    bln_first_res = Judgment_Contain_Diamond_Gift_Name(content)
    if username == '企鹅电竞系统提示':
        print(content)
        if Dict_system_mention.__contains__(msg_id):
            bln_mention_ext = False
            pass
        else:
            Dict_system_mention[msg_id] = time_stamp
            bln_mention_ext = True
        # print(bln_mention_ext)
        if '主播发起了抽奖活动，进入企鹅电竞APP马上参与' in content and bln_mention_ext:
            gl.set_value('start_time', time_stamp)
            # this_time_RMB_total += RMB_balance
            gl.set_value('new_lottery', True)
            gl.set_value('new_lottery_left', True)
            Dict_lottery_id = gl.get_value('Dict_lottery_id')
            while iii <= 20:
                try:
                    lottery_related_function(room_id)
                except Exception as e:
                    print(e)
                lottery_id = gl.get_value('lottery_id')
                if Dict_lottery_id.__contains__(lottery_id):
                    iii += 1
                    print('运行了', iii, '次')
                else:
                    Dict_lottery_id[lottery_id] = 1
                    iii += 1
                    break
            print(Dict_lottery_id)
            Dict_user.clear()
            Dict_id.clear()
            Dict_time_stamp.clear()
            print('新一轮红包开始。数据清零')
            print('------------------------------------------------------------')
            money_give_out += gl.get_value('total_lottery_value')
            print('给出的红包总额为: ', money_give_out)
            time_stamp_list = []
            id_list = []
            total_gift_value_diamond = 0
            total_rmb_value = 0
            cal_total_gift_value_diamond = 0
            every_local_money_back = 0
            RMB_balance = 0
            gift_total = 0
            iii = 0
            gl.set_value('user_total', 0)
            gl.set_value('gift_total', 0)
            gl.set_value('total_rmb_value', 0)
            gl.set_value('total_gift_value_diamond', 0)
            gl.set_value('RMB_balance', 0)
            gl.set_value('every_local_money_back', 0)
            gl.set_value('this_time_RMB_total', this_time_RMB_total)

    if bln_first_res:
        time_stamp_int = int(time_stamp)
        timeArray = time.localtime(time_stamp_int / 1000)
        otherStyleTime = time.strftime("%H:%M:%S", timeArray)

        if '梦幻盒子' in content or '梦幻迷你盒' in content or '至尊盒子' in content:  # 盒子和普通礼物的弹幕不同，所以要区别
            # if '梦幻盒子' in content:
            bln_DBJ = Dream_Box_Judgment(username, content)
            if bln_DBJ:
                if Dict_id.__contains__(msg_id):
                    bln_msgId_ext = False
                else:
                    Dict_id[msg_id] = 1
                    bln_msgId_ext = True

                if Dict_time_stamp.__contains__(time_stamp):
                    bln_TimeStamp_ext = False
                else:
                    Dict_time_stamp[time_stamp] = 1
                    bln_TimeStamp_ext = True

                if bln_TimeStamp_ext and bln_msgId_ext:
                    # time_stamp_list.append(int(time_stamp))
                    # id_list.append(msg_id)
                    bln_msgId_ext = False
                    bln_TimeStamp_ext = False
                    if '爆出 BUFF' in content:
                        (current_gift_value, NameGift, account) = caldiamond_buff(content, username, otherStyleTime,
                                                                                  msg_id)
                        NameGift = NameGift.replace(" ", '')
                        local_gift_value_diamond += current_gift_value  # 单独计算盒子
                        cal_local_gift_value_diamond += current_gift_value  # 用来单独计算减去香和轮后的RMB
                        # 这里尝试新加一个变量来代表出香和轮的返钱，保持总钻石和总RMB对应
                        local_total_rmb_value = cal_local_gift_value_diamond / 10 * float(Rmb_back) / 100
                        if NameGift == '梦幻迷迭香':
                            if account == 2:
                                local_money_back += Three_mdx_price - Mdx_price
                            if account == 1:
                                local_money_back += double_mdx_price - Mdx_price
                        if NameGift == '梦幻摩天轮':
                            if account == 2:
                                local_money_back += Three_mtl_price - Mtl_price
                            if account == 1:
                                local_money_back += Double_mtl_price - Mtl_price

                        # 这里统计的是本次直播一共的返钱数，所以不用清零
                        gl.set_value('local_money_back', local_money_back)

                        gl.set_value('solo_total_gift_value_diamond', local_gift_value_diamond)  # 将礼物钻石总价值存入全局变量
                        gl.set_value('solo_total_rmb_value',
                                     local_total_rmb_value - local_money_back)  # 将返点后所得RMB存入全局变量
                        final_balance = other_gift_total_diamond - money_give_out + local_total_rmb_value - local_money_back
                        gl.set_value('this_time_RMB_total', round(final_balance, 2))

                        try:
                            if '梦幻' in lottery_gift_name or lottery_gift_name is None:  #
                                total_gift_value_diamond += current_gift_value  # 累加砖石价值
                                cal_total_gift_value_diamond += current_gift_value  # 用来计算减去香和轮后的RMB

                                total_rmb_value = cal_total_gift_value_diamond / 10 * float(Rmb_back) / 100
                                if NameGift == '梦幻迷迭香':
                                    if Dict_every_mdx.__contains__(username):
                                        last_account = Dict_every_mdx.get(username)
                                        total = account + int(last_account)
                                        Dict_every_mdx.update({username: total})
                                    else:
                                        Dict_every_mdx[username] = account
                                    gl.set_value("dict_every_mdx", Dict_every_mdx)
                                    # print('迷迪香:',Dict_every_mdx)
                                    if account >= 2:
                                        every_local_money_back += Three_mdx_price - Mdx_price
                                    if account >= 1:
                                        every_local_money_back += double_mdx_price - Mdx_price

                                if NameGift == '梦幻摩天轮':
                                    if Dict_every_mtl.__contains__(username):
                                        last_account = Dict_every_mtl.get(username)
                                        total = account + int(last_account)
                                        Dict_every_mtl.update({username: total})
                                    else:
                                        Dict_every_mtl[username] = account
                                    gl.set_value("dict_every_mtl", Dict_every_mtl)
                                    # print('摩天轮',Dict_every_mtl)
                                    if account == 2:
                                        every_local_money_back += Three_mtl_price - Mtl_price
                                    if account == 1:
                                        every_local_money_back += Double_mtl_price - Mtl_price

                                # 判断盒子是否是当前抽奖礼物，如果是则累加，如果不是单独显示
                                gl.set_value('every_local_money_back', every_local_money_back)
                                gl.set_value('total_gift_value_diamond', total_gift_value_diamond)  # 将礼物总价值存入全局变量
                                gl.set_value('total_rmb_value', round(total_rmb_value, 2))  # 将返点后所得RMB存入全局变量
                                # 获取抽奖的金额以此来计算盈亏
                                total_lottery_value = gl.get_value('total_lottery_value')
                                RMB_balance = total_rmb_value - total_lottery_value - every_local_money_back
                                # 将结果存入全局变量
                                gl.set_value('RMB_balance', round(RMB_balance, 2))
                                # Dict_user 用于保存每轮的用户和钻石
                                if Dict_user.__contains__(username):
                                    last_account = Dict_user.get(username)
                                    total = current_gift_value + int(last_account)
                                    Dict_user.update({username: total})
                                else:
                                    Dict_user[username] = current_gift_value
                                # print(Dict_user)
                                monitor_info = operation_function(Dict_user)
                                # print('监控信息:', monitor_info)
                                gl.set_value('monitor_info', monitor_info)

                                # Dict_total_user 用于保存全程的用户和钻石
                                if Dict_total_user.__contains__(username):
                                    last_account = Dict_total_user.get(username)
                                    total = current_gift_value + int(last_account)
                                    Dict_total_user.update({username: total})
                                else:
                                    Dict_total_user[username] = current_gift_value
                                monitor_total_info = operation_function(Dict_total_user)
                                gl.set_value('monitor_total_info', monitor_total_info)

                                gl.set_value('user_total', len(Dict_user))
                                gift_total += account
                                gl.set_value('gift_total', gift_total)
                        except Exception as e:
                            print('BUFF计算出现问题:', e)
                    else:
                        (current_gift_value, NameGift, account) = caldiamond(content, username, otherStyleTime,
                                                                             msg_id)

                        #       current_gift_value, " 钻石 ")
                        NameGift = NameGift.replace(" ", '')
                        local_gift_value_diamond += current_gift_value  # 单独计算盒子
                        cal_local_gift_value_diamond += current_gift_value  # 用来单独计算减去香和轮后的RMB

                        # 这里尝试新加一个变量来代表出香和轮的返钱，保持总钻石和总RMB对应
                        local_total_rmb_value = cal_local_gift_value_diamond / 10 * float(Rmb_back) / 100
                        if NameGift == '梦幻迷迭香' and '梦幻盒子' in content:
                            # record = content + " " + msg_id + ' ' + str(otherStyleTime)
                            # text_create('高级礼物弹幕记录', record)
                            if account >= 2:
                                local_money_back += Mdx_price
                                local_money_back += Mdx_price * (account - 1)
                            else:
                                local_money_back += Mdx_price

                        if NameGift == '梦幻迷迭香' and '梦幻迷你盒' in content:

                            if account >= 2:
                                local_money_back += Mdx_price_small
                                local_money_back += Mdx_price_small * (account - 1)
                            else:
                                local_money_back += Mdx_price_small

                        if NameGift == '梦幻摩天轮' and '梦幻盒子' in content:

                            if account >= 2:
                                local_money_back += Mtl_price
                                local_money_back += Mtl_price * (account - 1)
                            else:
                                local_money_back += Mtl_price

                        if NameGift == '梦幻摩天轮' and '梦幻迷你盒' in content:
                            if account >= 2:
                                local_money_back += Mtl_price_small
                                local_money_back += Mtl_price_small * (account - 1)
                            else:
                                local_money_back += Mtl_price_small

                        if NameGift == '梦幻热气球':
                            local_money_back += Rqq_price

                        if NameGift == '星际战舰':
                            local_money_back += Xjzj_price

                        gl.set_value('local_money_back', local_money_back)
                        # print("本次直播一共返RMB", local_money_back)
                        gl.set_value('solo_total_gift_value_diamond', local_gift_value_diamond)  # 将礼物钻石总价值存入全局变量
                        gl.set_value('solo_total_rmb_value',
                                     local_total_rmb_value - local_money_back)  # 将返点后所得RMB存入全局变量
                        final_balance = other_gift_total_diamond - money_give_out + local_total_rmb_value - local_money_back
                        gl.set_value('this_time_RMB_total', round(final_balance, 2))
                        try:
                            if '梦幻' in lottery_gift_name or lottery_gift_name is None:  #
                                total_gift_value_diamond += current_gift_value  # 累加砖石价值
                                cal_total_gift_value_diamond += current_gift_value  # 用来计算减去香和轮后的RMB
                                # cal_total_gift_value_diamond = cal_buff_box(NameGift, account, cal_total_gift_value_diamond)
                                total_rmb_value = cal_total_gift_value_diamond / 10 * float(Rmb_back) / 100
                                if NameGift == '梦幻迷迭香':
                                    if Dict_every_mdx.__contains__(username):
                                        last_account = Dict_every_mdx.get(username)
                                        total = account + int(last_account)
                                        Dict_every_mdx.update({username: total})
                                    else:
                                        Dict_every_mdx[username] = account
                                    gl.set_value("dict_every_mdx", Dict_every_mdx)
                                    # print('迷迪香:',Dict_every_mdx)
                                    if '梦幻盒子' in content:
                                        if account >= 2:
                                            every_local_money_back += Mdx_price
                                            every_local_money_back += Mdx_price * (account - 1)
                                        else:
                                            every_local_money_back += Mdx_price
                                    if '梦幻迷你盒' in content:
                                        if account >= 2:
                                            every_local_money_back += Mdx_price_small
                                            every_local_money_back += Mdx_price_small * (account - 1)
                                        else:
                                            every_local_money_back += Mdx_price_small
                                if NameGift == '梦幻摩天轮':
                                    if Dict_every_mtl.__contains__(username):
                                        last_account = Dict_every_mtl.get(username)
                                        total = account + int(last_account)
                                        Dict_every_mtl.update({username: total})
                                    else:
                                        Dict_every_mtl[username] = account
                                    gl.set_value("dict_every_mtl", Dict_every_mtl)
                                    # print('摩天轮',Dict_every_mtl)
                                    if '梦幻盒子' in content:
                                        if account >= 2:
                                            every_local_money_back += Mtl_price
                                            every_local_money_back += Mtl_price * (account - 1)
                                        else:
                                            every_local_money_back += Mtl_price
                                    if '梦幻迷你盒' in content:
                                        if account >= 2:
                                            every_local_money_back += Mtl_price_small
                                            every_local_money_back += Mtl_price_small * (account - 1)
                                        else:
                                            every_local_money_back += Mtl_price_small

                                if NameGift == '梦幻热气球':
                                    every_local_money_back += Rqq_price
                                    if Dict_every_rqq.__contains__(username):
                                        last_account = Dict_every_rqq.get(username)
                                        total = account + int(last_account)
                                        Dict_every_rqq.update({username: total})
                                    else:
                                        Dict_every_rqq[username] = account
                                    gl.set_value("dict_every_rqq", Dict_every_rqq)

                                if NameGift == '星际战舰':
                                    every_local_money_back += Xjzj_price
                                    if Dict_every_xjzj.__contains__(username):
                                        last_account = Dict_every_xjzj.get(username)
                                        total = account + int(last_account)
                                        Dict_every_xjzj.update({username: total})
                                    else:
                                        Dict_every_xjzj[username] = account
                                    gl.set_value("dict_every_xjzj", Dict_every_xjzj)

                                # 判断盒子是否是当前抽奖礼物，如果是则累加，如果不是单独显示
                                # print("本轮红包一共返RMB", every_local_money_back)
                                gl.set_value('every_local_money_back', every_local_money_back)
                                gl.set_value('total_gift_value_diamond', total_gift_value_diamond)  # 将礼物总价值存入全局变量
                                gl.set_value('total_rmb_value', round(total_rmb_value, 2))  # 将返点后所得RMB存入全局变量
                                # 获取抽奖的金额以此来计算盈亏
                                total_lottery_value = gl.get_value('total_lottery_value')
                                # print('礼物的砖石总价值为: ', total_gift_value_diamond)
                                # print('返点后礼物RMB总价值为: ', round(total_rmb_value, 2))
                                RMB_balance = total_rmb_value - total_lottery_value - every_local_money_back
                                # 将结果存入全局变量
                                # gl.set_value('RMB_total_value', round(total_rmb_value, 2))
                                gl.set_value('RMB_balance', round(RMB_balance, 2))
                                # Dict_user 用于保存每轮的用户和钻石
                                if Dict_user.__contains__(username):
                                    last_account = Dict_user.get(username)
                                    total = current_gift_value + int(last_account)
                                    Dict_user.update({username: total})
                                else:
                                    Dict_user[username] = current_gift_value
                                # print(Dict_user)
                                monitor_info = operation_function(Dict_user)
                                # print('监控信息:', monitor_info)
                                gl.set_value('monitor_info', monitor_info)

                                # Dict_total_user 用于保存全程的用户和钻石
                                if Dict_total_user.__contains__(username):
                                    last_account = Dict_total_user.get(username)
                                    total = current_gift_value + int(last_account)
                                    Dict_total_user.update({username: total})
                                else:
                                    Dict_total_user[username] = current_gift_value
                                monitor_total_info = operation_function(Dict_total_user)
                                gl.set_value('monitor_total_info', monitor_total_info)

                                gl.set_value('user_total', len(Dict_user))
                                gift_total += account
                                gl.set_value('gift_total', gift_total)
                        except Exception as e:
                            print('正常计算出现问题:', e)

                    # print('---------------------------------------------------------')

        else:  # else 后面既是普通礼物的计算
            bln_NGJ = Normal_Gift_Judgement(username, content)
            if bln_NGJ:
                if Dict_id.__contains__(msg_id):
                    bln_msgId_ext = False
                else:
                    Dict_id[msg_id] = 1
                    bln_msgId_ext = True

                if Dict_time_stamp.__contains__(time_stamp):
                    bln_TimeStamp_ext = False
                else:
                    Dict_time_stamp[time_stamp] = 1
                    bln_TimeStamp_ext = True

                if bln_TimeStamp_ext and bln_msgId_ext:
                    bln_TimeStamp_ext = False
                    bln_msgId_ext = False
                    (gift_name, gift_account) = get_normal_gift_name(content, username)  # 拿到礼物名称和礼物数量
                    current_gift_value = normal_gift_cal(gift_name, gift_account)  # 计算礼物的钻石价值
                    other_gift_total_diamond += current_gift_value / 10 * float(
                        Rmb_back) / 100  # 计算除盒子外其他礼物所以的砖石价值，每轮不清零
                    if gift_name in lottery_gift_name or lottery_gift_name is None:  #
                        # 判断礼物是否是当前抽奖礼物，如果是则累加，不是则只显示不累加
                        total_gift_value_diamond += current_gift_value  # 累加砖石价值
                        cal_total_gift_value_diamond += current_gift_value  # 用来计算减去香和轮后的RMB
                        gl.set_value('total_gift_value_diamond', total_gift_value_diamond)  # 将礼物总价值存入全局变量
                        # print('礼物的砖石总价值为: ', total_gift_value_diamond)
                        # print('计算RMB的钻石数为: ', cal_total_gift_value_diamond)

                        try:
                            total_rmb_value = cal_total_gift_value_diamond / 10 * float(Rmb_back) / 100
                            total_lottery_value = gl.get_value('total_lottery_value')
                            RMB_balance = total_rmb_value - total_lottery_value - every_local_money_back
                            gl.set_value('RMB_balance', round(RMB_balance, 2))
                            gl.set_value('total_rmb_value', round(total_rmb_value, 2))  # 将返点后所得RMB存入全局变量
                            gl.set_value('every_local_money_back', every_local_money_back)
                            if Dict_user.__contains__(username):
                                last_account = Dict_user.get(username)
                                total = current_gift_value + int(last_account)
                                Dict_user.update({username: total})
                            else:
                                Dict_user[username] = current_gift_value
                            # print(Dict_user)
                            monitor_info = operation_function(Dict_user)
                            # print('监控信息:', monitor_info)
                            gl.set_value('monitor_info', monitor_info)

                            # Dict_total_user 用于保存全程的用户和钻石
                            if Dict_total_user.__contains__(username):
                                last_account = Dict_total_user.get(username)
                                total = current_gift_value + int(last_account)
                                Dict_total_user.update({username: total})
                            else:
                                Dict_total_user[username] = current_gift_value
                            monitor_total_info = operation_function(Dict_total_user)
                            gl.set_value('monitor_total_info', monitor_total_info)

                            gl.set_value('user_total', len(Dict_user))
                            gift_total += gift_account
                            gl.set_value('gift_total', gift_total)
                        except Exception as e:
                            print(e)
                        final_balance = other_gift_total_diamond - money_give_out + local_total_rmb_value - local_money_back
                        # print(final_balance)
                        gl.set_value('this_time_RMB_total', round(final_balance, 2))
    if username == '塔罗世界':
        if '超跑派对卡' in content:
            if Dict_id.__contains__(msg_id):
                bln_msgId_ext = False
            else:
                Dict_id[msg_id] = 1
                bln_msgId_ext = True

            if Dict_time_stamp.__contains__(time_stamp):
                bln_TimeStamp_ext = False
            else:
                Dict_time_stamp[time_stamp] = 1
                bln_TimeStamp_ext = True

            if bln_msgId_ext and bln_TimeStamp_ext:
                # 把派对卡给计算盒子的模块，这样才能在右边显示
                print('出超跑派对卡了' + content)
                gift_account, gift_name, user_name = caldiamond(content, username, time_stamp, msg_id)
                if Dict_pdk.__contains__(user_name):
                    last_account = Dict_pdk.get(user_name)
                    total = int(gift_account) + int(last_account)
                    Dict_pdk.update({username: total})
                else:
                    Dict_pdk[user_name] = int(gift_account)
                gl.set_value("dict_pdk", Dict_pdk)

                if Dict_every_pdk.__contains__(user_name):
                    last_account = Dict_every_pdk.get(user_name)
                    total = int(gift_account) + int(last_account)
                    Dict_every_pdk.update({username: total})
                else:
                    Dict_every_pdk[user_name] = int(gift_account)
                gl.set_value("dict_every_pdk", Dict_every_pdk)

    return 0
