/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50717
Source Host           : 127.0.0.1:3306
Source Database       : tinybbs

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2018-01-13 23:29:32
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for posts
-- ----------------------------
DROP TABLE IF EXISTS `posts`;
CREATE TABLE `posts` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `subject` varchar(255) DEFAULT NULL,
  `content` varchar(255) DEFAULT NULL,
  `userId` int(10) unsigned DEFAULT NULL,
  `sectionId` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of posts
-- ----------------------------
INSERT INTO `posts` VALUES ('1', 'LisiSubject01', '李四第一次发言内容', '2', '1');
INSERT INTO `posts` VALUES ('2', 'LisiSubject02', '李四第二次发言内容', '2', '2');
INSERT INTO `posts` VALUES ('3', 'ZhangsanSubject01', '张三第一次发言内容', '1', '1');

-- ----------------------------
-- Table structure for sections
-- ----------------------------
DROP TABLE IF EXISTS `sections`;
CREATE TABLE `sections` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sections
-- ----------------------------
INSERT INTO `sections` VALUES ('1', '计算机');
INSERT INTO `sections` VALUES ('2', '古诗词');

-- ----------------------------
-- Table structure for userandsection
-- ----------------------------
DROP TABLE IF EXISTS `userandsection`;
CREATE TABLE `userandsection` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `userId` int(10) unsigned DEFAULT NULL,
  `sectionId` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of userandsection
-- ----------------------------
INSERT INTO `userandsection` VALUES ('1', '1', '1');
INSERT INTO `userandsection` VALUES ('2', '1', '2');
INSERT INTO `userandsection` VALUES ('3', '2', '2');

-- ----------------------------
-- Table structure for userdetailses
-- ----------------------------
DROP TABLE IF EXISTS `userdetailses`;
CREATE TABLE `userdetailses` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `gender` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of userdetailses
-- ----------------------------
INSERT INTO `userdetailses` VALUES ('1', '男');
INSERT INTO `userdetailses` VALUES ('2', '女');

-- ----------------------------
-- Table structure for userpassports
-- ----------------------------
DROP TABLE IF EXISTS `userpassports`;
CREATE TABLE `userpassports` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `num` varchar(255) DEFAULT NULL,
  `userId` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of userpassports
-- ----------------------------
INSERT INTO `userpassports` VALUES ('1', 'lisinum', '2');
INSERT INTO `userpassports` VALUES ('2', 'zhangsannum', '1');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `usn` varchar(255) DEFAULT NULL,
  `loginName` varchar(255) DEFAULT NULL,
  `pwd` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES ('1', '张三', 'zhangsan', 'zhangsan');
INSERT INTO `users` VALUES ('2', '李四', 'lisi', 'lisi');
