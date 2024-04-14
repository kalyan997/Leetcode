class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        n = len(deck)
        deck.sort()
        
        my_q = deque()
        
        for i in range(n):
            my_q.append(i)
            
        result = [0]*n
        
        for card in deck:
            result[my_q.popleft()] = card

            if my_q:
                my_q.append(my_q.popleft())
                
        return result