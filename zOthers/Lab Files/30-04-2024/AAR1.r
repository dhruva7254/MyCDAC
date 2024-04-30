# one sample T-test
Indian_oil_ethanol <- read_excel("D:/Dhruva/Indian_oil_ethanol.xlsx")
attach(Indian_oil_ethanol)

# Assumptions
# 1. Continuous
# Normality
hist(mileage with ethanol)
library(moments)
skewness(mileage with ethnol)
kurtosis(milage with rthnol)
# normality
shapiro.test(mileage with ethanol)

