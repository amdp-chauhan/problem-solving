/*
Table: world

Sample data: 

  name	    continent	    area	     population	    gdp
Afghanistan	  Asia	     652230	      25500100	  20343000000
Albania	     Europe	     28748	      2831741	    12960000000
Algeria	     Africa	    2381741	      37100000	  188681000000
Andorra	    Europe	      468         78115	      3712000000
Angola	    Africa	    1246700	      20609294	  100990000000

/*

-- 1. List each country name where the population is larger than that of 'Russia'.

SELECT name FROM world
  WHERE population >
     (SELECT population FROM world
      WHERE name='Russia')



-- 2. Show the countries in Europe with a per capita GDP greater than 'United Kingdom'.

SELECT w1.name
FROM world w1,
(SELECT gdp/population as uk_per_capita_gdp FROM world WHERE name='United Kingdom') w2
WHERE 
w1.gdp/w1.population > w2.uk_per_capita_gdp AND
w1.continent = 'Europe'



-- 3. List the name and continent of countries in the continents containing either Argentina or Australia. Order by name of the country.

SELECT name, continent
FROM world
WHERE
continent IN (SELECT continent FROM world WHERE name in ('Argentina', 'Australia'))



-- 4. Which country has a population that is more than Canada but less than Poland? Show the name and the population.

SELECT name, population
FROM world
WHERE
population > (SELECT population FROM world WHERE name='Canada') AND
population < (SELECT population FROM world WHERE name='Poland')



-- 5. Germany (population 80 million) has the largest population of the countries in Europe. Austria (population 8.5 million) has 11% of the population of Germany.
--    Show the name and the population of each country in Europe. Show the population as a percentage of the population of Germany.

SELECT name, CONCAT(CAST((w1.population*100)/w2.population AS NUMERIC), '%') as percentage
FROM
world w1,
(SELECT population FROM world WHERE name='Germany') w2
WHERE w1.continent = 'Europe'



-- 6. Which countries have a GDP greater than every country in Europe? [Give the name only.] (Some countries may have NULL gdp values)

SELECT name 
FROM world
WHERE gdp > (SELECT MAX(gdp) FROM world WHERE continent='Europe')



-- 7. Find the largest country (by area) in each continent, show the continent, the name and the area:

SELECT w2.continent, w2.name, w2.area
FROM
(SELECT continent, MAX(area) as max_area
 FROM world GROUP BY continent) AS w1
INNER JOIN world w2
ON w2.continent = w1.continent AND 
   w2.area = w1.max_area



-- 8. List each continent and the name of the country that comes first alphabetically.

SELECT continent, name
FROM
(SELECT continent, name, ROW_NUMBER() over (PARTITION BY continent ORDER BY name) as row_num
FROM world) as w2
WHERE w2.row_num=1



-- 9. Find the continents where all countries have a population <= 25000000. Then find the names of the countries associated with these continents. Show name, continent and population.

SELECT w1.name, w1.continent, w1.population 
FROM
world W1,
(SELECT continent, MAX(population) as max_pop
FROM world
GROUP BY continent HAVING MAX(population) <= 25000000) W2
WHERE W1.continent = W2.continent



-- 10. Some countries have populations more than three times that of any of their neighbours (in the same continent). Give the countries and continents.
with temp1 as
(SELECT w1.name, w1.continent from world w1
inner join
(select name, continent, population
from world) w2
ON w1.continent=w2.continent where w1.population>3*w2.population)

select table_1.name, table_1.continent  From
(select name, continent, count(*) as count_1 from temp1 group by continent, name) table_1
INNER JOIN
(select continent, count(*) as count_2 from world group by continent) table_2
ON table_1.continent = table_2.continent
WHERE table_1.count_1+1=table_2.count_2
