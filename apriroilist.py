'''
install.packages("rlang")
install.packages("igraph")
install.packages("arules")
install.packages("arulesViz")
install.packages("visNetwork")

library(igraph)
library(arules)
library(arulesViz)
library(visNetwork)

transactions_list <- list(
  c("Diapers","Beer","Milk"),
  c("Diapers","Beer"),
  c("Bread","Milk"),
  c("Diapers","Beer","Milk","Bread"),
  c("Milk","Bread")
)

trans <- as(transactions_list, "transactions")

summary(trans)

itemFrequencyPlot(
  trans,
  topN = 10,
  type = "relative",
  col = "steelblue",
  main = "top items"
)

rules <- apriori(trans, parameter = list(conf = 0.6, supp = 0.2))

inspect(rules)

inspect(sort(rules, by = "confidence"))
'''
