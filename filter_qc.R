library(ggplot2)
library(dplyr)
setwd("/Volumes/Genetics/PGx RUNS - All files/5 Genotyper & CopyCaller .TXT Exports for Apollo/qc_dev_process")

data <- read.csv(file = "pgx_qc_20170105_151150.csv", header=T,sep=",",fileEncoding="latin1")

## filter data by sample ID NA17104 NA17109 NA17245

## NA17104
data_NA17104 <- data[data$Sample.ID == "NA17104",]

## NA17109
data_NA17109 <- data[data$Sample.ID == "NA17109",]

## NA17245
data_NA17245 <- data[data$Sample.ID == "NA17245",]


data_aggr <- aggregate(data, by=list("file_name"),FUN = sum)






data_aggr <- aggregate(count ~ file_name, data, sum)
data_reject_aggr <- aggregate(reject_count ~ month, data_reject, sum)
data_reject_date <- data_reject_aggr/data_aggr

df <- rbind(data.frame(fill="total", month=data_aggr$month,count=data_aggr$count),
            data.frame(fill="reject",month=data_reject_aggr$month,count=data_reject_aggr$reject_count))


ggplot(data_NA17245, aes(x=file_name, y=ROX)) + geom_density2d() 


ggplot(data_NA17245, aes(x=file_name)) + geom_histogram()

ggplot(data, aes(Assay.Name, fill=file_name) ) + geom_point(position="fill")

plot <- ggplot(data_NA17245 + aes(file_name)) + geom_point(position = "dodge")

ggplot(data_NA17104) + geom_point(aes(file_name, "ROX"))


plot1 <- ggplot(aes(x=file_name,y=,fill="Assay Name"),data=data_NA17245) 

line_reject <- plot1 + geom_bar(aes(fill="Assay Name"),stat = "identity")

