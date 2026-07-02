"""
Collections examples.

Demonstrates practical uses of Python's collections module,
including Counter, defaultdict, and deque for common
data processing tasks.
"""

from collections import Counter
from collections import defaultdict
from collections import deque


def has_events_in_window(events: list[tuple[str, int]]) -> bool:
	queue = deque()

	for event in events:
		queue.append(event)
		timestamp = event[1]

		while queue and timestamp - 5 > queue[0][1]:
			queue.popleft()

		if len(queue) >= 3:
			return True

	return False


def recent_critical_alerts(alerts: list[tuple[str, str]]) -> list[str]:
	recent_alerts = deque(maxlen=5)

	for (severity, alert_type) in alerts:
		if severity == "critical":
			recent_alerts.append(alert_type)

	return list(reversed(recent_alerts))


def detect_suspicious_users_counter(failed_logins: list[str]) -> list[str]:
	counter = Counter(failed_logins)
	max_failed = 3

	return [user for user, failures in counter.items() if failures >= max_failed]


def get_user_activity(events: list[tuple[str, str]]) -> dict[str, list[str]]:
	user_activity = defaultdict(list)

	for user, user_action in events:
		user_activity[user].append(user_action)

	return dict(user_activity)


def get_unique_user_activity(events: list[tuple[str, str]]) -> dict[str, set[str]]:
	user_activity = defaultdict(set)

	for user, user_action in events:
		user_activity[user].add(user_action)

	return dict(user_activity)
