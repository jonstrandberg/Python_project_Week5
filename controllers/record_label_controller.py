from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.record_label import Record_label
import repositories.record_label_repository as record_label_repository

record_labels_blueprint = Blueprint("record_labels", __name__)

# Show all record labels
@record_labels_blueprint.route("/record-labels") 
def record_labels():
    record_labels = record_label_repository.select_all()
    return render_template("record_labels/index.html", record_labels = record_labels)

@record_labels_blueprint.route("/record-labels/new", methods=['GET'])
def new_record_label():
    record_labels = record_label_repository.select_all()
    return render_template("record_labels/new.html", record_labels = record_labels)

#Create new record_label (form)
@record_labels_blueprint.route("/record-labels",  methods=['POST'])
def create_record_label():
    name = request.form['name']
    location = request.form['location']
    founded = request.form['founded']
    record_label = Record_label(name, location, founded)
    record_label_repository.save(record_label)
    return redirect('/record-labels')

# Show specific record label
@record_labels_blueprint.route("/record-labels/<id>", methods=['GET'])
def show_record_label(id):
    record_label = record_label_repository.select(id)
    return render_template('record_labels/show.html', record_label = record_label)

#Edit - GET
@record_labels_blueprint.route("/record-labels/<id>/edit", methods=['GET'])
def edit_record_label(id):
    record_label = record_label_repository.select(id)
    record_labels = record_label_repository.select_all()
    return render_template('record_labels/edit.html', record_label = record_label, record_labels = record_labels)

#Update album details - POST
@record_labels_blueprint.route("/record-labels/<id>", methods=['POST'])
def update_record_label(id):
    name  = request.form['name']
    location = request.form['location']
    founded = request.form['founded']
    record_label = Record_label(name, location, founded, id)
    record_label_repository.update(record_label)
    return redirect('/record-labels')

#Delete album - POST (button)
@record_labels_blueprint.route("/record-labels/<id>/delete", methods=['POST'])
def delete_record_label(id):
    record_label_repository.delete(id)
    return redirect('/record-labels')


