BEGIN;
--
-- Create model Match
--
CREATE TABLE "referee_match" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "match_number" varchar(10) NOT NULL, "date_time" datetime NOT NULL);
--
-- Create model MatchCategory
--
CREATE TABLE "referee_matchcategory" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL);
--
-- Create model MatchStatus
--
CREATE TABLE "referee_matchstatus" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "next_status" integer NULL);
--
-- Create model Team
--
CREATE TABLE "referee_team" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "city" varchar(50) NOT NULL, "telephone" varchar(11) NULL);
--
-- Create model RefereeDetails
--
CREATE TABLE "referee_refereedetails" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "referee_level" integer NOT NULL, "city" varchar(50) NULL, "telephone" varchar(11) NULL, "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model MatchResult
--
CREATE TABLE "referee_matchresult" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "home_team_goals" integer NULL, "away_team_goals" integer NULL, "winner" varchar(1) NULL, "match_id" integer NOT NULL REFERENCES "referee_match" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Add field away_team to match
--
CREATE TABLE "new__referee_match" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "match_number" varchar(10) NOT NULL, "date_time" datetime NOT NULL, "away_team_id" integer NULL REFERENCES "referee_team" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__referee_match" ("id", "match_number", "date_time", "away_team_id") SELECT "id", "match_number", "date_time", NULL FROM "referee_match";
DROP TABLE "referee_match";
ALTER TABLE "new__referee_match" RENAME TO "referee_match";
CREATE INDEX "referee_matchresult_match_id_ef3a6230" ON "referee_matchresult" ("match_id");
CREATE INDEX "referee_match_away_team_id_c610d9db" ON "referee_match" ("away_team_id");
--
-- Add field home_team to match
--
CREATE TABLE "new__referee_match" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "match_number" varchar(10) NOT NULL, "date_time" datetime NOT NULL, "away_team_id" integer NULL REFERENCES "referee_team" ("id") DEFERRABLE INITIALLY DEFERRED, "home_team_id" integer NULL REFERENCES "referee_team" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__referee_match" ("id", "match_number", "date_time", "away_team_id", "home_team_id") SELECT "id", "match_number", "date_time", "away_team_id", NULL FROM "referee_match";
DROP TABLE "referee_match";
ALTER TABLE "new__referee_match" RENAME TO "referee_match";
CREATE INDEX "referee_match_away_team_id_c610d9db" ON "referee_match" ("away_team_id");
CREATE INDEX "referee_match_home_team_id_1b045be1" ON "referee_match" ("home_team_id");
--
-- Add field match_category to match
--
CREATE TABLE "new__referee_match" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "match_number" varchar(10) NOT NULL, "date_time" datetime NOT NULL, "away_team_id" integer NULL REFERENCES "referee_team" ("id") DEFERRABLE INITIALLY DEFERRED, "home_team_id" integer NULL REFERENCES "referee_team" ("id") DEFERRABLE INITIALLY DEFERRED, "match_category_id" integer NULL REFERENCES "referee_matchcategory" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__referee_match" ("id", "match_number", "date_time", "away_team_id", "home_team_id", "match_category_id") SELECT "id", "match_number", "date_time", "away_team_id", "home_team_id", NULL FROM "referee_match";
DROP TABLE "referee_match";
ALTER TABLE "new__referee_match" RENAME TO "referee_match";
CREATE INDEX "referee_match_away_team_id_c610d9db" ON "referee_match" ("away_team_id");
CREATE INDEX "referee_match_home_team_id_1b045be1" ON "referee_match" ("home_team_id");
CREATE INDEX "referee_match_match_category_id_e3380a10" ON "referee_match" ("match_category_id");
--
-- Add field referee_a to match
--
CREATE TABLE "new__referee_match" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "match_number" varchar(10) NOT NULL, "date_time" datetime NOT NULL, "away_team_id" integer NULL REFERENCES "referee_team" ("id") DEFERRABLE INITIALLY DEFERRED, "home_team_id" integer NULL REFERENCES "referee_team" ("id") DEFERRABLE INITIALLY DEFERRED, "match_category_id" integer NULL REFERENCES "referee_matchcategory" ("id") DEFERRABLE INITIALLY DEFERRED, "referee_a_id" integer NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__referee_match" ("id", "match_number", "date_time", "away_team_id", "home_team_id", "match_category_id", "referee_a_id") SELECT "id", "match_number", "date_time", "away_team_id", "home_team_id", "match_category_id", NULL FROM "referee_match";
DROP TABLE "referee_match";
ALTER TABLE "new__referee_match" RENAME TO "referee_match";
CREATE INDEX "referee_match_away_team_id_c610d9db" ON "referee_match" ("away_team_id");
CREATE INDEX "referee_match_home_team_id_1b045be1" ON "referee_match" ("home_team_id");
CREATE INDEX "referee_match_match_category_id_e3380a10" ON "referee_match" ("match_category_id");
CREATE INDEX "referee_match_referee_a_id_7d3b306c" ON "referee_match" ("referee_a_id");
--
-- Add field referee_b to match
--
CREATE TABLE "new__referee_match" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "match_number" varchar(10) NOT NULL, "date_time" datetime NOT NULL, "away_team_id" integer NULL REFERENCES "referee_team" ("id") DEFERRABLE INITIALLY DEFERRED, "home_team_id" integer NULL REFERENCES "referee_team" ("id") DEFERRABLE INITIALLY DEFERRED, "match_category_id" integer NULL REFERENCES "referee_matchcategory" ("id") DEFERRABLE INITIALLY DEFERRED, "referee_a_id" integer NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "referee_b_id" integer NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__referee_match" ("id", "match_number", "date_time", "away_team_id", "home_team_id", "match_category_id", "referee_a_id", "referee_b_id") SELECT "id", "match_number", "date_time", "away_team_id", "home_team_id", "match_category_id", "referee_a_id", NULL FROM "referee_match";
DROP TABLE "referee_match";
ALTER TABLE "new__referee_match" RENAME TO "referee_match";
CREATE INDEX "referee_match_away_team_id_c610d9db" ON "referee_match" ("away_team_id");
CREATE INDEX "referee_match_home_team_id_1b045be1" ON "referee_match" ("home_team_id");
CREATE INDEX "referee_match_match_category_id_e3380a10" ON "referee_match" ("match_category_id");
CREATE INDEX "referee_match_referee_a_id_7d3b306c" ON "referee_match" ("referee_a_id");
CREATE INDEX "referee_match_referee_b_id_62223afe" ON "referee_match" ("referee_b_id");
COMMIT;
