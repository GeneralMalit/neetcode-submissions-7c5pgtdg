from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        sorted_hand = sorted(count.keys())
        for card in sorted_hand:
            current_count = count[card]
            if current_count > 0:
                for i in range(groupSize):
                    needed_card = card + i
                    if count[needed_card] < current_count:
                        return False
                    count[needed_card] -= current_count
        return True