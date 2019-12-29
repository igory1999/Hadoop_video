-- Reading records from a simple csv file, where records are separated by ',', into a Pig relation
-- If data type is not specified, Pig will figure it out. If it is, it might improve performance

records = LOAD 'pig/test1.csv' USING PigStorage(',') AS (name, age:int, money:float);
-- Print schema
describe records;
-- Dump relation to screen. Pig is translated into MapReduce and job is launched.
dump records;

-- Project only some columns from a relation
projection = FOREACH records GENERATE name,money;
describe projection;
dump projection;

-- If we want to apply some aggregation to a column, records must be grouped first
mrecs = GROUP records ALL;
describe mrecs;
dump mrecs;

tot = FOREACH mrecs GENERATE SUM(records.money);
dump tot;

--Suppose we want to find average money per age group and measure the size of the age group

agegroups = GROUP records by age;
describe agegroups;
dump agegroups;

avgmoneyperage = FOREACH agegroups GENERATE group, AVG(records.money);
describe avgmoneyperage;
dump avgmoneyperage;

countagegroup = FOREACH agegroups GENERATE group, COUNT(records);
dump countagegroup;


--Select only 3 records
records3 = limit records 3;
dump records3;

--Filter records by some condition
records4 = filter records by age > 20;
dump records4;

-- Derive a new columns
records5 = foreach records generate name, money/age as mpa;
describe records5;
dump records5;

-- Inner join by name
records6 = join records by name, records5 by name;
describe records6;
dump records6;

