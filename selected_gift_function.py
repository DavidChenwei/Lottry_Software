import re

info_list = []
info_list_plus = []
info_list_final = []
Dict_first = {}  # 用来存储迷迭香，摩天轮，派对卡
Dict_second = {}  # 用来存储热气球和战舰


def fomart_data(args1, args2, args3):
    global info_list
    info_list = []

    Dict_Mdx = args1
    Dict_Mtl = args2
    Dict_pdk = args3

    sorted(Dict_Mdx)
    sorted(Dict_Mtl)
    sorted(Dict_pdk)
    # 第一个for循环，拿迷迭香的字典中的key和另两个字典中key进行对比
    for key_mdx in Dict_Mdx:
        temp_str = key_mdx + ' ' + str(Dict_Mdx.get(key_mdx))
        if Dict_Mtl.__contains__(key_mdx):
            temp_str += ' ' + str(Dict_Mtl.get(key_mdx))
        else:
            temp_str += ' ' + '0'
        if Dict_pdk.__contains__(key_mdx):
            temp_str += ' ' + str(Dict_pdk.get(key_mdx))
        else:
            temp_str += ' ' + '0'
        if temp_str != '':
            info_list.append(temp_str)

    # 第二个for循环，拿摩天轮的字典中的key和另两个字典中的key进行对比
    for key_mtl in Dict_Mtl:
        temp_str = ''
        if Dict_Mdx.__contains__(key_mtl) and Dict_pdk.__contains__(key_mtl):
            pass
        if Dict_Mdx.__contains__(key_mtl) is not True and Dict_pdk.__contains__(key_mtl):
            temp_str += key_mtl + ' ' + '0' + ' ' + str(Dict_Mtl.get(key_mtl)) + ' ' + str(Dict_pdk.get(key_mtl))
        if Dict_Mdx.__contains__(key_mtl) is not True and Dict_pdk.__contains__(key_mtl) is not True:
            temp_str += key_mtl + ' ' '0' + ' ' + str(Dict_Mtl.get(key_mtl)) + ' ' + '0'  # 这里改动过
        if temp_str != '':
            info_list.append(temp_str)

    # 第三个for循环
    for key_pdk in Dict_pdk:
        temp_str = ''
        if Dict_Mdx.__contains__(key_pdk) or Dict_Mtl.__contains__(key_pdk):
            pass
        else:
            temp_str += key_pdk + ' ' + '0' + ' ' + '0' + ' ' + str(Dict_pdk.get(key_pdk))
        if temp_str != '':
            info_list.append(temp_str)

    sum_dict_mdx = sum(Dict_Mdx.values())
    sum_dict_mtl = sum(Dict_Mtl.values())
    sum_dict_pdk = sum(Dict_pdk.values())

    return info_list, sum_dict_mdx, sum_dict_mtl, sum_dict_pdk


def fomart_data_plus(args1, args2):
    global info_list_plus
    info_list_plus = []
    Dict_Rqq = args1
    Dict_Xjzj = args2
    sorted(Dict_Rqq)
    sorted(Dict_Xjzj)

    for key_Rqq in Dict_Rqq:
        temp_str = key_Rqq + ' ' + str(Dict_Rqq.get(key_Rqq))
        if Dict_Xjzj.__contains__(key_Rqq):
            temp_str += ' ' + str(Dict_Xjzj.get(key_Rqq))
        else:
            temp_str += ' ' + '0'
        if temp_str != '':
            info_list_plus.append(temp_str)

    for key_xjzj in Dict_Xjzj:
        temp_str = ''
        if Dict_Rqq.__contains__(key_xjzj):
            pass
        else:
            temp_str = key_xjzj + ' ' + '0' + ' ' + str(Dict_Xjzj.get(key_xjzj))
        if temp_str != '':
            info_list_plus.append(temp_str)
    sum_dict_rqq = sum(Dict_Rqq.values())
    sum_dict_xjzj = sum(Dict_Xjzj.values())
    # print(info_list_plus)
    return info_list_plus, sum_dict_rqq, sum_dict_xjzj


def integrated_list(args1, args2):
    global info_list_final
    info_list_final = []
    for i in args1:
        temp_array = re.split(r'[\s]', i, 1)
        Dict_first[temp_array[0]] = temp_array[1]

    for i in args2:
        temp_array = re.split(r'[\s]', i, 1)
        Dict_second[temp_array[0]] = temp_array[1]
    sorted(Dict_first)
    sorted(Dict_second)
    for key_f in Dict_first:
        temp_str = key_f + ' ' + str(Dict_first.get(key_f))
        if Dict_second.__contains__(key_f):
            temp_str += ' ' + str(Dict_second.get(key_f))
        else:
            temp_str += ' ' + '0' + ' ' + '0'
        if temp_str != '':
            info_list_final.append(temp_str)

    for key_s in Dict_second:
        temp_str = ''
        if Dict_first.__contains__(key_s):
            pass
        else:
            temp_str = key_s + ' ' + '0' + ' ' + '0' + ' ' + '0' + ' ' + str(Dict_second.get(key_s))
        if temp_str != '':
            info_list_final.append(temp_str)

    return info_list_final
