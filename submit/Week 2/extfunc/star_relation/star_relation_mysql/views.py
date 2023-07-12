from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
import django.core.handlers.wsgi
from django.contrib import messages
import MySQLdb
import MySQLdb.cursors as cors
import time
import pandas as pd
import os
import random
import json
# Create your views here.

# 处理重定向
def redirect(request):
    return HttpResponseRedirect('login')

# 处理用户登录
def login(request,method=['GET','POST']):
    assert isinstance(request,django.core.handlers.wsgi.WSGIRequest)
    if request.method == 'GET':
        name = request.COOKIES.get('name') or ''
        password = request.COOKIES.get('password') or ''
        if name == '':
            return render(request,'star_relation_mysql/login.html')
        db = None
        try:
            db = MySQLdb.connect("localhost",name,password,charset='utf8')
            return HttpResponseRedirect('/mysql/new')
        except:
            messages.error(request,'用户名或密码错误')
            return render(request,'star_relation_mysql/login.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        # print(name,password)
        try:
            db = MySQLdb.connect("localhost",name,password,charset='utf8')
            resp = HttpResponseRedirect('/mysql/new')
            resp.set_cookie('name',name)
            resp.set_cookie('password',password)
            return resp
        except:
            messages.error(request,'用户名或密码错误')
            return render(request,'star_relation_mysql/login.html')

# 处理创建数据库和表
def index(request,method=['GET']):
    # print(os.path.join(settings.STATIC_URL,'data/star_infos.csv'))
    # print(os.path.abspath(os.path.join(settings.STATIC_URL,'data/star_infos.csv')))
    if request.GET.get('newdb'):
        db = None
        name = request.COOKIES.get('name')
        password = request.COOKIES.get('password')
        try:
            db = MySQLdb.connect("localhost",name,password,charset='utf8')
        except:
            return HttpResponseRedirect('/mysql/login')
        cursor = db.cursor()
        #创建数据库
        cursor.execute("drop database if exists star_relation;")
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
        cursor.execute("drop table if exists 明星;")
        sql_create_star = """create table if not exists 明星(
                                id int not null primary key auto_increment,
                                name varchar(255),
                                image varchar(255),
                                homeland varchar(255), 
                                weight varchar(255),
                                birth date,
                                baike_url varchar(255)
                            );"""
        cursor.execute(sql_create_star)
        # 写入明星数据
        pwd=os.path.dirname(__file__)
        stars = pd.read_csv(pwd + '/data/star_infos.csv')
        for _,curr_star in stars.iterrows():
            if is_valid_date(curr_star['birth']):
                sql_insert_star = "insert into 明星(name, image, homeland, weight, birth, baike_url) VALUE ('{}','{}','{}','{}','{}','{}')".format(curr_star['name'],curr_star['image'],curr_star['homeland'],curr_star['weight'],curr_star['birth'],curr_star['baike_url'])
            else:
                sql_insert_star = "insert into 明星(name, image, homeland, weight, baike_url) VALUE ('{}','{}','{}','{}','{}')".format(curr_star['name'],curr_star['image'],curr_star['homeland'],curr_star['weight'],curr_star['baike_url'])
            # print(sql_insert_star)
            cursor.execute(sql_insert_star)

        # 创建不同关系表
        star_relations = pd.read_csv(pwd + '/data/all_star_relations.csv')
        relations = star_relations['relation'].unique()
        for relation in relations:
            cursor.execute("drop table if exists {};".format(relation))
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
        messages.success(request,'创建数据库成功！')
        return HttpResponseRedirect('/mysql/new')
    return render(request,'star_relation_mysql/new.html')

# 处理修改数据库,响应ajax发送的post请求，响应submit提交的post请求
def modify(request,method=['GET','POST']):
    db = None
    name = request.COOKIES.get('name')
    password = request.COOKIES.get('password')
    try:
        db = MySQLdb.connect("localhost",name,password,charset='utf8')
    except:
        return HttpResponseRedirect('/mysql/login')
    cursor = db.cursor()
    cursor.execute("use star_relation")
    cursor.execute("show tables")
    tables = cursor.fetchall()
    relations = []
    review_text = ''
    for table in tables:
        if str(table[0]) != '明星':
            relations.append(table[0])
    if request.method == 'GET':
        return render(request,'star_relation_mysql/modify.html',{'relations':relations})
    # 处理POST请求
    if request.method == 'POST':
        # print(request.POST)
        resp = request.POST
        values = dict(resp)
        context = {
            'relations':relations,
            'review_text':review_text,
            'is_add':values['act'][0] == 'add',
            'is_star':values['table'][0] == 'star',
        }
        context.update({key.replace('-','_'):value[0] for key,value in values.items()})
        context['can_submit'] = False
        # print(context)
        sql_execute = ''
        # 处理添加明星
        if resp['act'] == 'add' and resp['table'] == 'star':
            # print('进入添加明星')
            cursor.execute("select * from 明星 where name='{}'".format(context['star_name']))
            if cursor.fetchone():
                review_text = '数据库中已存在该明星，无法添加'
            elif context['star_name'] == '':
                review_text = '请输入明星姓名'
            else:
                review_text = '向表`明星`中添加明星，姓名：{},籍贯：{},生日：{},体重：{}'.format(resp['star-name'],resp['star-homeland'],resp['star-birth'],resp['star-weight'])
                context['can_submit'] = True
                if resp['star-birth']:
                    sql_execute = 'insert into 明星(name,homeland,weight,birth) value ("{}","{}","{}","{}")'.format(resp['star-name'],resp['star-homeland'],resp['star-weight'],resp['star-birth'])
                else:
                    sql_execute = 'insert into 明星(name,homeland,weight) value ("{}","{}","{}")'.format(resp['star-name'],resp['star-homeland'],resp['star-weight'])
        # 处理删除明星
        if resp['act'] == 'delete' and resp['table'] == 'star':
            cursor.execute("select * from 明星 where name='{}'".format(context['del_star_name']))
            if not cursor.fetchone():
                review_text = '数据库中没有该明星'
            else:
                review_text = '从表`明星`中删除明星：{}'.format(context['del_star_name'])
                sql_execute = "delete from 明星 where name='{}'".format(context['del_star_name'])
                context['can_submit'] = True
        # 处理添加关系
        if resp['act'] == 'add' and resp['table'] == 'relation':
            add_relation = context['add_relation']
            star1 = context['subject']
            star2 = context['object']
            cursor.execute("select * from 明星 where name='{}'".format(star1))
            fetch1 = cursor.fetchone()
            cursor.execute("select * from 明星 where name='{}'".format(star2))
            fetch2 = cursor.fetchone()
            if fetch1 and fetch2:
                review_text = '向表`{}`中添加关系：({})-[{}]->({})'.format(add_relation,star1,add_relation,star2)
                sql_execute = "insert into {}(star_subject_id,star_object_id) value('{}','{}')".format(add_relation,fetch1[0],fetch2[0])
                context['can_submit'] = True
            else:
                review_text = '无法添加，因为数据库中{}明星1，{}明星2'.format('有' if fetch1 else '没有','有' if fetch2 else '没有')
        # 处理删除关系
        if resp['act'] == 'delete' and resp['table'] == 'relation':
            del_relation = context['del_relation']
            star1 = context['del_subject']
            star2 = context['del_object']
            cursor.execute('select * from 明星 a,{} b,明星 c where a.id=b.star_subject_id and b.star_object_id = c.id and a.name="{}" and c.name="{}"'.format(del_relation,star1,star2))
            if not cursor.fetchall():
                review_text = '无法删除，因为数据库中没有该关系'
            else:
                review_text = '从表`{}`中删除关系：({})-[{}]->({})'.format(del_relation,star1,del_relation,star2)
                sql_execute = "delete from {} where star_subject_id in (select id from 明星 where name='{}') and star_object_id in (select id from 明星 where name='{}');".format(del_relation,star1,star2)
                context['can_submit'] = True
        # 处理提交请求
        if 'commit' in context:
            try:
                cursor.execute(sql_execute)
                db.commit()
                messages.success(request,'执行操作：{}，成功'.format(review_text))
                return HttpResponseRedirect('/mysql/modify')
            except:
                messages.success(request,'执行失败')
                return HttpResponseRedirect('/mysql/modify')
        context['review_text'] = review_text
        ret = {
            'review_text':review_text,
            'can_submit':context['can_submit'],
        }
        return HttpResponse(json.dumps(ret))

# 处理查询数据库
def query(request,method=['GET','POST']):
    sel = []
    db = None
    name = request.COOKIES.get('name')
    password = request.COOKIES.get('password')
    # print(name,password)
    try:
        db = MySQLdb.connect("localhost",name,password,charset='utf8')
    except:
        return HttpResponseRedirect('/mysql/login')
    cursor = db.cursor()
    cursor.execute("use star_relation")
    cursor.execute("show tables")
    tables = cursor.fetchall()
    relations = []
    for table in tables:
        if str(table[0]) != '明星':
            relations.append(table[0])
    cursor.execute("select * from 明星 order by name")
    stars = cursor.fetchall()
    all_star = {}
    for s in stars:
        star_id = s[0]
        star_info = {
            'id':s[0],
            'name':s[1],

            'des' : "籍贯：{}<br/>体重：{}<br/>出生日期：{}".format(s[3],s[4],s[5]),
        }
        all_star.update({star_id:star_info})
    star_nodes = {}
    star_relations = []
    if request.method == 'POST' and request.POST.getlist('sel'):
        sel = request.POST.getlist('sel')
        # print(sel)
        sel = list(int(i) for i in sel)
        star_nodes = {key:all_star[key] for key in sel}
        sel_str = str(sel)[1:-1]
        for relation in relations:
            cursor.execute("select * from {} where star_subject_id in ({})".format(relation,sel_str))
            all_path = cursor.fetchall()
            for path in all_path:
                star_nodes[path[2]] = all_star[path[2]]
            cursor.execute("select * from {} where star_object_id in ({})".format(relation,sel_str))
            all_path = cursor.fetchall()
            for path in all_path:
                star_nodes[path[1]] = all_star[path[1]]
        # print(star_nodes)
        node_list = list(star_nodes.keys())
        # print(node_list)
        node_str = str(node_list)[1:-1]
        for relation in relations:
            cursor.execute("select * from {} where star_subject_id in ({}) and star_object_id in ({})".format(relation,node_str,node_str))
            all_path = cursor.fetchall()
            for path in all_path:
                temp = {
                    'source':all_star[path[1]]['name'],
                    'target':all_star[path[2]]['name'],
                    'name':relation,
                }
                star_relations.append(temp)
    return render(request,'star_relation_mysql/query.html',{'all_star':list(all_star.values()),'sel':sel,'nodes':json.dumps(list(star_nodes.values())),'lines':json.dumps(star_relations)})
