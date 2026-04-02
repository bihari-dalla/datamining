'''
install.packages("igraph")
install.packages("visNetwork")
install.packages("arules")
install.packages("arulesViz")
library(arules)
library(arulesViz)
library(igraph)
library(visNetwork)

data<-read.csv("C:/Users/Admin/Downloads/transactions_sample.csv")

transaction_list<-split(data$itemDescription,data$memberid)
head(transaction_list)
str(transaction_list)
trans<-as(transaction_list,"transactions")
summary(trans)
itemFrequencyPlot(trans,
                  topN=10,
                  main="TOP ITEMS",
                  col="steelblue",
                  type="relative"
                  )
rules<-apriori(trans,parameter=list(conf=0.3,supp=0.05))
rules <- apriori(trans, parameter = list(conf = 0.3, supp = 0.05))

if (length(rules) > 0) {
  inspect(sort(rules, by="confidence"))
} else {
  cat("No rules generated\n")
}
'''
