/*
Navicat MySQL Data Transfer

Source Server         : 10
Source Server Version : 50149
Source Host           : 127.0.0.1:3308
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50149
File Encoding         : 65001

Date: 2022-06-12 11:43:43
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `tel` varchar(255) DEFAULT NULL,
  `address` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', '101', '101', '2040706101', '书院楼');
INSERT INTO `user` VALUES ('2', '102', '102', '2040706102', '书院楼');
INSERT INTO `user` VALUES ('105', '105', '105', '2040706105', '书院楼');
INSERT INTO `user` VALUES ('106', '106', '105', '2040706106', '书院楼');
INSERT INTO `user` VALUES ('107', '107', '105', '2040706107', '书院楼');
INSERT INTO `user` VALUES ('108', '108', '105', '2040706108', '书院楼');
