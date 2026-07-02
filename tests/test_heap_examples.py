"""
Tests for heap_examples.py.

Verifies priority queue examples implemented using heapq.
"""

from src.heap_examples import top_three_users


def test_top_three_users_returns_highest_priorities():
	alerts = [
		("alice", 20),
		("bob", 80),
		("charlie", 50),
		("david", 100),
		("eve", 10),
	]

	assert top_three_users(alerts) == [
		("david", 100),
		("bob", 80),
		("charlie", 50),
	]


def test_top_three_users_returns_all_when_less_than_three():
	alerts = [
		("alice", 20),
		("bob", 80),
	]

	assert top_three_users(alerts) == [
		("bob", 80),
		("alice", 20),
	]
