from dataclasses import dataclass
import re

@dataclass
class LogEntry:
    '''A class for representing a log entry.'''
    timestamp: str
    hostname: str
    service_name: str
    log_level: str
    message: str
    source_type: str

p = re.compile(r"^(?P<time>\w{3}\s+\d+\s+[\d:]+)\s+(?P<host>\S+)\s+(?P<service>[\w\-\.\/\[\]]+):\s+(?P<msg>.*)$")

def ParseSyslogLine(raw_line):
    line = raw_line.strip()

    match = p.match(line)

    if match:
        print("It matched!")
    else:
        print("No match.")

test_line = input("Enter a syslog line to test: ")

ParseSyslogLine(test_line)