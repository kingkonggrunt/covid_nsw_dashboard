from datetime import datetime, timezone
import pytz

class TimeHelper:
    def __init__(self):
        self._utc = datetime.now(timezone.utc)
        self._timezone = None
        self._fmt = None

    @property
    def time_now(self):
        return datetime.now(self._timezone)

    @property
    def time_now_str(self):
        return self.time_now.strftime(self._fmt)

    def set_timezone(self, tz):
        self._timezone = pytz.timezone(tz)
