#!/usr/bin/python

import csv
import gzip
import zerodb
import transaction
from datetime import datetime, timedelta
import time
from models import Trade


db = zerodb.DB(("localhost", 8001), username="root", password="demo")

f = gzip.GzipFile("data/coinbaseUSD.csv.gz")
reader = csv.DictReader(f, fieldnames=["timestamp", "last", "volume"])

olddate = None
oldi = 0
oldtime = time.time()

for i, row in enumerate(reader):
    # Add objects to the db
    obj = Trade(
        timestamp=datetime.fromtimestamp(int(row["timestamp"])),
        last=float(row["last"]),
        volume=float(row["volume"]))
    db.add(obj)

    # Report progress and commit tx every month
    if (not olddate) or (obj.timestamp - olddate >= timedelta(days=7)):
        olddate = obj.timestamp
        transaction.commit()

        print i, obj

        if oldi != i:
            tps = (i - oldi) / (time.time() - oldtime)
            oldi = i
            oldtime = time.time()
            print tps, "tx/s"

f.close()
db.disconnect()
