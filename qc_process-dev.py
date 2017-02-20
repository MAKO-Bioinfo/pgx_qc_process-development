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
#datapath = r'/Volumes/Genetics/PGx RUNS - All files/5 Genotyper & CopyCaller .TXT Exports for Apollo/'

datapath = r'/Volumes/Genetics/PGx RUNS - All files/Genotyper QC Files/'

QC_PROCESS_DIR = 'qc_dev_process'

os.chdir(datapath)

## use os walk to walk through the directory and glob file with file name contains "geno" or "Geno"

## OA dataframe
final_dataframe_OA = pandas.DataFrame()
no_amp_dataframe_OA= pandas.DataFrame()
und_dataframe_OA = pandas.DataFrame()

filter_frame_OA = pandas.DataFrame()
no_amp_frame_OA = pandas.DataFrame()
und_frame_OA = pandas.DataFrame()

## 384 dataframe
final_dataframe_384 = pandas.DataFrame()
no_amp_dataframe_384= pandas.DataFrame()
und_dataframe_384 = pandas.DataFrame()

filter_frame_384 = pandas.DataFrame()
no_amp_frame_384 = pandas.DataFrame()
und_frame_384 = pandas.DataFrame()


list1 = []
list2 = []
list3 = []

list4 = []
list5 = []
list6 = []

for subdir, dirs, allfile in os.walk(datapath):
    for files in allfile:
        if fnmatch.fnmatch(files, '*geno*.txt') | fnmatch.fnmatch(files, '*Geno*.txt') and fnmatch.fnmatch(files,'*_OA_*'):
        #if fnmatch.fnmatch(files, '61004100_geno_10062016.txt'):
        #if fnmatch.fnmatch(files, 'ITT Shipment 13_geno_12122016_2.txt'):
            fileName = os.path.splitext(files)[0]
            date     = os.path.splitext(files)[0].split('_')[2]
            allFiles = os.path.join(subdir,files)
            #print files

            df = pandas.read_table(allFiles,comment='#',index_col=False,skip_blank_lines=False,header=2)
            df['Manual'] = map(lambda x: str(x).upper(), df['Manual'])

            # attach filename as a column indicator
            df['file_name'] = fileName
            df['date']      = date

            df['sample_count'] = df["file_name"].count()
            #df['qc_fail'] = (df["Manual"] =='TRUE').count()

            filter_dataframe_OA = df[df['Manual']=='TRUE']
            no_amp_frame_OA = df[df['Call']=='NOAMP']
            und_frame_OA    = df[df['Call']=='UND']

            filter_dataframe_OA['qc_fail'] = len(filter_dataframe_OA.index)
            filter_dataframe_OA['qc_percent'] = filter_dataframe_OA['qc_fail']/(filter_dataframe_OA['sample_count'])*100
            #filter_dataframe_OA['qc_percent_assay'] = filter_dataframe_OA['qc_fail']/60*100


            no_amp_frame_OA['qc_fail'] = len(no_amp_frame_OA.index)
            no_amp_frame_OA['qc_percent'] = no_amp_frame_OA['qc_fail']/(no_amp_frame_OA['sample_count'])*100
            #no_amp_frame_OA['qc_percent_assay'] = no_amp_frame_OA['qc_fail']/60*100


            und_frame_OA['qc_fail'] = len(und_frame_OA)
            und_frame_OA['qc_percent'] = und_frame_OA['qc_fail']/(und_frame_OA['sample_count'])*100
            #und_frame_OA['qc_percent_assay'] = und_frame_OA['qc_fail']/60*100

            list1.append(filter_dataframe_OA)
            list2.append(no_amp_frame_OA)
            list3.append(und_frame_OA)

        elif fnmatch.fnmatch(files, '*geno*.txt') | fnmatch.fnmatch(files, '*Geno*.txt') and fnmatch.fnmatch(files,'*_384_*'):
            fileName = os.path.splitext(files)[0]
            date     = os.path.splitext(files)[0].split('_')[2]
            allFiles = os.path.join(subdir,files)
            #print files

            df = pandas.read_table(allFiles,comment='#',index_col=False,skip_blank_lines=False,header=2)
            df['Manual'] = map(lambda x: str(x).upper(), df['Manual'])

            # attach filename as a column indicator
            df['file_name'] = fileName
            df['date']      = date

            df['sample_count'] = df["file_name"].count()
            #df['qc_fail'] = (df["Manual"] =='TRUE').count()

            filter_dataframe_384 = df[df['Manual']=='TRUE']
            no_amp_frame_384 = df[df['Call']=='NOAMP']
            und_frame_384    = df[df['Call']=='UND']

            filter_dataframe_384['qc_fail'] = len(filter_dataframe_384.index)
            filter_dataframe_384['qc_percent'] = filter_dataframe_384['qc_fail']/(filter_dataframe_384['sample_count'])*100
            #filter_dataframe_384['qc_percent_assay'] = filter_dataframe_384['qc_fail']/60*100

            no_amp_frame_384['qc_fail'] = len(no_amp_frame_384.index)
            no_amp_frame_384['qc_percent'] = no_amp_frame_384['qc_fail']/(no_amp_frame_384['sample_count'])*100
            #no_amp_frame_384['qc_percent_assay'] = no_amp_frame_384['qc_fail']/60*100

            und_frame_384['qc_fail'] = len(und_frame_384)
            und_frame_384['qc_percent'] = und_frame_384['qc_fail']/(und_frame_384['sample_count'])*100
            #und_frame_384['qc_percent_assay'] = und_frame_384['qc_fail']/60*100

            list4.append(filter_dataframe_384)
            list5.append(no_amp_frame_384)
            list6.append(und_frame_384)


final_dataframe_OA = pandas.concat(list1)
no_amp_dataframe_OA= pandas.concat(list2)
und_dataframe_OA = pandas.concat(list3)

final_dataframe_384 = pandas.concat(list4)
no_amp_dataframe_384= pandas.concat(list5)
und_dataframe_384 = pandas.concat(list6)


## THIS IS THE OA metrics
writer = final_dataframe_OA.to_csv(os.path.join(datapath,'pgx_qc_manual_OA_{}.csv').format(pandas.datetime.today().strftime(
     '%Y%m%d_%H%M%S')))

writer = no_amp_dataframe_OA.to_csv(os.path.join(datapath,'pgx_qc_noamp_OA_{}.csv').format(pandas.datetime.today().strftime(
     '%Y%m%d_%H%M%S')))

writer = und_dataframe_OA.to_csv(os.path.join(datapath,'pgx_qc_und_OA_{}.csv').format(pandas.datetime.today().strftime(
     '%Y%m%d_%H%M%S')))


## THIS IS THE 384 metrics
writer = final_dataframe_384.to_csv(os.path.join(datapath,'pgx_qc_manual_384_{}.csv').format(pandas.datetime.today().strftime(
     '%Y%m%d_%H%M%S')))

writer = no_amp_dataframe_384.to_csv(os.path.join(datapath,'pgx_qc_noamp_384_{}.csv').format(pandas.datetime.today().strftime(
     '%Y%m%d_%H%M%S')))

writer = und_dataframe_384.to_csv(os.path.join(datapath,'pgx_qc_und_384_{}.csv').format(pandas.datetime.today().strftime(
     '%Y%m%d_%H%M%S')))



## THIS IS THE ENTIRE RUN
#writer = final_dataframe.to_csv('pgx_qc_{}.csv'.format(pandas.datetime.today().strftime('%Y%m%d_%H%M%S')))

