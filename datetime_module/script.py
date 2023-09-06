from datetime import datetime
import pytz


t_day = datetime.today()

event_date = datetime(2021, 8, 21, 9, 30, 45, 100000)

event_date_us_eastern = datetime(
    2021, 8, 21, 9, 30, 45, 100000, pytz.timezone("US/Eastern")
)
event_date_us_central = datetime(
    2021, 8, 21, 9, 30, 45, 100000, pytz.timezone("US/Central")
)
event_date_africa_lagos = datetime(
    2021, 8, 21, 9, 30, 45, 100000, pytz.timezone("Africa/Lagos")
)


if __name__ == "__main__":
    print("Today is", t_day)
    print("Event date", event_date)
    print("Event date US/Eastern", event_date_us_eastern)
    print("Event date US/Central", event_date_us_central)
    print("Event date Africa/Lagos", event_date_africa_lagos)
