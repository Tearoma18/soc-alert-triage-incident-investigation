from collections import Counter, defaultdict
from pathlib import Path
import re

log_file = Path(__file__).parent / "logs" / "simulated_auth.log"

if not log_file.exists():
    raise FileNotFoundError(f"Log file not found: {log_file}")

event_pattern = re.compile(
    r"^(?P<timestamp>\S+\s+\S+)\s+"
    r"(?P<event>AUTH_FAIL|AUTH_SUCCESS)\s+"
    r"user=(?P<user>\S+)\s+"
    r"source_ip=(?P<ip>\S+)"
    r"(?:\s+reason=(?P<reason>\S+))?$"
)

events = []
malformed_lines = []

with log_file.open(encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        line = line.strip()

        if not line:
            continue

        match = event_pattern.match(line)

        if not match:
            malformed_lines.append(line_number)
            continue

        events.append(match.groupdict())

if not events:
    raise ValueError("No valid events were found in the log.")

failed_by_user = Counter()
failed_by_ip = Counter()
timeline = defaultdict(list)

for event in events:
    user = event["user"]
    ip = event["ip"]

    if event["event"] == "AUTH_FAIL":
        failed_by_user[user] += 1
        failed_by_ip[ip] += 1

    timeline[user].append(event)

print("=== AUTHENTICATION LOG SUMMARY ===")
print(f"Valid events analyzed: {len(events)}")
print(f"Failed logins: {sum(failed_by_user.values())}")
print(
    "Successful logins: "
    f"{sum(e['event'] == 'AUTH_SUCCESS' for e in events)}"
)

print("\nFailed logins by user:")
for user, count in failed_by_user.most_common():
    print(f"  {user}: {count}")

print("\nFailed logins by source IP:")
for ip, count in failed_by_ip.most_common():
    print(f"  {ip}: {count}")

print("\n=== USER TIMELINES ===")
for user, user_events in sorted(timeline.items()):
    user_events.sort(key=lambda event: event["timestamp"])

    print(f"\nUser: {user}")

    for event in user_events:
        print(
            f"  {event['timestamp']} "
            f"{event['event']} "
            f"source_ip={event['ip']}"
        )

print("\n=== INVESTIGATION FLAGS ===")

for user, user_events in sorted(timeline.items()):
    user_events.sort(key=lambda event: event["timestamp"])

    for index, event in enumerate(user_events):
        if event["event"] != "AUTH_SUCCESS":
            continue

        previous = user_events[:index]
        recent_failures = [
            item for item in previous
            if item["event"] == "AUTH_FAIL"
            and item["ip"] == event["ip"]
        ]

        if len(recent_failures) >= 3:
            print(
                f"REVIEW: {user} had "
                f"{len(recent_failures)} earlier failed login(s) "
                f"from {event['ip']} before a successful login."
            )

if malformed_lines:
    print(f"\nMalformed lines skipped: {malformed_lines}")