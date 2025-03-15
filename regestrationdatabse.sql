create database Regestration; -- creation of database
use Regestration; 
create table reg_info(
username varchar(50),
password varchar(50),
email varchar(50)
-- Age int,
-- Height int,  -- comma dalo info likhne ke liye
-- Gender varchar(20)
);


insert into reg_info(name,password,Email,Age,Height,Gender) 
values('zineera','zini5','kazizineera@gmail.com',19,5,'female');

insert into reg_info(name,password,Email,Age,Height,Gender) 
values('yusra','yusra5','yusrakazi@gmail.com',16,6,'female'),
('Iffat','iffat5','Iffatkazi@gmail.com',40,5,'female') ;


insert into reg_info(name,password,Email,Age,Gender) 
values('Tauhid','tauhid5','Tauhidkazi@gmail.com',50,'male') ;

-- [create database tablename;
-- use tablename
-- create table tablename
  drop table reg_info;
 -- drop database reg-info;]
 
 select * from `food and calories - sheet1`;
 select * from reg_info;
 
 
update reg_info set Height=6 where name='Tauhid';
delete from reg_info where name='Tauhid';
select * from reg_info;  -- read query
select * from reg_info where Age=40;
-- semi colon jo query end karna ho toh

