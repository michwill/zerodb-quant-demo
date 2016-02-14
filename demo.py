import zerodb
from models import Trade
from zerodb.query import InRange, Gt
from datetime import datetime

db = zerodb.DB(("localhost", 8001), username="root", password="demo")

print len(db[Trade])
print db[Trade].query(InRange("timestamp", datetime(year=2015, month=2, day=1), datetime(year=2015, month=2, day=2)))
print db[Trade].query(Gt("timestamp", datetime(year=2015, month=2, day=1)))
