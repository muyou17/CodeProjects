from yahoo_fin import stock_info
stock_data = stock_info.get_data("VNM.VN", '2024-01-01', '2014-10-12')
print(stock_data.head)