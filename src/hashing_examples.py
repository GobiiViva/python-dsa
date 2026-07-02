"""
Hashing examples.

Demonstrates common uses of Python dictionaries and sets
for counting, grouping, and aggregating backend data.
"""

def count_failed_logins(logs: list[tuple[str, bool]]) -> dict[str, int]:

	failed_count_dict = {}

	for (ip, success) in logs:
		if not success:
			failed_count_dict[ip] = failed_count_dict.get(ip, 0) + 1

	return failed_count_dict


def detect_suspicious_users_dict(logs: list[tuple[str, str, str, bool]]) -> list[str]:

	suspected_users = set()
	max_failed_count = 3

	if len(logs) < max_failed_count:
		return []

	failed_count = {}

	for _, username, _, success in logs:
		failed_count[username] = 0 if success else (failed_count.get(username, 0) + 1)

		if failed_count[username] == max_failed_count:
			suspected_users.add(username)


	return list(suspected_users)


def get_critical_ips(feed: list[dict[str, str]]) -> list[str]:

	ip_list = []
	ip_seen = set()

	for entry in feed:
		ip = entry["ip"]
		severity = entry["severity"]

		if ip not in ip_seen and severity == "critical":
			ip_list.append(ip)
			ip_seen.add(ip)

	return ip_list


def group_events(events: list[tuple[str, str]]) -> dict[str, list[str]]:

	grouped_events = {}
	for ip, event_type in events:
		grouped_events[ip] = grouped_events.get(ip, [])
		grouped_events[ip].append(event_type)

	return grouped_events
