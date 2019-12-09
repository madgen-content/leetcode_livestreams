import json
from pprint import pprint
import datetime
import dateutil.parser

with open("/home/michael/Downloads/Takeout/YouTube/history/watch-history.json", 'r') as f:
    data = json.load(f)

times = list(sorted([d['time'] for d in data]))
datetime_objs = [dateutil.parser.parse(t) for t in times]
separator = datetime.timedelta(hours=2)

watchtime = datetime.timedelta(hours=0)
for i in range(len(datetime_objs) - 1):
    timediff = datetime_objs[i+1] - datetime_objs[i]
    if( timediff < separator):
        watchtime += timediff


hrs_spent = watchtime.total_seconds() / 60 / 60
start = datetime_objs[0].year
end = datetime_objs[-1].year

print(f"hrs_spent: {hrs_spent}")
print(f"start: {start}")
print(f"end: {end}")
print(f"avg per day: {hrs_spent / (end - start) / 365.25}")



