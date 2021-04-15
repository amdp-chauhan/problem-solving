/*
Question:

Growth of Airbnb
Estimate the growth of Airbnb each year using the number of hosts registered as the growth metric. The rate of growth is calculated by taking ((number of hosts registered in the current year - number of hosts registered in the previous year) / the number of hosts registered in the previous year) * 100.
Output the year, number of hosts in the current year, number of hosts in the previous year, and the rate of growth. Round the rate of growth to the nearest percent and order the result in the ascending order based on the year.
Assume that the dataset consists only of unique hosts, meaning there are no duplicate hosts listed.

Columns:

id                        int
price                     float
property_type             varchar
room_type                 varchar
amenities                 varchar
accommodates              int
bathrooms                 int
bed_type                  varchar
cancellation_policy       varchar
cleaning_fee              bool
cityvar                   char
host_identity_verified    varchar
host_response_rate        varchar
host_since                datetime
neighbourhood             varchar
number_of_reviews         int
review_scores_rating      float
zipcode                   int
bedrooms                  int
beds                      int

*/


WITH airbnb_yearly_host AS
    (SELECT EXTRACT(YEAR FROM host_since) AS year,
           COUNT(*) AS num_of_current_year_host
    FROM airbnb_search_details
    GROUP BY EXTRACT(YEAR FROM host_since)
    ORDER BY EXTRACT(YEAR FROM host_since)) 

SELECT year,
       num_of_current_year_host,
       num_of_last_year_host,
       (((num_of_current_year_host - num_of_last_year_host)*100)/num_of_last_year_host) AS rate_of_growth
FROM
    (SELECT year,
           num_of_current_year_host,
           LAG(num_of_current_year_host, 1) OVER (ORDER BY year) as num_of_last_year_host
    FROM airbnb_yearly_host) AS yearly_moving_table
