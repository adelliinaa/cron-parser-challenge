from typing import Dict, Tuple

CRON_FIELD_RANGES: Dict[str, Tuple[int, int]] = {
    "minute": (0, 59),
    "hour": (0, 23),
    "day_of_month": (1, 31),
    "month": (1, 12),
    "day_of_week": (1, 7)
}
