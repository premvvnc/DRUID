## Druid Indexer Parallelizer
This code will help to parallelize the druid reindexing task. You will occasionally need to redindex druid datasource if you need to backfill data or add a new dimension or metric to the existing data source. The Parallelizing concept is based on time based reindexing , say for example you have 1 year of data to reindex, you can create 12 intervals(monthly ranges) and run 12 tasks in parallel without locking each other.  

Assuming you have a json spec file to index data from a source file with all the existing data and the new metric or dimension added, you can use this code to submit x number of index tasks to coordinator that will run in parallel.

## Druid Config Settings
You can submit n number of tasks in parallel if you have n number of workers. So before you run Druid indexer parallelizer, update the runtime.properties file in the middlemanger as follows.
###
**Number of tasks per middleManager**
###
**druid.worker.capacity=n**
###
where n is number of tasks you want to run in parallel. Note that it is always recommnded that n=(number of cores)-1

## Running the Reindexer
* Update the coordinatorUrl in druid_config_example.py
* Update the SourceFileForReindexing(This is the json spec file for indexing) in DatasourceReindexer.py file.
and run the DatasourceReindexer.py file
* Finally check the Coordinator web console(coordinatorip:8090/console.html) to verify that the reindex tasks are running in parallel.

### Useful links
* Druid Indexing Task <http://druid.io/docs/latest/ingestion/tasks.html#index-task>