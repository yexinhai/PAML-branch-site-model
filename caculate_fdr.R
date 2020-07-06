data <- read.table(file = "all_array.txt", header = TRUE, sep = "\t")
a <- pchisq((data[,5]-data[,3])*2,1,lower.tail = FALSE) #alter-null
write.table(a,file = "p_value.txt")


data <- read.table(file = "p_value.txt", header = TRUE, sep = "\t")
head(data)
a <- data[,6]
head(a)
b <- p.adjust(a,method = "fdr",n = length(a) )
write.table(b, "fdr_result.txt",sep = "\t",row.names=TRUE)
