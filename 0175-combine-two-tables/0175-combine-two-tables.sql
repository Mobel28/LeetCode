# Write your MySQL query statement below
select p.firstname as firstName,p.lastname as lastName,a.city,a.state from person p 
left join address a on p.personId=a.personId;