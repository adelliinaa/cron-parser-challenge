from typing import List, Dict, Union
from pydantic import BaseModel, field_validator

from cron_constants import CRON_FIELD_RANGES
from validators import expand_field


class CronExpression(BaseModel):
    minute: Union[str, List[int]]
    hour: Union[str, List[int]]
    day_of_month: Union[str, List[int]]
    month: Union[str, List[int]]
    day_of_week: Union[str, List[int]]
    command: str

    @field_validator("minute", "hour", "day_of_month", "month", "day_of_week", mode='before')
    @classmethod
    def validate_cron_field(cls, value, info):
        field_name = info.field_name
        min_val, max_val = CRON_FIELD_RANGES[field_name]
        if isinstance(value, str):
            try:
                value = expand_field(value, min_val, max_val)
            except ValueError as e:
                raise ValueError(f"Value error, {field_name}: {e}")
        return value

    def expand(self) -> Dict[str, str]:
        return {
            "minute": ' '.join(map(str, self.minute)),
            "hour": ' '.join(map(str, self.hour)),
            "day_of_month": ' '.join(map(str, self.day_of_month)),
            "month": ' '.join(map(str, self.month)),
            "day_of_week": ' '.join(map(str, self.day_of_week)),
            "command": self.command
        }

    @classmethod
    def parse_cron(cls, cron_string: str) -> 'CronExpression':
        parts = cron_string.split()
        if len(parts) < 6:
            raise ValueError("Cron string must have 6 parts")
        return cls(
            minute=parts[0],
            hour=parts[1],
            day_of_month=parts[2],
            month=parts[3],
            day_of_week=parts[4],
            command=' '.join(parts[5:])
        )
