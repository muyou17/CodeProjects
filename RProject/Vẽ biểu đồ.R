# Cài package nếu cần
# install.packages("dplyr")
# install.packages("plotly")
# install.packages("htmlwidgets")

# Dùng thư viện
library(dplyr)
library(plotly)
library(htmlwidgets)

# Lấy dữ liệu từ file (để file vào cùng folder với script này)
dataframe <- read.csv("./tên_file.csv")

# Làm sạch dữ liệu
dataframe$Date <- as.Date(dataframe$Date, format = "%d/%m/%Y")
dataframe$Open <- as.numeric(gsub(",", "", gsub(" VND", "", dataframe$Open)))
dataframe$Close <- as.numeric(gsub(",", "", gsub(" VND", "", dataframe$Close)))
dataframe$High <- as.numeric(gsub(",", "", gsub(" VND", "", dataframe$High)))
dataframe$Low <- as.numeric(gsub(",", "", gsub(" VND", "", dataframe$Low)))
dataframe$Volume <- as.numeric(gsub(",", "", dataframe$Volume))

# Vẽ biểu đồ
figure <- dataframe %>% plot_ly(x = ~Date, type = "candlestick",
          open = ~Open, close = ~Close, high = ~High, low = ~Low)

# Lưu biểu đồ
saveWidget(figure, file = "Biểu đồ.html", selfcontained = TRUE)