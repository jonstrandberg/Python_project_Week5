import pdb

from models.album import Album
from models.record_label import Record_label

import repositories.record_label_repository as record_label_repository
import repositories.album_repository as album_repository

record_label_1 = Record_label("Warner Bros", "Los Angeles", 1958)
record_label_repository.save(record_label_1)
record_label_2 = Record_label("EMI", "London", 1934)
record_label_repository.save(record_label_2)
record_label_3 = Record_label("Colombia", "Washington D.C", 1887)
record_label_repository.save(record_label_3)
record_label_4 = Record_label("RCA", "New York", 1900)
record_label_repository.save(record_label_4)
record_label_5 = Record_label("Elektra", "New York", 1950)
record_label_repository.save(record_label_5)
record_label_6 = Record_label("Sire", "New York", 1966)
record_label_repository.save(record_label_6)
record_label_7 = Record_label("Geffen", "Santa Monica", 1980)
record_label_repository.save(record_label_7)
record_label_8 = Record_label("CBS", "New York", 1962)
record_label_repository.save(record_label_8)
record_label_9 = Record_label("Capitol", "Los Angeles", 1942)


album_1 = Album("Rumours", "Fleetwood Mac", "Pop-rock", record_label_1, 30, 18, 10)
album_repository.save(album_1)
album_2 = Album("Hounds of Love", "Kate Bush", "Pop", record_label_2, 5, 23, 13)
album_repository.save(album_2)
album_3 = Album("Born to Run", "Bruce Springsteen", "Rock", record_label_3, 2, 16, 11)
album_repository.save(album_3)
album_4 = Album("Automatic for the People", "R.E.M", "Alternative rock", record_label_1, 8, 17, 10)
album_repository.save(album_4)
album_5 = Album("The Dark Side of the Moon", "Pink Floyd", "Progressive Rock", record_label_2, 13, 15, 9)
album_repository.save(album_5)
album_6 = Album("Station to Station", "David Bowie", "Glam Rock", record_label_4, 4, 18, 11)
album_repository.save(album_6)
album_7 = Album("A Night at the Opera", "Queen", "Progressive Rock", record_label_5, 7, 16, 12)
album_repository.save(album_7)
album_8 = Album("The Queen is Dead", "The Smiths", "Indie Rock", record_label_6, 8, 18, 13)
album_repository.save(album_8)
album_9 = Album("Nevermind", "Nirvana", "Grunge", record_label_7, 15, 15, 10)
album_repository.save(album_9)
album_10 = Album("London's Calling", "The Clash", "Punk", record_label_8, 3, 13, 8)
album_repository.save(album_10)
album_11 = Album("Remain in Light", "Talking Heads", "Rock", record_label_5, 4, 17, 12)
album_repository.save(album_11)
album_12 = Album("OK Computer", "Radiohead", "Inde", record_label_9, 18, 17, 11)
album_repository.save(album_12)
