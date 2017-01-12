#!user/bin/env python
##===========================================================================##
## qc_process-dev.py
##
## This is the qc process python script that extract all the positive manual calls from
## output of the Quant Studio
## 1. Loop through each folder of datapath
## 2. Find filename contains "geno" or "Geno"
## 3. Use pandas read table to read filtered files, attached filename as a column indicator
##    ignore rows with "#"
## 4. Convert column "Manual" to string and convert to UpperCase
## 5. Apped all the dataframe and concate the list of dataframes into a big one
## 6. Write dataframe to csv files with timestamp   /
##
## Jack Yen
## Dec 30th, 2016
##===========================================================================##
##===========================================================================##
## All of the general library calls and PATH
##===========================================================================##

import os
import sys
import time
import csv, glob, fnmatch
from pandas import *

#datapath = r'/Volumes/Genetics/PGx RUNS - All files/5 Genotyper & CopyCaller .TXT Exports for Apollo/qc_dev_process'
datapath = r'/Volumes/Genetics/PGx RUNS - All files/5 Genotyper & CopyCaller .TXT Exports for Apollo/'

QC_PROCESS_DIR = 'qc_dev_process'

os.chdir(datapath)

## use os walk to walk through the directory and glob file with file name contains "geno" or "Geno"
final_dataframe = pandas.DataFrame()
filter_frame = pandas.DataFrame()
list = []
for subdir, dirs, allfile in os.walk(datapath):
    for files in allfile:
        if fnmatch.fnmatch(files, '*geno*.txt') | fnmatch.fnmatch(files, '*Geno*.txt') | fnmatch.fnmatch(files,'*GENO*'):
        #if fnmatch.fnmatch(files, '61004100_geno_10062016.txt'):
        #if fnmatch.fnmatch(files, 'ITT Shipment 13_geno_12122016_2.txt'):
            fileName = os.path.splitext(files)[0]
            allFiles = os.path.join(subdir,files)
            #print files

            df = pandas.read_table(allFiles,comment='#',index_col=False,skip_blank_lines=False,header=2)
            df['Manual'] = map(lambda x: str(x).upper(), df['Manual'])

            # attach filename as a column indicator
            df['file_name'] = fileName

            df['sample_count'] = df["file_name"].count()
            #df['qc_fail'] = (df["Manual"] =='TRUE').count()

            filter_dataframe = df[df['Manual']=='TRUE']
            filter_dataframe['qc_fail'] = len(filter_dataframe.index)
            filter_dataframe['qc_percent'] = filter_dataframe['qc_fail']/(filter_dataframe['sample_count'])
            list.append(filter_dataframe)

final_dataframe = pandas.concat(list)

## THIS IS THE QC DEV
writer = final_dataframe.to_csv(os.path.join(QC_PROCESS_DIR,'pgx_qc_{}.csv').format(pandas.datetime.today().strftime(
     '%Y%m%d_%H%M%S')))

## THIS IS THE ENTIRE RUN
#writer = final_dataframe.to_csv('pgx_qc_{}.csv'.format(pandas.datetime.today().strftime('%Y%m%d_%H%M%S')))

