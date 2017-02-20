library(ggplot2)
library(dplyr)
library(plyr)
#setwd("/Volumes/Genetics/PGx RUNS - All files/5 Genotyper & CopyCaller .TXT Exports for Apollo/qc_dev_process")
setwd("/Volumes/Genetics/PGx RUNS - All files/2016 GT QC Files/")
#data <- read.csv(file = "pgx_qc_20170112_102647.csv", header=T,sep=",",fileEncoding="latin1",stringsAsFactors = FALSE)

data <- read.csv(file = "pgx_qc_20170119_132433.csv", header=T,sep=",",fileEncoding="latin1",stringsAsFactors = FALSE)


## filter data by sample ID NA17104 NA17109 NA17245

## NA17104
data_NA17104 <- data[data$Sample.ID == "NA17104",]

## NA17109
data_NA17109 <- data[data$Sample.ID == "NA17109",]

## NA17245
data_NA17245 <- data[data$Sample.ID == "NA17245",]

## % QC failure
## NA17104

data_NA17104_unique <- data_NA17104[!duplicated(data_NA17104[,c('file_name','qc_fail')]),]

data_NA17104_unique$qc_percent <- data_NA17104_unique$qc_fail/data_NA17104_unique$sample_count



ggplot(data_NA17104_unique, aes(x=file_name, y=qc_percent))+geom_point(shape=1)+geom_smooth(method="lm",aes(group=1))+theme(axis.text.x=element_text(angle=70, hjust=1,face="bold"))+ggtitle("PGX Percent QC Failure NA17104")

   # Use hollow circles
   # Add linear regression line 
       #  (by default includes 95% confidence region)





## NA17109
data_NA17109_unique <- data_NA17109[!duplicated(data_NA17109[,c('file_name','qc_fail')]),]

data_NA17109_unique$qc_percent <- data_NA17109_unique$qc_fail/data_NA17109_unique$sample_count

ggplot(data_NA17109_unique, aes(x=file_name, y=qc_percent))+geom_point(shape=1)+geom_smooth()


## NA17245
data_NA17245_unique <- data_NA17245[!duplicated(data_NA17245[,c('file_name','qc_fail')]),]

data_NA17245_unique$qc_percent <- data_NA17245_unique$qc_fail/data_NA17245_unique$sample_count

ggplot(data_NA17245_unique, aes(x=file_name, y=qc_percent))+geom_point(shape=1)+geom_smooth(method="lm",aes(group=1))+theme(axis.text.x=element_text(angle=70, hjust=1,face="bold"))+ggtitle("PGX Percent QC Failure NA17245")



## DATA
## sort 
data[order(data$file_name),]
data_unique <- data[!duplicated(data[,c('file_name','qc_fail')]),]

data_unique$qc_fail_percent_sample <- data_unique$qc_fail/data_unique$sample_count
data_unique$qc_fail_percent_assay <- data$qc_precent_assay


ggplot(data, aes(x=file_name, y=data$qc_fail_sample))+geom_smooth(method="lm",aes(group=1))+theme(axis.text.x=element_text(angle=70, hjust=1,face="bold"))+ylim(0,0.4)+ggtitle("PGX Percent QC Failure")
ggplot(data, aes(x=file_name, y=data$qc_fail_percent_assay))+geom_smooth(method="lm",aes(group=1))+theme(axis.text.x=element_text(angle=70, hjust=1,face="bold"))+ylim(0,0.4)+ggtitle("PGX Percent QC Failure")



ggplot(data, aes(x=file_name, y=qc_percent))+geom_point()+geom_smooth(method="lm",aes(group=1))+theme(axis.text.x=element_text(angle=70, hjust=1,face="bold"))+ggtitle("PGX Percent QC Failure")

#ggplot(data, aes(x=file_name, y=qc_percent,fill=Assay.ID))+geom_bar()+geom_smooth(method="lm",aes(group=1))+theme(axis.text.x=element_text(angle=70, hjust=1,face="bold"))+ggtitle("PGX Percent QC Failure")




ggplot(data, aes(factor(file_name), qc_fail_percent_assay, fill = file_name)) + geom_bar(stat="identity", position = "dodge")+labs(x="assay",y="percent_qc_fail")+theme(axis.text.x=element_text(angle=90, hjust=1)) 





# Simple Scatterplot
attach(data)
plot(data$file_name, data$qc_fail_percent_assay, main="Scatterplot Example", xlab="batch_name", ylab="qc_fail_percent_assay", pch=19)
plot(data$file_name, data$qc_fail_percent_sample, main="Scatterplot Example", xlab="batch_name", ylab="qc_fail_percent_sample", pch=19)

qc_fail_percent_assay <- data$qc_precent_assay
qc_fail_percent_sample <- data$qc_fail_percent_sample
file_name <- data$file_name
# Basic Scatterplot Matrix
pairs(~qc_fail_percent_assay+file_name,data=data,  main="Simple Scatterplot Matrix")

