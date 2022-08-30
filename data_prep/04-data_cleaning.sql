-- To count the rows with no comments available
SELECT COUNT(*) 
FROM restaurant_reviews.tripadvisor_raw
WHERE comments = "";
-- To update NA comments with string: 'not available'
-- Ensures that sentimental analysis would work with Python
UPDATE restaurant_reviews.tripadvisor_raw 
SET comments = 'not available'
WHERE comments = "";
-- Export as CSV file (Execute query > Result Grid > Export)
SELECT *
FROM restaurant_reviews.tripadvisor_raw
LIMIT 3063;