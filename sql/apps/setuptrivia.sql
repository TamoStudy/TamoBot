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
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Which country gifted the Statue of Liberty to the United States?', 'Germany', 'France', 'Spain', 'Italy', 1, 'TamoBot', 'History');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('In what year did World War II end?', '1945', '1939', '1941', '1942', 0, 'TamoBot', 'History');

INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('What is the capital of Canada?', 'Ottawa', 'Toronto', 'Vancouver', 'Montreal', 0, 'TamoBot', 'Geography');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Who wrote the book "To Kill a Mockingbord"?', 'Ernest Hemingway', 'J.D. Salinger', 'Harper Lee', 'F. Scott Fitzgerald', 2, 'TamoBot', 'Literature');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('In which year did the first-ever iPhone release?', '2005', '2006', '2007', '2008', 2, 'TamoBot', 'Technology');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Who painted the famous artwork "The Starry Night"?', 'Vincent van Gogh', 'Pablo Picasso', 'Claude Monet', 'Salvador Dali', 0, 'TamoBot', 'Art');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('What is the name of the largest planet in our solar system?', 'Saturn', 'Mars', 'Jupiter', 'Venus', 2, 'TamoBot', 'Science');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Which continent is the smallest in terms of land area?', 'Europe', 'Asia', 'Australia', 'Antarctica', 3, 'TamoBot', 'Geography');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Who directed the movie "Jurassic Park"?', 'Steven Spielberg', 'James Cameron', 'Martin Scorsese', 'Quentin Tarantino', 0, 'TamoBot', 'Entertainment');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('What is the capital of Australia?', 'Melbourne', 'Canberra', 'Sydney', 'Brisbane', 1, 'TamoBot', 'Geography');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('What does the acronym "GPS" stand for?', 'Global Positioning System', 'General Product Specification', 'Graphical Processing System', 'Global Payment Service', 0, 'TamoBot', 'Technology');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Which gas makes up the majority of the Earth''s atmosphere?', 'Oxygen', 'Nitrogen', 'Carbon dioxide', 'Hydrogen', 1, 'TamoBot', 'Science');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Who was the first female Prime Minister of the United Kingdom?', 'Theresa May', 'Margaret Thatcher', 'Angela Merkel', 'Jacinda Ardern', 1, 'TamoBot', 'History');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('In which 1997 film did Leonardo DiCaprio and Kate Winslet co-star for the first time?', 'Titanic', 'Catch Me If You Can', 'The Departed', 'Revolutionary Road', 0, 'TamoBot', 'Entertainment');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Who wrote the novel "Pride and Prejudice"?', 'Emily Bronte', 'Charlotte Bronte', 'Jane Austen', 'Virginia Woolf', 2, 'TamoBot', 'Literature');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('As of April 2023, who is the current CEO of Google?', 'Sundar Pichai', 'Tim Cook', 'Larry Page', 'Jeff Bezos', 0, 'Tech Buddies Podcast', 'Technology');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('As of April 2023, who is the current CEO of Microsoft?', 'Bill Gates', 'Steve Ballmer', 'John W. Thompson', 'Satya Nadella', 3, 'Tech Buddies Podcast', 'Technology');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('As of April 2023, who is the current CEO of Apple?', 'John Sculley', 'Tim Cook', 'Mike Markkula', 'Steve Jobs', 1, 'Tech Buddies Podcast', 'Technology');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('What was the first brand in this mellenium to get a trillion dollar valuation?', 'Amazon', 'Telsa', 'Google', 'Apple', 3, 'Tech Buddies Podcast', 'Business');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('As of April 2023, what is the most populous country in the world?', 'India', 'United States', 'China', 'Brazil', 2, 'Tech Buddies Podcast', 'Geography');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Which city is popularly known as the floating city?', 'Venice', 'Bangkok', 'Amsterdam', 'Srinagar', 0, 'Tech Buddies Podcast', 'Geography');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('What is the capital of Somalia?', 'Hargeisa', 'Kismayo', 'Mogadishu', 'Bosaso', 2, 'Tech Buddies Podcast', 'Geography');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('In what year did the popular social media platform Facebook launch?', '2006', '2004', '2008', '2010', 1, 'TamoBot', 'Technology');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Which famous playwright wrote the plays "Hamlet", "Macbeth", and "Romeo and Juliet"?', 'Oscar Wilde', 'William Shakespeare', 'George Bernard Shaw', 'Tennesse Williams', 1, 'TamoBot', 'Literature');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('What is the tallest mountain in Africa?', 'Mount Everest', 'Mount Aconcagua', 'Mount Kilimanjaro', 'Mount Denali', 2, 'TamoBot', 'Geography');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Who directed the 1994 crime film "Pulp Fiction"?', 'Martin Scorsese', 'Quentin Tarantino', 'Steven Spielberg', 'Francis Ford Coppola', 0, 'TamoBot', 'Entertainment');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('In what year did the United States declare independence from Great Britain?', '1738', '1812', '1794', '1776', 3, 'TamoBot', 'History');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Which famous painting is housed in the Louvre Museum in Paris and depicts a woman with a mysterious smile?', 'The Scream', 'The Starry Night', 'The Mona Lisa', 'The Last Supper', 2, 'TamoBot', 'Art');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('In what year did World War I begin?', '1920', '1939', '1914', '1917', 2, 'TamoBot', 'History');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('What is the process by which plants convert sunlight into energy called?', 'Fermentation', 'Respiration', 'Photosynthesis', 'Glycolysis', 2, 'TamoBot', 'Science');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Which actor played the character of Neo in the movie "The Matrix"?', 'Tom Cruise', 'Leonardo Dicaprio', 'Brad Pitt', 'Keanu Reeves', 3, 'TamoBot', 'Entertainment');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Who wrote the book "The Catcher in the Rye"?', 'J.D Salinger', 'F. Scott Fitzgerald', 'Ernest Hemingway', 'William Faulkner', 0, 'TamoBot', 'Literature');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('In what year did the Berlin Wall fall?', '1989', '1991', '1993', '1983', 0, 'TamoBot', 'History');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Who is the founder of SpaceX?', 'Jeff Bezos', 'Elon Musk', 'Richard Branson', 'Mark Zuckerberg', 1, 'TamoBot', 'Technology');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Which part of the human ear play no role in hearing as such but is otherwise very much required?', 'Ear ossicle', 'Eustachian tube', 'Organ of corti', 'Vestibular apparatus', 3, 'Magic', 'Science');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Which of the following disorders is caused due to shortening of eyeball in anterio-posterior axis and can be corrected using convex lens?', 'Myopia', 'Glaucoma', 'Astigmatism', 'Hypermetropia', 3, 'Magic', 'Science');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Multipolar neurons are found in the...', 'Embryonic stage', 'Retina of the eye', 'Ear lobe', 'Cerebral cortex', 3, 'Magic', 'Science');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('One haemoglobin molecule carries a maximum of...', 'One molecule of oxygen', 'Two molecules of oxygen', 'Three molecules of oxygen', 'Four molecules of oxygen', 3, 'Magic', 'Science');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Who was the first woman to win a Nobel Prize?', 'Marie Curie', 'Dorothy Hodgkin', 'Rosalind Franklin', 'Barbara McClintock', 0, 'TamoBot', 'History');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Which Asian country is the largest in terms of land area?', 'China', 'India', 'Russia', 'Japan', 2, 'TamoBot', 'Geography');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('What is the smallest bone in the human body?', 'Incus', 'Stapes', 'Malleus', 'Hyoid', 1, 'TamoBot', 'Science');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Who was the first person to fly solo across the Atlantic Ocean?', 'Amelia Earhart', 'Charles Lindbergh', 'Bessie Coleman', 'Wilbur Wright', 1, 'TamoBot', 'History');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Which social media platform was founded by Mark Zuckerberg?', 'LinkedIn', 'Facebook', 'Twitter', 'Instagram', 1, 'TamoBot', 'Technology');
INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) VALUES ('Which planet in our solar system has the most moons?', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 0, 'TamoBot', 'Science');

INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) 
VALUES 
('In which city would you find the Eiffel Tower?', 'Paris', 'London', 'Berlin', 'New York', 0, 'TamoBot', 'Geography'),
('What is the smallest country in the world?', 'Monaco', 'Vatican City', 'San Marino', 'Liechtenstein', 1, 'TamoBot', 'Geography'),
('Which of the following countries does not have a monarchy?', 'Japan', 'Norway', 'Thailand', 'Italy', 3, 'TamoBot', 'History'),
('Who is the author of the book "The Hunger Games"?', 'Suzanne Collins', 'J.K. Rowling', 'Stephenie Meyer', 'Veronica Roth', 0, 'TamoBot', 'Literature'),
('What is the capital of Canada?', 'Ottawa', 'Toronto', 'Montreal', 'Vancouver', 0, 'TamoBot', 'Geography'),
('What is the chemical symbol for gold?', 'Au', 'Ag', 'Cu', 'Fe', 0, 'TamoBot', 'Science'),
('What is the name of the highest mountain in Africa?', 'Mount Kilimanjaro', 'Mount Everest', 'Mount Fuji', 'Mount Denali', 0, 'TamoBot', 'Geography'),
('Which actress played Hermione Granger in the "Harry Potter" movies?', 'Emma Watson', 'Emma Stone', 'Emma Roberts', 'Emma Thompson', 0, 'TamoBot', 'Entertainment'),
('What is the name of the first man to walk on the moon?', 'Neil Armstrong', 'Buzz Aldrin', 'Michael Collins', 'Yuri Gagarin', 0, 'TamoBot', 'History'),
('What is the largest continent in the world?', 'Asia', 'Africa', 'North America', 'South America', 0, 'TamoBot', 'Geography'),
('What is the highest number on a standard roulette wheel?', '36', '38', '40', '42', 1, 'TamoBot', 'Entertainment'),
('What is the name of the famous Parisian cabaret that was established in 1889?', 'Moulin Rouge', 'Lido', 'Folies Bergère', 'Crazy Horse', 0, 'TamoBot', 'Entertainment'),
('What is the name of the world''s largest ocean?', 'Pacific', 'Atlantic', 'Indian', 'Arctic', 0, 'TamoBot', 'Geography'),
('Who painted the famous work "The Starry Night"?', 'Vincent van Gogh', 'Pablo Picasso', 'Claude Monet', 'Leonardo da Vinci', 0, 'TamoBot', 'Art'),
('What is the chemical symbol for silver?', 'Ag', 'Au', 'Cu', 'Fe', 0, 'TamoBot', 'Science'),
('Which of the following is not one of the four main components of blood?', 'Plasma', 'Calcium', 'Red blood cells', 'White blood cells', 1, 'TamoBot', 'Science'),
('Who was the lead singer of the rock band Queen?', 'John Lennon', 'Freddie Mercury', 'David Bowie', 'Elvis Presley', 1, 'TamoBot', 'Entertainment');

INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) 
VALUES 
('Who invented the telephone?', 'Alexander Graham Bell', 'Thomas Edison', 'Nikola Tesla', 'Michael Faraday', 0, 'TamoBot', 'History'),
('What is the name of the world''s largest desert?', 'Sahara', 'Gobi', 'Arabian', 'Kalahari', 0, 'TamoBot', 'Geography'),
('Which element has the chemical symbol "Hg"?', 'Mercury', 'Hydrogen', 'Helium', 'Manganese', 0, 'TamoBot', 'Science'),
('What is the currency of Japan?', 'Dollar', 'Won', 'Rupee', 'Yen', 3, 'TamoBot', 'Geography'),
('What was the name of the first spacecraft to land on the moon?', 'Apollo 11', 'Sputnik 1', 'Voyager 1', 'Chandrayaan-1', 0, 'TamoBot', 'Science'),
('What is the name of the largest lake in Africa?', 'Lake Victoria', 'Lake Tanganyika', 'Lake Malawi', 'Lake Chad', 0, 'TamoBot', 'Geography'),
('Which metal is known as the "most expensive metal" in the world?', 'Rhodium', 'Gold', 'Platinum', 'Silver', 0, 'TamoBot', 'Science'),
('Which of the following is not a programming language?', 'Ruby', 'Java', 'Python', 'Microsoft', 3, 'TamoBot', 'Technology'),
('What is the name of the currency used in Switzerland?', 'Swiss franc', 'Swiss dollar', 'Swiss pound', 'Swiss euro', 0, 'TamoBot', 'Geography');

INSERT INTO triviaquestion (title, option_a, option_b, option_c, option_d, correct, author, category) 
VALUES 
('What is the tallest mammal on Earth?', 'Elephant', 'Giraffe', 'Hippopotamus', 'Rhinoceros', 1, 'TamoBot', 'Science'),
('What is the name of the currency used in South Africa?', 'Dollar', 'Rand', 'Euro', 'Pound', 1, 'TamoBot', 'Geography'),
('Who invented the World Wide Web (WWW)?', 'Steve Jobs', 'Bill Gates', 'Tim Berners-Lee', 'Mark Zuckerberg', 2, 'TamoBot', 'Technology'),
('What is the name of the largest waterfall in the world?', 'Victoria Falls', 'Niagara Falls', 'Angel Falls', 'Iguaçu Falls', 0, 'TamoBot', 'Geography'),
('What is the chemical symbol for the element potassium?', 'P', 'K', 'Po', 'Pt', 1, 'TamoBot', 'Science');






