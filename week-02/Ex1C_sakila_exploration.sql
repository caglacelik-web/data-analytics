/*
a) The actor table includes information about actors such as actor_id, first_name, last_name, and last_update.
b) The film table includes information about films such as film_id, title, description, release_year, language_id, rental information, rating, and other movie details.
c) The film_actor table contains both actor_id and film_id.
d) The rental table includes information about rentals such as rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, and last_update. This information is somewhat hard to read by itself because it mostly uses IDs instead of descriptive names.
e) The inventory table includes information about inventory items such as inventory_id, film_id, store_id, and last_update.
f) To understand the names of all films rented on a specific date you need the rental, inventory, and film tables. The rental table tells you when something was rented, the inventory table connects a rental to a specific film copy and the film table gives the film title.
*/

SELECT rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;