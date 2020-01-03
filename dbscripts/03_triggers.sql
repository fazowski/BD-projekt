create trigger t_insert_winner after insert or update on referee_matchresult
    for each row
    execute procedure f_insert_winner();

drop trigger t_insert_winner on referee_matchresult;

create or replace function f_insert_winner()
returns trigger as
    $BODY$
    BEGIN
        if new.home_team_goals > new.away_team_goals then
            update referee_matchresult set winner = 'A' where id = new.id;
        else
            update referee_matchresult set winner = 'B' where id = new.id;
        end if;

        return new;
    end;
    $BODY$

language plpgsql volatile;