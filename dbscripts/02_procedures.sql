-- 1. Pokazywanie drużyn z danego miasta
create or replace function f_show_teams_from_city(t_city varchar)
returns setof referee_team
    language sql
    as
    $$
        select * from referee_team rt where rt.city = t_city;
    $$;

-- 2. Wyświetlanie sędziów z danego miasta
create or replace function f_show_ref_from_city(r_city varchar)
returns setof v_ref_details
language sql
as
    $$
        select * from v_ref_details vrd where vrd.city = r_city;
    $$;

-- 3. Wyświetlanie meczy gdzie dana drużyna jest gospodarzem
create or replace function f_show_matches_where_team_is_home(f_team varchar)
returns setof v_match_details
language sql
as
    $$
        select * from v_match_details vmd where vmd.home_team = f_team;
    $$;

-- 4. Wyświetlanie meczy gdzie dana drużyna jest gościem
create or replace function f_show_matches_where_team_is_away(f_team varchar)
returns setof v_match_details
language sql
as
    $$
        select * from v_match_details vmd where vmd.away_team = f_team;
    $$;


-- create or replace procedure p_change_match_status()
-- language sql
-- as
--     $$
--
--     $$;