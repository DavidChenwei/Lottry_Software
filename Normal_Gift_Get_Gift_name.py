import re


def get_normal_gift_name(content: str, username: str):
    len_username = len(username)
    length = len(content)
    content = content[len_username:length]
    char_1 = '个'
    nPos = content.index(char_1)
    # 获取礼物个数
    # 以送出为分割符第一次切割
    Array1 = content.split('送出')
    # 以个为分割符第二次切割
    Array2 = Array1[1].split('个')
    # Array2 中第一个元素为礼物数量
    Array3 = re.findall(r"\d+\.?\d*", Array2[0])
    account_str = Array3[0]
    account = int(account_str)
    # 获取礼物名称'
    NameGift = content[nPos + 1:length].strip()
    if '连击' in NameGift:
        Array4 = NameGift.split('连击')
        Array5 = Array4[0].split('x')
        NameGift = Array5[0]
        account = account * int(Array5[1])
        NameGift = NameGift.strip()
    return NameGift, account

# print(get_normal_gift_name('神秘人 送出66个 要抱抱 x2连击','神秘人'))