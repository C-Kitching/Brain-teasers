class PnLCalculator:
    def __init__(self):
        self.trades = {}
        self.prices = {}
        self.worst_trades = {}
    
    def process_trade(self, trade_id, instrument_id, buy_sell, price, volume):
        
        # new instrument
        if instrument_id not in self.trade:
            self.trades[instrument_id] = []
            self.worst_trades[instrument_id] = None

        # calculate pnl
        if buy_sell == "SELL":
            pnl = price - self.prices.get(instrument_id, price)
        else:
            pnl = self.prices.get(instrument_id, price) - price

        # update worst trade
        if self.worst_trades[instrument_id] is None or pnl < self.worst_trades[instrument_id][1]:
            self.worst_trades[instrument_id] = (trade_id, pnl)

    def process_price_update(self, instrument_id, price):
        self.prices[instrument_id] = price

    def output_worst_trade(self, instrument_id):
        
        # get worst trade
        worst_trade = self.worst_trades[instrument_id]

        # no bad trades
        if worst_trade is None:
            return "NO BAD TRADES"
        
        # return trade id of worst trade
        return str(worst_trade[0])
    

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