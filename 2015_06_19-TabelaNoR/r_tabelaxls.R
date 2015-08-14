install.packages("gdata")
library("gdata")
ourdata <- read.xls('ie_data.xls')
head(ourdata)
ourdata[7,]
data <- read.xls('ie_data.xls', skip = 6)
head(data)
names(ourdata)
names(ourdata) = c('Date','S&P Comp','Dividend','Earnings','C. P. Index','Date Fraction','Long Interest Rate GS10','Real Price','Real Dividend','Real Earnings','CAPE','X')
names(ourdata)
ourdata$X
ourdata$X <- NULL
names(ourdata)
