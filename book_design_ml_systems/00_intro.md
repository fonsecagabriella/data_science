# Designing Machine Learning Systems

👩🏽‍💻 [Github repo](https://github.com/chiphuyen/dmls-book)

> Machine learning is an approach to **learn complex patterns from existing data** and use these patterns to **make predictions on unseen data**.

___“ML algorithms don’t predict the future, but encode the past, thus perpetuating the biases in the data and more”__

## Introduction

- Companies don't care about fancy ML metrics; they care about business metrics (maximise profits)

- Before starting a ML project, ask yourself **which business metric corresponds to the ML metric?**

- **Requirements for ML system**
    - Reliability
    - Scalability
    - Maintainability
    - Adaptability

<img scr="./imgs/task_types.png">

- _“In general, when there are multiple objectives, it’s a good idea to decouple them first because it makes model development and maintenance easier.”_

## Data Engineering Fundamentals

- Data warehouse: Repo for structured data
- Data lake: Repo for unstructured data

### Data formats

- CSV is 'row-major', parquet is 'column-major'; 
    - If you want to access an example, CSV is quicker, but to access a feature, parquet is quicker. 
    - If you have have many rows and fewer features, parquet will be more efficient in memory.

- Row-major is good when you have to do a lot of writes; column-major is better if you do a lot of column reads.

- Pandas is column-major; accessing a DF by rows is much slower than accessing it by columns; if you convert this DF to a NumPy ndarray, accessing a row will become much faster.

- Text formats are human-readable, binary formats are not; binary formats are faster to unload and use less storage space.

### Data models

- Relational
- NoSQL (not only SQL)
- Graph

## Training Data

### Sampling

- Non-probability sampling: isn't based on any probability criteria
    - Convenience sampling
    - Snowball sampling
    - Judgment sampling
    - Quote sampling
- Probabilistic sampling
    - Simple random sampling
    - Stratified sampling
    - Weighted sampling
    - Reservoir sampling: commonly used in streaming/production
    - Importance sampling

### Labelling

- It's important to keep a `data lineage` log, so you know if you train your model with new data, and the performance declines, it could a problem in the annotation of the new data

- **Pertubation-based** method: You add some pertubation to the data, but that should not change its label. Used to generate more data.