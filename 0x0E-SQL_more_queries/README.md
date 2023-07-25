# SQL - More queries

This project is about SQL more queries and it covers topics such as creating users and granting privileges, using primary and foreign keys, using constraints, retrieving data from multiple tables, using subqueries, joins and unions.

## Tasks

| Tasks | File name | Description |
| ----- | --------- | ----------- |
| 0. My privileges! | [0-privileges.sql](0-privileges.sql) | Lists all privileges of the MySQL users user_0d_1 and user_0d_2 on the server. |
| 1. Root user | [1-create_user.sql](1-create_user.sql) | Creates the MySQL server user user_0d_1 with all privileges and password 0d_1_pwd. |
| 2. Read user | [2-create_read_user.sql](2-create_read_user.sql) | Creates the database hbtn_0d_2 and the user user_0d_2 with password 0d_2_pwd and only SELECT privilege in the database hbtn_0d_2. |
| 3. Always a name | [3-force_name.sql](3-force_name.sql) | Creates the table force_name on the database hbtn_0d_2 with name as non-nullable varchar(256). |
| 4. ID can't be null | [4-never_empty.sql](4-never_empty.sql) | Creates the table id_not_null on the database hbtn_0d_2 with id as non-nullable integer with auto increment and name as non-nullable varchar(256). |
| 5. Unique ID | [5-unique_id.sql](5-unique_id.sql) | Creates the table unique_id on the database hbtn_0d_2 with id as non-nullable integer with auto increment, unique and name as non-nullable varchar(256). |
| 6. States table | [6-states.sql](6-states.sql) | Creates the database hbtn_0d_usa and the table states in it with id as non-nullable integer with auto increment, unique, primary key and name as non-nullable varchar(256). |
| 7. Cities table | [7-cities.sql](7-cities.sql) | Creates the database hbtn_0d_usa and the table cities in it with id as non-nullable integer with auto increment, unique, primary key, state_id as non-nullable integer that references states.id and name as non-nullable varchar(256). |
| 8. Cities of California | [8-cities_of_california_subquery.sql](8-cities_of_california_subquery.sql) | Lists all the cities of California that can be found in the database hbtn_0d_usa using a subquery. |
| 9. Cities by States | [9-cities_by_state_join.sql](9-cities_by_state_join.sql) | Lists all cities contained in the database hbtn_0d_usa using a JOIN statement. |
| 10. Genre ID by show | [10-genre_id_by_show.sql](10-genre_id_by_show.sql) | Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked using a JOIN statement. |
| 11. Genre ID for all shows | [11-genre_id_all_shows.sql](11-genre_id_all_shows.sql) | Lists all shows contained in the database hbtn_0d_tvshows using a LEFT JOIN statement. |
| 12. No genre | [12-no_genre.sql](12-no_genre.sql) | Lists all shows contained in hbtn_0d_tvshows without a genre linked using a LEFT JOIN statement. |
| 13. Number of shows by genre | [13-count_shows_by_genre.sql](13-count_shows_by_genre.sql) | Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each using a JOIN statement. |
| 14. My genres | [14-my_genres.sql](14-my_genres.sql) | Uses the hbtn_0d_tvshows database to list all genres of the show Dexter using a JOIN statement. |
| 15. Only Comedy | [15-comedy_only.sql](15-comedy_only.sql) | Lists all Comedy shows in the database hbtn_0d_tvshows using a JOIN statement. |
| 16. List shows and genres | [16-shows_by_genre.sql](16-shows_by_genre.sql) | Lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows using a JOIN statement. |

## Advanced Tasks

| Tasks | File name | Description |
| --- | --- | --- |
| 17. Not my genre | [16-shows_by_genre.sql](16-shows_by_genre.sql) | List all genres not linked to the show Dexter |
| 18. No Comedy tonight! | [100-not_my_genres.sql](100-not_my_genres.sql) | List all shows without the genre Comedy in the database hbtn_0d_tvshows |
| 19. Rotten tomatoes | [101-not_a_comedy.sql](101-not_a_comedy.sql) | List all shows with a score greater or equal to 8.5 in the database hbtn_0d_tvshows |
