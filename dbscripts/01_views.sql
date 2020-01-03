create or replace view v_match_details as
select
       rm.match_number AS MATCH_NUMBER,
       rm.date_time AS DATE_TIME,
       rmc.name AS MATCH_CATEGORY,
       rtA.name AS HOME_TEAM,
       rtB.name as AWAY_TEAM,
       auA.last_name as REFEREE_A,
       auB.last_name as REFEREE_B,
       rmr.home_team_goals as HOME_TEAM_GOALS,
       rmr.away_team_goals as AWAY_TEAM_GOALS
from
     referee_match rm
join referee_matchcategory rmc on rm.match_category_id = rmc.id
join referee_team rtA on rm.home_team_id = rtA.id
join referee_team rtB on rm.away_team_id = rtB.id
join referee_matchresult rmr on rm.id = rmr.match_id
join auth_user auA on rm.referee_a_id = auA.id
join auth_user auB on rm.referee_b_id = auB.id;

-- Wyświetlanie danych sędziego

create or replace view v_ref_details as
select
    au.first_name,
    au.last_name,
    rr.city,
    rr.referee_level,
    rr.telephone
from
     auth_user au
join referee_refereedetails rr on au.id = rr.user_id;

select * from v_match_details;
select * from v_ref_details;