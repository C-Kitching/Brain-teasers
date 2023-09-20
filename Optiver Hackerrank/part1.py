class PnLCalculator:
    def __init__(self):
        self.trades = {}
        self.prices = {}
    
    def process_trade(self, trade_id, instrument_id, buy_sell, price, volume):
        if instrument_id not in self.trades:
            self.trades[instrument_id] = []
        self.trades[instrument_id].append((trade_id, buy_sell, price, volume))

    def process_price_update(self, instrument_id, price):
        self.prices[instrument_id] = price

    def output_worst_trade(self, instrument_id):
        
        # if instrument trades
        if instrument_id in self.trades:
            
            # go through all trades
            trades = self.trades[instrument_id]
            if trades:
                
                # calculate pnl
                pnl = []
                for trade in trades:
                    trade_id, buy_sell, trade_price, volume = trade
                    if buy_sell == "BUY":
                        pnl.append((self.prices[instrument_id] - trade_price, trade_id))
                    elif buy_sell == "SELL":
                        pnl.append((trade_price - self.prices[instrument_id], trade_id))
            
                # find the worst trade (min pnl)
                min_pnl = min(pnl, key = lambda x: (x[0], -x[1]))
                if min_pnl[0] >= 0:
                    return "NO BAD TRADES"
                else:
                    return str(min_pnl[1])
 
        return "NO BAD TRADES"

if __name__ == "__main__":
    import sys

    calculator = PnLCalculator()
    line = sys.stdin.readline().split()
    n = int(line[0])
    for _ in range(n):
        line = sys.stdin.readline().split()
        if line[0] == "TRADE":
            tradeId = int(line[1])
            instrumentId = line[2]
            buySell = line[3]
            price = int(line[4])
            volume = int(line[5])
            calculator.process_trade(tradeId, instrumentId, buySell, price, volume)
        elif line[0] == "PRICE":
            instrumentId = line[1]
            price = int(line[2])
            calculator.process_price_update(instrumentId, price)
        elif line[0] == "WORST_TRADE":
            instrumentId = line[1]
            print(calculator.output_worst_trade(instrumentId))
        else:
            raise Exception("Malformed input!")