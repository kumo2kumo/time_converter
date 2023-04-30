from datetime import datetime
from zoneinfo import ZoneInfo


class Converter:
    def __init__(self, area, time):
        self.area = area
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

    def convert(self) -> str:
        # もう片方の時間に変換する
        other_area = "Asia/Tokyo" if self.area == "America/Los_Angeles" else "America/Los_Angeles"
        convert_time: datetime = self.time.astimezone(ZoneInfo(other_area))
        return convert_time.strftime("%m/%d-%H:%M") + convert_time.tzname()
