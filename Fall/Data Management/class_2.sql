select statecoffee.state, areacoffee.areacode, sum(sales)
from factcoffee, areacoffee, statecoffee,
(   
    select x.stateid, avg(x.sumsales) as avgsales
    from(
        select statecoffee.stateid, areacoffee.areacode, sum(sales) as sumsales
        from factcoffee, areacoffee, statecoffee
        where factcoffee.areacode = areacoffee.areacode
            and areacoffee.stateid = statecoffee.stateid
            and extract(year from factorydate) = 2013
        group by areacoffee.areacode, statecoffee.stateid
        ) x
    group by x.stateid
    ) avgsales
where factcoffee.areacode = areacoffee.areacode
    and areacoffee.stateid = statecoffee.stateid
    and avgsales.stateid=areacoffee.stateid
    and extract(year from factorydate)=2013
group by statecoffee.state, areacoffee.areacode, avgsales.avgsales
having sum(sales) > 1.1*avgsales.avgsales;
