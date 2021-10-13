import time
import pyupbit
import datetime
access = "rnbsbUeuw96s99VAt6WOEit4cxY39c68cECyxr4Q"
secret = "XpQqKIsfOD1yOvofIYnQnq9nWBEALH0ZmEUMx1DX"
def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price
def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time
def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

#def get_current_price(ticker): #왜안되냐
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]
# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")
# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)
        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-STPT", 0.5)
            current_price = pyupbit.get_current_price("KRW-STPT")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-STPT", krw*0.9995)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-HUM", 0.5)
            current_price = pyupbit.get_current_price("KRW-HUM")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-HUM", krw*0.9995)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-STX", 0.5)
            current_price = pyupbit.get_current_price("KRW-STX")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-STX", krw*0.9995)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-OMG", 0.5)
            current_price = pyupbit.get_current_price("KRW-OMG")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-OMG", krw*0.9995)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-QKC", 0.5)
            current_price = pyupbit.get_current_price("KRW-QKC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-QKC", krw*0.9995)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-XEC", 0.5)
            current_price = pyupbit.get_current_price("KRW-XEC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-XEC", krw*0.9995)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-HUNT", 0.5)
            current_price = pyupbit.get_current_price("KRW-HUNT")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-HUNT", krw*0.9995)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-AHT", 0.5)
            current_price = pyupbit.get_current_price("KRW-AHT")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-AHT", krw*0.9995)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-AXS", 0.5)
            current_price = pyupbit.get_current_price("KRW-AXS")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-AXS", krw*0.9995)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-ARK", 0.5)
            current_price = pyupbit.get_current_price("KRW-ARK")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-ARK", krw*0.9995)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-TON", 0.5)
            current_price = pyupbit.get_current_price("KRW-TON")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-TON", krw*0.9995)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-CBK", 0.5)
            current_price = pyupbit.get_current_price("KRW-CBK")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-CBK", krw*0.9995)
        elif start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-WAVES", 0.5)
            current_price = pyupbit.get_current_price("KRW-WAVES")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-WAVES", krw*0.9995)
        else:
            stpt = get_balance("STPT")
            hum = get_balance("HUM")
            stx = get_balance("STX")
            omg = get_balance("OMG")
            qkc = get_balance("QKC")
            xec = get_balance("XEC")
            hunt = get_balance("HUNT")
            aht = get_balance("AHT")
            axs = get_balance("AXS")
            ark = get_balance("ARK")
            ton = get_balance("TON")
            cbk = get_balance("CBK")
            waves = get_balance("WAVES")

            if stpt > 0.00008:
                upbit.sell_market_order("KRW-STPT", stpt*0.9995)
            elif hum > 0.00008:
                upbit.sell_market_order("KRW-HUM", hum*0.9995)
            elif stx > 0.00008:
                upbit.sell_market_order("KRW-STX", stx*0.9995)
            elif omg > 0.00008:
                upbit.sell_market_order("KRW-OMG", omg*0.9995)
            elif qkc > 0.00008:
                upbit.sell_market_order("KRW-QKC", qkc*0.9995)
            elif xec > 0.00008:
                upbit.sell_market_order("KRW-XEC", xec*0.9995)
            elif hunt > 0.00008:
                upbit.sell_market_order("KRW-HUNT", hunt*0.9995)
            elif aht > 0.00008:
                upbit.sell_market_order("KRW-AHT", aht*0.9995)
            elif axs > 0.00008:
                upbit.sell_market_order("KRW-AXS", axs*0.9995)
            elif ark > 0.00008:
                upbit.sell_market_order("KRW-ARK", ark*0.9995)
            elif ton > 0.00008:
                upbit.sell_market_order("KRW-TON", ton*0.9995)
            elif cbk > 0.00008:
                upbit.sell_market_order("KRW-CBK", cbk*0.9995)
            elif waves > 0.00008:
                upbit.sell_market_order("KRW-WAVES", waves*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
        
