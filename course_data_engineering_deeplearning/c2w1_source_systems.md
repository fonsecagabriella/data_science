# C2W1 - Working with source systems

## Types of data

- Structured data: Tabular data

- Semi-structured data: not in tabular format, but has some structure (JSON)

- Unstructured data: no pre-defined structure (text, video, image, audio)

## Types of source systems

- Databases (structured and semi-structured)
    - CRUD > Create Read Update Delete
    - Relational databases
    - Non-relational databases (NoSQL)

- Files (unstructured or semi-structured)
    - A file is a sequency of bytes that represent information

- Streaming systems (semi-structured)
    - Continuous flow of data
    - ie. Stream of events


## Relational databases
- OLTP: Online Transaction process

- Commonly organised as data is organised in the business, with tables connected by keys

- Reduce redundancy

- Make it easier to manager 

- Data normalisation: approach developed in 1970s to minimise redundancy and ensure integrity 

- Nowadays data might be duplicated, because normalised data is slow to query

- OBT: one big table approach

- Relational Database Management Systems *RDBMS* (MySQL, Postgres, SQL Server)

## NoSQL Databases

- Types:
    - Key value
    - Document
    - Wide-Column
    - Graph

- Don't require schema
- Horizontal scaling
- You can read data from a node, before all nodes are updated

- Not all guarantee ACID compliance

- Do not use SQL, different ways to retrieve documents

- Document databases can become messy to manage; flexibility comes with downsides.

## ACID Compliance

- Atomicity: Transaction are atomic, treated as a single, indivisible unit

- Consistency: Any changes to the data made within a transaction follow the set of rules or constraints defined by the database schema

- Isolation: Each transation is executed independently in sequential order

- Durability: Once a transaction is complete, its effect are permanent and will persist even with future system failures

- If you relax some of these constraints, you can achieve more flexibility but you need to know what you're trading

