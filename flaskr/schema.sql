DROP TABLE IF EXISTS tracks;

CREATE TABLE tracks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  artist TEXT NOT NULL,
  genre TEXT NOT NULL,
  lenght INTEGER NOT NULL
);


    INSERT INTO tracks (title, artist, genre, lenght)
    VALUES
        ('The Astronaut', 'JIN', 'K-Pop', 146),
        ('All Eyes on Me', 'Dj Belite', 'Dance', 157),
        ('Daylight', 'David Kushner', 'Pop', 134),
        ('All My Life (feat. J. Cole)', 'Lil Durk', 'Hip-Hop/Rap', 183),
        ('Makeba', 'Jain', 'Pop', 171),
        ('Calm Down','Rema','Afrobeats', 193),
        ('Holiday', 'Rema','Afrobeats', 198),
        ('White Tee','Summer Walker & NO1-NOAH','R&B/Soul',195),
        ('Smooth Operator','Sade','Pop',175),
        ('Heart of Steel','TVORCHI','Pop',187);



