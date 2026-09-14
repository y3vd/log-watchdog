from dataclasses import dataclass
import re

@dataclass
class LogEntry:
    # A class for representing a log entry.
    timestamp: str
    hostname: str
    service_name: str
    log_level: str
    message: str
    source_type: str

compiled_line = re.compile(r"^(?P<time>\w{3}\s+\d+\s+[\d:]+)\s+(?P<host>\S+)\s+(?P<service>[\w\-\.\/\[\]]+):\s+(?P<msg>.*)$")

def parse_syslog_line(raw_line):
    line = raw_line.strip()

    match = compiled_line.match(line)

    if match:
        # Extract the components from the matched groups
        time = match.group("time")
        host = match.group("host")
        service = match.group("service")
        msg = match.group("msg")

        if "Failed" in msg or "Invalid" in msg or "Accepted password" in msg:
            log_level = "CRITICAL"
        elif "warning" in msg or "error" in msg:
            log_level = "WARNING"
        else:
            log_level = "INFO"

        log_entry = LogEntry(
            timestamp=time,
            hostname=host,
            service_name=service,
            log_level=log_level,
            message=msg,
            source_type="syslog"
        )

        return log_entry
    else:
        print("No match.")
        return None

test_line = "Sep 14 17:42:31 server01 sshd[4217]: Failed password for root"
test_line2 = "test"
result = parse_syslog_line(test_line)

print(result)
print(result.hostname)
print(result.log_level)