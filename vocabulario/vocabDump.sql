-- MySQL dump 10.13  Distrib 5.5.40, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: tematres
-- ------------------------------------------------------
-- Server version	5.5.40-0ubuntu0.12.04.1

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
-- Table structure for table `bit__config`
--

DROP TABLE IF EXISTS `bit__config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bit__config` (
  `id` int(5) unsigned NOT NULL AUTO_INCREMENT,
  `titulo` varchar(255) NOT NULL DEFAULT '',
  `autor` varchar(255) NOT NULL DEFAULT '',
  `idioma` char(5) NOT NULL DEFAULT 'es',
  `cobertura` text,
  `keywords` varchar(255) DEFAULT NULL,
  `tipo` varchar(100) DEFAULT NULL,
  `polijerarquia` tinyint(1) NOT NULL DEFAULT '1',
  `cuando` date NOT NULL DEFAULT '0000-00-00',
  `observa` text,
  `url_base` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bit__config`
--

LOCK TABLES `bit__config` WRITE;
/*!40000 ALTER TABLE `bit__config` DISABLE KEYS */;
INSERT INTO `bit__config` VALUES (1,'bdpr','equipe do participa.br','pt','','','Controlled vocabulary',2,'2014-11-06',NULL,'http://localhost/tematres/vocab/'),(2,'outrovoc','','ab','','','',0,'1998-01-01',NULL,'http://localhost/tematres/vocababo');
/*!40000 ALTER TABLE `bit__config` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bit__indice`
--

DROP TABLE IF EXISTS `bit__indice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bit__indice` (
  `tema_id` int(11) NOT NULL DEFAULT '0',
  `indice` varchar(250) NOT NULL DEFAULT '',
  PRIMARY KEY (`tema_id`),
  KEY `indice` (`indice`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='indice de temas';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bit__indice`
--

LOCK TABLES `bit__indice` WRITE;
/*!40000 ALTER TABLE `bit__indice` DISABLE KEYS */;
INSERT INTO `bit__indice` VALUES (1,'|1'),(2,'|2'),(3,'|3'),(4,'|4'),(5,'|5'),(6,'|6'),(7,'|7'),(8,'|8'),(9,'|9'),(10,'|10'),(41,'|41'),(11,'|11'),(12,'|12'),(13,'|13'),(14,'|14'),(15,'|15'),(16,'|16'),(17,'|17'),(18,'|18'),(19,'|19'),(20,'|20'),(21,'|21'),(22,'|22'),(23,'|23'),(24,'|24'),(25,'|25'),(26,'|26'),(27,'|27'),(28,'|28'),(29,'|29'),(31,'|31'),(30,'|30'),(34,'|34'),(35,'|35'),(32,'|32'),(33,'|33'),(36,'|36'),(37,'|37'),(38,'|38'),(39,'|39'),(40,'|40'),(42,'|42'),(43,'|43'),(44,'|44'),(45,'|45'),(46,'|46'),(47,'|47'),(48,'|48'),(49,'|49'),(50,'|50'),(51,'|51'),(53,'|53'),(52,'|52'),(54,'|54'),(55,'|55'),(56,'|56'),(57,'|57'),(58,'|58'),(59,'|59'),(60,'|60'),(61,'|61'),(62,'|62'),(63,'|63'),(64,'|64'),(65,'|65'),(66,'|66'),(67,'|67'),(68,'|68'),(69,'|69'),(70,'|70'),(71,'|71'),(72,'|72'),(73,'|73'),(74,'|74'),(75,'|75'),(76,'|76'),(77,'|77'),(78,'|78'),(79,'|79'),(80,'|80'),(81,'|81'),(82,'|82'),(90,'|90'),(83,'|83'),(84,'|84'),(85,'|85'),(87,'|87'),(86,'|86'),(88,'|88'),(89,'|89'),(91,'|91'),(92,'|92'),(93,'|93'),(94,'|94'),(95,'|95'),(96,'|96'),(97,'|97'),(98,'|98'),(99,'|99'),(100,'|100'),(101,'|101'),(102,'|102'),(103,'|103'),(104,'|104'),(105,'|105'),(106,'|106'),(107,'|107'),(108,'|108'),(109,'|109'),(110,'|110'),(111,'|111'),(112,'|112'),(113,'|113'),(114,'|114'),(115,'|115'),(116,'|116'),(117,'|117'),(118,'|118'),(119,'|119'),(120,'|120'),(121,'|121'),(122,'|122'),(123,'|123'),(124,'|124'),(125,'|125'),(126,'|126'),(127,'|127'),(128,'|128'),(129,'|129'),(130,'|130'),(131,'|131'),(132,'|132'),(133,'|133'),(134,'|134'),(135,'|135'),(136,'|136'),(137,'|137'),(138,'|138'),(139,'|139'),(140,'|140'),(141,'|141'),(142,'|142'),(143,'|143'),(144,'|144'),(145,'|145'),(146,'|146');
/*!40000 ALTER TABLE `bit__indice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bit__notas`
--

DROP TABLE IF EXISTS `bit__notas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bit__notas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_tema` int(11) NOT NULL DEFAULT '0',
  `tipo_nota` char(3) NOT NULL DEFAULT 'NA',
  `lang_nota` varchar(7) DEFAULT NULL,
  `nota` mediumtext NOT NULL,
  `cuando` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `uid` int(5) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `id_tema` (`id_tema`),
  KEY `orden_notas` (`tipo_nota`,`lang_nota`),
  FULLTEXT KEY `notas` (`nota`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bit__notas`
--

LOCK TABLES `bit__notas` WRITE;
/*!40000 ALTER TABLE `bit__notas` DISABLE KEYS */;
/*!40000 ALTER TABLE `bit__notas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bit__tabla_rel`
--

DROP TABLE IF EXISTS `bit__tabla_rel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bit__tabla_rel` (
  `id_mayor` int(5) NOT NULL DEFAULT '0',
  `id_menor` int(5) NOT NULL DEFAULT '0',
  `t_relacion` tinyint(1) unsigned NOT NULL DEFAULT '0',
  `rel_rel_id` int(22) DEFAULT NULL,
  `id` int(9) unsigned NOT NULL AUTO_INCREMENT,
  `uid` int(10) unsigned NOT NULL DEFAULT '0',
  `cuando` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`),
  UNIQUE KEY `NewIndex` (`id_mayor`,`id_menor`),
  KEY `unico` (`t_relacion`),
  KEY `id_menor` (`id_menor`),
  KEY `id_mayor` (`id_mayor`),
  KEY `rel_rel_id` (`rel_rel_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bit__tabla_rel`
--

LOCK TABLES `bit__tabla_rel` WRITE;
/*!40000 ALTER TABLE `bit__tabla_rel` DISABLE KEYS */;
/*!40000 ALTER TABLE `bit__tabla_rel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bit__tema`
--

DROP TABLE IF EXISTS `bit__tema`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bit__tema` (
  `tema_id` int(10) NOT NULL AUTO_INCREMENT,
  `code` varchar(150) DEFAULT NULL COMMENT 'code_term',
  `tema` varchar(250) DEFAULT NULL,
  `tesauro_id` int(5) NOT NULL DEFAULT '0',
  `uid` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `cuando` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `uid_final` int(5) unsigned DEFAULT NULL,
  `cuando_final` datetime DEFAULT NULL,
  `estado_id` int(5) NOT NULL DEFAULT '13',
  `cuando_estado` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `isMetaTerm` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`tema_id`),
  KEY `code` (`code`),
  KEY `tema` (`tema`),
  KEY `cuando` (`cuando`,`cuando_final`),
  KEY `uid` (`uid`,`uid_final`),
  KEY `tesauro_id` (`tesauro_id`),
  KEY `estado_id` (`estado_id`),
  KEY `isMetaTerm` (`isMetaTerm`)
) ENGINE=MyISAM AUTO_INCREMENT=147 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bit__tema`
--

LOCK TABLES `bit__tema` WRITE;
/*!40000 ALTER TABLE `bit__tema` DISABLE KEYS */;
INSERT INTO `bit__tema` VALUES (1,NULL,'Adjunto',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(2,NULL,'Ambiente Virtual de Participação Social',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(3,NULL,'Área de Política',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(4,NULL,'Assessoria',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(5,NULL,'Assunto',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(6,NULL,'Ata de Conselho',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(7,NULL,'Ato Normativo',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(8,NULL,'Ato Normativo',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(9,NULL,'Audiência Pública',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(10,NULL,'Caderno de Propostas',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(11,NULL,'Capacitação de Participante',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(12,NULL,'Capacitação de Sociedade Externa',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(13,NULL,'Carta',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(14,NULL,'Carta Convite',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(15,NULL,'Comissão',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(16,NULL,'Comissão Interna',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(17,NULL,'Comitê',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(18,NULL,'Composição',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(19,NULL,'Compromisso Consensual',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(20,NULL,'Conferência',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(21,NULL,'Conferência Estadual',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(22,NULL,'Conferência Extraordinária',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(23,NULL,'Conferência Intermunicipal',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(24,NULL,'Conferência Livre',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(25,NULL,'Conferência Municipal',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(26,NULL,'Conferência Regional',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(27,NULL,'Conferência Virtual',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(28,NULL,'Conselho',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(29,NULL,'Consulta Pública',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(30,NULL,'Convocar',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(31,NULL,'Convocação de Conferência',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(32,NULL,'Coordenador',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(33,NULL,'Coordenar',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(34,NULL,'Coordenação',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(35,NULL,'Coordenação',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(36,NULL,'Corpo Gestor',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(37,NULL,'Corpo Gestor de Conferência',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(38,NULL,'Cota',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(39,NULL,'Criação',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(40,NULL,'Cultura Participativa',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(41,NULL,'Câmara dos Deputados',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(42,NULL,'de Trabalho',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(43,NULL,'Decisão ad Referendum',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(44,NULL,'Decreto',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(45,NULL,'Decreto Presidencial',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(46,NULL,'Delegado',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(47,NULL,'Demanda',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(48,NULL,'Denúncia',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(49,NULL,'Desenvolvimento Econômico',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(50,NULL,'Divulgar',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(51,NULL,'Documento de Referência',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(52,NULL,'Editorial',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(53,NULL,'Edição de Conferência',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(54,NULL,'Eixo Temático',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(55,NULL,'Eixos Temáticos',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(56,NULL,'Especial',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(57,NULL,'Estatuto',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(58,NULL,'Etapa de Conferência',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(59,NULL,'Executivo',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(60,NULL,'Formulação',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(61,NULL,'Fórum',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(62,NULL,'Fórum Interconselhos',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(63,NULL,'Fórum não Governamental',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(64,NULL,'Garantia de Direitos',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(65,NULL,'Geral',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(66,NULL,'Governo',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(67,NULL,'Grupo de Trabalho',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(68,NULL,'Grupo Étnico',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(69,NULL,'Infraestrutura',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(70,NULL,'Instância Consultiva',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(71,NULL,'Instância de Participação Social',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(72,NULL,'Instância Deliberativa',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(73,NULL,'Instância ou Mecanismo de Participação Social',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(74,NULL,'Iteração com Instância ou Mecanismo de Participação Social',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(75,NULL,'Lei',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(76,NULL,'Manual',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(77,NULL,'Mecanismo Consultivo',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(78,NULL,'Mecanismo de Participação Social',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(79,NULL,'Mecanismo Deliberativo',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(80,NULL,'Mecanismo Orientador',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(81,NULL,'Membro',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(82,NULL,'Mesa de Diálogo',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(83,NULL,'Metodologia de Conferência',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(84,NULL,'Metodologia de Consulta Pública',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(85,NULL,'Ministério',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(86,NULL,'Momento Participativo',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(87,NULL,'Moção',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(88,NULL,'Mulher',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(89,NULL,'Município',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(90,NULL,'Método de Seleção de Participantes',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(91,NULL,'Objetivo',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(92,NULL,'Oficina',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(93,NULL,'Ofício de Movimento Social',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(94,NULL,'Organização',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(95,NULL,'Organização Nacional de Conferência',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(96,NULL,'Órgão Público',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(97,NULL,'Ouvidoria',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(98,NULL,'Palestra',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(99,NULL,'Paridade',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(100,NULL,'Participante',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(101,NULL,'Pauta',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(102,NULL,'Periodicidade',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(103,NULL,'Plano Nacional',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(104,NULL,'Plenária',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(105,NULL,'Plenária Temática',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(106,NULL,'Política ou Plano Nacional',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(107,NULL,'Política Pública',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(108,NULL,'Políticas Sociais',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(109,NULL,'Portaria',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(110,NULL,'Portaria de Criação',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(111,NULL,'Portaria Ministerial',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(112,NULL,'Portaria Normativa',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(113,NULL,'Presidência',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(114,NULL,'Presidência',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(115,NULL,'Priorização',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(116,NULL,'Problema',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(117,NULL,'Programa Federal',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(118,NULL,'Proposta',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(119,NULL,'Proposta Aprovada',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(120,NULL,'Qualificador de Grupo',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(121,NULL,'Recondução de Mandato',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(122,NULL,'Recursos Naturais',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(123,NULL,'Reformulação',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(124,NULL,'Regimento',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(125,NULL,'Regimento',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(126,NULL,'Regimento Interno',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(127,NULL,'Regulamento',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(128,NULL,'Relator',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(129,NULL,'Relatório de Auditoria',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(130,NULL,'Relatório de Monitoramento',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(131,NULL,'Requerimento',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(132,NULL,'Resolução',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(133,NULL,'Secretaria',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(134,NULL,'Secretaria com Status de Ministério',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(135,NULL,'Secretaria Executiva',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(136,NULL,'Secretaria Executiva',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(137,NULL,'Secretário',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(138,NULL,'Sgpr',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(139,NULL,'Sistema Nacional',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(140,NULL,'Socialização Política',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(141,NULL,'Subcomitê',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(142,NULL,'Tema',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(143,NULL,'Tema',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(144,NULL,'Texto Base Para Diálogo',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(145,NULL,'Vaga',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0),(146,NULL,'Voto de Qualidade',1,1,'2014-11-06 06:56:06',NULL,NULL,13,'2014-11-06 06:56:06',0);
/*!40000 ALTER TABLE `bit__tema` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bit__term2tterm`
--

DROP TABLE IF EXISTS `bit__term2tterm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bit__term2tterm` (
  `tterm_id` int(22) NOT NULL AUTO_INCREMENT,
  `tvocab_id` int(22) NOT NULL,
  `tterm_url` varchar(200) NOT NULL,
  `tterm_uri` varchar(200) NOT NULL,
  `tterm_string` varchar(250) NOT NULL,
  `cuando` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cuando_last` timestamp NULL DEFAULT NULL,
  `uid` int(22) NOT NULL,
  `tema_id` int(22) NOT NULL,
  PRIMARY KEY (`tterm_id`),
  KEY `tvocab_id` (`tvocab_id`,`cuando`,`cuando_last`,`uid`),
  KEY `tema_id` (`tema_id`),
  KEY `target_terms` (`tterm_string`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bit__term2tterm`
--

LOCK TABLES `bit__term2tterm` WRITE;
/*!40000 ALTER TABLE `bit__term2tterm` DISABLE KEYS */;
/*!40000 ALTER TABLE `bit__term2tterm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bit__tvocab`
--

DROP TABLE IF EXISTS `bit__tvocab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bit__tvocab` (
  `tvocab_id` int(22) NOT NULL AUTO_INCREMENT,
  `tvocab_label` varchar(150) NOT NULL,
  `tvocab_tag` varchar(20) NOT NULL,
  `tvocab_lang` varchar(5) DEFAULT NULL,
  `tvocab_title` varchar(200) NOT NULL,
  `tvocab_url` varchar(250) NOT NULL,
  `tvocab_uri_service` varchar(250) NOT NULL,
  `tvocab_status` tinyint(1) NOT NULL,
  `cuando` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `uid` int(22) NOT NULL,
  PRIMARY KEY (`tvocab_id`),
  KEY `uid` (`uid`),
  KEY `status` (`tvocab_status`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bit__tvocab`
--

LOCK TABLES `bit__tvocab` WRITE;
/*!40000 ALTER TABLE `bit__tvocab` DISABLE KEYS */;
/*!40000 ALTER TABLE `bit__tvocab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bit__uri`
--

DROP TABLE IF EXISTS `bit__uri`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bit__uri` (
  `uri_id` int(22) NOT NULL AUTO_INCREMENT,
  `tema_id` int(22) NOT NULL,
  `uri_type_id` int(22) NOT NULL,
  `uri` tinytext NOT NULL,
  `uid` int(22) NOT NULL,
  `cuando` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`uri_id`),
  KEY `tema_id` (`tema_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='external URIs associated to terms';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bit__uri`
--

LOCK TABLES `bit__uri` WRITE;
/*!40000 ALTER TABLE `bit__uri` DISABLE KEYS */;
/*!40000 ALTER TABLE `bit__uri` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bit__usuario`
--

DROP TABLE IF EXISTS `bit__usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bit__usuario` (
  `APELLIDO` varchar(150) DEFAULT NULL,
  `NOMBRES` varchar(150) DEFAULT NULL,
  `uid` int(9) unsigned DEFAULT NULL,
  `cuando` date DEFAULT NULL,
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `mail` varchar(255) DEFAULT NULL,
  `pass` varchar(60) NOT NULL DEFAULT '',
  `orga` varchar(255) DEFAULT NULL,
  `nivel` tinyint(1) unsigned NOT NULL DEFAULT '2',
  `estado` set('ACTIVO','BAJA') NOT NULL DEFAULT 'BAJA',
  `hasta` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `user_activation_key` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mail` (`mail`),
  KEY `pass` (`pass`),
  KEY `user_activation_key` (`user_activation_key`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bit__usuario`
--

LOCK TABLES `bit__usuario` WRITE;
/*!40000 ALTER TABLE `bit__usuario` DISABLE KEYS */;
INSERT INTO `bit__usuario` VALUES ('Renato','Fabbri',1,'2014-11-06',1,'renato.fabbri@gmail.com','Jockey67','TemaTres',1,'ACTIVO','2014-11-06 05:59:56',NULL),('','',1,'2014-11-06',2,'','','',2,'ACTIVO','2014-11-06 06:21:27',NULL);
/*!40000 ALTER TABLE `bit__usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bit__values`
--

DROP TABLE IF EXISTS `bit__values`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bit__values` (
  `value_id` int(11) NOT NULL AUTO_INCREMENT,
  `value_type` varchar(64) NOT NULL DEFAULT '0',
  `value` longtext NOT NULL,
  `value_order` tinyint(4) DEFAULT NULL,
  `value_code` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`value_id`),
  KEY `value_type` (`value_type`)
) ENGINE=MyISAM AUTO_INCREMENT=49 DEFAULT CHARSET=utf8 COMMENT='general values table';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bit__values`
--

LOCK TABLES `bit__values` WRITE;
/*!40000 ALTER TABLE `bit__values` DISABLE KEYS */;
INSERT INTO `bit__values` VALUES (2,'t_relacion','Termino relacionado',NULL,'TR'),(3,'t_relacion','Termino superior',NULL,'TG'),(4,'t_relacion','Usado por',NULL,'UP'),(5,'t_relacion','Equivalencia parcial',NULL,'EQ_P'),(6,'t_relacion','Equivalencia total',NULL,'EQ'),(7,'t_relacion','No equivalencia',NULL,'EQ_NO'),(8,'t_nota','Nota de alcance',1,'NA'),(9,'t_nota','Nota histórica',2,'NH'),(10,'t_nota','Nota bibliografica',3,'NB'),(11,'t_nota','Nota privada',4,'NP'),(1,'t_usuario','Admin',NULL,'admin'),(12,'t_estado','termino candidato',1,'C'),(13,'t_estado','termino activo',2,'A'),(14,'t_estado','termino rechazado',3,'R'),(15,'t_nota','Nota catalográfica',2,'NC'),(16,'config','_USE_CODE',1,'0'),(17,'config','_SHOW_CODE',1,'0'),(18,'config','CFG_MAX_TREE_DEEP',NULL,'3'),(19,'config','CFG_VIEW_STATUS',NULL,'0'),(20,'config','CFG_SIMPLE_WEB_SERVICE',NULL,'1'),(21,'config','CFG_NUM_SHOW_TERMSxSTATUS',NULL,'200'),(22,'config','CFG_MIN_SEARCH_SIZE',NULL,'2'),(23,'config','_SHOW_TREE',1,'1'),(24,'config','_PUBLISH_SKOS',1,'0'),(25,'4','Spelling variant',NULL,'SP'),(26,'4','MisSpelling',NULL,'MS'),(27,'3','Partitive',NULL,'P'),(28,'3','Instance',NULL,'I'),(30,'4','Abbreviation',NULL,'AB'),(31,'4','Full form of the term',NULL,'FT'),(32,'URI_TYPE','broadMatch',NULL,'broadMatch'),(33,'URI_TYPE','closeMatch',NULL,'closeMatch'),(34,'URI_TYPE','exactMatch',NULL,'exactMatch'),(35,'URI_TYPE','relatedMatch',NULL,'relatedMatch'),(36,'URI_TYPE','narrowMatch',NULL,'narrowMatch'),(37,'DATESTAMP','2014-11-06 05:59:56',NULL,'NOTE_CHANGE'),(38,'DATESTAMP','2014-11-06 05:59:56',NULL,'TERM_CHANGE'),(39,'DATESTAMP','2014-11-06 05:59:56',NULL,'TTERM_CHANGE'),(40,'DATESTAMP','2014-11-06 05:59:56',NULL,'THES_CHANGE'),(41,'METADATA','',2,'dc:contributor'),(42,'METADATA','',5,'dc:publisher'),(43,'METADATA','',9,'dc:rights'),(44,'4','Hidden',NULL,'H'),(45,'config','CFG_SEARCH_METATERM',NULL,'0'),(46,'config','CFG_ENABLE_SPARQL',NULL,'0'),(47,'config','CFG_SUGGESTxWORD',NULL,'1'),(48,'CONTACT_MAIL','',NULL,'NULL');
/*!40000 ALTER TABLE `bit__values` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-11-06  6:57:11
