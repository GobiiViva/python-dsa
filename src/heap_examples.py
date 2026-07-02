"""
Heap examples.

Demonstrates priority queue operations using Python's
heapq module for efficiently selecting and ordering data.
"""

import heapq


def top_three_users(alerts: list[tuple[str, int]]) -> list[tuple[str, int]]:
	heap = []

	for user, priority in alerts:
		heapq.heappush(heap, (-priority, user))

	return [
		(user, -priority)
		for priority, user in heapq.nsmallest(3, heap)
	]
