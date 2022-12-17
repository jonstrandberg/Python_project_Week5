import pdb

from models.album import Album
from models.record_label import Record_label

import repositories.record_label_repository as record_label_repository
import repositories.album_repository as album_repository

record_label_1 = Record_label("Warner Bros")
record_label_repository.save(record_label_1)
record_label_2 = Record_label("EMI")
record_label_repository.save(record_label_2)

album_1 = Album("Rumours", "Fleetwood Mac", "Pop-rock", record_label_1, 30, 18, 10)
album_repository.save(album_1)
album_2 = Album("Hounds of Love", "Kate Bush", "Pop", record_label_2, 5, 23, 13)
album_repository.save(album_2)

