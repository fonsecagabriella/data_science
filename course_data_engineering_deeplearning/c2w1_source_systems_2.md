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
    - A file is a sequence of bytes that represent information

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

## Object Storage

- Treats data with no hierarchy, the UI feature of creating folders is just visual.

- Good repository for semi-structured and unstructured data

- Good for serving data for ML models

- Each object has a UUID key (universal unique identifier) and meta keys

- Objects are immutable (do not support CRUD);
    - If an object is updated it gets a new ID, and you can also use a meta key for version

- Easily scale

- Flexibility to store several data formats

- Replicate data across several availability zones

- Often cheaper than other storage options, especially for data that do not need to be accessed often

## Streaming Systems

- Event: Something that happened and changed the state of a system

- Message: Record of information about an event (details, metadata, timestamp)

- Stream: A sequency of messages

- Streaming system:
    - Event producer: Generates the messages
    - Event consumer: Processes the message
    - Event Router / Streaming Broker: Acts as a buffer to filter and distribute the messages; decouples producer from consumer

- Often the terms `event` and `message` are used interchangedbly

- Message Queue: FIFO basis; A buffer that accumulates messages and delivers those messages to consumers Asynchornously

- Event Streaming Platform: Log, append-only record of events; possible to replay or reprocess any events in the log.

## Ways of connecting to source systems 

- Management console is convenient for small changes and checks, but not traceable

- CLI is common but used only for simple workloads

- SDK or API connectors is a more programmatic away

## IAM and Permissions

- IAM is a framework for managing permissions
    - I AM User: A person or service that interacts with resources

    - I AM Group: A collection of users that inherit the same permissions from the group

    - I AM role: Temporary permissions

- Policies connect identities to resources

## Basics of networking

### VPC

- A VPC (Virtual Private Cloud) is an isolated private network where you can launch your AWS resources. 

- A VPC exists inside a region and can span multiple availability zones. A region can contain multiple VPCs: each region comes with a preconfigured VPC, known as the default VPC, that you can use to launch your resources, or you can create your own custom VPC within the same region.

- A VPC can span across several regions

- Each VPC has a default public

- By default resources from different VPCs cannot communicate, but this can be changed

### Subnets

- Subnets: Public for internet-face services or private for internal services

### Internet gateway

- An internet gateway enables resources created inside a public subnet to send and receive traffic from the public internet. It allows both inbound and outbound traffic, connecting resources within a public subnet to the internet and allowing outside resources to connect to your resources. 

- In AWS, You can attach only one internet gateway to each VPC

- Resources that are created within a public subnet should have two types of IP addresses: one private IP address used to communicate with resources within the same VPC and another public IP address that allows outside resources to connect to them.

### NAT Gateway

- Resources in a private subnet can establish a one-way connection to the internet for outgoing requests (e.g., to download an update or send an email). You can enable this one-way connection by using a NAT gateway (Network Address Translation service).

### Route table

- "a collection of street signs that direct the traffic generated from a subnet to reach its destination.

### Network ACL

- To add additional security to your subnets, you can also set up a firewall that filters traffic to and from your subnets; this is done by using network ACLs (access control lists) to explicitly mention what traffic is allowed to enter or leave a subnet. 

- A network ACL consists of a list of rules that specify which inbound or outgoing traffic is allowed or denied. It is created at the VPC level and can be associated with specific subnets.

### Security groups

- While a network ACL acts as a firewall that filters traffic to and from your subnets, a security group acts as a firewall for a specific EC2 instance to control incoming and outgoing traffic for that specific instance. It adds an additional layer of security for any of your resources that run on your EC2 instances, and allows you to specify inbound rules (to control incoming traffic to your instance) and outbound rules (to control outbound traffic from your instance).

### Endpoints

- Interface endpoints can be placed in a public subnet or private subnet to allow resources in these subnets to connect to AWS public resources.

- Gateway endpoints can be attached to a VPC to allow the resources in the VPC to connect to S3 and DynamoDB. (S3 can also be reached using an interface endpoint, but DynamoDB can only be reached using gateway endpoint).