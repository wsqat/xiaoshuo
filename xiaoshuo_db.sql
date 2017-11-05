-- MySQL dump 10.13  Distrib 5.7.19, for macos10.12 (x86_64)
--
-- Host: localhost    Database: xiaoshuo_db
-- ------------------------------------------------------
-- Server version	5.7.19

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
-- Table structure for table `novel_author`
--

DROP TABLE IF EXISTS `novel_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `novel_author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `author` varchar(100) DEFAULT NULL,
  `collects` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `novel_author`
--

LOCK TABLES `novel_author` WRITE;
/*!40000 ALTER TABLE `novel_author` DISABLE KEYS */;
INSERT INTO `novel_author` VALUES (1,'﻿author','collects','20171104'),(2,'唐家三少','39247199','20171104'),(3,'辰东','37164599','20171104'),(4,'我吃西红柿','35095345','20171104'),(5,'猫腻','34899019','20171104'),(6,'耳根','25856600','20171104'),(7,'骷髅精灵','25673500','20171104'),(8,'忘语','25483400','20171104'),(9,'血红','25333065','20171104'),(10,'月关','20084083','20171104'),(11,'林海听涛','17456695','20171104'),(12,'烟雨江南','17229754','20171104'),(13,'荆柯守','17163488','20171104'),(14,'方想','16703755','20171104'),(15,'跳舞','16190317','20171104'),(16,'风凌天下','15712548','20171104'),(17,'萧鼎','15312203','20171104'),(18,'天蚕土豆','14744002','20171104'),(19,'骁骑校','13758311','20171104'),(20,'雷云风暴','13502000','20171104'),(21,'萧潜','12988079','20171104');
/*!40000 ALTER TABLE `novel_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `novel_collects`
--

DROP TABLE IF EXISTS `novel_collects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `novel_collects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `author` varchar(100) DEFAULT NULL,
  `collects` varchar(100) DEFAULT NULL,
  `reviews` varchar(100) DEFAULT NULL,
  `month` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `novel_collects`
--

LOCK TABLES `novel_collects` WRITE;
/*!40000 ALTER TABLE `novel_collects` DISABLE KEYS */;
INSERT INTO `novel_collects` VALUES (1,'择天记','猫腻','21374489','26118589','4764.0','20171104'),(2,'圣墟','辰东','15228000','6159299','125308.0','20171104'),(3,'一念永恒','耳根','14303500','6552100','84048.0','20171104'),(4,'斗战狂潮','骷髅精灵','13828000','9629300','94212.0','20171104'),(5,'青帝','荆柯守','13807289','8702303','2064.0','20171104'),(6,'凡人修仙传','忘语','13803100','101118600','6596.0','20171104'),(7,'从零开始','雷云风暴','13386900','64911600','764.0','20171104'),(8,'天影','萧鼎','11429300','10080500','86288.0','20171104'),(9,'罪恶之城','烟雨江南','10836094','168832302','2532328.0','20171104'),(10,'我真是大明星','尝谕','9915500','2935500','34608.0','20171104'),(11,'超凡传','萧潜','9360000','9630200','89840.0','20171104'),(12,'女华佗种田记','倾情一诺','9099700','7204100','1216.0','20171104'),(13,'联盟之谁与争锋','乱','9038561','15609506','556.0','20171104'),(14,'大官人','三戒大师','8907092','6069030','1052.0','20171104'),(15,'五行天','方想','8665100','4202500','5412.0','20171104'),(16,'大明武夫','特别白','8049022','5435592','1300.0','20171104'),(17,'大主宰','天蚕土豆','8010599','32397900','1452.0','20171104'),(18,'不朽凡人','鹅是老五','7942200','3728300','33388.0','20171104'),(19,'盘龙','我吃西红柿','7727000','94633500','64.0','20171104'),(20,'冠军之光','林海听涛','7618122','2685148','400.0','20171104');
/*!40000 ALTER TABLE `novel_collects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `novel_month`
--

DROP TABLE IF EXISTS `novel_month`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `novel_month` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `author` varchar(100) DEFAULT NULL,
  `collects` varchar(100) DEFAULT NULL,
  `reviews` varchar(100) DEFAULT NULL,
  `month` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `novel_month`
--

LOCK TABLES `novel_month` WRITE;
/*!40000 ALTER TABLE `novel_month` DISABLE KEYS */;
INSERT INTO `novel_month` VALUES (1,'修罗武神','善良的蜜蜂','2201082','3988965700','103494809.0','20171104'),(2,'超级兵王','步千帆','363702','325057345','27865134.0','20171104'),(3,'九星霸体诀','平凡魔术师','134069','182944982','21554205.0','20171104'),(4,'武逆','只是小虾米','351418','408241557','15772552.0','20171104'),(5,'龙符','梦入神机','483169','226300822','15724002.0','20171104'),(6,'传奇再现','伪戒','242734','424263161','14707570.0','20171104'),(7,'混沌剑神','心星逍遥','448526','275722940','13383075.0','20171104'),(8,'大逆之门','知白','107925','146303222','12030996.0','20171104'),(9,'万域之王','逆苍天','220962','168436532','11235802.0','20171104'),(10,'终极教官','梁七少','99900','230305702','11218750.0','20171104'),(11,'女神的近身护卫','肥茄子','124943','233477537','11166228.0','20171104'),(12,'龙血战神','风青阳','1031923','518839023','10733941.0','20171104'),(13,'人皇纪','皇甫奇','272013','927599865','9185087.0','20171104'),(14,'贴身兵王','笑笑星儿','210810','230448497','7303242.0','20171104'),(15,'火帝神尊','西门飘血','116570','121762292','7212735.0','20171104'),(16,'傲世丹神','寂小贼','232158','450444345','6517656.0','20171104'),(17,'美女请留步','老施','2744057','533009201','5934897.0','20171104'),(18,'斩龙','失落叶','3628704','1063149101','5456037.0','20171104'),(19,'武道至尊','暗夜幽殇','194119','222315570','5342327.0','20171104'),(20,'权力巅峰','梦入洪荒','1068346','148625857','5254543.0','20171104');
/*!40000 ALTER TABLE `novel_month` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `novel_reviews`
--

DROP TABLE IF EXISTS `novel_reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `novel_reviews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `author` varchar(100) DEFAULT NULL,
  `collects` varchar(100) DEFAULT NULL,
  `reviews` varchar(100) DEFAULT NULL,
  `month` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `novel_reviews`
--

LOCK TABLES `novel_reviews` WRITE;
/*!40000 ALTER TABLE `novel_reviews` DISABLE KEYS */;
INSERT INTO `novel_reviews` VALUES (1,'11处特工皇妃','潇湘冬儿','98000','5500000000','609476.0','20171104'),(2,'修罗武神','善良的蜜蜂','2201082','3988965700','103494809.0','20171104'),(3,'万古仙穹','观棋','577496','1132361196','4437562.0','20171104'),(4,'斩龙','失落叶','3628704','1063149101','5456037.0','20171104'),(5,'人皇纪','皇甫奇','272013','927599865','9185087.0','20171104'),(6,'杀手房东俏房客','老施','997679','706544907','3714911.0','20171104'),(7,'美女请留步','老施','2744057','533009201','5934897.0','20171104'),(8,'龙血战神','风青阳','1031923','518839023','10733941.0','20171104'),(9,'网游之天下无双','失落叶','3221959','506158086','3857583.0','20171104'),(10,'我的美女老师','黑夜de白羊','846213','469590101','2120628.0','20171104'),(11,'傲世丹神','寂小贼','232158','450444345','6517656.0','20171104'),(12,'传奇再现','伪戒','242734','424263161','14707570.0','20171104'),(13,'武逆','只是小虾米','351418','408241557','15772552.0','20171104'),(14,'我们是兄弟','纯银耳坠','2063132','400627992','4748962.0','20171104'),(15,'少年医仙','逐没','915794','397671415','2071149.0','20171104'),(16,'暧昧高手','紫气东来','554237','339259714','835179.0','20171104'),(17,'超级兵王','步千帆','363702','325057345','27865134.0','20171104'),(18,'混沌剑神','心星逍遥','448526','275722940','13383075.0','20171104'),(19,'吞天记','风青阳','298286','259992357','4390680.0','20171104'),(20,'狩魔手记','烟雨江南','6167169','258254768','809476.0','20171104');
/*!40000 ALTER TABLE `novel_reviews` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-11-04 21:30:07
