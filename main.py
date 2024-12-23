from angleone_broker import *
import time

def main():
    print("Hello")
    start = time.time()
    print("T0 : {}".format(start))
    obj = angleone()

    user_data = obj.get_user_data()
    print("user data : ", user_data)
    print("---------------------------------------------------------\n")

    user_amt = obj.get_available_margin()
    print("available margin : ", user_amt)
    print("---------------------------------------------------------\n")

    exchange = "NSE"
    stock = "INFY-EQ"
    datestamp=dt.date.today()
    duration = 10

    current_price = obj.get_current_price(stock, exchange)
    print("current_price : ", current_price)
    print("---------------------------------------------------------\n")

    data1 = obj.hist_data_daily(stock, duration, exchange, datestamp)
    print("data1 : ", data1)
    print("---------------------------------------------------------\n")

    data2 = obj.hist_data_intraday(stock, exchange, datestamp)
    print("data2 : ", data2)
    print("---------------------------------------------------------\n")

    quantity = 1
    oid = obj.place_buy_order(stock, quantity, exchange)
    print("Order ID : ", oid)
    print("---------------------------------------------------------\n")

    status = obj.get_oder_status(oid)
    print("Order status : ", status)
    print("Order status error : ", obj.error_msg)
    print("---------------------------------------------------------\n")

    oid = obj.place_sell_order(stock, quantity, exchange)
    print("Order ID : ", oid)
    print("---------------------------------------------------------\n")

    status = obj.get_oder_status(oid)
    print("Order status : ", status)
    print("Order status error : ", obj.error_msg)
    print("---------------------------------------------------------\n")

    exchange = "NSE"
    stock = "INFY-EQ"
    quantity = 1
    status = obj.verify_position(stock, quantity)
    print("Position status : ", status)
    print("---------------------------------------------------------\n")

    status = obj.verify_position(stock, quantity, True)
    print("Position status : ", status)
    print("---------------------------------------------------------\n")

    status = obj.verify_holding(stock, quantity)
    print("holding status : ", status)
    print("---------------------------------------------------------\n")

    stock = "NIFTYBEES-EQ"
    quantity = 60
    status = obj.verify_position(stock, quantity)
    print("Position status : ", status)
    print("---------------------------------------------------------\n")

    status = obj.verify_position(stock, quantity, True)
    print("Position status : ", status)
    print("---------------------------------------------------------\n")

    status = obj.verify_holding(stock, quantity)
    print("holding status : ", status)
    print("---------------------------------------------------------\n")

    stock = "INFY-EQ"
    price = obj.get_entry_exit_price(stock)
    print("Entry Price : ", price)
    print("---------------------------------------------------------\n")

    price = obj.get_entry_exit_price(stock, True)
    print("Exit Price : ", price)
    print("---------------------------------------------------------\n")

    del obj
    #######################################################################

    print("Done ...")
    end = time.time()
    print("T1 : {}".format(end))
    diff = end - start
    print("T: {} \n".format(time.strftime('%H:%M:%S', time.gmtime(diff))))

if __name__ == "__main__":
    main()
