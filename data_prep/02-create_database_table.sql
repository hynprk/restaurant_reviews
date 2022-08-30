-- Create database and table for Tripadvisor reviews data

DROP DATABASE IF EXISTS `restaurant_reviews`;
CREATE DATABASE `restaurant_reviews`;
USE `restaurant_reviews`;

-- Match column names with original dataset to avoid confusions
CREATE TABLE `tripadvisor_raw` (
  `Name` varchar(1000) DEFAULT NULL,
  `Street Address` varchar(1000) DEFAULT NULL,
  `Location` varchar(1000) DEFAULT NULL,
  `Type` varchar(1000) DEFAULT NULL,
  `Reviews` varchar(1000) DEFAULT NULL,
  `No of Reviews` varchar(1000) DEFAULT NULL,
  `Comments` varchar(1000) DEFAULT NULL,
  `Contact Number` varchar(1000) DEFAULT NULL,
  `Trip_advisor Url` varchar(1000) DEFAULT NULL,
  `Menu` varchar(1000) DEFAULT NULL, 
  `Price_Range` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
