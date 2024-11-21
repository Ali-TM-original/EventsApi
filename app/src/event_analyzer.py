from typing import List
from collections import Counter


class EventAnalyzer:
    @staticmethod
    def get_joiners_multiple_meetings_method(events) -> List[str]:
        joiner_counts = Counter()
        for e in events:
            if e["joiners"]:
                for joiner in e["joiners"]:
                    joiner_counts[joiner["name"]] += 1
        return [joiner for joiner, count in joiner_counts.items() if count >= 2]
