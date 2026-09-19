from dataclasses import dataclass, asdict
import re
import json
import time

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

def parseSyslogLine(raw_line):
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

def tailAndParseFile(file_path):
    with open(file_path, "r") as file:
        while True:
            current_line = file.readline()

            # Make sure current line is not empty
            if current_line:
                entry = parseSyslogLine(current_line)

                if entry != None:
                    json_payload = json.dumps(asdict(entry))
                    print(json_payload)
            else:
                time.sleep(0.5)


def main():
    log_target = "var/log/auth.log"
    print("Starting Log Collector Watchdog on: " + log_target)

    try:
        tailAndParseFile(log_target)
    except FileNotFoundError:
        print("Error: Target log file does not exist.")
    except KeyboardInterrupt:
        print("Stopping watchdog...")

if __name__ == "__main__":
    main()
