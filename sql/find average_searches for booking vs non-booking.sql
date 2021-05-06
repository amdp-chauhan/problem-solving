/*
Bookings vs Non-Bookings
------------------------
Reference: https://platform.stratascratch.com/coding-question?id=10124&python=

Display the number of times a user performed a search which led to a successful booking and the number of times a user performed a search but did not lead to a booking. The output should have a column named action with values 'does not book' and 'books' as well as a 2nd column named average_searches with the average number of searches per action. Consider that the booking did not happen if the booking date is null.

Table: airbnb_contacts, airbnb_searches

airbnb_contacts:
----------------
id_guest              varchar
id_host               varchar
id_listing            varchar
ts_contact_at         datetime
ts_reply_at           datetime
ts_accepted_at        datetime
ts_booking_at         datetime
ds_checkin            datetime
ds_checkout           datetime
n_guests              int
n_messages            int

airbnb_searches:
----------------
dsdatetime
id_user               varchar
ds_checkin            datetime
ds_checkout           datetime
n_searches            int
n_nights              float
n_guests_min          int
n_guests_max          int
origin_country        varchar
filter_price_min      float
filter_price_max      float
filter_room_types     varchar
filter_neighborhoods  datetime
*/



WITH search_action_outcome AS
    (SELECT ACo.id_guest, ACo.ts_booking_at, ASe.n_searches, 
        (CASE
            WHEN ACo.ts_booking_at IS NOT NULL
                THEN 'books'
            ELSE 'does not book'
        END) AS action 
    FROM airbnb_contacts ACo
    FULL OUTER JOIN airbnb_searches ASe
    ON ACo.id_guest = ASe.id_user)

SELECT action, (SUM(n_searches)/COUNT(*)) AS average_searches
FROM search_action_outcome
GROUP BY action
