-- MySQL dump 10.13  Distrib 5.6.35, for macos10.12 (x86_64)
--
-- Host: localhost    Database: food_db
-- ------------------------------------------------------
-- Server version	5.6.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `app_access_log`
--

DROP TABLE IF EXISTS `app_access_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_access_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` bigint(20) NOT NULL DEFAULT '0' COMMENT 'uid',
  `referer_url` varchar(255) NOT NULL DEFAULT '' COMMENT '当前访问的refer',
  `target_url` varchar(255) NOT NULL DEFAULT '' COMMENT '访问的url',
  `query_params` text NOT NULL COMMENT 'get和post参数',
  `ua` varchar(255) NOT NULL DEFAULT '' COMMENT '访问ua',
  `ip` varchar(32) NOT NULL DEFAULT '' COMMENT '访问ip',
  `note` varchar(1000) NOT NULL DEFAULT '' COMMENT 'json格式备注字段',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_uid` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=utf8mb4 COMMENT='用户访问记录表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_access_log`
--

LOCK TABLES `app_access_log` WRITE;
/*!40000 ALTER TABLE `app_access_log` DISABLE KEYS */;
INSERT INTO `app_access_log` VALUES (1,0,'','http://127.0.0.1:8900/','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-28 12:05:28'),(2,0,'','http://127.0.0.1:8900/user/login','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-28 12:05:28'),(3,0,'http://127.0.0.1:8900/user/login','http://127.0.0.1:8900/','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-28 12:05:54'),(4,0,'http://127.0.0.1:8900/user/login','http://127.0.0.1:8900/user/login','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-28 12:05:54'),(5,0,'http://127.0.0.1:8900/user/login','http://127.0.0.1:8900/user/login','{\"login_name\": \"54php.cn\", \"login_pwd\": \"123456\"}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-28 12:20:36'),(6,1,'http://127.0.0.1:8900/user/login','http://127.0.0.1:8900/','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-28 12:20:39'),(7,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/chart/dashboard','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-28 12:20:39'),(8,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/chart/finance','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-28 12:20:39'),(9,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/account/index','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-28 12:20:45'),(10,1,'http://127.0.0.1:8900/account/index','http://127.0.0.1:8900/food/index','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-28 12:20:51'),(11,1,'http://127.0.0.1:8900/food/index','http://127.0.0.1:8900/member/index','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-28 12:20:55'),(12,1,'http://127.0.0.1:8900/member/index','http://127.0.0.1:8900/finance/index','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-28 12:20:57'),(13,1,'http://127.0.0.1:8900/finance/index','http://127.0.0.1:8900/stat/index','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-28 12:20:58'),(14,1,'http://127.0.0.1:8900/stat/index','http://127.0.0.1:8900/chart/finance','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-28 12:20:59'),(15,1,'http://127.0.0.1:8900/stat/index','http://127.0.0.1:8900/','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-28 12:21:08'),(16,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/chart/dashboard','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-28 12:21:08'),(17,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/chart/finance','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-28 12:21:08'),(18,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/user/edit','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-28 12:21:16'),(19,1,'http://127.0.0.1:8900/user/edit','http://127.0.0.1:8900/user/reset-pwd','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-28 12:24:51'),(20,1,'','http://127.0.0.1:8900/','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 03:54:04'),(21,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/chart/dashboard','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 03:54:05'),(22,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/chart/finance','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 03:54:05'),(23,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/food/index','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 03:54:11'),(24,1,'http://127.0.0.1:8900/food/index','http://127.0.0.1:8900/food/set','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 03:54:24'),(25,1,'http://127.0.0.1:8900/food/set','http://127.0.0.1:8900/upload/ueditor?action=config&&noCache=1538193264822','{\"action\": \"config\", \"noCache\": \"1538193264822\"}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 03:54:25'),(26,1,'http://127.0.0.1:8900/food/set','http://127.0.0.1:8900/food/cat','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 03:55:04'),(27,1,'http://127.0.0.1:8900/food/cat','http://127.0.0.1:8900/food/cat-set','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 03:55:06'),(28,0,'','http://127.0.0.1:8900/','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 12:53:30'),(29,0,'','http://127.0.0.1:8900/user/login','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 12:53:30'),(30,0,'','http://127.0.0.1:8900/','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 12:53:30'),(31,0,'','http://127.0.0.1:8900/user/login','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 12:53:30'),(32,0,'http://127.0.0.1:8900/user/login','http://127.0.0.1:8900/user/login','{\"login_name\": \"admin\", \"login_pwd\": \"123456\"}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 12:53:37'),(33,1,'http://127.0.0.1:8900/user/login','http://127.0.0.1:8900/','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 12:53:38'),(34,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/chart/dashboard','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 12:53:38'),(35,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/chart/finance','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 12:53:38'),(36,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/food/index','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 12:53:41'),(37,1,'http://127.0.0.1:8900/food/index','http://127.0.0.1:8900/food/set','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 12:53:50'),(38,1,'http://127.0.0.1:8900/food/set','http://127.0.0.1:8900/upload/ueditor?action=config&&noCache=1538225630547','{\"action\": \"config\", \"noCache\": \"1538225630547\"}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 12:53:51'),(39,1,'','http://127.0.0.1:8900/food/set','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 12:54:22'),(40,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/food/index','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 12:56:02'),(41,1,'http://127.0.0.1:8900/food/index','http://127.0.0.1:8900/food/set','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 12:56:05'),(42,1,'http://127.0.0.1:8900/food/set','http://127.0.0.1:8900/upload/ueditor?action=config&&noCache=1538225764908','{\"action\": \"config\", \"noCache\": \"1538225764908\"}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 12:56:05'),(43,1,'http://127.0.0.1:8900/food/index','http://127.0.0.1:8900/food/set','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 12:56:49'),(44,1,'http://127.0.0.1:8900/food/set','http://127.0.0.1:8900/upload/ueditor?action=config&&noCache=1538225809511','{\"action\": \"config\", \"noCache\": \"1538225809511\"}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 12:56:50'),(45,1,'http://127.0.0.1:8900/food/index','http://127.0.0.1:8900/food/set','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 13:01:00'),(46,1,'http://127.0.0.1:8900/food/set','http://127.0.0.1:8900/upload/ueditor?action=config&&noCache=1538226060451','{\"action\": \"config\", \"noCache\": \"1538226060451\"}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 13:01:00'),(47,1,'http://127.0.0.1:8900/food/index','http://127.0.0.1:8900/food/set','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 13:03:40'),(48,1,'http://127.0.0.1:8900/food/set','http://127.0.0.1:8900/upload/ueditor?action=config&&noCache=1538226220007','{\"action\": \"config\", \"noCache\": \"1538226220007\"}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 13:03:40'),(49,1,'','http://127.0.0.1:8900/food/set','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 13:03:46'),(50,1,'http://127.0.0.1:8900/food/index','http://127.0.0.1:8900/food/set','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-09-29 13:28:38'),(51,1,'','http://127.0.0.1:8900/','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:27:02'),(52,1,'','http://127.0.0.1:8900/','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:27:03'),(53,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/chart/dashboard','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:27:04'),(54,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/chart/finance','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:27:04'),(55,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/stat/index','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:27:08'),(56,1,'http://127.0.0.1:8900/stat/index','http://127.0.0.1:8900/chart/finance','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:27:09'),(57,1,'http://127.0.0.1:8900/stat/index','http://127.0.0.1:8900/stat/food','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:27:14'),(58,1,'http://127.0.0.1:8900/stat/food','http://127.0.0.1:8900/stat/member','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:27:16'),(59,1,'http://127.0.0.1:8900/stat/member','http://127.0.0.1:8900/stat/share','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:27:21'),(60,1,'http://127.0.0.1:8900/stat/share','http://127.0.0.1:8900/chart/share','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:27:21'),(61,1,'http://127.0.0.1:8900/stat/share','http://127.0.0.1:8900/stat/index','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:27:23'),(62,1,'http://127.0.0.1:8900/stat/index','http://127.0.0.1:8900/chart/finance','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:27:23'),(63,1,'http://127.0.0.1:8900/stat/index','http://127.0.0.1:8900/stat/food','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:27:25'),(64,1,'http://127.0.0.1:8900/stat/food','http://127.0.0.1:8900/stat/member','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:27:45'),(65,1,'http://127.0.0.1:8900/stat/member','http://127.0.0.1:8900/stat/food','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:27:47'),(66,1,'http://127.0.0.1:8900/stat/food','http://127.0.0.1:8900/stat/index','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:27:48'),(67,1,'http://127.0.0.1:8900/stat/index','http://127.0.0.1:8900/chart/finance','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:27:48'),(68,1,'http://127.0.0.1:8900/stat/index','http://127.0.0.1:8900/finance/index','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:28:01'),(69,1,'http://127.0.0.1:8900/finance/index','http://127.0.0.1:8900/stat/index','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:28:02'),(70,1,'http://127.0.0.1:8900/stat/index','http://127.0.0.1:8900/chart/finance','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:28:03'),(71,1,'http://127.0.0.1:8900/stat/index','http://127.0.0.1:8900/','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:46:13'),(72,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/chart/dashboard','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:46:14'),(73,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/chart/finance','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 03:46:14'),(74,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/stat/index','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 04:00:47'),(75,1,'http://127.0.0.1:8900/stat/index','http://127.0.0.1:8900/chart/finance','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 04:00:47'),(76,1,'http://127.0.0.1:8900/stat/index','http://127.0.0.1:8900/stat/index','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 04:00:57'),(77,1,'http://127.0.0.1:8900/stat/index','http://127.0.0.1:8900/chart/finance','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 04:00:57'),(78,1,'http://127.0.0.1:8900/stat/index','http://127.0.0.1:8900/stat/index','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 04:09:42'),(79,1,'http://127.0.0.1:8900/stat/index','http://127.0.0.1:8900/chart/finance','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 04:09:42'),(80,1,'http://127.0.0.1:8900/stat/index','http://127.0.0.1:8900/','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 06:02:53'),(81,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/chart/dashboard','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 06:02:54'),(82,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/chart/finance','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 06:02:54'),(83,1,'http://127.0.0.1:8900/stat/index','http://127.0.0.1:8900/','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 06:03:28'),(84,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/chart/dashboard','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 06:03:29'),(85,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/chart/finance','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 06:03:29'),(86,0,'http://127.0.0.1:8900/','http://127.0.0.1:8900/member/index','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 08:41:48'),(87,0,'http://127.0.0.1:8900/','http://127.0.0.1:8900/user/login','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 08:41:48'),(88,0,'http://127.0.0.1:8900/user/login','http://127.0.0.1:8900/user/login','{\"login_name\": \"admin\", \"login_pwd\": \"123456\"}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 08:41:56'),(89,1,'http://127.0.0.1:8900/user/login','http://127.0.0.1:8900/','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 08:41:57'),(90,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/chart/dashboard','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 08:41:57'),(91,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/chart/finance','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 08:41:57'),(92,1,'http://127.0.0.1:8900/','http://127.0.0.1:8900/member/index','{}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 08:41:58'),(93,1,'http://127.0.0.1:8900/member/index','http://127.0.0.1:8900/member/index?status=0&mix_kw=&p=','{\"status\": \"0\", \"mix_kw\": \"\", \"p\": \"\"}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 08:42:40'),(94,1,'http://127.0.0.1:8900/member/index?status=0&mix_kw=&p=','http://127.0.0.1:8900/member/index?status=1&mix_kw=lao&p=','{\"status\": \"1\", \"mix_kw\": \"lao\", \"p\": \"\"}','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','127.0.0.1','','2018-10-01 08:42:52');
/*!40000 ALTER TABLE `app_access_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_error_log`
--

DROP TABLE IF EXISTS `app_error_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_error_log` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `referer_url` varchar(255) NOT NULL DEFAULT '' COMMENT '当前访问的refer',
  `target_url` varchar(255) NOT NULL DEFAULT '' COMMENT '访问的url',
  `query_params` text NOT NULL COMMENT 'get和post参数',
  `content` longtext NOT NULL COMMENT '日志内容',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='app错误日表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_error_log`
--

LOCK TABLES `app_error_log` WRITE;
/*!40000 ALTER TABLE `app_error_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_error_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `food`
--

DROP TABLE IF EXISTS `food`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `food` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `cat_id` int(11) NOT NULL DEFAULT '0' COMMENT '分类id',
  `name` varchar(100) NOT NULL DEFAULT '' COMMENT '书籍名称',
  `price` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '售卖金额',
  `main_image` varchar(100) NOT NULL DEFAULT '' COMMENT '主图',
  `summary` varchar(10000) NOT NULL DEFAULT '' COMMENT '描述',
  `stock` int(11) NOT NULL DEFAULT '0' COMMENT '库存量',
  `tags` varchar(200) NOT NULL DEFAULT '' COMMENT 'tag关键字，以","连接',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '状态 1：有效 0：无效',
  `month_count` int(11) NOT NULL DEFAULT '0' COMMENT '月销售数量',
  `total_count` int(11) NOT NULL DEFAULT '0' COMMENT '总销售量',
  `view_count` int(11) NOT NULL DEFAULT '0' COMMENT '总浏览次数',
  `comment_count` int(11) NOT NULL DEFAULT '0' COMMENT '总评论量',
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后插入时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COMMENT='食品表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food`
--

LOCK TABLES `food` WRITE;
/*!40000 ALTER TABLE `food` DISABLE KEYS */;
INSERT INTO `food` VALUES (4,1,'美食1',12.00,'20180930/6c69c506993e4153b208901f1685ed01.jpg','<p>集天地之精华而提炼出来的美食</p>',19,'超级好吃,不辣',1,0,0,0,0,'2018-09-30 05:51:43','2018-09-30 05:51:43'),(5,1,'美食2',13.01,'20180930/0ee7ee04acdc424ebad1e13fb4af1d7b.jpg','<p>集日月之精华而萃取的美食</p>',100,'绝味',1,0,0,0,0,'2018-09-30 12:25:32','2018-09-30 05:53:58'),(6,1,'美食3',14.07,'20180930/76bfda2b67794b68bd512f6d5d9f711a.jpg','<p>别盯着看，否则你会晕倒</p>',30,'还好',1,0,0,0,0,'2018-09-30 05:54:46','2018-09-30 05:54:46'),(7,1,'美食4',11.11,'20180930/d9d10f3a74594921addd80563d35d0d2.jpg','<p>味道美极了</p>',17,'味道美极了',1,0,0,0,0,'2018-09-30 13:03:53','2018-09-30 05:55:23'),(8,1,'美食5',10.09,'20180930/98320e7d7e9f474dad4ffb1dba0ae751.jpg','<p><img src=\"http://127.0.0.1:8080/static/upload/20181001/ef1e3a7721f14ad6b0a6abf14094eef8.jpeg\" width=\"220\" height=\"183\" style=\"width: 220px; height: 183px;\"/></p><p>看到了吗，新鲜牛排</p>',90,'美味',1,0,0,0,0,'2018-10-01 10:55:33','2018-09-30 05:56:04'),(9,2,'狮子头',15.00,'20181001/b520048f50604fd389215c61c24bb49f.jpeg','<p>我最爱的狮子头</p><p><img src=\"http://127.0.0.1:8080/static/upload/20181001/18d3fb3dbeea43d3a856ad727beef68f.jpeg\" width=\"358\" height=\"259\" style=\"width: 358px; height: 259px;\"/></p>',100,'美味',1,0,0,0,0,'2018-10-01 13:37:54','2018-10-01 13:37:54');
/*!40000 ALTER TABLE `food` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `food_cat`
--

DROP TABLE IF EXISTS `food_cat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `food_cat` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '' COMMENT '类别名称',
  `weight` tinyint(4) NOT NULL DEFAULT '1' COMMENT '权重',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '状态 1：有效 0：无效',
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_name` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COMMENT='食品分类';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food_cat`
--

LOCK TABLES `food_cat` WRITE;
/*!40000 ALTER TABLE `food_cat` DISABLE KEYS */;
INSERT INTO `food_cat` VALUES (1,'东北菜',5,1,'2018-09-29 11:29:37','2018-09-29 11:29:37'),(2,'淮扬菜',10,1,'2018-09-30 05:21:53','2018-09-30 05:21:53'),(3,'川菜',6,1,'2018-09-30 05:22:10','2018-09-30 05:22:10'),(4,'其他',12,1,'2018-09-30 05:22:35','2018-09-30 05:22:35');
/*!40000 ALTER TABLE `food_cat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `food_sale_change_log`
--

DROP TABLE IF EXISTS `food_sale_change_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `food_sale_change_log` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `food_id` int(11) NOT NULL DEFAULT '0' COMMENT '商品id',
  `quantity` int(11) NOT NULL DEFAULT '0' COMMENT '售卖数量',
  `price` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '售卖金额',
  `member_id` int(11) NOT NULL DEFAULT '0' COMMENT '会员id',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '售卖时间',
  PRIMARY KEY (`id`),
  KEY `idx_food_id_id` (`food_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COMMENT='商品销售情况';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food_sale_change_log`
--

LOCK TABLES `food_sale_change_log` WRITE;
/*!40000 ALTER TABLE `food_sale_change_log` DISABLE KEYS */;
INSERT INTO `food_sale_change_log` VALUES (1,7,1,11.11,2,'2018-10-01 02:42:12'),(2,7,1,11.11,2,'2018-10-01 02:48:36'),(3,4,1,12.00,2,'2018-10-01 02:48:36');
/*!40000 ALTER TABLE `food_sale_change_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `food_stock_change_log`
--

DROP TABLE IF EXISTS `food_stock_change_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `food_stock_change_log` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `food_id` int(11) NOT NULL COMMENT '商品id',
  `unit` int(11) NOT NULL DEFAULT '0' COMMENT '变更多少',
  `total_stock` int(11) NOT NULL DEFAULT '0' COMMENT '变更之后总量',
  `note` varchar(100) NOT NULL DEFAULT '' COMMENT '备注字段',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `idx_food_id` (`food_id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COMMENT='数据库存变更表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food_stock_change_log`
--

LOCK TABLES `food_stock_change_log` WRITE;
/*!40000 ALTER TABLE `food_stock_change_log` DISABLE KEYS */;
INSERT INTO `food_stock_change_log` VALUES (1,3,12,12,'后台修改','2018-09-30 13:11:08'),(2,4,20,20,'后台修改','2018-09-30 13:51:43'),(3,5,100,100,'后台修改','2018-09-30 13:53:58'),(4,6,30,30,'后台修改','2018-09-30 13:54:46'),(5,7,20,20,'后台修改','2018-09-30 13:55:23'),(6,8,90,90,'后台修改','2018-09-30 13:56:04'),(7,8,-1,89,'在线购买','2018-09-30 20:01:59'),(8,5,-1,99,'在线购买','2018-09-30 20:01:59'),(9,7,-1,19,'在线购买','2018-09-30 20:19:50'),(10,7,-2,17,'在线购买','2018-09-30 20:24:14'),(11,7,2,19,'订单取消','2018-09-30 20:25:27'),(12,7,1,20,'订单取消','2018-09-30 20:25:30'),(13,8,1,90,'订单取消','2018-09-30 20:25:32'),(14,5,1,100,'订单取消','2018-09-30 20:25:32'),(15,7,-1,19,'在线购买','2018-09-30 20:26:35'),(16,7,1,20,'订单取消','2018-09-30 21:03:53'),(17,7,-1,19,'在线购买','2018-09-30 21:04:23'),(18,4,-1,19,'在线购买','2018-09-30 21:04:23'),(19,7,-1,18,'在线购买','2018-09-30 22:07:06'),(20,7,-1,17,'在线购买','2018-09-30 23:11:24'),(21,8,0,90,'后台修改','2018-10-01 18:55:33'),(22,9,100,100,'后台修改','2018-10-01 21:37:54');
/*!40000 ALTER TABLE `food_stock_change_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `images`
--

DROP TABLE IF EXISTS `images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `images` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `file_key` varchar(60) NOT NULL DEFAULT '' COMMENT '文件名',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `images`
--

LOCK TABLES `images` WRITE;
/*!40000 ALTER TABLE `images` DISABLE KEYS */;
INSERT INTO `images` VALUES (25,'20180930/4d5d90d5c6ef449ca4672aea510c8b39.jpg','2018-09-30 05:45:34'),(26,'20180930/43e21f5d69d84c62849dea66cb32e2b2.jpg','2018-09-30 05:46:26'),(27,'20180930/298ffc8f4622425093c6c29bb7df394e.jpg','2018-09-30 05:47:36'),(28,'20180930/6c69c506993e4153b208901f1685ed01.jpg','2018-09-30 05:50:45'),(29,'20180930/0ee7ee04acdc424ebad1e13fb4af1d7b.jpg','2018-09-30 05:53:29'),(30,'20180930/76bfda2b67794b68bd512f6d5d9f711a.jpg','2018-09-30 05:54:17'),(31,'20180930/d9d10f3a74594921addd80563d35d0d2.jpg','2018-09-30 05:55:07'),(32,'20180930/98320e7d7e9f474dad4ffb1dba0ae751.jpg','2018-09-30 05:55:41'),(33,'20181001/26dad4f2a3944df984eb732421636130.jpeg','2018-10-01 09:49:39'),(34,'20181001/16850e1b527545bf8ea57c8809387e2c.jpeg','2018-10-01 09:51:30'),(35,'20181001/736eb9e354ab4f6d93b8e99dfe16dcf1.jpeg','2018-10-01 10:51:59'),(36,'20181001/ef1e3a7721f14ad6b0a6abf14094eef8.jpeg','2018-10-01 10:54:54'),(37,'20181001/34d6cbdb4989419fbc5e12c9754805b1.jpeg','2018-10-01 12:51:37'),(38,'20181001/957c0fd2e0744060ae9d1a78048f6494.jpeg','2018-10-01 13:11:02'),(39,'20181001/2ca2c91c56a04da4a6984b1c3f284dc9.jpeg','2018-10-01 13:12:14'),(40,'20181001/b520048f50604fd389215c61c24bb49f.jpeg','2018-10-01 13:37:15'),(41,'20181001/18d3fb3dbeea43d3a856ad727beef68f.jpeg','2018-10-01 13:37:33');
/*!40000 ALTER TABLE `images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `member` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `nickname` varchar(100) NOT NULL DEFAULT '' COMMENT '会员名',
  `mobile` varchar(11) NOT NULL DEFAULT '' COMMENT '会员手机号码',
  `sex` tinyint(1) NOT NULL DEFAULT '0' COMMENT '性别 1：男 2：女',
  `avatar` varchar(200) NOT NULL DEFAULT '' COMMENT '会员头像',
  `salt` varchar(32) NOT NULL DEFAULT '' COMMENT '随机salt',
  `reg_ip` varchar(100) NOT NULL DEFAULT '' COMMENT '注册ip',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '状态 1：有效 0：无效',
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COMMENT='会员表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'向右看','',1,'https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTIdzx7bG3cKItJCUmPWxYEdia9bgrzljsjBdZPlGKmemf5UQCvNPtnTtSrUhvuKR5gyjDKIApxEsOA/132','ikwEFpFJ6PXdsuYT','',1,'2018-09-29 08:53:22','2018-09-29 08:53:22'),(2,'向右看','',1,'https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTIdzx7bG3cKItJCUmPWxYEdia9bgrzljsjBdZPlGKmemf5UQCvNPtnTtSrUhvuKR5gyjDKIApxEsOA/132','aEEwkQtWkdjGsYm6','',1,'2018-09-30 08:37:30','2018-09-30 08:37:30');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member_address`
--

DROP TABLE IF EXISTS `member_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `member_address` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `member_id` int(11) NOT NULL DEFAULT '0' COMMENT '会员id',
  `nickname` varchar(20) NOT NULL DEFAULT '' COMMENT '收货人姓名',
  `mobile` varchar(11) NOT NULL DEFAULT '' COMMENT '收货人手机号码',
  `province_id` int(11) NOT NULL DEFAULT '0' COMMENT '省id',
  `province_str` varchar(50) NOT NULL DEFAULT '' COMMENT '省名称',
  `city_id` int(11) NOT NULL DEFAULT '0' COMMENT '城市id',
  `city_str` varchar(50) NOT NULL DEFAULT '' COMMENT '市名称',
  `area_id` int(11) NOT NULL DEFAULT '0' COMMENT '区域id',
  `area_str` varchar(50) NOT NULL DEFAULT '' COMMENT '区域名称',
  `address` varchar(100) NOT NULL DEFAULT '' COMMENT '详细地址',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '是否有效 1：有效 0：无效',
  `is_default` tinyint(1) NOT NULL DEFAULT '0' COMMENT '默认地址',
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `idx_member_id_status` (`member_id`,`status`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COMMENT='会员收货地址';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_address`
--

LOCK TABLES `member_address` WRITE;
/*!40000 ALTER TABLE `member_address` DISABLE KEYS */;
INSERT INTO `member_address` VALUES (1,2,'陆亮','1234567890',110000,'北京市',110101,'丰台区',0,'','天安门',1,0,'2018-09-30 11:50:15','2018-09-30 09:45:14'),(2,2,'陆亮','1234567890',330000,'浙江省',330100,'杭州市',330104,'江干区','浙江理工大学',1,1,'2018-09-30 12:26:32','2018-09-30 11:46:00');
/*!40000 ALTER TABLE `member_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member_cart`
--

DROP TABLE IF EXISTS `member_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `member_cart` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `member_id` bigint(20) NOT NULL DEFAULT '0' COMMENT '会员id',
  `food_id` int(11) NOT NULL DEFAULT '0' COMMENT '商品id',
  `quantity` int(11) NOT NULL DEFAULT '0' COMMENT '数量',
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `idx_member_id` (`member_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COMMENT='购物车';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_cart`
--

LOCK TABLES `member_cart` WRITE;
/*!40000 ALTER TABLE `member_cart` DISABLE KEYS */;
/*!40000 ALTER TABLE `member_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member_comments`
--

DROP TABLE IF EXISTS `member_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `member_comments` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `member_id` int(11) NOT NULL DEFAULT '0' COMMENT '会员id',
  `food_ids` varchar(200) NOT NULL DEFAULT '' COMMENT '商品ids',
  `pay_order_id` int(11) NOT NULL DEFAULT '0' COMMENT '订单id',
  `score` tinyint(4) NOT NULL DEFAULT '0' COMMENT '评分',
  `content` varchar(200) NOT NULL DEFAULT '' COMMENT '评论内容',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `idx_member_id` (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='会员评论表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_comments`
--

LOCK TABLES `member_comments` WRITE;
/*!40000 ALTER TABLE `member_comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `member_comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth_member_bind`
--

DROP TABLE IF EXISTS `oauth_member_bind`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oauth_member_bind` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `member_id` int(11) NOT NULL DEFAULT '0' COMMENT '会员id',
  `client_type` varchar(20) NOT NULL DEFAULT '' COMMENT '客户端来源类型。qq,weibo,weixin',
  `type` tinyint(3) NOT NULL DEFAULT '0' COMMENT '类型 type 1:wechat ',
  `openid` varchar(80) NOT NULL DEFAULT '' COMMENT '第三方id',
  `unionid` varchar(100) NOT NULL DEFAULT '',
  `extra` text NOT NULL COMMENT '额外字段',
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `idx_type_openid` (`type`,`openid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COMMENT='第三方登录绑定关系';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth_member_bind`
--

LOCK TABLES `oauth_member_bind` WRITE;
/*!40000 ALTER TABLE `oauth_member_bind` DISABLE KEYS */;
INSERT INTO `oauth_member_bind` VALUES (2,2,'',1,'oxSmu4tWKTtCx61SBhN-CBml0utk','','','2018-09-30 08:37:30','2018-09-30 08:37:30');
/*!40000 ALTER TABLE `oauth_member_bind` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pay_order`
--

DROP TABLE IF EXISTS `pay_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pay_order` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `order_sn` varchar(40) NOT NULL DEFAULT '' COMMENT '随机订单号',
  `member_id` bigint(11) NOT NULL DEFAULT '0' COMMENT '会员id',
  `total_price` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '订单应付金额',
  `yun_price` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '运费金额',
  `pay_price` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '订单实付金额',
  `pay_sn` varchar(128) NOT NULL DEFAULT '' COMMENT '第三方流水号',
  `prepay_id` varchar(128) NOT NULL DEFAULT '' COMMENT '第三方预付id',
  `note` text NOT NULL COMMENT '备注信息',
  `status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '1：支付完成 0 无效 -1 申请退款 -2 退款中 -9 退款成功  -8 待支付  -7 完成支付待确认',
  `express_status` tinyint(4) NOT NULL DEFAULT '0' COMMENT '快递状态，-8 待支付 -7 已付款待发货 1：确认收货 0：失败',
  `express_address_id` int(11) NOT NULL DEFAULT '0' COMMENT '快递地址id',
  `express_info` varchar(1000) NOT NULL DEFAULT '' COMMENT '快递信息',
  `comment_status` tinyint(1) NOT NULL DEFAULT '0' COMMENT '评论状态',
  `pay_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '付款到账时间',
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最近一次更新时间',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_order_sn` (`order_sn`),
  KEY `idx_member_id_status` (`member_id`,`status`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COMMENT='在线购买订单表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pay_order`
--

LOCK TABLES `pay_order` WRITE;
/*!40000 ALTER TABLE `pay_order` DISABLE KEYS */;
INSERT INTO `pay_order` VALUES (1,'b8344cacd74264357d2cfb705bafb60c',2,23.10,0.00,23.10,'','','',0,-8,1,'{\"mobile\": \"1234567890\", \"nickname\": \"\\u9646\\u4eae\", \"address\": \"\\u5317\\u4eac\\u5e02\\u4e30\\u53f0\\u533a\\u5929\\u5b89\\u95e8\"}',0,'2018-09-30 12:01:58','2018-09-30 12:25:32','2018-09-30 12:01:59'),(2,'d6db6afc915647a3606b1f77d26f4c44',2,11.11,0.00,11.11,'','','',0,-8,1,'{\"mobile\": \"1234567890\", \"nickname\": \"\\u9646\\u4eae\", \"address\": \"\\u5317\\u4eac\\u5e02\\u4e30\\u53f0\\u533a\\u5929\\u5b89\\u95e8\"}',0,'2018-09-30 12:19:50','2018-09-30 12:25:30','2018-09-30 12:19:50'),(3,'99d04aa6c6bcb6eca697ccf2ba87aaf6',2,22.22,0.00,22.22,'','','',0,-8,1,'{\"mobile\": \"1234567890\", \"nickname\": \"\\u9646\\u4eae\", \"address\": \"\\u5317\\u4eac\\u5e02\\u4e30\\u53f0\\u533a\\u5929\\u5b89\\u95e8\"}',0,'2018-09-30 12:24:13','2018-09-30 12:25:27','2018-09-30 12:24:14'),(4,'24c802bb390b45d9d3a8874c4dc80b0e',2,11.11,0.00,11.11,'','','',0,-8,2,'{\"mobile\": \"1234567890\", \"nickname\": \"\\u9646\\u4eae\", \"address\": \"\\u6d59\\u6c5f\\u7701\\u676d\\u5dde\\u5e02\\u6c5f\\u5e72\\u533a\\u6d59\\u6c5f\\u7406\\u5de5\\u5927\\u5b66\"}',0,'2018-09-30 12:26:35','2018-09-30 13:03:53','2018-09-30 12:26:35'),(5,'2ebc5bd94941eb4b59f3a90530500c3d',2,23.11,0.00,23.11,'','','',1,-7,2,'{\"mobile\": \"1234567890\", \"nickname\": \"\\u9646\\u4eae\", \"address\": \"\\u6d59\\u6c5f\\u7701\\u676d\\u5dde\\u5e02\\u6c5f\\u5e72\\u533a\\u6d59\\u6c5f\\u7406\\u5de5\\u5927\\u5b66\"}',0,'2018-10-01 02:48:36','2018-10-01 02:48:36','2018-09-30 13:04:23'),(6,'951f208d7cf82cb2b7ecc5c423cde5ca',2,11.11,0.00,11.11,'','','',-8,-8,2,'{\"mobile\": \"1234567890\", \"nickname\": \"\\u9646\\u4eae\", \"address\": \"\\u6d59\\u6c5f\\u7701\\u676d\\u5dde\\u5e02\\u6c5f\\u5e72\\u533a\\u6d59\\u6c5f\\u7406\\u5de5\\u5927\\u5b66\"}',0,'2018-09-30 14:07:05','2018-09-30 14:07:06','2018-09-30 14:07:06'),(7,'3586a6869daf53e3211fcd9f0e33e923',2,11.11,0.00,11.11,'','','',1,-7,2,'{\"mobile\": \"1234567890\", \"nickname\": \"\\u9646\\u4eae\", \"address\": \"\\u6d59\\u6c5f\\u7701\\u676d\\u5dde\\u5e02\\u6c5f\\u5e72\\u533a\\u6d59\\u6c5f\\u7406\\u5de5\\u5927\\u5b66\"}',0,'2018-09-30 15:11:24','2018-10-01 02:42:12','2018-09-30 15:11:24');
/*!40000 ALTER TABLE `pay_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pay_order_item`
--

DROP TABLE IF EXISTS `pay_order_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pay_order_item` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `pay_order_id` int(11) NOT NULL DEFAULT '0' COMMENT '订单id',
  `member_id` bigint(11) NOT NULL DEFAULT '0' COMMENT '会员id',
  `quantity` int(11) NOT NULL DEFAULT '1' COMMENT '购买数量 默认1份',
  `price` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '商品总价格，售价 * 数量',
  `food_id` int(11) NOT NULL DEFAULT '0' COMMENT '美食表id',
  `note` text NOT NULL COMMENT '备注信息',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '状态：1：成功 0 失败',
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最近一次更新时间',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `id_order_id` (`pay_order_id`),
  KEY `idx_food_id` (`food_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COMMENT='订单详情表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pay_order_item`
--

LOCK TABLES `pay_order_item` WRITE;
/*!40000 ALTER TABLE `pay_order_item` DISABLE KEYS */;
INSERT INTO `pay_order_item` VALUES (1,1,2,1,10.09,8,'',1,'2018-09-30 12:01:59','2018-09-30 12:01:59'),(2,1,2,1,13.01,5,'',1,'2018-09-30 12:01:59','2018-09-30 12:01:59'),(3,2,2,1,11.11,7,'',1,'2018-09-30 12:19:50','2018-09-30 12:19:50'),(4,3,2,2,11.11,7,'',1,'2018-09-30 12:24:14','2018-09-30 12:24:14'),(5,4,2,1,11.11,7,'',1,'2018-09-30 12:26:35','2018-09-30 12:26:35'),(6,5,2,1,11.11,7,'',1,'2018-09-30 13:04:23','2018-09-30 13:04:23'),(7,5,2,1,12.00,4,'',1,'2018-09-30 13:04:23','2018-09-30 13:04:23'),(8,6,2,1,11.11,7,'',1,'2018-09-30 14:07:06','2018-09-30 14:07:06'),(9,7,2,1,11.11,7,'',1,'2018-09-30 15:11:24','2018-09-30 15:11:24');
/*!40000 ALTER TABLE `pay_order_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stat_daily_food`
--

DROP TABLE IF EXISTS `stat_daily_food`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stat_daily_food` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `food_id` int(11) NOT NULL DEFAULT '0' COMMENT '菜品id',
  `total_count` int(11) NOT NULL DEFAULT '0' COMMENT '售卖总数量',
  `total_pay_money` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '总售卖金额',
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `date_food_id` (`date`,`food_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='书籍售卖日统计';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stat_daily_food`
--

LOCK TABLES `stat_daily_food` WRITE;
/*!40000 ALTER TABLE `stat_daily_food` DISABLE KEYS */;
/*!40000 ALTER TABLE `stat_daily_food` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stat_daily_member`
--

DROP TABLE IF EXISTS `stat_daily_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stat_daily_member` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL COMMENT '日期',
  `member_id` int(11) NOT NULL DEFAULT '0' COMMENT '会员id',
  `total_shared_count` int(11) NOT NULL DEFAULT '0' COMMENT '当日分享总次数',
  `total_pay_money` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '当日付款总金额',
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `idx_date_member_id` (`date`,`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='会员日统计';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stat_daily_member`
--

LOCK TABLES `stat_daily_member` WRITE;
/*!40000 ALTER TABLE `stat_daily_member` DISABLE KEYS */;
/*!40000 ALTER TABLE `stat_daily_member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stat_daily_site`
--

DROP TABLE IF EXISTS `stat_daily_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stat_daily_site` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL COMMENT '日期',
  `total_pay_money` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '当日应收总金额',
  `total_member_count` int(11) NOT NULL COMMENT '会员总数',
  `total_new_member_count` int(11) NOT NULL COMMENT '当日新增会员数',
  `total_order_count` int(11) NOT NULL COMMENT '当日订单数',
  `total_shared_count` int(11) NOT NULL,
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `idx_date` (`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='全站日统计';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stat_daily_site`
--

LOCK TABLES `stat_daily_site` WRITE;
/*!40000 ALTER TABLE `stat_daily_site` DISABLE KEYS */;
/*!40000 ALTER TABLE `stat_daily_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `uid` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '用户uid',
  `nickname` varchar(100) NOT NULL DEFAULT '' COMMENT '用户名',
  `mobile` varchar(20) NOT NULL DEFAULT '' COMMENT '手机号码',
  `email` varchar(100) NOT NULL DEFAULT '' COMMENT '邮箱地址',
  `sex` tinyint(1) NOT NULL DEFAULT '0' COMMENT '1：男 2：女 0：没填写',
  `avatar` varchar(64) NOT NULL DEFAULT '' COMMENT '头像',
  `login_name` varchar(20) NOT NULL DEFAULT '' COMMENT '登录用户名',
  `login_pwd` varchar(32) NOT NULL DEFAULT '' COMMENT '登录密码',
  `login_salt` varchar(32) NOT NULL DEFAULT '' COMMENT '登录密码的随机加密秘钥',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1：有效 0：无效',
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`uid`),
  UNIQUE KEY `login_name` (`login_name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COMMENT='用户表（管理员）';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Python','11012345679','abc@163.com',1,'','admin','816440c40b7a9d55ff9eb7b20760862c','cF3JfH5FJfQ8B2Ba',1,'2017-03-15 06:08:48','2017-03-15 06:08:48');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wx_share_history`
--

DROP TABLE IF EXISTS `wx_share_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wx_share_history` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `member_id` int(11) NOT NULL DEFAULT '0' COMMENT '会员id',
  `share_url` varchar(200) NOT NULL DEFAULT '' COMMENT '分享的页面url',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COMMENT='微信分享记录';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wx_share_history`
--

LOCK TABLES `wx_share_history` WRITE;
/*!40000 ALTER TABLE `wx_share_history` DISABLE KEYS */;
INSERT INTO `wx_share_history` VALUES (1,0,'pages/food/info?id=7','2018-09-30 08:54:41');
/*!40000 ALTER TABLE `wx_share_history` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-01 22:03:19
