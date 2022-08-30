LOAD DATA LOCAL INFILE  
'/Users/hyoeungracepark/Desktop/restaurant_reviews/data/TripAdvisor_RestaurantRecommendation.csv'
INTO TABLE restaurant_reviews.tripadvisor_raw
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(`Name`,`Street Address` , `Location`, `Type`, `Reviews`, 
`No of Reviews`, `Comments`, `Contact Number`, 
`Trip_advisor Url`, `Menu`, `Price_Range`);