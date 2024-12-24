# Portfolio
Welcome to my workspace! I'm Kunxiao, a master student in DS studying at JHU. I graduated from UC-Santa Barbara and majored in Stats and Data Science.

This portfolio is mainly used to collect and back up my sample of work, including but not limited to research paper, sample codes, posters, presentations and so on. All files shown here are allowed to download for any proper use. For any file containing group works or collaborations, the display permits are obtained with the clear citation to each contributor. The briefly description of each file will be summarized below for easier access, but the description will not go into details since the main purpose of this page is to record my learning progress for personal use.
## Identifying Early Markers of AD with Language and Speech pattern
- Sample paper to be submitted is included in this folder.
- Code is still in process to be collated and uploaded soon.

## GNN Efficiency Improvements by Using Graph Sampling Strategies
- Sample paper and poster to be submitted is included in this folder.
- Some sample code is updated.

## Machine Learning in Medical Applications
- Some sample code is updated.
- Sample presentation is included in this folder.

## Machine Translation
- Sample peper is included.
## Internship in Glodon, Beijing
Sample work which could be show without any sensitive or private data. 

### Brief background introduction: 
During my internship at Glodon, I worked on leveraging machine learning and data analysis techniques to optimize Building Information Modeling (BIM) processes. My primary focus was on developing predictive models to identify potential project risks, improving efficiency and decision-making for construction management.
### Methodology:
-   Data Collection and Preprocessing: Analyzed large-scale construction datasets, performed cleaning, and handled missing values to ensure data quality.
-   Feature Engineering: Identified key variables influencing project risks, such as timeline deviations and budget discrepancies, using domain-specific insights.
Model Development:
-   Built predictive models using Random Forests and Gradient Boosting Machines (GBMs) to predict project risks.
-   Compared traditional machine learning methods with deep learning models, such as feed-forward neural networks, to evaluate performance.
-   Validation and Optimization: Conducted cross-validation to ensure model robustness and fine-tuned hyperparameters to maximize accuracy and reliability.
-   Visualization and Reporting: Created dashboards and visualizations using Python libraries (e.g., matplotlib, seaborn) to present findings to cross-functional teams, including engineers and architects.
## Capstone project Amgen
This file includes all the works of the Capstone project assignment with Amgen Company. 

### Brief background introduction: 

-   Our project essentially benchmarks the performance of the NER task using this specific type of model on free text coming from published articles and research papers on FierceBiotech.com. So far in our project, we have gotten through the initial task of NER; although, moving forward, we can work towards the competition of an algorithm which produces a Knowledge Graph from free text by additionally completing the NEL task and RE task.
-   Knowledge Graph (KG): a network model that links together named entities ('nodes') based on some common relation ('edge')
-   Named Entity Recognition (NER): training a model to parse unstructured text and classify named entities of a particular class.

### Methodology:

-   BERT (Bidirectional Encoder Representations from Transformers): a state-of-the-art Transformer-based language model most prominently used by Google to process search inquiries. Distinguished from other Transformer models by weighing the context on either side of each word in the input to better infer the meaning of each specific word in the input.
-   To obtain an entity-recognition model, we trained PubMedBERT on the BioRed dataset. To test how applicable the model is, we labeled a novel dataset filled with abstracts and news articles and tested our model on it.

## Capstone project biomarkers-group9
This file includes all the works of the Capstone project assignment in group 9: biomarkers. 

### Brief background introduction: 

-   Levels of proteins in plasma/serum are altered in autism spectrum disorder (ASD). Goal: identify a panel of proteins useful as a blood biomarker for early detection of ASD. So in other words, we want to find proteins whose serum levels are predictive of ASD.
-   Serum samples are from 76 boys with ASD and 78 typically developing (TD) boys, 18 months-8 years of age. A total of 1,125 proteins were analyzed from each sample: 1,317 measured, 192 failed quality control (we don’t know which ones failed QC so will use all).

### Methodology:

-   Variable selection (`LASSO regularization`), classification (`logistic regression` and `random forests`), and multiple testing correlations (with FDR control) will all be accessed to find good protein panels whose serum levels are predictive of ASD; the `classification accuracy metrics` will also be discussed to test the performance of the models. At the same time, we also care about the problems like `data partitioning`, `model interpretability` and `high dimensional data`.

`data` contains all the raw data and processed data used in analysis. 

`scripts` contains the tool functions that could be learned and applied, and the whole group's draft works.

`results` contain the final outcomes: `report.qmd` `report.html`.

All the details are included in the project file.

## Capstone project webpage classification-group10
This file includes all the works of the Capstone project assignment in group 10: fraud claims. 

### Brief background introduction: 

-   Goal: Use different predictive models to flag webpages that may contain evidence related to fraud claims. (Given a webpage, want to predict whether contents include potential evidence).
-   Data available to develop a model are a collection of about 3,000 labeled webpages that are manually assigned labels to multiple classes. (Sampling method unclear which comes from a 2021-2022 capstone project, and predictive model fit to this data may not work well in general for an arbitrary webpage).

### Methodology:

-   `HTML scraping` strategies for captureing webpages' content; `NLP` techniques for converting text to data and web scraping tools in R; Dimension reduction techniques (`PCA`) for reducing dimension; multiclass classification methods for identifying webpage categories: training `Multinomial Logistic Regression Models` (with and without running PCA), `Neural Networks`, `SVM`, and `Recurrent Neural Network` in R. The `classification accuracy metrics` will also be discussed to test the performance of different models.

`data` contains all the raw data and processed data used in analysis. 

`scripts` contains the tool functions that could be learned and applied, and the whole group's draft works.

`results` contain the summaries of classification accuracy metrics for different models.

`writeups` contain the final outcomes: `prediction-summary.html`, `prediction-summary.qmd`, `tasks_summary.html`, and `tasks_summary.qmd`.

All the details are included in the project file.

## Capstone project clustering methods-group8
This file includes all the works of the Capstone project assignment in group 8: clustering methods. 

### Brief background introduction: 

-   To fighting poverty and providing the people of backward countries with basic amenities and relief during the time of disasters and natural calamities, we have to make decision to choose the countries that are in the direst need of aid. 
-   Goal: To categorise the countries using socio-economic and health factors that determine the overall development of the country.
-   To demonstrate each of these clustering methods, we will use a country-level data set that includes 167 unique observations (not every country is represented). The variables related to socio-economic and health are included, such as `gdpp`, `child_mortality`, `health`, and so on. 

### Methodology:

-   Optimization methods: `Elbow method`, `Average Silhouette method`, `Gap Statistic method`; Clustering methods used to train the models: `Hierarchical clustering`, `Model-based clustering` (including the algorithm to choose the best model), `Density-based clustering`; Dimension reduction techniques (`PCA`) for reducing dimension; Visualization techniques to visualize results: `Dendrograms` and `Maps`. 

`data` contains all the raw data and processed data used in analysis. 

`scripts` contains the tool functions that could be learned and applied, and the whole group's draft works.

`image` contain the images sources used in the report.

The final outcomes: `Vignette.Rmd` `Vignette.html`.

All the details are included in the project file.

## Machine Learning Final Project
This file includes all the works of the Final project assignment in PSTAT131 Machine learning. 

### Brief background introduction: 
-   As the midterm elections in the United States is currently being held near the midpoint of the current president’s four-year term of office, it is a good time for us to review the 2020 United States presidential election data. Despite that the 2016 presidential election came as a big surprise to many, Biden’s victory in the 2020 presidential election has been widely predicted.
-   Goal: Analyze and visualize the 2020 presidential election dataset. We will primarily work towards building state/county-level red/blue map plots that are commonly shown on media coverage. In other words, we will combine the Untied States county-level census data with the election data and our target would then be building and selecting classification models to predict the election winner.
-   Two data sets:  election data in the county level and the 2017 United States county-level census data.

### Methodology:
-   Optimization methods: `Cross-validation`; Classification methods used to train the models: `Logistic Regression` Method, `Lasso Logistic Regression` Method, `Decision Tree` Method; `Random Forest` Method; `SVM` Method; Dimension reduction techniques (`PCA`) for reducing dimension; Visualization techniques to visualize results: `Dendrograms` and `Maps`; The `classification accuracy metrics` and `ROC graphs` will also be discussed to test the performance of different models.

The final outcomes: `Kunxiao Gao Final Project-HTML.Rmd` and `Kunxiao Gao Final Project-HTML.html`.

All the details are included in the project file.

## Internship Glodon

This file includes all the works in the internship at Glodon. 

### Brief background introduction:

Aimed to predict customer purchasing behavior and provide customer data with high purchasing power.

### Methodology

-   Classification methods used to train the models: `XGBoosting` Model; Optimization methods: `Randomized Search` and `Bayesian Optimization`;  Data Binning techniques: `One-hot`,`woe`, `iv`; Dimension reduction techniques (`PCA`) for reducing dimension; Visualization techniques to visualize results: `ROC` and `K-S Curve`.
-   Wrote fuzzy matching algorithm and aggregation back-tracking algorithm to clean and explore the data.
-   Implemented XGBoosting model with Randomized Search and Bayesian Optimization to train model and fine tuned the parameters, acquiring the best model base on 65.893 AUC.

## Internship PPT Auto-Generation

This file includes all the tools about PPT Auto-Generation used for the internship at China Unicom. 

### Brief background introduction: 

-   Goals: Generate PPT for Nine Cities Macro Indicators Summary. 

### Libraries used (in Python): 

-   `pptx.util`, `pptx.dml.color`, `pptx.enum.text`, `pptx.chart.data`, and so on.
-   For various reasons, all relevant scripts and results were not stored in the personal device and are nowhere to be found. Thus, only relevant templates and tools can be saved.

## MCMC
This file mainly includes some examples and course works for PSTAT115 Bayes Data Analysis and it is still to be updated. The contents are mainly about Implementation about different samplers in MCMC algorithm and some examples of writing codes with Stan. The reason why I uploaded those stuffs is that I think they are very useful learning materials containing lots of good example codes, which I could directly apply in the future. 

### The samplers included:
-   `Metropolis-Hasting algorithm`:
-   `Metropolis algorithm`, `HMC algorithm`, and `Gibbs algorithm`.

All the details about background information and data sets used are included in the files.

## Capstone lab
This file mainly includes most of the lab works for PSTAT197A Capstone Project and it is still to be updated. Each `rmd` file contain the codes I summarize in each week's material. The main topic of each lab work is labeled as the file name. 

Untill now, I have already summarized and uploaded the example codes and material about: 

-   `usage of tensorflow`, `iteration Strategies`, `logistic model and accuracy table`, `NLP`, `neural networks`, `splines regression`, and `curve fitting`. 
The files about time series and spatial prediction will be uploaded in the near future. 

The reason why I uploaded those stuffs is that I think they are very useful learning materials containing lots of good example codes, which I could directly apply in the future. 

## Machine Learning Lab
This file mainly includes most of the lab works for PSTAT131 Machine Learning and it is still to be updated. Each `rmd` file contain the codes I summarize in each week's material. The main topic of each lab work is labeled as the file name. 

Untill now, I have already summarized and uploaded the example codes and material about: 

-   `SVM`, `PCA`, `Clustering`, `Bagging and Random Forest`, `decision trees`, `Ridge and Lasso Regression`, `Corss Validation`, `logistic regression`, and `KNN`.

## CS9 lab
This file mainly includes most of the lab works for CS9 Intermediate Python Programming. Each `py` file contain the codes I summarize in each week's material. The main topic of each lab work is labeled as the file name. Intermediate topics in Computer Science using the Python programming language. Topics include object oriented programming, runtime analysis, data structures, and software testing methodologies.

## To be Continued






