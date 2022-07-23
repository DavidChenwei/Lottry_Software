import datetime

import pymysql

curr_time = datetime.datetime.now()
time_str = curr_time.strftime("%Y%m%d")
around_number = 1


# 该放方法建立统计数字的表
def create_balance_table():
    db = pymysql.connect(host='localhost', user='root', password='wl19871005', port=3306, db='qedj')
    cursor = db.cursor()
    table_name = 'Balance_table_' + time_str
    try:
        sql = """CREATE TABLE {table_name} (
                 Red_luck_out CHAR(40) NOT NULL, 
                 Gift_out CHAR(40) NOT NULL,
                 Number_people CHAR(20) NOT NULL,  
                 Number_gift CHAR(40) NOT NULL,
                 Diamond_total CHAR(40) NOT NULL,
                 RMB_in CHAR(40) NOT NULL,
                 RMB_balance CHAR(40) NOT NULL,
                 Box_diamond_total CHAR(40) NOT NULL,
                 Box_rmb_back CHAR(40) NOT NULL,
                 Total_rmb_balance CHAR(40) NOT NULL,
                 pry_key int(40) primary key NOT NULL)""".format(table_name=table_name)
        cursor.execute(sql)
        print("CREATE BALANCE TABLE OK")
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    db.close()


# 查询数据库，表中无数据则插入，有数据则更新
def update_data_balance_table(red_luck_out: str, gift_out: str, number_people: str, number_gift: str,
                              diamond_total: str, rmb_in: str, rmb_balance: str, box_diamond_total: str,
                              box_rmb_back: str, total_rmb_balance: str, pry_key: int):
    db = pymysql.connect(host='localhost', user='root', password='wl19871005', port=3306, db='qedj')
    cursor = db.cursor()
    table_name = 'Balance_table_' + time_str
    data = {
        'Red_luck_out': red_luck_out,
        'Gift_out': gift_out,
        'Number_people': number_people,
        'Number_gift': number_gift,
        'Diamond_total': diamond_total,
        'RMB_in': rmb_in,
        'RMB_balance': rmb_balance,
        'Box_diamond_total': box_diamond_total,
        'Box_rmb_back': box_rmb_back,
        'Total_rmb_balance': total_rmb_balance,
        'pry_key': pry_key
    }
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table_name, keys=keys,
                                                                                         values=values)
    update = ','.join([" {key} = %s".format(key=key) for key in data])
    sql += update
    try:
        cursor.execute(sql, tuple(data.values()) * 2)
        # print('Update balance table Successful')
        db.commit()
    except Exception as e:
        print(e)
        print('Failed')
        db.rollback()
    cursor.close()
    db.close()


# 该方法建立一个表来贮存玩家在砸盒子中砸到的礼物
def create_gift_table():
    db = pymysql.connect(host='localhost', user='root', password='wl19871005', port=3306, db='qedj')
    cursor = db.cursor()
    table_name = 'Gift_table_info_' + time_str
    try:
        sql = """CREATE TABLE {table_name} (
                 Gift_number INT primary key NOT NULL , 
                 Time CHAR(40) NOT NULL,
                 User_name CHAR(40) NOT NULL,  
                 Prize_name CHAR(40) NOT NULL,
                 Gift_account CHAR(20) NOT NULL,
                 Diamond_value CHAR(40) NOT NULL,
                 Buff CHAR(40) NOT NULL)""".format(table_name=table_name)
        cursor.execute(sql)
        print("CREATE GIFT TABLE OK")
        db.close()
    except Exception as e:
        print(e)


# 砸到的礼物信息全部为插入
def insert_gift_info(gift_number: int, time: str, user_name: str, prize_name: str, gift_account: str,
                     diamond_value: str, buff: str):
    db = pymysql.connect(host='localhost', user='root', password='wl19871005', port=3306, db='qedj')
    cursor = db.cursor()
    table_name = 'Gift_table_info_' + time_str
    data = {
        'Gift_number': gift_number,
        'Time': time,
        'User_name': user_name,
        'Prize_name': prize_name,
        'Gift_account': gift_account,
        'Diamond_value': diamond_value,
        'Buff': buff
    }
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table_name, keys=keys, values=values)
    try:
        cursor.execute(sql, tuple(data.values()))
        print('Gift Info Insert Successful')
        db.commit()
    except Exception as e:
        print(e)
        print('Failed')
        db.rollback()
    cursor.close()
    db.close()


# 该方法是建立表统计每轮玩家砸出的礼物
def create_every_around():
    db = pymysql.connect(host='localhost', user='root', password='wl19871005', port=3306, db='qedj')
    cursor = db.cursor()
    global around_number
    table_name = 'Every_around_info_' + time_str + "_around" + str(around_number)
    try:
        sql = """CREATE TABLE {table_name} (
                 User_name CHAR(40) primary key NOT NULL , 
                 Mdx_number int NOT NULL,
                 Mtl_number int NOT NULL,  
                 Rqq_number int NOT NULL,
                 Xjzj_number int NOT NULL,
                 Pdk_number int NOT NULL)""".format(table_name=table_name)
        cursor.execute(sql)
        print("CREATE " + table_name + " OK")
        db.close()
        around_number += 1
    except Exception as e:
        around_number += 1
        print(e)


# 插入或者更新每轮礼物中的数据
def update_every_around_info(user_name: str, mdx_number: int, mtl_number: int, rqq_number: int, xjzj_number: int,
                             pdk_number: int):
    db = pymysql.connect(host='localhost', user='root', password='wl19871005', port=3306, db='qedj')
    print('sssssssssssssssssssssssss')
    cursor = db.cursor()
    table_name = 'Every_around_info_' + time_str + "_around" + str(around_number - 1)
    data = {
        'User_name': user_name,
        'Mdx_number': mdx_number,
        'Mtl_number': mtl_number,
        'Rqq_number': rqq_number,
        'Xjzj_number': xjzj_number,
        'Pdk_number': pdk_number,
    }
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table_name, keys=keys,
                                                                                         values=values)
    update = ','.join([" {key} = %s".format(key=key) for key in data])
    sql += update
    try:
        cursor.execute(sql, tuple(data.values()) * 2)
        print('Update ' + table_name + ' Successful')
        db.commit()
    except Exception as e:
        print(e)
        print('Failed')
        db.rollback()
    cursor.close()
    db.close()


# 创建表来贮存所有玩家砸出的礼物信息
def create_total_around():
    db = pymysql.connect(host='localhost', user='root', password='wl19871005', port=3306, db='qedj')
    cursor = db.cursor()
    table_name = 'Total_around_info_' + time_str
    try:
        sql = """CREATE TABLE {table_name} (
                 User_name CHAR(40) primary key NOT NULL , 
                 Mdx_number int NOT NULL,
                 Mtl_number int NOT NULL,  
                 Rqq_number int NOT NULL,
                 Xjzj_number int NOT NULL,
                 Pdk_number int NOT NULL)""".format(table_name=table_name)
        cursor.execute(sql)
        print("CREATE TOTAL AROUND TABLE OK")
        db.close()
    except Exception as e:
        print(e)


# 插入或者更新所有玩家表数据
def update_total_around_info(user_name: str, mdx_number: int, mtl_number: int, rqq_number: int, xjzj_number: int,
                             pdk_number: int):
    db = pymysql.connect(host='localhost', user='root', password='wl19871005', port=3306, db='qedj')
    cursor = db.cursor()
    table_name = 'Total_around_info_' + time_str
    data = {
        'User_name': user_name,
        'Mdx_number': mdx_number,
        'Mtl_number': mtl_number,
        'Rqq_number': rqq_number,
        'Xjzj_number': xjzj_number,
        'Pdk_number': pdk_number,
    }
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table_name, keys=keys,
                                                                                         values=values)
    update = ','.join([" {key} = %s".format(key=key) for key in data])
    sql += update
    try:
        cursor.execute(sql, tuple(data.values()) * 2)
        # print('Successful')
        db.commit()
    except Exception as e:
        print(e)
        print('Failed')
        db.rollback()
    cursor.close()
    db.close()


def del_table():
    db = pymysql.connect(host='localhost', user='root', password='wl19871005', port=3306, db='qedj')
    cursor = db.cursor()
    sql = 'DROP TABLE every_around_info_20200814_around1'

    try:
        cursor.execute(sql)
        print("Delete TABLE OK")
        db.commit()
        db.close()
    except Exception as e:
        print(e)

# del_table()
