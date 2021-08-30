from sqlalchemy import create_engine, text
import psycopg2

engine = create_engine('postgresql+psycopg2://postgres:nomad_43@localhost:5432/testdb')

result_set = engine.execute(text("INSERT INTO shema1.status (id, name) VALUES (:id, :name)"), '123', 'text')

engine.execute(table_addresses.insert(), id=321, name='text')