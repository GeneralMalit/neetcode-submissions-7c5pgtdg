from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)
        sorted_hand = sorted(counts.keys())

        for card in sorted_hand:
            curr_count = counts[card]
            for i in range(groupSize):
                needed = card + i
                if curr_count > counts[needed]:
                    return False
                counts[needed] -= curr_count
        return True
                