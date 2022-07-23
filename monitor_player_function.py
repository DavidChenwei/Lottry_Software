from PyQt5.QtCore import QTimer
from numpy import around

import utils.globalvar as gl


def operation_function(args):
    try:
        player_info = ''
        player_1_name = gl.get_value('player_1_name')
        player_1_discount = gl.get_value('player_1_discount')

        player_2_name = gl.get_value('player_2_name')
        player_2_discount = gl.get_value('player_2_discount')

        player_3_name = gl.get_value('player_3_name')
        player_3_discount = gl.get_value('player_3_discount')

        player_4_name = gl.get_value('player_4_name')
        player_4_discount = gl.get_value('player_4_discount')

        player_5_name = gl.get_value('player_5_name')
        player_5_discount = gl.get_value('player_5_discount')

        for key in args:
            if key == player_1_name:
                name = key
                discount = float(args[key]) * float(player_1_discount) / 100 / 10
                player_info += name + ' ' + str(args[key]) + ' ' + str(around(discount, 2)) + " || "

            if key == player_2_name:
                name = key
                discount = float(args[key]) * float(player_2_discount) / 100 / 10
                player_info += name + ' ' + str(args[key]) + ' ' + str(around(discount, 2)) + " || "

            if key == player_3_name:
                name = key
                discount = float(args[key]) * float(player_3_discount) / 100 / 10
                player_info += name + ' ' + str(args[key]) + ' ' + str(around(discount, 2)) + " || "

            if key == player_4_name:
                name = key
                discount = float(args[key]) * float(player_4_discount) / 100 / 10
                player_info += name + ' ' + str(args[key]) + ' ' + str(around(discount, 2)) + " || "

            if key == player_5_name:
                name = key
                discount = float(args[key]) * float(player_5_discount) / 100 / 10
                player_info += name + ' ' + str(args[key]) + ' ' + str(around(discount, 2)) + " || "
        # print(player_info)

    except Exception as e:
        print(e)

    return player_info



