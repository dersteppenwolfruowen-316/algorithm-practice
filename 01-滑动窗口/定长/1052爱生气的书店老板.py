class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        all_customer = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                all_customer += customers[i]
        
        # statisfy = all_custormer - 1*c 总顾客-生气顾客
        not_angry = 0
        res = 0
        for i, c in enumerate(customers):
            if grumpy[i] == 1:
                not_angry += c
            left = i - minutes + 1
            if left < 0:
                continue
            res = max(res, not_angry)
            if grumpy[left] == 1:
                not_angry -= customers[left]
        return all_customer + res




            
        