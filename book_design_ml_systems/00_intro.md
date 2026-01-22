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

- **Natural labels** are labels that come from natural activities, and don't need explicitly label (for example, if you have a recommendation system, label 1 happens if someone clicked on the recommendation, and 0 otherwise)

### Class imbalance

- Class imbalance also happens with regression tasks; you might need to make your model be better at predicting the 90th or 95th percentile even if that harms overall metrics (because if you're prediciting hospital bills, for example, a 100% increase in a bill might be too much to handle)

- Need to think about the cost of wrong prediciton for majority class agains the cost of wrong predicition for the classes that show up less often

- Class imbalance is more prpblematic for complex problems, and usually doesn't impact too much problems that are less complex

- How to tackle imbalance:
    - Choose right metrics: the class that appears more often might not be one you care the most about
    - Data-level methods (resampling): Remove randomly instances from majority class or add instance of minority class so the model can learn better; if you resample, you can't evaluate performance on re-sample data as that will give you a wrong idea. There are many algorithms that tackle this approach, search for it when needed.
    - Algorithm-level methods: Altering the loss function; Some examples are cost-sensitive learning, class-balance loss, focal loss.

### Data Augmentation

- Simple label-preserving transformations: altering the data but preserving its label. For images, you can crop, flip, rotate, invert horizontally or vertically; for text, you can replace a word in the sentence with another word of same meaning.

- Pertubation: adding some noise to the data without changing its label (a little noise shouldn't influence the label)

- Data Synthesis: Use a script of rule to create new data points

## Feature Engineering

- Having a good set of features usually outperforms parameter tunning.

- Split data by time into train/valid/test splits instead of doing it randomly.

- If you oversample your data, do it after splitting.

- Scale and normalize your data after splitting to avoid data leakage.

- Use statistics from only the train split, instead of the entire data, to scale your features and handle missing values.

- Understand how your data is generated, collected, and processed. Involve domain experts if possible.

- Keep track of your data’s lineage.

- Understand feature importance to your model.

- Use features that generalize well.

- Remove no longer useful features from your models.

- Really cool to understand how features influence the model [InterpretML](https://github.com/interpretml/interpret?tab=readme-ov-file)

### Common Feature Engineering Operations

- **Missing values**: You can either *delete* or *imput* but first, you need to understand the type of data that is missing to avoid biases or issues with the model.
    - Missing not a random: deliberately not shared
    - Missing at random: when one value is missing and corresponds to a "class", or another value that is present
    - Missing completely at random: no pattern why the value is missing

- **Scaling**: You always have to look at the distribution (statistics) if you feed the model new data; if the stats are very different than the ones you trained your model, you might need to retrain now with all the data; Types of scaling are:
    - Normalisation (between 0 and 1) or between (-1 and 1)
    - Standardisation: if your distribution follows a normal distribution
    - Log transformation: if you have very skewed data

- **Discretisation (quantisation or binning)**: Rarely helps; it menas turning a continuous feature into a discrete one.

- **Enconding categorical features**: For production systems with a lot of new data, this can be tricky.  If you come across this, look into 'hashing trick'(especially Vowpal Wabbit, developed at Microsoft)

- **Feature crossing**: Useful to model nonlinear relationships (for example, *married with number of children* might be likely to buy a house); more useful for models that are bad in non-linear relationships (like linear/logistic and tree-models), less useful for NN. 

- **Positioning embedding**: Used in computer vision and NLP.

### Data Leakage

When information is available during training but not during prediciton; for example, during covid models learned to predict if a patient was very sick based on the font-type of their scans; which is non-sense and also not replicable into real case predictions.

Causes and solutions:

- Splitting by time: Instead of just randomly splitting data into train and test, for time-series data you need to split by time; for example, use day 1, 2, 3, 4 to train and predict day 5.

- Splitting it first: Split your data first before scaling, then use the stats from the train to scale all the splits; Some suggest to split all data before exploratory data analysis and preprocessing, so we don't get accidentaly get information that is not available in production or over the test split.

- Filling in data with statistics from the test splot: don't do this; if you are filling NA use values from the train split only.

- Duplicated data needs to be treated/removed (check this especially if you did oversampling)

- Group leakage: when the data is slightly different, but has the same label (for example, two cancer scans taken 2 weeks apart but with the same label; a camera detector); this is hard to detect if you don't know how your data is originated. 

- Ablation studies: They are useful to understand how much one feature influence your model; if you remove that feature and your model performance changes drastically, you need to investigate why (also if a new feature makes your model much better, you need to investigate if that is due to data leakage)

## Model Development and Offline Evaluation

- Resource: [AutoML - Auto parameter optimisation](./AutoML_Book_Chapter1.pdf)

### Ensemble

- [Kaggle ensemble guide](https://github.com/MLWave/Kaggle-Ensemble-Guide)

- Not usually used in production due to complexity and latency

- Can help with class imbalance, especially together with resampling (boosting and bagging)

- Types:
    - **Bagging** (bootstrap aggregating): reduces variance and helps with overfitting; sample with replacement instead of training whole dataset. A random forest is an example of bagging.
    - **Boosting**: convert weak learners into strong ones.
    - **Stacking**: create base learners and then create a meta-learner that combines the outputs from the base learners for a final prediction.


### Model offline evaluation

- Ideally you'd use the same metrics in production and development, but in development you have metrics that in production you don't (if the model is to detect attack, how would you know in production that you actually got all the attacks?)

- Evaluation metrics without a baseline do not mean anything. Types of baseline that can be useful:
    - Random baseline: from uniform distribution (predicting each label with equal probability) or task's label distribution 
    - Simple heuristic
    - Zero rule baseline: always predicts the most common class
    - Human baseline: is it better than what a human alone could achieve?
    - Existing solutions: how does it compare with existing / current solution?

### Evaluation methods

- **Pertubation tests:** the data your model has to work with in production are usually more 'noisy' compared to what you have in development; you might want to add some pertubation to your test sets to get a better sense of how your model would actually perform in production. The more sensitive to noise your model is, the harder will be to maintain it.

- **Invariance tests:** keep the input the same, but change sensitive information to see if the output changes (for example, race, gender, etc); another alternative: exclude sensitive information from training

- **Directional expectation tests:** Some changes to input are expected to change the output (if you increase the lot size of a house, its price should increase). Test these scenarios.

- **Model calibration:** For example, change 0.5 default prediction to another value; another example: user watches 80% sci-fi and 20% comedy: the system should show recommendations with that in mind, not 100% sci-fi because user watches mostly sci-fi. In sci-ki learn you can use `sklearn.calibration.calibration_curve`.

- **Confidence measurement**: Confidence of measurement of each sample.

- **Slice-based evaluation**: slice your data, also considering the groups within it, and check how your model performs. First identify your critical slices (for example, mobile vs desktop, locations, gender, etc)

## Model Deployment and Prediction Service

- Exporting a model means converting it into a format that be used by other applications (also called serialisation)

- Inference: the process of generating predictions

- There are two parts of the model that you can export:
    - The model definitions
    - The model parameter's values

- Online prediction (on demand prediction) are generated as soon as the requests for the predictions arrive;

- Batch predictions are asynchronous; they are made and stored. The name can be confusing because both online and batch predicitons can be predictions on batches of data.

- How to make your model predict faster:
    - Model compression (make the model smaller)
    - Inference optimisation (make the predictions being generated faster)

- You can compute the output of your model:
    - On the cloud
    - On the Edge (predictions are made using user's computer, like browser, cameras, robots, etc)

### Important basis

- A company might have hundreds of models in production at the same time;
- Model performance decays over time, especially when the distribution of data changes;
- Models should be retrained with great frequency (sometimes even hourly);

### Main modes of prediction

- **Batch prediction**: uses only batch features
- **Online prediction with batch only**: uses only batch features (pre-computed embeddings)
- **Streaming prediction**: Online prediction with both batch features and streaming features.

| | Batch prediction (asynchronous) | Online prediction (synchronous) |
| :--- | :--- | :--- |
| **Frequency** | Periodical, such as every four hours | As soon as requests come |
| **Useful for** | Processing accumulated data when you don't need immediate results (such as recommender systems) | When predictions are needed as soon as a data sample is generated (such as fraud detection) |
| **Optimized for** | High throughput | Low latency |

## Data Distribution Shifts and Monitoring

- ML pipelines mostly fail due to non-ML issues, which also requires software engineering skills from ML engineers

- Edge cases are the data samples that are so extreme that cause a model to make very biggit a mistakes.

- **Degenerate feedback loops:** happens when a prediction influence the feedback, which in turn, influences the next iteration of the model (the system output is used as a system input, and the influences future outputs - especially common in natural labels tasks). It happens often with recommender systems and needs to be tackled (*does the user click on the recommended song in 1st position because it's a good recommendation or because it's in the 1st position*)

### Data Distribution Shifts
 - Source distribution: the data the model is trained on

 - Target distribution: the data the model makes inferences on
 
 - There are different types of shifts, but usually ML people only care how to fix them as they require math/probability specific knowledge. Types of shifts:
    - Covariate shift: Happens when P(X) changes but P(Y|X) remains the same; very common with unbalanced classes, for example;
    - Label shift: When P(Y) changes but (P(X|Y)) remains the same
    - Concept drift: When P(Y|X) changes by P(X) remains the same (same input, different output; are usually seasonal or cyclic)
