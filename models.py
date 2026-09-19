from dataclasses import dataclass, asdict

@dataclass
class LogEntry:
    # A class for representing a log entry.
    timestamp: str
    hostname: str
    service_name: str
    log_level: str
    message: str
    source_type: str

@dataclass
class Alert:
    # A class for alerts
    alert_type: str
    severity: str
    message: str
    source_ip: str
    timestamp: str
    metadata: dict
