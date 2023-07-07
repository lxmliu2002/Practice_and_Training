```mysql
# 书库
create table 书库
(
    ISBN varchar NOT NULL PRIMARY KEY,
    书名 varchar NOT NULL,
    作者 varchar NOT NULL,
    类别 varchar NOT NULL,
    出版社 varchar NOT NULL,
    出版时间 date NOT NULL,
    价格 varchar NOT NULL,
    库存数量 int NOT NULL
);
# 书店
create table 书店
(
    书店ID int NOT NULL PRIMARY KEY,
    书店名字 varchar NOT NULL,
    书店地址 varchar NOT NULL,
    书店联系电话 varchar,
    书店店长 varchar NOT NULL
);
# 顾客
create table 顾客
(
    顾客ID int NOT NULL PRIMARY KEY,
    姓名 varchar NOT NULL,
    电话 varchar NOT NULL,
    地址 varchar,
    积分 int NOT NULL DEFAULT 0
);
# 书店员工
create table 书店员工
(
    员工ID int NOT NULL PRIMARY KEY,
    员工姓名 varchar NOT NULL,
    员工电话 varchar NOT NULL,
    入职时间 date NOT NULL,
    员工性别 tinyint(1) NOT NULL DEFAULT 0， # 0表示男
    员工住址 varchar NOT NULL,
    工资 float NOT NULL DEFAULT 0
);
# 订单
create table 订单
(
    订单号 int NOT NULL PRIMARY KEY,
    顾客ID int NOT NULL REFERENCES 顾客(顾客ID)，
    日期 date NOT NULL,
    收银员ID int NOT NULL REFERENCES 书店员工(员工ID) DEFAULT 0, # 0表示自助收银
    金额 float NOT NULL DEFAULT 0,
    自提or外送 tinyint(1) NOT NULL DEFAULT 0 # 0表示自提
);
# 外送
create table 外送
(
    订单号 int NOT NULL PRIMARY KEY REFERENCES 订单(订单号),
    送货员ID int NOT NULL REFERENCES 书店员工(员工ID),
    期望送达时间 date NOT NULL,
    收货人姓名 varchar NOT NULL,
    收货人电话 varchar NOT NULL,
    收货地址 varchar NOT NULL
);
# 订单明细
create table 订单明细
(
    订单号 int NOT NULL PRIMARY KEY REFERENCES 订单(订单号),
    书名 varchar NOT NULL REFERENCES 书库(书名),
    ISBN varchar NOT NULL REFERENCES 书库(ISBN),
    数量 int NOT NULL DEFAULT 1,
    单价 float NOT NULL DEFAULT 0 REFERENCES 书库(价格),
    折扣 float NOT NULL DEFAULT 0,
    实际价格 float NOT NULL
);
```

