def Normal_Gift_Judgement(username: str, content: str):
    try:
        bln_NGJ = False
        # print('传到这个里的用户名是'+username)
        # print('传到这个里的内容是' + content)
        length = len(username)
        # print('截取的内容是' + content[0:length])
        if username == content[0:length]:
            length_1 = len(content)
            char_1 = '个'
            nPos = content.index(char_1)
            NameGift = content[nPos + 1:length_1]
            res = '鹅蛋' in NameGift or '爆灯' in NameGift or '金卡' in NameGift or '小星星' in NameGift or '大神奖章' in NameGift \
                  or '梦幻马车' in NameGift or '甜蜜火箭' in NameGift or '吃瓜' in NameGift or '冲冲葱' in NameGift \
                  or '星战总动员' in NameGift
            if not res:
                bln_NGJ = True
    except Exception as e:
        pass
        # print(e)
    return bln_NGJ
