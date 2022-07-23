def Judgment_Contain_Diamond_Gift_Name(content: str):
    bln_res = False
    if '闪电超跑' in content or '要抱抱' in content or '666' in content or '大炮' in content or '黄金大炮' in content or \
            '爱你一万年' in content or '比心' in content or '盛典葱鸭' in content or '守护主播' in content or \
            '银河战机' in content or '至尊王者' in content or '幸运星' in content or '海洋之心' in content or \
            '告白气球' in content or '么么哒' in content or '喜欢你' in content or '打call' in content or \
            '你最棒' in content or '梦幻花环' in content or '梦幻情书' in content or '梦幻摩天轮' in content \
            or '梦幻迷迭香' in content or '排面' in content or '夺宝战机' in content or '超级666' in content or '梦幻水晶鞋' in content\
            or '梦幻千纸鹤' in content or '超粉战机' in content or '超粉飞船' in content or '超粉冲冲冲' in content or '超粉舰队' in content \
            or '魔力包' in content or '宠你一万年' in content or '永恒魔法棒' in content or '梦幻热气球' in content or '星际战舰' in content:

        if '撮佸嚭' not in content and '挱闂磋' not in content and '分享' not in content:
            bln_res = True

    return bln_res
