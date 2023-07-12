import pymysql
import pandas as pd
import time

db = pymysql.connect(host='localhost',user='root',passwd='root')
cursor = db.cursor()
#创建数据库
cursor.execute("create database if not exists star_relation;")
cursor.execute("use star_relation;")

def is_valid_date(strdate):
    '''判断是否是一个有效的日期字符串'''
    try:
        time.strptime(strdate, "%Y-%m-%d")
        return True
    except:
        return False

# 创建明星表
sql_create_star = """create table if not exists 明星(
                        id int not null primary key auto_increment,
                        name varchar(255),
                        image varchar(255),
                        homeland varchar(255) default null, 
                        weight varchar(255) default null,
                        birth date default null,
                        baike_url varchar(255)
                    );"""
cursor.execute(sql_create_star)
# 写入明星数据
stars = pd.read_csv('./data/data/star_infos_new2.csv')
for _,curr_star in stars.iterrows():
    if is_valid_date(curr_star['birth']):
        sql_insert_star = "insert into 明星(name, image, homeland, weight, birth, baike_url) VALUE ('{}','{}','{}','{}','{}','{}')".format(curr_star['name'],curr_star['image'],curr_star['homeland'],curr_star['weight'],curr_star['birth'],curr_star['baike_url'])
    else:
        sql_insert_star = "insert into 明星(name, image, homeland, weight, baike_url) VALUE ('{}','{}','{}','{}','{}')".format(curr_star['name'],curr_star['image'],curr_star['homeland'],curr_star['weight'],curr_star['baike_url'])
    # print(sql_insert_star)
    cursor.execute(sql_insert_star)

# 创建不同关系表
star_relations = pd.read_csv('./data/data/all_star_relations.csv')
relations = star_relations['relation'].unique()
relations
for relation in relations:
    sql_create_relation = """create table if not exists {}(
                                    id int not null primary key auto_increment,
                                    star_subject_id int references star(id),
                                    star_object_id int references star(id)
                                );""".format(relation)
    cursor.execute(sql_create_relation)
    curr_star_relations = star_relations.loc[star_relations['relation'] == relation]
    # 写入当前关系数据
    for _,curr_star_relation in curr_star_relations.iterrows():
        cursor.execute('select id from 明星 where name = "{}"'.format(curr_star_relation['subject']))
        star_subject_id = cursor.fetchone()[0]
        cursor.execute('select id from 明星 where name = "{}"'.format(curr_star_relation['object']))
        star_object_id = cursor.fetchone()[0]
        sql_insert_relation = 'insert into {}(star_subject_id,star_object_id) value ({},{})'.format(relation,str(star_subject_id),str(star_object_id))
        cursor.execute(sql_insert_relation)

db.commit()
db.close()
print('End================================')

