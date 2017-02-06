import datetime
import json
from pip._vendor import requests
from druid_config_example import *


##Reindex Spec File
SourceFileForReindexing="your reindex spec file goes here"
#SourceFileForReindexing="IndexSpec.json"

## set the Begin and End Boundaries you want to ReIndex
beginBoundary = datetime.date(2016, 01, 01)
endBoundary = datetime.date(2016, 12, 31)

## Set the Number of intervals to be created between startdate and enddate
intervals = 12

##declare datelist as array
Fromdate_list = []
ToDate_list=[]

## Calculate Delta to split the from and to boundaries into intervals
delta = (endBoundary - beginBoundary)/intervals
beginplusone=beginBoundary+datetime.timedelta(days=1)

## Generate From and To Boundary Intervals
for i in range(0,1):
    ToDate_list.append((beginBoundary).strftime('%Y-%m-%d'))
for i in range(1, intervals+1 ):
    ToDate_list.append((beginplusone+i*delta).strftime('%Y-%m-%d'))
for i in range(0, intervals+1 ):
    Fromdate_list.append((beginBoundary+i*delta).strftime('%Y-%m-%d'))

## Load the json file which is used a source for reindexing the druid segements
with open(SourceFileForReindexing, 'r') as f:
    my_dict = json.loads(f.read())

##For Every Interval(12 in this case) submit the reindexing task to coordinator
for i in range(0, intervals):
    split_date1 = (ToDate_list[i] + '/' + Fromdate_list[i+1])
    list=[split_date1]
    my_dict['spec']['dataSchema']['granularitySpec']['intervals'] = list
    url=coordinatorUrl+'/druid/indexer/v1/task'
    headers = {'content-type': 'application/json'}
    r = requests.post(url,data=json.dumps(my_dict),headers=headers)

