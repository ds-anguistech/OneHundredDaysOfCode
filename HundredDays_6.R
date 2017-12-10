#100DaysofCode Day 6

apple_stock <- c(109.49, 109.90, 109.11, 109.95, 111.03, 112.12, 113.95, 113.30, 115.19, 115.19, 115.82, 115.97, 116.64, 116.95, 117.06, 116.29, 116.52, 117.26, 116.76, 116.73, 115.82)
plot(apple_stock, type = "p")
plot(apple_stock, type = "l")
title(main = "Apple Stock Prices", col.main = "purple")

#Vector Math
dan <- c(100, 200, 150)
rob <- c(50, 75, 100)
sum(dan + rob)

# Weights and returns
micr_ret <- 7
sony_ret <- 9
micr_weight <- .2
sony_weight <- .8

# Portfolio return
portf_ret <- (micr_ret * micr_weight) + (sony_ret * sony_weight)

portf_ret

# Weights, returns, and company names
ret <- c(7, 9)
weight <- c(.2, .8)
companies <- c("Microsoft", "Sony")

# Assign company names to your vectors
names(ret) <- companies
names(weight) <- companies

# Multiply the returns and weights together 
ret_X_weight <- ret * weight

# Print ret_X_weight
ret_X_weight

# Sum to get the total portfolio return
portf_ret <- sum(ret_X_weight)

# Print portf_ret
portf_ret

# Vector Subsetting
twelve_months <- c(5, 2, 3, 7, 8, 3, 5, 9, 1, 4, 6, 3)
names(twelve_months) <- month.name
twelve_months[1]
twelve_months[3:7]
twelve_months [c(1, 2, 3)]
twelve_months [c("January", "May", "June")]
twelve_months[-1]

