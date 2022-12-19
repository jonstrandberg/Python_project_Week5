from db.run_sql import run_sql

from models.record_label import Record_label
from models.album import Album
import repositories.record_label_repository as record_label_repository


def save(album):
    sql = "INSERT INTO albums (title, artist, genre, record_label_id, stock, buy_price, sell_price) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [album.title, album.artist, album.genre, album.record_label.id, album.stock, album.buy_price, album.sell_price]
    results = run_sql(sql, values)
    id = results[0], ['id']
    album.id = id
    return album

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        record_label = record_label_repository.select(row['record_label_id'])
        album = Album(row['title'], row['artist'], row['genre'], record_label, row['stock'], row['buy_price'], row['sell_price'], row['id'])
        albums.append(album)
    return albums

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        record_label = record_label_repository.select(result['record_label_id'])
        album = Album(result['title'], result['artist'], result['genre'], record_label, result['stock'], result['buy_price'], result ['sell_price'], result['id'])
    return album

def delete_all():
    sql = "DELETE  FROM albums"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(album):
    sql = "UPDATE albums SET (title, artist, genre, record_label_id, stock, buy_price, sell_price) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [album.title, album.artist, album.genre, album.record_label.id, album.stock, album.buy_price, album.sell_price, album.id] 
    print(values)
    run_sql(sql, values)