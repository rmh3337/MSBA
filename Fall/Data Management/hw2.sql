--Q1
select p.product, sum(f.sales) Sales, extract(year from f.factorydate) Year
from prodcoffee p, factcoffee f
where p.productid = f.productid and extract(year from f.factorydate) = 2013
group by p.product, extract(year from f.factorydate)
order by sum(f.sales) desc
fetch first 5 rows only;

--Q2
select x.areacode, s.state, x.sales, x.budgetsales
from statecoffee s, areacoffee a, (select areacode, budgetsales, sales
from factcoffee
where sales > budgetsales * 2 and budgetsales >= 100
and extract(year from factorydate) = 2012) x
where s.stateid = a.stateid and x.areacode = a.areacode
;

--q3
select sum(sales), extract(month from factorydate)
from factcoffee
where extract(year from factorydate) = 2012 
group by extract(month from factorydate)

having sum(sales) > (select avg(x.sales)
from (
        select sum(sales) as sales
        from factcoffee
        where extract(year from factorydate) = 2012
        group by extract(month from factorydate)
    ) x
)
order by extract(month from factorydate) 
;

--Q4
select difference_sales, areacode 
from(
    select (sum(sales) - sum(budgetsales)) difference_sales, areacode
    from factcoffee
    where extract(year from factorydate) = 2013
    group by areacode, extract(year from factorydate))
where difference_sales > (
    select avg(y.difference)
    from
    (select (sum(sales)-sum(budgetsales)) as difference
    from factcoffee
    where extract(year from factorydate) = 2013
    group by areacode) y
    )
order by areacode desc;
    
--Q5
select product, market, max_sales
from
( 
    select p.product product, s.market market, sum(f.sales) tot_sales
    from prodcoffee p, statecoffee s, factcoffee f, areacoffee a
    where extract(year from f.factorydate) = 2012 and p.productid = f.productid
    and a.areacode = f.areacode and s.stateid = a.stateid
    group by s.market, p.product),
    
    (select product1, max(tot_sales1) as max_sales
    from (
        select p.product as product1, s.market market1, sum(f.sales) tot_sales1
        from prodcoffee p, statecoffee s, factcoffee f, areacoffee a
        where extract(year from f.factorydate) = 2012 and p.productid = f.productid 
        and a.areacode = f.areacode and s.stateid = a.stateid
        group by s.market, p.product)
    group by product1
    )
where tot_sales = max_sales
order by max_sales desc;



