Diamond = 0


def normal_gift_cal(gift_name: str, gift_account: int):
    global Diamond
    if '闪电超跑' == gift_name:
        Diamond = 1880
    if '要抱抱' == gift_name:
        Diamond = 1
    if '666' == gift_name:
        Diamond = 1
    if '大炮' == gift_name:
        Diamond = 100
    if '爱你一万年' == gift_name:
        Diamond = 1314
    if '黄金大炮' == gift_name:
        Diamond = 100
    if '比心' == gift_name:
        Diamond = 2
    if '盛典葱鸭' == gift_name:
        Diamond = 1
    if '守护主播' == gift_name:
        Diamond = 60
    if '银河战机' == gift_name:
        Diamond = 5000
    if '夺宝战机' == gift_name:
        Diamond = 5000
    if '至尊王者' == gift_name:
        Diamond = 20000
    if '幸运星' == gift_name:
        Diamond = 10
    if '海洋之心' == gift_name:
        Diamond = 520
    if '告白气球' == gift_name:
        Diamond = 9999
    if '么么哒' == gift_name:
        Diamond = 520
    if '喜欢你' == gift_name:
        Diamond = 99
    if '打call' == gift_name:
        Diamond = 52
    if '你最棒' == gift_name:
        Diamond = 6
    if '盛典冲锋机' == gift_name:
        Diamond = 1000
    if '排面' == gift_name:
        Diamond = 10
    if '爱心抱抱' == gift_name:
        Diamond = 1
    if '超级666' == gift_name:
        Diamond = 1
    if '超粉飞船' == gift_name:
        Diamond = 66
    if '超粉战机' == gift_name:
        Diamond == 1000
    if '超粉舰队' == gift_name:
        Diamond == 10000
    if '超粉冲冲冲' == gift_name:
        Diamond = 1
    if '魔力包' == gift_name:
        Diamond = 1 * 0.1
    if '宠你一万年' == gift_name:
        Diamond = 1314
    return Diamond * gift_account
