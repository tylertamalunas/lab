# generates a single log line with timestamp
# appends that line to a file on disk
# prints line to stdout then exits

from datetime import datetime

time = datetime.now()
timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")

with open('/logs/app.log', 'a') as f:
    print(f"{timestamp}: Here are some log files", file=f)
    print(f"{timestamp}: Here are some log files")
