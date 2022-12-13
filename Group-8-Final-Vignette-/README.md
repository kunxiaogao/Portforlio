# vignette-clustering-methods

Vignette on implementing clustering methods (hierarchical, model-based, density-based) using unlabeled country data; created as a class project for PSTAT197A in Fall 2022.

## Contributors

KunXiao Gao, Justin Liu, Ruoxin Wang, Kassandra Trejo 

## Vignette Abstract

Clustering refers to the idea of partitioning observations from a data set into distinct groups without being given the labels beforehand. As an unsupervised learning technique, the goal of clustering is not to generate predictions but rather to draw inferences from the data. For our topic, we specialized in three different types of clustering methods. In hierarchical clustering, the distance between observations determines which cluster each observation falls into – we use the Euclidean distance as our metric. In model-based clustering, clusters are formed based on a probability distribution – we demonstrate this using Gaussian mixture models. In density-based clustering, the data is grouped in areas where many points are close together – we use DBSCAN to illustrate this. Unlike model-based clustering, density-based clustering is a non-parametric method since it does not assume that the points come from a predetermined probability distribution. We implemented these 3 methods to perform unsupervised classification on an unlabeled country data set. Overall, we found that model-based clustering gave us the most detailed clusters while still maintaining a good level of interpretability.

## Repository Contents

The vignette files (`vignette.Rmd` and `vignette.html`) can be found in the root directory of this repository. The `vignette-clustering-methods.Rproj` file opens the R project and sets the working directory.

The `data` folder includes the raw country data set used in the vignette (`country-data.csv`) and its corresponding codebook (`data-dictionary.csv`), both of which were downloaded from [Kaggle](https://www.kaggle.com/).

The `scripts` folder includes a script containing all of the code from the vignette (`vignette-script.R`) as well as a `drafts` subfolder containing any drafts of our code.

The `img` folder includes images that we utilized in our vignette.

## Instructions

Clone the repository or download it as a ZIP file. Once it is on your local machine, simply click on `vignette.html` to view the vignette in your web browser. To run the code in `vignette.Rmd` and `scripts/vignette-script.R`, click on `vignette-clustering-methods.Rproj` beforehand to set the working directory.

## References

For further references on the clustering methods mentioned in this vignette, there are many websites and textbooks that provide extensive information on these topics. Here are a few that we accessed to help us:

-   Data set

    -   [[Data] "Unsupervised Learning on Country Data" | Kaggle](https://www.kaggle.com/datasets/rohan0301/unsupervised-learning-on-country-data)

-   Hierarchical clustering

    -   [[Textbook] *An Introduction to Statistical Learning*, Chapter 10.3.2 ](https://link.springer.com/book/10.1007/978-1-4614-7138-7)
    -   [[Article] "How Many Clusters?" | Satoru Hayasaka](https://towardsdatascience.com/how-many-clusters-6b3f220f0ef5)

-   Model-based clustering

    -   [[Article] "Model-based clustering and Gaussian mixture model in R" | Ivan Morgun](https://en.proft.me/2017/02/1/model-based-clustering-r/)
    -   [[Video] "Model-base clustering: an introduction to Gaussian Mixture Models" | Mario Castro](https://youtu.be/h7RVeO-P3zc)
    -   [[Paper] Description of the `mclust` package](https://stat.uw.edu/sites/default/files/files/reports/2012/tr597.pdf)

-   Density-based clustering

    -   [[Article] "How Density-based Clustering works" | ArcGIS Pro](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-statistics/how-density-based-clustering-works.htm)
    -   [[Video] "DBSCAN" | StatQuest](https://youtu.be/RDZUdRSDOok)
    -   [[Forum] "Estimating/Choosing optimal Hyperparameters for DBSCAN" | Stack Overflow](https://stackoverflow.com/questions/15050389/estimating-choosing-optimal-hyperparameters-for-dbscan)

-   Analysis

    -   [[Article] "The Demographic Transition Model" | Prateek Agarwal](https://www.intelligenteconomist.com/demographic-transition-model/)
