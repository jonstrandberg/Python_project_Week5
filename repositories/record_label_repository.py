from db.run_sql import run_sql

from models.record_label import Record_label

def save(record_label):

    sql = "INSERT INTO record_labels(name) VALUES (%s) RETURNING *"
    values = [record_label.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    record_label.id = id
    return record_label


def select_all():
    record_labels = []

    sql = "SELECT * FROM record_labels"
    results = run_sql(sql)
    for row in results: 
        record_label = Record_label (row['name'], row['id'])
        record_labels.append(record_label)
    return record_labels

def select(id):
    record_label = None
    sql = "SELECT * FROM record_labels WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        record_label = Record_label(result['name'], result['id'])
    return record_label

def delete_all():
    sql = "DELETE  FROM record_labels"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM record_labels WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(record_label):
    sql = "UPDATE record_labels SET (name) = (%s) WHERE id = %s"
    values = [record_label.name, record_label.id]
    run_sql(sql, values)
