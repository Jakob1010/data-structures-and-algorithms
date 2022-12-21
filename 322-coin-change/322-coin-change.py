class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = set()
        mem.add(amount)
        q = deque([(amount,0)])
        
        while q:
            current_amt, level = q.popleft()
            if current_amt == 0:
                    return level
            for coin in coins:
                new_amt, new_level = current_amt - coin, level +1
                if new_amt >= 0 and new_amt not in mem:
                    mem.add(new_amt)
                    q.append((new_amt,new_level))
        return -1