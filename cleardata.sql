

create table temp0 as
select * from marks
UNION
select * from med
UNION
select * from nuggs
UNION
select * from lytics;


create table articles as
	select trim(body) as body
	from temp0
	where length(body)>2200
	group by body
	having count(*)<2
	union
	select trim(body) as body
	from temp0
	where length(body)>2200
	group by body
	having count(*)>1;
	
create table article_titles as
	select trim(title) as title
	from temp0
	where length(body)>2200
	group by title
	having count(*)<2
	union
	select trim(title) as title
	from temp0
	where length(body)>2200
	group by title
	having count(*)>1
	
	
	


