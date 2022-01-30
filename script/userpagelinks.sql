/*select * from uinfo a where a.uname = '小琪子减脂';*/
#select * from userpagelinks a join (select uName from userpagelinks where id = 1) b on a.uname = b.uname where a.uname = '健身小乔';
#select * from userpagelinks a join (select uName from userpagelinks where id = 1) b on a.uname = b.uname where a.id = 1;
#select * from userpagelinks where uname = '健身小乔';
#create table tmp1 (uplink varchar(200), uname varchar(50) primary key);
#create table tmp2 (uname varchar(50) primary key);
#load data infile 'C:\\Users\\Bonn\\Desktop\\1.csv' into table tmp1 fields terminated by ',';
#load data infile 'C:\\Users\\Bonn\\Desktop\\2.csv' into table tmp2 fields terminated by ',';
#select * from tmp1 left join tmp2 on tmp1.uname = tmp2.uname limit 10000;
# into outfile 'C:\\Users\\Bonn\\Desktop\\1.csv'
#select count(*) from userpagelinks;
#delete from userpagelinks;
#CREATE TABLE tmp (ulink varchar(200));
#load data infile 'C:\\Users\\Bonn\\Desktop\\2.csv' into table tmp fields terminated by ',';
#CREATE TABLE tmp (uplink varchar(200) primary key);
#load data infile 'C:\\Users\\Bonn\\Desktop\\2.csv' into table tmp1 fields terminated by ',';

select * from tmp left join tmp1 on tmp.uplink = tmp1.uplink limit 10000;
#show create table tmp;
#show create table tmp1; 


