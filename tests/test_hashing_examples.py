"""
Tests for hashing_examples.py.

Verifies the behavior of the hashing examples using
representative inputs and common edge cases.
"""

from src.hashing_examples import (
	count_failed_logins,
	detect_suspicious_users_dict,
	get_critical_ips,
	group_events
)


def test_count_failed_logins_counts_only_failed_attempts():
	logs = [
		("192.168.1.1", False),
		("192.168.1.1", False),
		("192.168.1.2", True),
		("192.168.1.1", False),
		("192.168.1.2", False)
	]

	assert count_failed_logins(logs) == {
		"192.168.1.1": 3,
		"192.168.1.2": 1
	}


def test_count_failed_logins_returns_empty_dictionary():
	assert count_failed_logins([]) == {}


def test_detect_suspicious_users_returns_users_with_three_failures():
	logs = [
		("10:00", "alice", "192.168.1.1", False),
		("10:01", "alice", "192.168.1.1", False),
		("10:02", "bob", "192.168.1.2", False),
		("10:03", "alice", "192.168.1.1", False),
		("10:04", "charlie", "192.168.1.3", True)
	]

	assert detect_suspicious_users_dict(logs) == ["alice"]


def test_detect_suspicious_users_resets_after_success():
	logs = [
		("10:00", "alice", "192.168.1.1", False),
		("10:01", "alice", "192.168.1.1", False),
		("10:02", "alice", "192.168.1.1", True),
		("10:03", "alice", "192.168.1.1", False),
		("10:04", "alice", "192.168.1.1", False)
	]

	assert detect_suspicious_users_dict(logs) == []


def test_get_critical_ips_returns_unique_ips():
	feed = [
		{"ip": "192.168.1.1", "severity": "critical"},
		{"ip": "192.168.1.2", "severity": "warning"},
		{"ip": "192.168.1.1", "severity": "critical"},
		{"ip": "192.168.1.3", "severity": "critical"}
	]

	assert get_critical_ips(feed) == [
		"192.168.1.1",
		"192.168.1.3"
	]


def test_group_events_groups_by_ip():
	events = [
		("192.168.1.1", "login"),
		("192.168.1.2", "logout"),
		("192.168.1.1", "download")
	]

	assert group_events(events) == {
		"192.168.1.1": ["login", "download"],
		"192.168.1.2": ["logout"]
	}

def test_group_events_returns_empty_dictionary():
	assert group_events([]) == {}
