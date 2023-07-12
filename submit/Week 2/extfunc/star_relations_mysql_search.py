import MySQLdb
import MySQLdb.cursors as cors


db = MySQLdb.connect("localhost","root","root",charset='utf8')
cursor = db.cursor()
cursor.execute("use star_relation")
star_name = input("请输入明星的姓名：")
cursor.execute("select id from 明星 where name='{}'".format(star_name))
star_id = cursor.fetchone()[0]
if not star_id:
    print("查无此人")
else:
    cursor.execute("show tables")
    tables = cursor.fetchall()
    relations = []
    all_star = set()
    all_star.add(star_id)
    # 查询所有的表，提取所有的关系
    for table in tables:
        if str(table[0]) != '明星':
            relations.append(table[0])
    star_nodes = []
    # 查询所有涉及到的明星
    for relation in relations:
        cursor.execute("select * from {} where star_subject_id={}".format(relation,star_id))
        all_path = cursor.fetchall()
        for path in all_path:
            all_star.add(path[2])
        cursor.execute("select * from {} where star_object_id={}".format(relation,star_id))
        all_path = cursor.fetchall()
        for path in all_path:
            all_star.add(path[1])
    # print(str(all_star)[1:-1])
    node_str = str(all_star)[1:-1]
    star_dict = {}
    # 查询明星姓名
    cursor.execute("select id,name from 明星 where id in ({})".format(node_str))
    stars = tables = cursor.fetchall()
    for star in stars:
        star_dict[star[0]] = star[1]
    # 查询所有关系
    print('存在以下关系：')
    for relation in relations:
        cursor.execute("select * from {} where star_subject_id in ({}) and star_object_id in ({})".format(relation,node_str,node_str))
        all_path = cursor.fetchall()
        for path in all_path:
            print("({})-[{}]->({})".format(star_dict[path[1]],relation,star_dict[path[2]]))
