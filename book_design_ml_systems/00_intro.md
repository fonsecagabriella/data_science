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

### Class imbalance

- Class imbalance also happens with regression tasks; you might need to make your model be better at predicting the 90th or 95th percentile even if that harms overall metrics (because if you're prediciting hospital bills, for example, a 100% increase in a bill might be too much to handle)

- Need to think about the cost of wrong prediciton for majority class agains the cost of wrong predicition for the classes that show up less often

- Class imbalance is more prpblematic for complex problems, and usually doesn't impact too much problems that are less complex

- How to tackle imbalance:
    - Choose right metrics: the class that appears more often might not be one you care the most about
    - Data-level methods (resampling): Remove randomly instances from majority class or add instance of minority class so the model can learn better; if you resample, you can't evaluate performance on re-sample data as that will give you a wrong idea. There are many algorithms that tackle this approach, search for it when needed.
    - Algorithm-level methods: Altering the loss function; Some examples are cost-sensitive learning, class-balance loss, focal loss.