from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.album import Album
import repositories.record_label_repository as record_label_repository
import repositories.album_repository as album_repository

albums_blueprint = Blueprint("albums", __name__)

# Show all albums
@albums_blueprint.route("/albums")
def albums():
    albums = album_repository.select_all()
    return render_template("albums/index.html", all_albums = albums)

# New album
@albums_blueprint.route("/albums/new", methods=['GET'])
def new_album():
    record_labels = record_label_repository.select_all()
    return render_template("albums/new.html", all_record_labels = record_labels)

#Create new album (form)
@albums_blueprint.route("/albums",  methods=['POST'])
def create_album():
    title = request.form['title']
    artist = request.form['artist']
    genre = request.form['genre']
    record_label = record_label_repository.select(request.form['record_label_id'])
    stock = request.form['stock']
    buy_price = request.form['buy_price']
    sell_price = request.form['sell_price']
    album = Album(title, artist, genre, record_label, stock, buy_price, sell_price)
    album_repository.save(album)
    return redirect('/albums')

# Show specific album
@albums_blueprint.route("/albums/<id>", methods=['GET'])
def show_album(id):
    album = album_repository.select(id)
    return render_template('albums/show.html', album = album)

#Edit - GET
@albums_blueprint.route("/albums/<id>/edit", methods = ['GET'])
def edit_album(id):
    album = album_repository.select(id)
    record_labels = record_label_repository.select_all()
    return render_template('album/edit.html', album = album, all_record_labels = record_labels)

#Update album details - POST
@albums_blueprint.route("/albums/<id>", methods=['POST'])
def update_album(id):
    title  = request.form['title']
    artist = request.form['artist']
    genre = request.form['genre']
    record_label = record_label_repository.select(request.form['record_label_id'])
    stock = request.form['stock']
    buy_price = request.form['buy_price']
    sell_price = request.form['sell_price']
    album = Album(title, artist, genre, record_label, stock, buy_price, sell_price, id)
    album_repository.update(album)
    return redirect('/albums')

#Delete album - POST (button)
@albums_blueprint.route("/albums/<id>/delete", methods = ['POST'])
def delete_album(id):
    album_repository.delete(id)
    return redirect('/albums')



