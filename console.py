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

album_1 = Album("Rumours", "Fleetwood Mac", "Pop-rock", record_label_1, 30, 18, 10)
album_repository.save(album_1)
album_2 = Album("Hounds of Love", "Kate Bush", "Pop", record_label_2, 5, 23, 13)
album_repository.save(album_2)
album_3 = Album("Born to Run", "Bruce Springsteen", "Rock", record_label_3, 2, 16)
album_repository.save(album_3)
album_4 = Album("Automatic for the People", "R.E.M", "Alternative rock", record_label_1, 8, 17)
album_repository.save(album_4)
album_5 = Album("The Dark Side of the Moon", "Pink Floyd", "Progressive Rock", record_label_2, 13, 15)
album_repository.save(album_5)
album_6 = Album("Station to Station", "David Bowie", "Glam Rock", record_label_4, 4, 18)


