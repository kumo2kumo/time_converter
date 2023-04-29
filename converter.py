from datetime import datetime
from zoneinfo import ZoneInfo


class Converter:
    def __init__(self, area, time):
        self.area = area
        # self.zoneInfo_area = ZoneInfo(area)
        # input: xxxx/++++
        time_only: str = time[0:4] + time[5:]
        self.time: datetime = datetime(
            datetime.now().year,
            int(time_only[:2]),
            int(time_only[2:4]),
            int(time_only[4:6]),
            int(time_only[6:]),
            tzinfo=ZoneInfo(self.area)
        )

    def convert(self):
        # もう片方の時間に変換する
        other_area = "Asia/Tokyo" if self.area == "America/Los_Angeles" else "America/Los_Angeles"
        convert_time: datetime = self.time.astimezone(ZoneInfo(other_area))
        print(convert_time.strftime("%m/%d-%H:%M") + self.time.tzname())
        # return
