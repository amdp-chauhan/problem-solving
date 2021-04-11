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


Q1. Show the total population of the world.

SELECT SUM(population)
FROM world


Q2. List all the continents - just once each.

SELECT DISTINCT(continent) 
FROM world


Q3. Give the total GDP of Africa

SELECT sum(gdp)
FROM world
WHERE
continent='Africa'


Q4. How many countries have an area of at least 1000000

SELECT count(*) 
FROM world
WHERE area >= 1000000


Q5. What is the total population of ('Estonia', 'Latvia', 'Lithuania')

SELECT sum(population)
FROM world
WHERE name in ('Estonia', 'Latvia', 'Lithuania')


Q6. For each continent show the continent and number of countries.

SELECT continent, count(*)
FROM world
GROUP BY continent


Q7. For each continent show the continent and number of countries with populations of at least 10 million.

SELECT continent, count(*)
FROM world
WHERE population > 10000000
GROUP BY continent


Q8. List the continents that have a total population of at least 100 million.

SELECT continent
FROM world
GROUP BY continent HAVING SUM(population) > 100000000
