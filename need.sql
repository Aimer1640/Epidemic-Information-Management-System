/*
Navicat MySQL Data Transfer

Source Server         : 10
Source Server Version : 50149
Source Host           : 127.0.0.1:3308
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50149
File Encoding         : 65001

Date: 2022-06-12 11:43:36
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for need
-- ----------------------------
DROP TABLE IF EXISTS `need`;
CREATE TABLE `need` (
  `userid` int(11) DEFAULT NULL,
  `needthing` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `tel` varchar(255) DEFAULT NULL,
  `grade` varchar(255) DEFAULT NULL,
  `address` varchar(255) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of need
-- ----------------------------
INSERT INTO `need` VALUES ('101', '作业纸', '2040706101', '1', '书院楼');
INSERT INTO `need` VALUES ('101', '水果', '2040706101', '2', '书院楼');
INSERT INTO `need` VALUES ('102', '作业纸', '2040706102', '1', '书院楼');
INSERT INTO `need` VALUES ('102', '黑色水笔', '2040706102', '2', '书院楼');
INSERT INTO `need` VALUES ('103', '作业纸', '2040706103', '1', '书院楼');
INSERT INTO `need` VALUES ('103', '胶纸', '2040706103', '2', '书院楼');
