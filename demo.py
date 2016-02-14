import zerodb
from models import Trade
from zerodb.query import InRange, Gt
from datetime import datetime, timedelta

db = zerodb.DB(("localhost", 8001), username="root", password="demo")

print len(db[Trade])
print db[Trade].query(InRange("timestamp", datetime(year=2015, month=2, day=1), datetime(year=2015, month=2, day=2)))
print db[Trade].query(Gt("timestamp", datetime(year=2015, month=2, day=1)))

# Some graphs
from pandas import DataFrame
import pylab
t = datetime(year=2015, month=5, day=1)
dt = timedelta(hours=1)
data = db[Trade].query(InRange("timestamp", t, t + dt))
df = DataFrame(data.dictify())
df.plot(x="timestamp", y="last")
ax = pylab.twinx()
df.plot(x="timestamp", y="volume", ax=ax, c="red")
pylab.show()

high = db[Trade].query(Gt("last", 490), sort_index="timestamp")
print high
