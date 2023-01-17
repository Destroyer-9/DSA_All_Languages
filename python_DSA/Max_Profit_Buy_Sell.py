def maxProfit(prices: list[int]) -> int:
        bp = 1e18
        profit = 0
        ar = []
        for p in prices:    
            if p < bp:
                bp = p
            ar.append(p-bp)
            profit = max(profit,p-bp)
            
        print("All Profits Possible:",ar)
        return profit

prices = [7,1,5,3,6,4]

print("Max Profits Possible:",maxProfit(prices))
