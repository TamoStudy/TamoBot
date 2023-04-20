-- TamoBot Trivia Question Creation
-- Utilizing MySQL Server

USE serverId;

-- Initialize triviaquestion database table
CREATE TABLE triviaquestion(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    title VARCHAR(500) NOT NULL,
    option_a VARCHAR(100) NOT NULL,
    option_b VARCHAR(100) NOT NULL,
    option_c VARCHAR(100) NOT NULL,
    option_d VARCHAR(100) NOT NULL,
    correct SMALLINT NOT NULL,
    author VARCHAR(100) NOT NULL,
    category VARCHAR(100) NOT NULL,
    PRIMARY KEY (id)
);

-- Create sample trivia questions
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('What is Discord''s signature color?', 'Red', 'Blurple', 'Green', 'Gray', 1, 'TamoBot', 'Entertainment');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('What is the capital of France?', 'Berlin', 'Paris', 'Madrid', 'Rome', 1, 'TamoBot', 'Geography');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Who was the first person to walk the moon?', 'Neil Armstrong', 'Buzz Aldrin', 'Michael Collins', 'Yuri Gagarin', 0, 'TamoBot', 'Science');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Which planet in our solar system is known as the "Red Planet"?', 'Jupiter', 'Mars', 'Venus', 'Saturn', 1, 'TamoBot', 'Science');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Which famous scientist wrote the book "A Brief History of Time"?', 'Albert Einstein', 'Stephen Hawking', 'Isaac Newton', 'Galileo Galilei', 1, 'TamoBot', 'Science');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Which country gifted the Statue of Liberty to the United States?', 'Berlin', 'Paris', 'Madrid', 'Rome', 1, 'TamoBot', 'History');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('In what year did World War II end?', '1945', '1939', '1941', '1942', 0, 'TamoBot', 'History');