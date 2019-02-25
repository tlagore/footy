CREATE TABLE "player" (
  "id" int PRIMARY KEY,
  "firstname" varchar,
  "lastname" varchar,
  "position" char,
  "nationality" varchar,
  "age" int,
  "weight" varchar
);

CREATE TABLE "team" (
  "id" int PRIMARY KEY,
  "name" varchar UNIQUE,
  "country" varchar,
  "city" varchar
);

CREATE TABLE "matchstats" (
  "id" int PRIMARY KEY,
  "player" int,
  "team" int,
  "goals" int,
  "match" int,
  "minutesplayed" int,
  "penaltykicks" int,
  "shotsontarget" int,
  "goalsconceded" int,
  "assists" int,
  "foulscommited" int,
  "foulssuffered" int,
  "yellowcards" int,
  "redcards" int,
  UNIQUE(player,match)
);

CREATE TABLE "aggregatedstats" (
  "id" int PRIMARY KEY,
  "player" int,
  "team" int,
  "season" int,
  "league" int,
  "goals" int,
  "minutesplayed" int,
  "penaltykicks" int,
  "shotsontarget" int,
  "goalsconceded" int,
  "assists" int,
  "foulscommited" int,
  "foulssuffered" int,
  "yellowcards" int,
  "redcards" int,
  UNIQUE(player,team,season,league)
);

CREATE TABLE "season" (
  "id" int PRIMARY KEY,
  "startdate" date,
  "enddate" date,
  UNIQUE(startdate,enddate)
);

CREATE TABLE "league" (
  "id" int PRIMARY KEY,
  "name" varchar UNIQUE,
  "descripton" varchar
);

CREATE TABLE "match" (
  "id" int PRIMARY KEY,
  "playedon" date,
  "home" int,
  "away" int,
  "season" int,
  "league" int,
  UNIQUE(playedon, home, away, season, league)
);

ALTER TABLE "match" ADD FOREIGN KEY ("home") REFERENCES "team" ("id");

ALTER TABLE "match" ADD FOREIGN KEY ("away") REFERENCES "team" ("id");

ALTER TABLE "match" ADD FOREIGN KEY ("season") REFERENCES "season" ("id");

ALTER TABLE "match" ADD FOREIGN KEY ("league") REFERENCES "league" ("id");

ALTER TABLE "matchstats" ADD FOREIGN KEY ("team") REFERENCES "team" ("id");

ALTER TABLE "matchstats" ADD FOREIGN KEY ("player") REFERENCES "player" ("id");

ALTER TABLE "matchstats" ADD FOREIGN KEY ("match") REFERENCES "match" ("id");

ALTER TABLE "aggregatedstats" ADD FOREIGN KEY ("team") REFERENCES "team" ("id");

ALTER TABLE "aggregatedstats" ADD FOREIGN KEY ("league") REFERENCES "league" ("id");

ALTER TABLE "aggregatedstats" ADD FOREIGN KEY ("season") REFERENCES "season" ("id");

ALTER TABLE "aggregatedstats" ADD FOREIGN KEY ("player") REFERENCES "player" ("id");