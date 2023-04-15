-- TamoBot Database Setup
-- Utilizing MySQL Server

-- Create Database
CREATE DATABASE serverId;
USE serverId;

-- Initialize Database Tables
CREATE TABLE user(
    id BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    drole VARCHAR(20),
    tokens INT UNSIGNED NOT NULL,
    stime BIGINT UNSIGNED NOT NULL,
    zoneid VARCHAR(60) NOT NULL,
    hex VARCHAR(7),
    feat VARCHAR(255),
    trivia INT UNSIGNED
);

CREATE TABLE monthtime(
    user_id BIGINT UNSIGNED NOT NULL,
    mth SMALLINT NOT NULL,
    yr SMALLINT NOT NULL,
    stime INT UNSIGNED NOT NULL,
    PRIMARY KEY (user_id, mth, yr),
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE dailytime(
    user_id BIGINT UNSIGNED NOT NULL,
    d SMALLINT NOT NULL,
    mth SMALLINT NOT NULL,
    yr SMALLINT NOT NULL,
    stime INT UNSIGNED NOT NULL,
    PRIMARY KEY (user_id, d, mth, yr),
    FOREIGN KEY (user_id) REFERENCES user(id)
);