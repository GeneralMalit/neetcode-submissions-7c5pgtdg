from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)
        sorted_hand = sorted(counts.keys())
        for card in sorted_hand:
            current_count = counts[card]
            for i in range(groupSize):
                needed = card + i
                counts[needed] -= current_count
                if counts[needed] < 0:
                    return False
        return True
