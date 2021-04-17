/*
Host Popularity Rental Prices
-----------------------------

You’re given a table of rental property searches by users. The table consists of search results and outputs host information for searchers. Find the minimum, average, maximum rental prices for each host’s popularity rating. The host’s popularity rating is defined as below:
    0 reviews: New
    1 to 5 reviews: Rising
    6 to 15 reviews: Trending Up
    16 to 40 reviews: Popular
    more than 40 reviews: Hot

Tip: The `id` column in the table refers to the search ID. You'll need to create your own host_id by concating price, room_type, host_since, zipcode, and number_of_reviews.

Table: airbnb_host_searches

      id                          int
      price                       float                              
      property_type               varchar
      room_type                   varchar
      amenities                   varchar
      accommodates                int
      bathrooms                   int
      bed_type                    varchar
      cancellation_policy         varchar
      cleaning_fee                bool
      city                        varchar
      host_identity_verified      varchar
      host_response_rate          varchar
      host_since                  datetime
      neighbourhood               varchar
      number_of_reviews           int
      review_scores_rating        float
      zipcode                     int
      bedrooms                    int
      beds                        int

*/

-- Creating host_population_table
WITH host_population_table AS
    (SELECT 
        RANK() OVER(ORDER BY price, room_type, host_since, zipcode) AS id, 
        price, room_type, host_since, zipcode, 
        SUM(number_of_reviews) AS host_reviews, 
        (CASE
            WHEN SUM(number_of_reviews)=0 
                THEN 'New'
            WHEN SUM(number_of_reviews)>=1 AND SUM(number_of_reviews)<=5 
                THEN 'Rising'
            WHEN SUM(number_of_reviews)>=6 AND SUM(number_of_reviews)<=15 
                THEN 'Trending Up'
            WHEN SUM(number_of_reviews)>=16 AND SUM(number_of_reviews)<=40 
                THEN 'Popular'
            ELSE 'Hot'
        END) AS popularity
    FROM airbnb_host_searches
    GROUP BY (price, room_type, host_since, zipcode)
    ORDER BY id)


-- Aggregate prices over groupbed popularities
SELECT 
    popularity,
    MIN(price) AS min_retail_price,
    AVG(price) AS avg_retail_price,
    MAX(price) AS max_retail_price
FROM host_population_table
GROUP BY popularity
