-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.1.50-community


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema bookshop
--

CREATE DATABASE IF NOT EXISTS bookshop;
USE bookshop;

--
-- Definition of table `addresses`
--

DROP TABLE IF EXISTS `addresses`;
CREATE TABLE `addresses` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '地址表的主键, 代理主键, 整型, 自增. ',
  `address` varchar(100) DEFAULT NULL COMMENT '地址表地址字段',
  `customerId` int(10) unsigned DEFAULT NULL COMMENT '地址表的外键字段, 表述和客户表的关联关系.',
  PRIMARY KEY (`id`),
  KEY `FK_Customers_Addresses` (`customerId`),
  CONSTRAINT `FK_Customers_Addresses` FOREIGN KEY (`customerId`) REFERENCES `customers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='地址表, 和客户表是多对一的关联关系. ';

--
-- Dumping data for table `addresses`
--

/*!40000 ALTER TABLE `addresses` DISABLE KEYS */;
INSERT INTO `addresses` (`id`,`address`,`customerId`) VALUES 
 (1,'zhangsanAddress01',1),
 (2,'zhangsanAddress02',1),
 (3,'zhangsanAddress03',1);
/*!40000 ALTER TABLE `addresses` ENABLE KEYS */;


--
-- Definition of table `authors`
--

DROP TABLE IF EXISTS `authors`;
CREATE TABLE `authors` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '作者表的主键, 代理主键, 整型, 自增. ',
  `name` varchar(50) DEFAULT NULL COMMENT '作者表的作者名称字段. ',
  `gender` varchar(10) DEFAULT NULL COMMENT '作者表的性别字段. ',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COMMENT='作者表, 和图书表是多对多的关联关系. ';

--
-- Dumping data for table `authors`
--

/*!40000 ALTER TABLE `authors` DISABLE KEYS */;
INSERT INTO `authors` (`id`,`name`,`gender`) VALUES 
 (1,'authorA','male'),
 (2,'authorB','female'),
 (3,'authorC','male'),
 (4,'zhaoliu','male'),
 (5,'maqi','female'),
 (6,'wangba','male'),
 (7,'liujiu','male'),
 (8,'qianshi','male');
/*!40000 ALTER TABLE `authors` ENABLE KEYS */;


--
-- Definition of table `bookandauthor`
--

DROP TABLE IF EXISTS `bookandauthor`;
CREATE TABLE `bookandauthor` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '图书作者对照表的主键, 代理主键, 整型, 自增. ',
  `bookId` int(10) unsigned DEFAULT NULL COMMENT '图书作者对照表的图书表外键字段, 表示和图书表的多对一关联关系. ',
  `authorId` int(10) unsigned DEFAULT NULL COMMENT '图书作者对照表的作者表的外键字段, 表示和作者表的多对一的关联关系. ',
  PRIMARY KEY (`id`),
  KEY `fk_Books_BookAndAuthor` (`bookId`),
  KEY `fk_Authors_BookAndAuthor` (`authorId`),
  CONSTRAINT `fk_Authors_BookAndAuthor` FOREIGN KEY (`authorId`) REFERENCES `authors` (`id`),
  CONSTRAINT `fk_Books_BookAndAuthor` FOREIGN KEY (`bookId`) REFERENCES `books` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COMMENT='图书作者对照表, 表示图书和作者的多对多的关联关系. 是纯粹的关系表. ';

--
-- Dumping data for table `bookandauthor`
--

/*!40000 ALTER TABLE `bookandauthor` DISABLE KEYS */;
INSERT INTO `bookandauthor` (`id`,`bookId`,`authorId`) VALUES 
 (1,1,1),
 (2,1,2),
 (3,2,2),
 (4,2,3),
 (5,3,1),
 (6,3,2),
 (7,3,3);
/*!40000 ALTER TABLE `bookandauthor` ENABLE KEYS */;


--
-- Definition of table `bookandcategory`
--

DROP TABLE IF EXISTS `bookandcategory`;
CREATE TABLE `bookandcategory` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '图书类别对照表的主键, 代理主键, 整型, 自增. ',
  `bookId` int(10) unsigned DEFAULT NULL COMMENT '图书类别对照表的图书表外键字段, 表述和图书表的多对一的关联关系. ',
  `categoryId` int(10) unsigned DEFAULT NULL COMMENT '图书类别对照表的类别表外键字段, 表述和类别表的多对一的关联关系. ',
  PRIMARY KEY (`id`),
  KEY `FK_Book_BookAndCategory` (`bookId`),
  KEY `FK_Category_BookAndCategory` (`categoryId`),
  CONSTRAINT `FK_Book_BookAndCategory` FOREIGN KEY (`bookId`) REFERENCES `books` (`id`),
  CONSTRAINT `FK_Category_BookAndCategory` FOREIGN KEY (`categoryId`) REFERENCES `categories` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='图书和类别对照表, 表示图书和类别的多对多的关联关系, 是纯粹的关系表. ';

--
-- Dumping data for table `bookandcategory`
--

/*!40000 ALTER TABLE `bookandcategory` DISABLE KEYS */;
/*!40000 ALTER TABLE `bookandcategory` ENABLE KEYS */;


--
-- Definition of table `books`
--

DROP TABLE IF EXISTS `books`;
CREATE TABLE `books` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '图书表的主键, 代理主键, 整型, 自增. ',
  `name` varchar(50) DEFAULT NULL COMMENT '图书表书名字段',
  `isbn` varchar(30) DEFAULT NULL COMMENT '图书表isbn字段, 唯一, 需要添加唯一索引的约束.',
  `price` decimal(10,2) DEFAULT NULL COMMENT '图书表价格字段. ',
  `bookcover` varchar(50) DEFAULT NULL COMMENT '图书表图书封面字段, 主要保存图书封面图片的文件名.',
  `createtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '图书表创建时间字段, 时间戳类型, 缺省值为插入图书记录的当前时间. ',
  `updatetime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '图书表更新时间字段, 缺省值为插入数据的当前时间, 每次当前记录时, 自动更新为系统当前时间.',
  `pressId` int(10) unsigned NOT NULL COMMENT '图书表的外键字段, 表示和出版社的多对一的关联关系. ',
  `sellNum` int(10) unsigned NOT NULL COMMENT '图书销量',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_isbn` (`isbn`),
  KEY `fk_presses_books` (`pressId`),
  CONSTRAINT `fk_presses_books` FOREIGN KEY (`pressId`) REFERENCES `presses` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COMMENT='图书表, 系统的中心表. 和其他的几个表均有关联关系. ';

--
-- Dumping data for table `books`
--

/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` (`id`,`name`,`isbn`,`price`,`bookcover`,`createtime`,`updatetime`,`pressId`,`sellNum`) VALUES 
 (1,'bookA','bookAIsbn','1.10','1.jpg','2017-10-09 09:09:59','2017-05-04 21:00:18',3,6),
 (2,'bookB','bookBIsbn','2.20','2.jpg','2017-10-09 09:09:59','2017-05-04 21:00:24',3,5),
 (3,'bookC','bookCIsbn','3.30','3.jpg','2017-10-09 09:09:59','2017-05-04 21:00:32',1,4),
 (4,'book1','book1isbn','1.10','1495820724129.jpg','2017-10-09 09:09:59','2017-05-27 01:45:24',1,3),
 (5,'book2','book2isbn','2.20','1495821339051.jpg','2017-10-09 09:09:59','2017-05-27 01:55:39',1,2),
 (6,'book3','book3isbn','3.30','1495832535608.jpg','2017-10-09 09:10:00','2017-05-27 05:02:16',1,1);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;


--
-- Definition of table `categories`
--

DROP TABLE IF EXISTS `categories`;
CREATE TABLE `categories` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '类别表的主键, 代理主键, 整型, 自增. ',
  `name` varchar(50) DEFAULT NULL COMMENT '类别表类别名称字段. ',
  `parentId` int(10) unsigned DEFAULT NULL COMMENT '类别表和自身的关联的外键字段. 表示当前类别的父类的信息. ',
  PRIMARY KEY (`id`),
  KEY `fk_PraentCategory_ChildrenCategory` (`parentId`),
  CONSTRAINT `fk_PraentCategory_ChildrenCategory` FOREIGN KEY (`parentId`) REFERENCES `categories` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='类别表是和自身的自反关联, 即:自身和自身的关联. 其中parentId字段表示父类别在当前类别表中对应的id字段. ';

--
-- Dumping data for table `categories`
--

/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;


--
-- Definition of table `customers`
--

DROP TABLE IF EXISTS `customers`;
CREATE TABLE `customers` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '客户表的主键, 代理主键, 整型, 自增. ',
  `name` varchar(50) DEFAULT NULL COMMENT '客户姓名字段',
  `email` varchar(50) DEFAULT NULL COMMENT '客户表邮件字段, 唯一, 需要添加唯一索引的约束',
  `phone` varchar(20) DEFAULT NULL COMMENT '客户表电话字段, 唯一, 需要添加唯一索引的约束',
  `password` varchar(255) DEFAULT NULL COMMENT '客户表客户密码字段, 需要使用MD5进行数字签名. ',
  `age` int(11) DEFAULT NULL COMMENT '客户表年龄字段',
  `gender` varchar(10) DEFAULT NULL COMMENT '客户表性别字段',
  `salary` decimal(8,2) DEFAULT NULL COMMENT '客户表工资字段',
  `birthday` date DEFAULT NULL COMMENT '客户表生日字段',
  `regtime` timestamp NULL DEFAULT NULL COMMENT '客户表注册时间字段, 时间戳类型, 默认值为插入数据时的当前时间. ',
  `updatetime` timestamp NULL DEFAULT NULL,
  `passportId` int(10) unsigned DEFAULT NULL COMMENT '和Passport为一对一, Customers表中含有外键字段, 为主体表.',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_phone` (`phone`),
  UNIQUE KEY `idx_email` (`email`),
  UNIQUE KEY `idx_passportid` (`passportId`),
  CONSTRAINT `fk_Customer_Passport` FOREIGN KEY (`passportId`) REFERENCES `passports` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COMMENT='客户表, 和地址表是一对多的关联关系. ';

--
-- Dumping data for table `customers`
--

/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` (`id`,`name`,`email`,`phone`,`password`,`age`,`gender`,`salary`,`birthday`,`regtime`,`updatetime`,`passportId`) VALUES 
 (1,'zhangsan','zhangsan@bookshop.com','13900000001','zhangsan',20,'male','1.10','2016-12-01','2016-12-26 14:57:14','2017-05-21 23:29:44',1),
 (2,'lisi','lisi@bookshop.com','13900000002','lisi',30,'female','2.20','2016-12-02','2016-12-26 14:58:17','2017-05-21 23:30:09',3),
 (6,'wangwu','wangwu@bookshop.com','13900000006','wangwu',80,'男','6.60','2016-12-27','2016-12-27 15:56:56','2017-05-21 23:30:19',2);
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;


--
-- Definition of table `employees`
--

DROP TABLE IF EXISTS `employees`;
CREATE TABLE `employees` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '雇员表的主键, 代理主键, 整型, 自增. ',
  `name` varchar(255) DEFAULT NULL COMMENT '雇员表的姓名字段',
  `password` varchar(255) DEFAULT NULL COMMENT '雇员表的登录密码字段',
  `type` varchar(255) DEFAULT NULL COMMENT '雇员表的类型字段, 1表示管理员, 2表示普通员, 后期可以扩充. ',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='雇员表, 兼顾后台登录管理功能. ';

--
-- Dumping data for table `employees`
--

/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` (`id`,`name`,`password`,`type`) VALUES 
 (1,'tom','password','1'),
 (2,'jack','password','2');
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;


--
-- Definition of table `operatelogs`
--

DROP TABLE IF EXISTS `operatelogs`;
CREATE TABLE `operatelogs` (
  `id` varchar(50) NOT NULL COMMENT '使用Java UUID作为主键, String类型. ',
  `name` varchar(255) DEFAULT NULL COMMENT '本次操作用户名',
  `operateTime` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `operateDesc` varchar(255) DEFAULT NULL COMMENT '具体操作描述',
  `ipaddress` varchar(255) DEFAULT NULL COMMENT '本次操作来自的IP地址',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='记录操作日志的日志表. ';

--
-- Dumping data for table `operatelogs`
--

/*!40000 ALTER TABLE `operatelogs` DISABLE KEYS */;
/*!40000 ALTER TABLE `operatelogs` ENABLE KEYS */;


--
-- Definition of table `orderdetailses`
--

DROP TABLE IF EXISTS `orderdetailses`;
CREATE TABLE `orderdetailses` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '订单细节表的主键, 代理主键, 整型, 自增. ',
  `orderId` int(10) unsigned DEFAULT NULL COMMENT '订单细节表的订单外键字段, 表示和订单表的多对一的关联关系. 给出当前订单细节记录属于哪个订单的信息. ',
  `bookId` int(10) unsigned DEFAULT NULL COMMENT '订单细节表的图书外键字段, 表示和图书表的多对一的关联关系. 给出当前订单细节对应的图书信息. ',
  `price` double DEFAULT NULL COMMENT '订单细节表的订购图书的价格字段, 冗余存储, 以防止图书价格的变动. ',
  `num` int(10) unsigned DEFAULT NULL COMMENT '订单细节表图书购买数量字段. ',
  `subPrice` double DEFAULT NULL COMMENT '订单细节表的价格小计字段. ',
  PRIMARY KEY (`id`),
  KEY `FK_Orders_OrderDetailses` (`orderId`),
  KEY `FK_Books_OrderDetailses` (`bookId`),
  CONSTRAINT `FK_Books_OrderDetailses` FOREIGN KEY (`bookId`) REFERENCES `books` (`id`),
  CONSTRAINT `FK_Orders_OrderDetailses` FOREIGN KEY (`orderId`) REFERENCES `orders` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `orderdetailses`
--

/*!40000 ALTER TABLE `orderdetailses` DISABLE KEYS */;
INSERT INTO `orderdetailses` (`id`,`orderId`,`bookId`,`price`,`num`,`subPrice`) VALUES 
 (1,1,1,1.1,2,2.2),
 (2,1,2,2.2,1,2.2),
 (3,2,1,1.1,1,1.1),
 (4,2,2,2.2,1,2.2),
 (5,2,3,3.3,1,3.3);
/*!40000 ALTER TABLE `orderdetailses` ENABLE KEYS */;


--
-- Definition of table `orders`
--

DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '订单表的主键, 代理主键, 整型, 自增. ',
  `orderNum` varchar(20) DEFAULT NULL COMMENT '订单表的订单编号字段, 唯一, 需要添加唯一索引的约束. ',
  `orderDate` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '订单表订购日期字段, 缺省值为生成订单插入订单数据的当前时间. ',
  `totalPrice` double DEFAULT NULL COMMENT '订单表订单总价字段',
  `realPrice` double DEFAULT NULL COMMENT '订单表实际购买价格字段',
  `customerId` int(10) unsigned DEFAULT NULL COMMENT '订单表的客户外键字段, 表示和客户表达的多对一的关联关系. ',
  `makerId` int(10) unsigned DEFAULT NULL COMMENT '订单表的制单员外键字段, 表示和雇员表的多对一的关联关系. ',
  `payeeId` int(10) unsigned DEFAULT NULL COMMENT '订单表的收款人外键字段, 表示和雇员表的多对一的关联关系. ',
  `addressId` int(10) unsigned DEFAULT NULL COMMENT '订单表的收货地址外键字段, 表示和地址表的多对一的关联关系. ',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_orderNum` (`orderNum`),
  KEY `FK_Employees_Order_Maker` (`makerId`),
  KEY `FK_Employees_Orders_Payee` (`payeeId`),
  KEY `FK_Customers_Orders` (`customerId`),
  KEY `FK_Addresses_Orders` (`addressId`),
  CONSTRAINT `FK_Addresses_Orders` FOREIGN KEY (`addressId`) REFERENCES `addresses` (`id`),
  CONSTRAINT `FK_Customers_Orders` FOREIGN KEY (`customerId`) REFERENCES `customers` (`id`),
  CONSTRAINT `FK_Employees_Orders_Payee` FOREIGN KEY (`payeeId`) REFERENCES `employees` (`id`),
  CONSTRAINT `FK_Employees_Order_Maker` FOREIGN KEY (`makerId`) REFERENCES `employees` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `orders`
--

/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` (`id`,`orderNum`,`orderDate`,`totalPrice`,`realPrice`,`customerId`,`makerId`,`payeeId`,`addressId`) VALUES 
 (1,'orderNum001','2017-01-04 00:00:00',4.4,4.4,1,1,1,3),
 (2,'orderNum002','2017-01-04 00:00:00',6.6,6.6,1,1,1,1);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;


--
-- Definition of table `passports`
--

DROP TABLE IF EXISTS `passports`;
CREATE TABLE `passports` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '护照表的主键, 代理主键, 整型, 自增. ',
  `passportNum` varchar(20) DEFAULT NULL COMMENT '护照表的护照号字段, 唯一, 需要添加唯一索引的约束. ',
  `expire` int(11) DEFAULT NULL COMMENT '护照表过期时间字段. ',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_passportNum` (`passportNum`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `passports`
--

/*!40000 ALTER TABLE `passports` DISABLE KEYS */;
INSERT INTO `passports` (`id`,`passportNum`,`expire`) VALUES 
 (1,'zhangsanpassport',10),
 (2,'wangwupassport',30),
 (3,'lisipassport',20);
/*!40000 ALTER TABLE `passports` ENABLE KEYS */;


--
-- Definition of table `presses`
--

DROP TABLE IF EXISTS `presses`;
CREATE TABLE `presses` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '出版社表的主键, 代理主键, 整型, 自增.',
  `name` varchar(50) DEFAULT NULL COMMENT '出版社表出版社名称字段',
  `address` varchar(200) DEFAULT NULL COMMENT '出版社表出版社地址字段',
  `employeeNums` int(11) DEFAULT NULL COMMENT '出版社表出版社雇员数量字段',
  `createtime` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='出版社表, 和图书表是一对多的关联关系. ';

--
-- Dumping data for table `presses`
--

/*!40000 ALTER TABLE `presses` DISABLE KEYS */;
INSERT INTO `presses` (`id`,`name`,`address`,`employeeNums`,`createtime`) VALUES 
 (1,NULL,NULL,NULL,NULL),
 (3,'天津工业大学出版社','工大西门',10,'2016-12-29 10:44:22');
/*!40000 ALTER TABLE `presses` ENABLE KEYS */;


--
-- Definition of table `shoppingcarts`
--

DROP TABLE IF EXISTS `shoppingcarts`;
CREATE TABLE `shoppingcarts` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '购物车表的主键, 代理主键, 整型, 自增. ',
  `customerId` int(10) unsigned DEFAULT NULL COMMENT '购物车表的客户表外键字段, 表述和客户表的多对一的关联关系. ',
  `bookId` int(10) unsigned DEFAULT NULL COMMENT '购物车表的图书表外键字段, 表述和图书表的多对一的关联关系.',
  `num` int(10) unsigned DEFAULT NULL COMMENT '购物车表的图书购买数量字段. ',
  PRIMARY KEY (`id`),
  KEY `FK_Customers_Carts` (`customerId`),
  KEY `FK_Books_Cart` (`bookId`),
  CONSTRAINT `FK_Books_Cart` FOREIGN KEY (`bookId`) REFERENCES `books` (`id`),
  CONSTRAINT `FK_Customers_Carts` FOREIGN KEY (`customerId`) REFERENCES `customers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `shoppingcarts`
--

/*!40000 ALTER TABLE `shoppingcarts` DISABLE KEYS */;
/*!40000 ALTER TABLE `shoppingcarts` ENABLE KEYS */;


--
-- Definition of procedure `getBookName`
--

DROP PROCEDURE IF EXISTS `getBookName`;

DELIMITER $$

/*!50003 SET @TEMP_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `getBookName`(in Book_Id int, out Book_Name varchar(255))
begin 
	select name into Book_Name
	from Books 
	where id = Book_Id;
end $$
/*!50003 SET SESSION SQL_MODE=@TEMP_SQL_MODE */  $$

DELIMITER ;

--
-- Definition of procedure `QueryBooksAndPress`
--

DROP PROCEDURE IF EXISTS `QueryBooksAndPress`;

DELIMITER $$

/*!50003 SET @TEMP_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `QueryBooksAndPress`()
BEGIN
	#Routine body goes here...
	select * from Books;
	select * from Presses where id = 3;
END $$
/*!50003 SET SESSION SQL_MODE=@TEMP_SQL_MODE */  $$

DELIMITER ;

--
-- Definition of procedure `sp_add`
--

DROP PROCEDURE IF EXISTS `sp_add`;

DELIMITER $$

/*!50003 SET @TEMP_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_add`(in a int, in b int, out c int)
begin 
	set c = a + b;
end $$
/*!50003 SET SESSION SQL_MODE=@TEMP_SQL_MODE */  $$

DELIMITER ;



/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
