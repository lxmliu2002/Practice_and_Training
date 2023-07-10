-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: myweb
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `learn_author`
--

DROP TABLE IF EXISTS `learn_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `learn_author` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `gender` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `learn_author`
--

LOCK TABLES `learn_author` WRITE;
/*!40000 ALTER TABLE `learn_author` DISABLE KEYS */;
INSERT INTO `learn_author` VALUES (1,'卡卡西',1),(2,'娜美',0),(3,'宋神宗',NULL);
/*!40000 ALTER TABLE `learn_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `learn_authordetail`
--

DROP TABLE IF EXISTS `learn_authordetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `learn_authordetail` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `birth_date` date DEFAULT NULL,
  `address` varchar(64) NOT NULL,
  `profile` longtext NOT NULL,
  `author_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `author_id` (`author_id`),
  CONSTRAINT `learn_authordetail_author_id_2f01db5d_fk_learn_author_id` FOREIGN KEY (`author_id`) REFERENCES `learn_author` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `learn_authordetail`
--

LOCK TABLES `learn_authordetail` WRITE;
/*!40000 ALTER TABLE `learn_authordetail` DISABLE KEYS */;
INSERT INTO `learn_authordetail` VALUES (1,'1520-09-15','火之国木叶村可爱大道202号','暗部队长，第七班老师，六代火影，五五开绝技拥有者',1),(2,'1640-07-03','东海可可亚西村幸福大街007号','聪明又机灵，爱好金钱和橘子，精通航海术和气象学，会武术',2),(3,'1048-05-25','濮安懿王宫邸睦亲宅18号','北宋皇帝，王安石变法支持者，击败安南，元丰改制，忧郁而逝',3);
/*!40000 ALTER TABLE `learn_authordetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `learn_course`
--

DROP TABLE IF EXISTS `learn_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `learn_course` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `pub_date` date NOT NULL,
  `stu_number` int NOT NULL,
  `author_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `learn_course_author_id_8000d995_fk_learn_author_id` (`author_id`),
  CONSTRAINT `learn_course_author_id_8000d995_fk_learn_author_id` FOREIGN KEY (`author_id`) REFERENCES `learn_author` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `learn_course`
--

LOCK TABLES `learn_course` WRITE;
/*!40000 ALTER TABLE `learn_course` DISABLE KEYS */;
INSERT INTO `learn_course` VALUES (1,'Linux 基础教程','2011-01-12',123,1),(2,'Git 与 Github 入门实践','2018-12-22',678,1),(3,'Python 异步编程','2019-04-03',59,2),(4,'Julia 简明教程','2019-10-12',80,2),(5,'Django 入门与实践','2001-10-12',300,2),(6,'C++ 实现简易 Docker 容器','2013-03-24',957,3);
/*!40000 ALTER TABLE `learn_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `learn_tag`
--

DROP TABLE IF EXISTS `learn_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `learn_tag` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `learn_tag`
--

LOCK TABLES `learn_tag` WRITE;
/*!40000 ALTER TABLE `learn_tag` DISABLE KEYS */;
INSERT INTO `learn_tag` VALUES (1,'Python'),(2,'Linux'),(3,'Web'),(4,'网络安全'),(5,'C++'),(6,'数据库'),(7,'Julia'),(8,'Git');
/*!40000 ALTER TABLE `learn_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `learn_tag_course`
--

DROP TABLE IF EXISTS `learn_tag_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `learn_tag_course` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tag_id` bigint NOT NULL,
  `course_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `learn_tag_course_tag_id_course_id_75be407c_uniq` (`tag_id`,`course_id`),
  KEY `learn_tag_course_course_id_d811b787_fk_learn_course_id` (`course_id`),
  CONSTRAINT `learn_tag_course_course_id_d811b787_fk_learn_course_id` FOREIGN KEY (`course_id`) REFERENCES `learn_course` (`id`),
  CONSTRAINT `learn_tag_course_tag_id_2272f09e_fk_learn_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `learn_tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `learn_tag_course`
--

LOCK TABLES `learn_tag_course` WRITE;
/*!40000 ALTER TABLE `learn_tag_course` DISABLE KEYS */;
INSERT INTO `learn_tag_course` VALUES (5,2,1),(3,2,3),(6,8,2),(4,8,3);
/*!40000 ALTER TABLE `learn_tag_course` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-09  4:31:55
