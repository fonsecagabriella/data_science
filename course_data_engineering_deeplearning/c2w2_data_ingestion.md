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
