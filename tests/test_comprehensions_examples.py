"""
Tests for comprehensions_examples.py.

Verifies filtering and transformation utilities implemented
using Python list and dictionary comprehensions.
"""

from src.comprehensions_examples import (
	find_suspicious_domains,
	get_active_users,
	get_failed_active_users
)


def test_get_failed_active_users_returns_only_active_users_with_failures():
	users = [
		{"name": "alice", "active": True, "failed": 3},
		{"name": "bob", "active": True, "failed": 0},
		{"name": "charlie", "active": False, "failed": 5},
		{"name": "david", "active": True, "failed": 1}
	]

	assert get_failed_active_users(users) == [
		"alice",
		"david"
	]


def test_get_failed_active_users_returns_empty_list():
	assert get_failed_active_users([]) == []


def test_get_active_users_returns_failed_counts():
	users = [
		{"name": "alice", "active": True, "failed": 2},
		{"name": "bob", "active": False, "failed": 5},
		{"name": "charlie", "active": True, "failed": 0}
	]

	assert get_active_users(users) == {
		"alice": 2,
		"charlie": 0,
	}


def test_find_suspicious_domains_detects_common_keywords():
	domains = [
		"google.com",
		"secure-login.net",
		"VerifyAccount.org",
		"github.com",
		"update-payment.com"
	]

	assert find_suspicious_domains(domains) == [
		"secure-login.net",
		"VerifyAccount.org",
		"update-payment.com"
	]
