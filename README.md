# Portforlio
Welcome to my workspace! I'm Kunxiao, an undergrad data science student studying at UCSB:)

This portfolio is mainly used to collect and back up my main work and study documents, including but not limited to learning materials, lab codes, project outcomes, and so on. All files shown here are allowed to download for any proper use. For any file containing group works or collaborations, the display permits are obtained with the clear citation to each contributor. The briefly description of each file will be summarized below for easier access, but the description will not go into details since the main purpose of this page is to record my learning progress for personal use.

## Capstone lab
This file mainly includes most of the lab works for PSTAT197A Capstone Project and it is still be to updated. Each `rmd` file contain the codes I summarise in each week's material. The main topic of each lab work is labeled as the file name. 

Untill now, I have already summarised and uploaded the example codes and material about: 

-   `usage of tensorflow`, `iteration Strategies`, `logistic model and accuracy table`, `NLP`, `neural networks`, `splines regression`, and `curve fitting`. 
The files about time series and spatial prediction will be uploaded in the near future. 

The reason why I uploaded those stuffs is that I think they are very useful learning materials containing lots of good example codes, which I could directly apply in the future. 

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

All the details all included in the project file.

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

All the details all included in the project file.









