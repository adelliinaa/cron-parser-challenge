import sys
from models import CronExpression


def main():
    if len(sys.argv) != 2:
        print("Usage: cli.py '<cron_string>'")
        return

    cron_string = sys.argv[1]
    try:
        cron = CronExpression.parse_cron(cron_string)
        expanded_cron = cron.expand()
        for key in ["minute", "hour", "day_of_month", "month", "day_of_week", "command"]:
            print(expanded_cron[key])
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == '__main__':
    main()
