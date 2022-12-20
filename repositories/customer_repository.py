from db.run_sql import run_sql

from models.record_label import Record_label
from models.album import Album
from models.customer import Customer
import repositories.record_label_repository as record_label_repository

def save(customer):

    sql = "INSERT INTO customers(name) VALUES (%s) RETURNING *"
    values = [customer.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    customer.id = id
    return customer


def select_all():
    customers = []

    sql = "SELECT * FROM customers"
    results = run_sql(sql)
    for row in results: 
        customer = Customer (row['name'], row['id'])
        customers.append(customer)
    return customers

def select(id):
    customer = None
    sql = "SELECT * FROM customers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        customer = Customer(result['name'], result['id'])
    return customer

def delete_all():
    sql = "DELETE  FROM customers"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM customers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(customer):
    sql = "UPDATE customers SET (name) = (%s) WHERE id = %s"
    values = [customer.name, customer.id]
    run_sql(sql, values)