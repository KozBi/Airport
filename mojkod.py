from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from my_class.api.server import PlaneLog

engine = create_engine("postgresql+psycopg2://postgres:admin@localhost/airport")

with Session(engine) as session:
    results = session.query(PlaneLog).all()
    for r in results:
        print(r.id, r.has_landed, r.start_coordinate,r.connection_time)