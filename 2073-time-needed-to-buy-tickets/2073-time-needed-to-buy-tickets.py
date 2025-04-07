class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        secs=0
        i=0
        while tickets[k]!=0:
            current_ticket=tickets.pop(0)
            if current_ticket>0:
                tickets.append(current_ticket-1)
                secs+=1
            if k==0:
                k=len(tickets)-1
            else:
                k-=1
        return secs
    
        
        