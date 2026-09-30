# C2W2 - Data Ingestion

- Unbounded data: continuous stream of events

- Batch ingestion boundaries examples:
    - Total number of records
    - Size
    - Timeframe

- REST API: Representational State Transfer, uses HTTP as the basis for communication
    
- HTTP requests types:
    - GET: Get a resource
    - POST: Create a resource
    - DELETE:
    - PUT: Change/replace a resource

## ETL x ELT

- In the past ETL was the best practice because storage was expensive

- For ETL transformations rely on the processing tool that is used to ingest data; For ELT it relies on the power of the data repository (data warehouse)

- ETL is used typically for structured data, while ELT for unstructured

## Change Data Capture (CDC)

- Full snapshot / full load: All the old data is replaced by current data in the source system. Most used when there's no need for frequent updates

- Incremental / differential load: Only load updates and changes from the source systems. You might use a column as `last_update`to control this. This process is known as CDC

- Two approaches to CDC
    - Push: Some sort of logic is implemented to capture changes in the source database, that are pushed to the target system.
    - Pull: The target systems checks the source database for some changes.

- CDC Implementation Patterns
    - Batch-oriented or query-based (pull): You implement a check based on the `last_update` coklumn
    - Continuous or log-based (pull): Each update in the DB is treated as an event, and the log is used to perform the updates
    - Trigger-based (push): a trigger is runs when a specific column changes; too many triggers can have a negative impact on performance.