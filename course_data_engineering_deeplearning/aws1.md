# AWS 


- Amazon RDS: relational databases

- AWS Glue: ETL; used to connect to the RDS database and retrieve data.

- Amazon S3: Object Storage solution, saved in parquet

- Amazon Athena: Query service, used to query the data stored in the S3 bucket; enables SQL queries

- Amazon CloudWatch: monitor computing resources and network activity on your web application.

- Lambda: Servelss piece of code

- - Amazon EMR is specifically built for massive big data processing (Hadoop, Spark, Trino, etc.),

- AWS Glue ETL is a fully managed, serverless ETL service that abstract away infrastructure management (provisioning, configuring, and scaling clusters), making it significantly more convenient for standard ETL pipelines.

- AWS Kinesis Data Streams receives the online user activity from the sales platform log. It then streams this data to Kinesis Data Firehose, which acts as a delivery service that handles loading data streams into S3. Amazon Kinesis Data Streams is an AWS-native, fully managed, serverless streaming service designed for quick setup with seamless integration into the AWS ecosystem (such as IAM, Lambda, S3, and CloudWatch), offering a highly convenient "out-of-the-box" experience.

- Amazon Managed Streaming for Apache Kafka (MSK) carries more operational overhead than Kinesis because it manages standard Kafka cluster architectures (brokers, zookeeper/KRaft modes, topic partitions, cluster sizing/upgrades)

- Amazon EC2 Auto Scaling group: this group consists of a collection of EC2 instances. 

- EC2 instance: Virtual server in the cloud. It mainly consists of Central Processing Unit (CPU) and Random Access Memory (RAM). 

- Application Load Balancer: The Auto Scaling group is associated with an application load balancer, which distributes incoming application traffic (clients requests’ or inputs) across the EC2 instances. The load balancer serves as the single point of contact for clients.

- VPC (Virtual Private Cloud): There's no communication between this network and the internet unless set. Resources within can communicate with each other. If you want some resources inside the VPC to be public, they are set inside a public subnet.

- Amazon DynamoDB: Database that stores key-values


## Useful


- List of AWS CLI commands: https://docs.aws.amazon.com/cli/latest/

- An endpoint is the URL of the entry point for the AWS web service.

- The fact table contains the measurements that they need to aggregate (total of sales, average of prices, ... ) and the dimension tables help make these aggregations more specific (total of sales done in a given country, maximum number of quantities ordered for each product line). 

## Data pipeline example C1

<img src="./imgs/data-pipeline-example.png" width="90%">

<img src="./imgs/3-tier-example.png">

### 3-tier architecture 

- Presentation tier: this tier represents the user interface of the website (ex.: a web page) that allows clients to interact with the web application using their devices. This is where you can display the analytical dashboards for clients.

- Logic tier: this tier, also known as the application tier, represents the business logic that processes clients' input, queries the internal data stores and returns the results that need to be displayed on the presentation layer.

- Data tier: this tier is where the data associated with the web application is stored.

<img src="./imgs/3-tier.png">
