tripadvisor_raw = read_csv("data/TripAdvisor_RestauarantRecommendation.csv")
tripadvisor_raw <- tripadvisor_raw %>% mutate(
  Comments = str_replace_na(Comments, "not available")
)
write_csv(tripadvisor_raw, "data/tripadvisor_raw.csv")
