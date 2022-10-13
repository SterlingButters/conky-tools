import pandas as pd
from datetime import datetime, timezone
import jicson
import json, yaml
import Fetch, wget
from dotenv import load_dotenv
import os

load_dotenv()

CANVAS_DOMAIN = os.environ.get("CANVAS_DOMAIN")
CANVAS_TOKEN = os.environ.get("CANVAS_TOKEN")

today = datetime.today()
currentDay = today.day
currentMonth = today.month
currentYear = today.year

# Right now there are no ics events that aren't assignment deadlines so it makes this difficult to test (could add lecture times ics)
# def convert(iso_string):
#     date, time = iso_string.split("T")
#     date = "{}-{}-{}".format(date[:4], date[4:6], date[6:])
#     time = "{}:{}:{}".format(time[:2], time[2:4], time[4:-1])
#     return "{}T{}".format(date, time)
#
# courses = Fetch.fetchActiveCourses(CANVAS_DOMAIN, CANVAS_TOKEN)
# for course in courses:
#     # print(json.dumps(course, indent=4))
#     url = course['calendar']['ics']
#     if not url:
#         print("No calendar found")
#     else:
#         # wget.download(url, "course.ics")
#         CALENDAR = jicson.fromFile('/home/sterlingbutters/Utilities/conky-tools/course.ics')['VCALENDAR']
#         # print(json.dumps(CALENDAR, indent=4))
#         assert len(CALENDAR) == 1 # Not sure when this would be > 1
#         CALENDAR = CALENDAR[0]
#         for event in CALENDAR['VEVENT']:
#             if 'DTEND' not in event.keys():
#                 eventStart = [event[key] for key in event.keys() if key.startswith("DTSTART")][0]
#                 eventEnd = eventStart
#                 print(event)
#                 print(eventStart, eventEnd)
#
#             elif event['DTEND'].startswith(str(currentYear)):
#                 eventStart = datetime.fromisoformat(convert(event['DTSTART'])).replace(tzinfo=timezone.utc).astimezone(tz=None).strftime('%Y-%m-%d %I:%M %p')
#                 eventEnd = datetime.fromisoformat(convert(event['DTEND'])).replace(tzinfo=timezone.utc).astimezone(tz=None).strftime('%Y-%m-%d %I:%M %p')
#                 print(event)
#                 print(eventStart, eventEnd)
#
#        os.system("rm course.ics")

CALENDAR = jicson.fromFile('/home/sterlingbutters/Utilities/conky-tools/invite.ics')['VCALENDAR']
print(json.dumps(CALENDAR, indent=4))
assert len(CALENDAR) == 1 # Not sure when this would be > 1
CALENDAR = CALENDAR[0]

##############################################################################3

# MONTH_B = datetime(currentYear, currentMonth, 1)
# MONTH_E = datetime(currentYear, currentMonth, (MONTH_B + pd.offsets.MonthEnd(1)).day)
# RANGE = pd.date_range(start=MONTH_B, end=MONTH_E)
#
# MAP = {6: 0, 0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6}
# converted = []
# for d in range(len(RANGE)):
#     day_of_week = MAP[RANGE[d].dayofweek]
#     if RANGE[d].day == 1:
#         for i in range(day_of_week):
#             converted.append("")
#         converted.append(RANGE[d].day)
#
#     elif RANGE[d] == RANGE[-1]:
#         converted.append(RANGE[d].day)
#         for i in range(6 - day_of_week):
#             converted.append("")
#
#     else:
#         converted.append(RANGE[d].day)
#
# table = [ tuple(converted[x:x+7]) for x in range(0, len(converted), 7) ]
#
# df = pd.DataFrame(table, columns=["S", "M", "T", "W", "R", "F", "S"])
# # df['Tasks'] = ["Test" for i in range(len(df))]
#
# print("${voffset 20}${offset 150}Test${hr 1}${voffset -20}${offset 0}")
# print(today.strftime("%B"), currentYear)
# print(df.to_string(index=False))
