install.packages("rmcfs")
install.packages("caret")
library("rmcfs")
library("caret")
data <- read.csv(file.choose(), header = T,sep = ",")
foldsCrossValidationStratified <- createFolds(factor(data$rating), k=10,list = TRUE)
for (i in 1:length(foldsCrossValidationStratified)){
    result <- mcfs(rating~., data[-foldsCrossValidationStratified[[i]],])
}