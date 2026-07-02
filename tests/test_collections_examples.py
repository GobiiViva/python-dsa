"""
Tests for collections_examples.py.

Verifies examples using Counter, defaultdict, and deque
for common data processing tasks.
"""

from src.collections_examples import (
	detect_suspicious_users_counter,
	get_unique_user_activity,
	get_user_activity,
	has_events_in_window,
	recent_critical_alerts
)


def test_has_events_in_window_detects_three_events():
	events = [
		("login", 1),
		("logout", 3),
		("download", 5)
	]

	assert has_events_in_window(events) is True


def test_has_events_in_window_returns_false():
	events = [
		("login", 1),
		("logout", 10),
		("download", 20)
	]

	assert has_events_in_window(events) is False


def test_recent_critical_alerts_returns_latest_five():
	alerts = [
		("critical", "A"),
		("warning", "B"),
		("critical", "C"),
		("critical", "D"),
		("critical", "E"),
		("critical", "F"),
		("critical", "G")
	]

	assert recent_critical_alerts(alerts) == [
		"G",
		"F",
		"E",
		"D",
		"C"
	]


def test_detect_suspicious_users_counter_returns_threshold_users():
	failed_logins = [
		"alice",
		"alice",
		"alice",
		"bob",
		"bob",
		"charlie"
	]

	assert detect_suspicious_users_counter(failed_logins) == [
		"alice"
	]


def test_get_user_activity_groups_events():
	events = [
		("alice", "login"),
		("alice", "download"),
		("bob", "logout")
	]

	assert get_user_activity(events) == {
		"alice": [
			"login",
			"download"
		],
		"bob": ["logout"]
	}


def test_get_user_activity_returns_empty_dictionary():
	assert get_user_activity([]) == {}


def test_get_unique_user_activity_removes_duplicates():
	events = [
		("alice", "login"),
		("alice", "login"),
		("alice", "download")
	]

	assert get_unique_user_activity(events) == {
		"alice": {"login", "download"}
	}
