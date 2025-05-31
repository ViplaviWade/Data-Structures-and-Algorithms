# Online Stock Span

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
    
obj1 = StockSpanner()
prices = [100, 80, 60, 70, 60, 75, 85]
res = [obj1.next(price) for price in prices]
print(res)