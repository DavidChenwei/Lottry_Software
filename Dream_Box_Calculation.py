import utils.globalvar as gl

# from Dream_Box_CSV import writeExecl

gl._init()
Dict_Mtl = {}
Dict_Mdx = {}
Dict_Rqq = {}
Dict_Xjzj = {}
gl.set_value("dict_Mdx", Dict_Mdx)
gl.set_value("dict_Mtl", Dict_Mtl)
str_info = '没有信息'
num_mdx = 0
num_mtl = 0
num_rqq = 0
num_xjzj = 0
num_row = 0

def caldiamond_buff(content: str, username: str, time_stamp: int, msg_id: str):
    global num_mdx, num_mtl, num_rqq, num_xjzj
    global Dict_Mdx, Dict_Mtl, Dict_Rqq, Dict_Xjzj
    global num_row
    global str_info
    Diamond = 0
    length = len(content)
    length_name = len(username)
    info = content[length_name:length]
    # print(info)
    arry_1 = info.split(" 爆出 BUFF ")
    #print(arry_1)
    str_temp = arry_1[1].split("x")
    #print(str_temp)
    # 获取礼物名称
    NameGift = str_temp[0]
    # 获取礼物个数
    str_temp_1 = str_temp[1].split("个")
    account = int(str_temp_1[0][0:1])
    # print('收到了', account, '个', NameGift)
    # Total_Account += account
    # gl.set_value('TotalAccount', Total_Account)
    selected_gift = gl.get_value('selected_gift')

    if '梦幻迷迭香' in NameGift:
        Diamond = 1000
        str_info = str(time_stamp) + "," + username + "," + NameGift + "," + str(account) + "," + str(
            Diamond * account) + ',normal' + ',True' + "," + msg_id
        # try:
        #     writeExecl(str_info)
        # except Exception as e:
        #     print(e)
        gl.set_value(num_row, str_info)
        num_row += 1
        try:
            if Dict_Mdx.__contains__(username):
                last_account = Dict_Mdx.get(username)
                total = account + int(last_account)
                Dict_Mdx.update({username: total})
            else:
                Dict_Mdx[username] = account
            gl.set_value("dict_Mdx", Dict_Mdx)

            # print('初始字典 :', Dict_Mdx)
        except Exception as e:
            print(e)
        num_mdx = num_mdx + account
        gl.set_value('num_mdx', num_mdx)

    if '梦幻摩天轮' in NameGift:
        Diamond = 10000
        str_info = str(time_stamp) + "," + username + "," + NameGift + "," + str(account) + "," + str(
            Diamond * account) + ',normal' + ',True' + "," + msg_id
        # try:
        #     writeExecl(str_info)
        # except Exception as e:
        #     print(e)
        gl.set_value(num_row, str_info)
        num_row += 1
        try:
            if Dict_Mtl.__contains__(username):
                last_account = Dict_Mtl.get(username)
                total = account + int(last_account)
                Dict_Mtl.update({username: total})
            else:
                Dict_Mtl[username] = account
            # print(Dict_Mtl)
            gl.set_value("dict_Mtl", Dict_Mtl)
        except Exception as e:
            print(e)
        num_mtl = num_mtl + account
        # print(Dict_Mtl)
        gl.set_value('num_mtl', num_mtl)

    return Diamond * account, NameGift, account


def caldiamond(content: str, username: str, time_stamp: int, msg_id: str):
    global num_mdx, num_mtl, num_rqq, num_xjzj
    global Dict_Mdx, Dict_Mtl, Dict_Rqq, Dict_Xjzj
    global num_row
    global str_info

    if '赠送魔力包获得' in content:
        temp_array = content.split('赠送魔力包获得')
        username = temp_array[0]
        try:
            temp_array_2 = temp_array[1].split('，')
            length =len(temp_array_2)
            for i in range(0, length):
                if '超跑派对卡' in temp_array_2[i]:
                    pdk_arr = temp_array_2[i].split('x')
                    gift_name = pdk_arr[0]
                    gift_account = pdk_arr[1]
        except:
            temp_array_2 = temp_array[1].split('x')
            gift_name = temp_array_2[0]
            gift_account = temp_array_2[1]

        str_info = str(time_stamp) + "," + username + "," + gift_name + "," + str(gift_account) + "," + str(
            0) + "," + msg_id
        gl.set_value(num_row, str_info)
        num_row += 1

        return gift_account, gift_name, username
    Diamond = 0
    length = len(content)
    length_name = len(username)
    info = content[length_name:length]
    # print(info)
    arry_1 = info.split(" 变幻出 ")
    # print(arry_1)
    str_temp = arry_1[1].split("x")
    # print(str_temp)
    # 获取礼物名称
    NameGift = str_temp[0]
    # 获取礼物个数
    str_temp_1 = str_temp[1].split("个")
    account = int(str_temp_1[0][0:1])
    # print('收到了', account, '个', NameGift)
    # Total_Account += account
    # gl.set_value('TotalAccount', Total_Account)
    selected_gift = gl.get_value('selected_gift')

    if '梦幻花环' in NameGift:
        Diamond = 60
        # if '梦幻花环' in selected_gift:
        #     str_info = str(time_stamp) + "," + username + "," + NameGift + "," + str(account) + "," + str(
        #         Diamond * account) + "," + msg_id
        #     gl.set_value(num_row, str_info)
        #     # print(str_info)
        #     # try:
        #     #     writeExecl(str_info)
        #     # except Exception as e:
        #     #     print(e)
        #     num_row += 1

    if '梦幻情书' in NameGift:
        Diamond = 660
        # if '梦幻情书' in selected_gift:
        #     str_info = str(time_stamp) + "," + username + "," + NameGift + "," + str(account) + "," + str(
        #         Diamond * account) + "," + msg_id
        #     # print(str_info)
        #     gl.set_value(num_row, str_info)
        #     # try:
        #     #     writeExecl(str_info)
        #     # except Exception as e:
        #     #     print(e)
        #     num_row += 1

    if '永恒魔法棒' in NameGift:
        Diamond = 660
        # if '永恒魔法棒' in selected_gift:
        # str_info = str(time_stamp) + "," + username + "," + NameGift + "," + str(account) + "," + str(
        #     Diamond * account) + "," + msg_id
        # # print(str_info)
        # gl.set_value(num_row, str_info)
        # # try:
        # #     writeExecl(str_info)
        # # except Exception as e:
        # #     print(e)
        # num_row += 1

    if '梦幻千纸鹤' in NameGift:
        Diamond = 6
        # if '梦幻千纸鹤' in selected_gift:
        #     str_info = str(time_stamp) + "," + username + "," + NameGift + "," + str(account) + "," + str(
        #         Diamond * account) + "," + msg_id
        #     gl.set_value(num_row, str_info)
        #     # # try:
        #     # #     writeExecl(str_info)
        #     # # except Exception as e:
        #     # #     print(e)
        #     num_row += 1

    if '梦幻水晶鞋' in NameGift:
        Diamond = 100
        # str_info = str(time_stamp) + "," + username + "," + NameGift + "," + str(account) + "," + str(
        #     Diamond * account) + "," + msg_id
        # gl.set_value(num_row, str_info)
        # # try:
        # #     writeExecl(str_info)
        # # except Exception as e:
        # #     print(e)
        # num_row += 1

    if '梦幻迷迭香' in NameGift and '梦幻迷你盒' in content:
        Diamond = 1000
        str_info = str(time_stamp) + "," + username + "," + NameGift + "," + str(account) + "," + str(
            Diamond * account) + ',mini' + ',False' + "," + msg_id
        # try:
        #     writeExecl(str_info)
        # except Exception as e:
        #     print(e)
        gl.set_value(num_row, str_info)
        num_row += 1
        try:
            if Dict_Mdx.__contains__(username):
                last_account = Dict_Mdx.get(username)
                total = account + int(last_account)
                Dict_Mdx.update({username: total})
            else:
                Dict_Mdx[username] = account
            gl.set_value("dict_Mdx", Dict_Mdx)

            # print('初始字典 :', Dict_Mdx)
        except Exception as e:
            print(e)
        num_mdx = num_mdx + account
        gl.set_value('num_mdx', num_mdx)

    if '梦幻迷迭香' in NameGift and '梦幻盒子' in content:
        Diamond = 1000
        str_info = str(time_stamp) + "," + username + "," + NameGift + "," + str(account) + "," + str(
            Diamond * account) + ',normal' + ',False' + "," + msg_id
        gl.set_value(num_row, str_info)
        num_row += 1
        try:
            if Dict_Mdx.__contains__(username):
                last_account = Dict_Mdx.get(username)
                total = account + int(last_account)
                Dict_Mdx.update({username: total})
            else:
                Dict_Mdx[username] = account
            gl.set_value("dict_Mdx", Dict_Mdx)

            # print('初始字典 :', Dict_Mdx)
        except Exception as e:
            print(e)
        num_mdx = num_mdx + account
        gl.set_value('num_mdx', num_mdx)

    if '梦幻热气球' in NameGift:
        Diamond = 9999
        str_info = str(time_stamp) + "," + username + "," + NameGift + "," + str(account) + "," + str(
            Diamond * account) + ',normal' + ',False' + "," + msg_id
        # try:
        #     writeExecl(str_info)
        # except Exception as e:
        #     print(e)
        gl.set_value(num_row, str_info)
        num_row += 1
        try:
            if Dict_Rqq.__contains__(username):
                last_account = Dict_Rqq.get(username)
                total = account + int(last_account)
                Dict_Rqq.update({username: total})
            else:
                Dict_Rqq[username] = account
            # gl.set_value("dict_Mdx", Dict_Mdx)
        except Exception as e:
            print(e)
        num_rqq = num_rqq + account
        gl.set_value('num_rqq', num_rqq)

    if '梦幻摩天轮' in NameGift and '梦幻迷你盒' in content:
        Diamond = 10000
        str_info = str(time_stamp) + "," + username + "," + NameGift + "," + str(account) + "," + str(
            Diamond * account) + ',mini' + ',False' + "," + msg_id
        # try:
        #     writeExecl(str_info)
        # except Exception as e:
        #     print(e)
        gl.set_value(num_row, str_info)
        num_row += 1
        try:
            if Dict_Mtl.__contains__(username):
                last_account = Dict_Mtl.get(username)
                total = account + int(last_account)
                Dict_Mtl.update({username: total})
            else:
                Dict_Mtl[username] = account
            # print(Dict_Mtl)
            gl.set_value("dict_Mtl", Dict_Mtl)
        except Exception as e:
            print(e)
        num_mtl = num_mtl + account
        # print(Dict_Mtl)
        gl.set_value('num_mtl', num_mtl)

    if '梦幻摩天轮' in NameGift and '梦幻盒子' in content:
        Diamond = 10000
        str_info = str(time_stamp) + "," + username + "," + NameGift + "," + str(account) + "," + str(
            Diamond * account) + ',normal' + ',False' + "," + msg_id
        gl.set_value(num_row, str_info)
        num_row += 1
        try:
            if Dict_Mtl.__contains__(username):
                last_account = Dict_Mtl.get(username)
                total = account + int(last_account)
                Dict_Mtl.update({username: total})
            else:
                Dict_Mtl[username] = account
            # print(Dict_Mtl)
            gl.set_value("dict_Mtl", Dict_Mtl)
        except Exception as e:
            print(e)
        num_mtl = num_mtl + account
        # print(Dict_Mtl)
        gl.set_value('num_mtl', num_mtl)

    if '星际战舰' in NameGift:
        Diamond = 50000
        str_info = str(time_stamp) + "," + username + "," + NameGift + "," + str(account) + "," + str(
            Diamond * account) + ',normal' + ',False' + "," + msg_id
        gl.set_value(num_row, str_info)
        num_row += 1
        try:
            if Dict_Xjzj.__contains__(username):
                last_account = Dict_Xjzj.get(username)
                total = account + int(last_account)
                Dict_Xjzj.update({username: total})
            else:
                Dict_Xjzj[username] = account
            # print(Dict_Mtl)
            # gl.set_value("dict_Mtl", Dict_Mtl)
        except Exception as e:
            print(e)
        num_xjzj = num_xjzj + account
        gl.set_value('num_xjzj ', num_xjzj )

    return Diamond * account, NameGift, account

# print(caldiamond_buff('住手丶那奖是我的 赠送 梦幻迷你盒 爆出 BUFF 梦幻迷迭香 x2个 ', '住手丶那奖是我的','11:42:19','T6ozCrxkAAALr985eKsFAOB8CwBh'))

