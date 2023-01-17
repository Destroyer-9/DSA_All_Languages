def max_Loss(prices: list[int]) -> int:
        bp = 1e18
        loss = 0

        ar = []
        
        for p in prices:    
            if p < bp:
                bp = p
        
            ar.append(bp-p)
            profit = min(loss,bp-p)
            
        print("All Losses Possible:",ar)
        return profit

prices = [1,2,3,4,5,6] #[7,1,5,3,6,4]

print("Max Loss Possible:", max_Loss(prices[::-1]))
