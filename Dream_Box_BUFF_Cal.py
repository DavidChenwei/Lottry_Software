def cal_buff_box(NameGift: str, account: int, cal_total_gift_value_diamond: float):
    if NameGift == '梦幻迷迭香':
        # print(NameGift, account)
        if account >= 2:
            cal_total_gift_value_diamond = cal_total_gift_value_diamond - (
                    1659.75104 * 1)
            cal_total_gift_value_diamond = cal_total_gift_value_diamond - (
                    1327.80083 * (account - 1))
        else:
            cal_total_gift_value_diamond = cal_total_gift_value_diamond - (
                    1659.75104 * account)
    if NameGift == '梦幻摩天轮':
        if account >= 2:
            cal_total_gift_value_diamond = cal_total_gift_value_diamond - (
                    16590.75104 * 1)
            cal_total_gift_value_diamond = cal_total_gift_value_diamond - (
                    13270.80083 * (account - 1))
        else:
            cal_total_gift_value_diamond = cal_total_gift_value_diamond - (
                    16590.75104 * account)
    return cal_total_gift_value_diamond
