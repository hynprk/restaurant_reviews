## Draft ##
unique(tripadvisor["Price_Range"])
tripadvisor %>% filter(`Price_Range` %in% c("American", "Italian", "Not Specified"))
states <- str_extract(pattern = "([A-Z]+){2}", string = tripadvisor_raw$Location)
gsub(pattern = ".*,\\s(.*)\\s.*", replacement = "\\1", x = tripadvisor_raw$Location)
grepl("Vegan|Vegetarian", c("veg friend", "Vegan Friendly", "Vegetarian Options"))
unique(tripadvisor_cleaned["state"])
unique(tripadvisor_cleaned["city"])

tripadvisor_cleaned %>% filter(is.na(state)) # Part of Canada according to borders
tripadvisor_cleaned[rowSums(is.na(tripadvisor_cleaned)) > 0, ] # Check types that are missing