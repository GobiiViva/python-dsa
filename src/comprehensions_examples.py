"""
Comprehension examples.

Demonstrates Python list and dictionary comprehensions
for concise filtering, transformation, and data extraction.
"""


def get_failed_active_users(users: list[dict]) -> list[str]:
	return [
		user["name"]
		for user in users
		if (user["active"] and user["failed"] > 0)
	]


def get_active_users(users: list[dict]) -> dict[str, int]:
	return {
		user["name"]: user["failed"]
		for user in users
		if user["active"]
	}


def find_suspicious_domains(domains: list[str]) -> list[str]:
	signals = [
	    "secure",
	    "verify",
	    "login",
	    "update"
	]
	suspects = []

	for domain in domains:
		d = domain.lower()

		if any(signal in d for signal in signals):
			suspects.append(domain)

	return suspects
