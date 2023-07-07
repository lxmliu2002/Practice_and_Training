/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50717
Source Host           : 127.0.0.1:3306
Source Database       : mybbs

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2017-09-20 05:53:34
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for bbs_forum
-- ----------------------------
DROP TABLE IF EXISTS `bbs_forum`;
CREATE TABLE `bbs_forum` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID标识',
  `parentId` int(10) unsigned DEFAULT NULL COMMENT '父级Id',
  `name` varchar(50) DEFAULT NULL COMMENT '版块名称',
  `sortOrder` int(11) DEFAULT NULL COMMENT '数字排序',
  `intro` varchar(200) DEFAULT NULL COMMENT '版块介绍',
  `rule` varchar(200) DEFAULT NULL COMMENT '版规',
  `topicCount` int(11) DEFAULT NULL COMMENT '主题总计数量',
  `replyCount` int(11) DEFAULT NULL COMMENT '回复帖子总计(不包含主题)',
  `depth` int(11) DEFAULT NULL COMMENT '分类级别，根分类级别为1',
  `lastTopicId` int(10) unsigned DEFAULT NULL COMMENT '最后发表回复贴子对应的主题ID，或是主题ID',
  `imgUrl` varchar(100) DEFAULT NULL COMMENT 'Logo图片路径',
  `createdBy` int(10) unsigned DEFAULT NULL COMMENT '创建者ID',
  `createdOn` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '创建者时间',
  PRIMARY KEY (`id`),
  KEY `Fk_Parent_Children` (`parentId`),
  KEY `Fk_Topic_Forum_LastTopic` (`lastTopicId`),
  KEY `Fk_User_Forum_Created` (`createdBy`),
  CONSTRAINT `Fk_Parent_Children` FOREIGN KEY (`parentId`) REFERENCES `bbs_forum` (`id`),
  CONSTRAINT `Fk_Topic_Forum_LastTopic` FOREIGN KEY (`lastTopicId`) REFERENCES `bbs_topic` (`id`),
  CONSTRAINT `Fk_User_Forum_Created` FOREIGN KEY (`createdBy`) REFERENCES `bbs_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='版块表';

-- ----------------------------
-- Records of bbs_forum
-- ----------------------------

-- ----------------------------
-- Table structure for bbs_forum_moderator
-- ----------------------------
DROP TABLE IF EXISTS `bbs_forum_moderator`;
CREATE TABLE `bbs_forum_moderator` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID标识',
  `forumId` int(10) unsigned DEFAULT NULL COMMENT '版块ID',
  `userId` int(10) unsigned DEFAULT NULL COMMENT '用户ID',
  PRIMARY KEY (`id`),
  KEY `Fk_Forum_ForumModerator` (`forumId`),
  KEY `Fk_User_ForumModerator` (`userId`),
  CONSTRAINT `Fk_Forum_ForumModerator` FOREIGN KEY (`forumId`) REFERENCES `bbs_forum` (`id`),
  CONSTRAINT `Fk_User_ForumModerator` FOREIGN KEY (`userId`) REFERENCES `bbs_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='版块版主表';

-- ----------------------------
-- Records of bbs_forum_moderator
-- ----------------------------

-- ----------------------------
-- Table structure for bbs_online
-- ----------------------------
DROP TABLE IF EXISTS `bbs_online`;
CREATE TABLE `bbs_online` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID标识',
  `sessionId` varchar(100) DEFAULT NULL COMMENT '用户SessionID, 唯一',
  `userId` int(10) unsigned DEFAULT NULL COMMENT '用户ID, 唯一',
  `loginTime` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '登陆时间',
  `lastActiveTime` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '最后活动时间',
  `ipAddress` varchar(100) DEFAULT NULL COMMENT '用户IP地址',
  `createdOn` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `Idx_SessionId` (`sessionId`),
  UNIQUE KEY `Idx_UserId` (`userId`),
  CONSTRAINT `Fk_User_Online` FOREIGN KEY (`userId`) REFERENCES `bbs_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='在线用户表';

-- ----------------------------
-- Records of bbs_online
-- ----------------------------

-- ----------------------------
-- Table structure for bbs_operatelog
-- ----------------------------
DROP TABLE IF EXISTS `bbs_operatelog`;
CREATE TABLE `bbs_operatelog` (
  `id` varchar(10) NOT NULL,
  `userId` int(10) unsigned DEFAULT NULL,
  `ipAddress` varchar(100) DEFAULT NULL,
  `operateDesc` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='操作日志表';

-- ----------------------------
-- Records of bbs_operatelog
-- ----------------------------

-- ----------------------------
-- Table structure for bbs_reply
-- ----------------------------
DROP TABLE IF EXISTS `bbs_reply`;
CREATE TABLE `bbs_reply` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID标识',
  `topicId` int(10) unsigned DEFAULT NULL COMMENT '主题Id',
  `title` varchar(100) DEFAULT NULL COMMENT '标题',
  `content` varchar(255) DEFAULT NULL COMMENT '回复内容',
  `userId` int(10) unsigned DEFAULT NULL COMMENT '回复用户Id',
  `modifiedOn` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '最后编辑时间',
  `createdOn` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  KEY `Fk_Topic_Reply` (`topicId`),
  KEY `Fk_User_Reply_Created` (`userId`),
  CONSTRAINT `Fk_Topic_Reply` FOREIGN KEY (`topicId`) REFERENCES `bbs_topic` (`id`),
  CONSTRAINT `Fk_User_Reply_Created` FOREIGN KEY (`userId`) REFERENCES `bbs_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='回帖表';

-- ----------------------------
-- Records of bbs_reply
-- ----------------------------

-- ----------------------------
-- Table structure for bbs_topic
-- ----------------------------
DROP TABLE IF EXISTS `bbs_topic`;
CREATE TABLE `bbs_topic` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID标识',
  `forumId` int(10) unsigned DEFAULT NULL COMMENT '版块分类Id',
  `title` varchar(100) DEFAULT NULL COMMENT '主帖标题',
  `content` varchar(255) DEFAULT NULL COMMENT '内容',
  `userId` int(10) unsigned DEFAULT NULL COMMENT '发帖用户Id',
  `hits` int(11) DEFAULT NULL COMMENT '访问总量,即点击数量',
  `replyCount` int(11) DEFAULT NULL COMMENT '回复总计',
  `modifiedBy` int(10) unsigned DEFAULT NULL COMMENT '最后编辑用户Id',
  `modifiedOn` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '最后编辑时间',
  `repliedBy` int(10) unsigned DEFAULT NULL COMMENT '最后回复用户Id',
  `repliedOn` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '最后回复时间',
  `isClose` bit(1) DEFAULT NULL COMMENT '是否关闭[关闭贴不给回复]',
  `imgUrl` varchar(100) DEFAULT NULL COMMENT '帖子展示图片',
  `createdOn` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  KEY `Fk_User_Topic_Created` (`userId`),
  KEY `Fk_User_Topic_Modified` (`modifiedBy`),
  KEY `Fk_Forum_Topic` (`forumId`),
  CONSTRAINT `Fk_Forum_Topic` FOREIGN KEY (`forumId`) REFERENCES `bbs_forum` (`id`),
  CONSTRAINT `Fk_User_Topic_Created` FOREIGN KEY (`userId`) REFERENCES `bbs_user` (`id`),
  CONSTRAINT `Fk_User_Topic_Modified` FOREIGN KEY (`modifiedBy`) REFERENCES `bbs_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='主题表';

-- ----------------------------
-- Records of bbs_topic
-- ----------------------------

-- ----------------------------
-- Table structure for bbs_user
-- ----------------------------
DROP TABLE IF EXISTS `bbs_user`;
CREATE TABLE `bbs_user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ID标识符',
  `userName` varchar(50) DEFAULT NULL COMMENT '唯一值, 用户名',
  `nickName` varchar(100) DEFAULT NULL COMMENT '用户用于显示的昵称',
  `password` varchar(20) DEFAULT NULL COMMENT '密码',
  `email` varchar(50) DEFAULT NULL COMMENT 'Email',
  `headUrl` varchar(100) DEFAULT NULL COMMENT '用户头像',
  `introduction` varchar(200) DEFAULT NULL COMMENT '自我介绍',
  `signature` varchar(200) DEFAULT NULL COMMENT '个人签名',
  `topicCount` int(10) unsigned DEFAULT NULL COMMENT '发帖数',
  `replyCount` int(10) unsigned DEFAULT NULL COMMENT '回复帖子数',
  `lastTopicId` int(10) unsigned DEFAULT NULL COMMENT '最后发帖ID',
  `lastReplyId` int(10) unsigned DEFAULT NULL COMMENT '最后回复帖子ID',
  `createdOn` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `Idx_UserName` (`userName`),
  KEY `Fk_User_Topic` (`lastTopicId`),
  KEY `Fk_User_Reply` (`lastReplyId`),
  CONSTRAINT `Fk_User_Reply` FOREIGN KEY (`lastReplyId`) REFERENCES `bbs_reply` (`id`),
  CONSTRAINT `Fk_User_Topic` FOREIGN KEY (`lastTopicId`) REFERENCES `bbs_topic` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';

-- ----------------------------
-- Records of bbs_user
-- ----------------------------
