def Dream_Box_Judgment(username: str, content: str):
    bln_DBJ = False
    # print('传到这个里的用户名是'+username)
    # print('传到这个里的内容是' + content)
    length = len(username)
    # print('截取的内容是' + content[0:length])
    if username == content[0:length]:
        length_1 = len(content)
        info = content[length:length_1]
        res = '梦幻花环' in info or '梦幻情书' in info or '梦幻迷迭香' in info or '梦幻摩天轮' in info or '梦幻千纸鹤' in info \
              or '梦幻水晶鞋' in info or '永恒魔法棒' in info or '梦幻热气球' in info or '梦幻热气球' in info\
            or '星际战舰' in info
        if res:
            bln_DBJ = True
    return bln_DBJ
