library(ggplot2)
library(dplyr)
library(plyr)
setwd("/Volumes/Genetics/PGx RUNS - All files/5 Genotyper & CopyCaller .TXT Exports for Apollo/qc_dev_process")

data <- read.csv(file = "pgx_qc_20170112_102647.csv", header=T,sep=",",fileEncoding="latin1",stringsAsFactors = FALSE)

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

data_unique$qc_fail_percent <- data_unique$qc_fail/data_unique$sample_count

ggplot(data_unique, aes(x=file_name, y=qc_fail_percent))+geom_smooth(method="lm",aes(group=1))+theme(axis.text.x=element_text(angle=70, hjust=1,face="bold"))+ylim(0,0.4)+ggtitle("PGX Percent QC Failure")



ggplot(data, aes(x=file_name, y=qc_percent))+geom_point()+geom_smooth(method="lm",aes(group=1))+theme(axis.text.x=element_text(angle=70, hjust=1,face="bold"))+ggtitle("PGX Percent QC Failure")

ggplot(data, aes(x=file_name, y=qc_percent,fill=Assay.ID))+geom_bar()+geom_smooth(method="lm",aes(group=1))+theme(axis.text.x=element_text(angle=70, hjust=1,face="bold"))+ggtitle("PGX Percent QC Failure")


data_test <- unique(data)


#data_unique_assay_id <- data[!duplicated(data[,c('Assay.ID')]),]
#data_unique_assay_id_file_name <- data_unique_assay_id[!duplicated(data_unique_assay_id[,c('file_name')]),]

ggplot(data, aes(x=file_name, y=qc_percent,fill=Assay.ID))+geom_line()+geom_smooth(method="lm",aes(group=1))+theme(axis.text.x=element_text(angle=70, hjust=1,face="bold"))+ylim(0,0.4)+ggtitle("PGX Percent QC Failure")




data_aggr <- aggregate(count ~ file_name, data, sum)
data_reject_aggr <- aggregate(reject_count ~ month, data_reject, sum)
data_reject_date <- data_reject_aggr/data_aggr

df <- rbind(data.frame(fill="total", month=data_aggr$month,count=data_aggr$count),
            data.frame(fill="reject",month=data_reject_aggr$month,count=data_reject_aggr$reject_count))


ggplot(data_NA17245, aes(x=file_name, y=ROX)) + geom_density2d() 



