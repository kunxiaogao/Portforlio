## ---- include=FALSE-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# set code chunk options
knitr::opts_chunk$set(echo = TRUE, 
                      fig.align = 'center',
                      cache = TRUE)

# allow scrolling for long code
options(width = 200)


## ---- eval=FALSE--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## # install packages
## install.packages('tidyverse')
## install.packages('factoextra')
## install.packages('cluster')
## install.packages('dendextend')
## install.packages('mclust')
## install.packages('dbscan')
## install.packages('fpc')


## ---- message=FALSE-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# load packages
library(tidyverse)
library(factoextra)
library(cluster)
library(dendextend)
library(mclust)
library(dbscan)
library(fpc)

# read data
countries <- read.csv("data/country-data.csv")

# use countries as the row names
df <- countries %>%
  column_to_rownames(var = "country")

# show the first few rows of the dataframe
head(df)


## -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# scale and center the dataframe
scaled.df <- df %>% scale()

# run elbow method (best = 5 clusters)
fviz_nbclust(scaled.df,
             hcut,
             method = "wss") +
  # vertical dashed line at the optimal number of clusters
  geom_vline(xintercept = 5, 
             linetype = 2)


## -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# run average silhouette method (best = 2 clusters)
fviz_nbclust(scaled.df, 
             hcut, 
             method = "silhouette")


## -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# calculate gap statistic
set.seed(123)
gap_stat <- clusGap(scaled.df,
                    hcut,
                    K.max = 10, # max number of clusters to consider
                    B = 500)    # number of samples to bootstrap

# run gap statistic method (best = 3 clusters)
fviz_gap_stat(gap_stat)


## ---- fig.height=20-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
df %>%
  scale() %>%                # scale and center the columns
  dist() %>%                 # get the Euclidean distances between rows             
  hclust() %>%               # apply hierarchical clustering
  as.dendrogram() %>%        # turn the cluster output into a dendrogram
  set("labels_cex", 0.4) %>% # make the font size smaller
  color_branches(k = 2) %>%  # color the branches based on the 2 clusters
  color_labels(k = 2) %>%    # color the labels based on the 2 clusters
  plot(horiz = TRUE)         # make the labels appear on the right


## ---- fig.height=20-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
df %>%
  scale() %>%                # scale and center the columns
  dist() %>%                 # get the Euclidean distances between rows  
  hclust() %>%               # apply hierarchical clustering
  as.dendrogram() %>%        # turn the cluster output into a dendrogram
  set("labels_cex", 0.4) %>% # make the font size smaller
  color_branches(k = 3) %>%  # color the branches based on the 3 clusters
  color_labels(k = 3) %>%    # color the labels based on the 3 clusters
  plot(horiz = TRUE)         # make the labels appear on the right


## ---- fig.height=20-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
df %>%
  scale() %>%                # scale and center the columns
  dist() %>%                 # get the Euclidean distances between rows  
  hclust() %>%               # apply hierarchical clustering
  as.dendrogram() %>%        # turn the cluster output into a dendrogram
  set("labels_cex", 0.4) %>% # make the font size smaller
  color_branches(k = 4) %>%  # color the branches based on the 4 clusters
  color_labels(k = 4) %>%    # color the labels based on the 4 clusters
  plot(horiz = TRUE)         # make the labels appear on the right


## ---- fig.height=20-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
df %>%
  scale() %>%                # scale and center the columns
  dist() %>%                 # get the Euclidean distances between rows  
  hclust() %>%               # apply hierarchical clustering
  as.dendrogram() %>%        # turn the cluster output into a dendrogram
  set("labels_cex", 0.4) %>% # make the font size smaller
  color_branches(k = 5) %>%  # color the branches based on the 5 clusters
  color_labels(k = 5) %>%    # color the labels based on the 5 clusters
  plot(horiz = TRUE)         # make the labels appear on the right


## -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# perform hierarchical clustering and get k clusters
k_hclust <- function(.df, k) {
  .df %>%
    scale() %>%  # scale and center the columns
    dist() %>%   # get the Euclidean distances between rows
    hclust() %>% # apply hierarchical clustering
    cutree(k)    # separate observations into k clusters
}

# turn the cluster output into a dataframe
clust_to_df <- function(.clust) {
  .clust %>%                              # must be a named vector: clusters as values, countries as names
    cbind() %>%                           # combine countries and clusters by column
    data.frame() %>%                      # convert to data frame
    rename(cluster = 1) %>%               # rename the first column as 'cluster'
    mutate(cluster = factor(cluster)) %>% # convert the 'cluster' column into a factor
    rownames_to_column("country")         # turn the row names (countries) into a column called 'country'
}

# rename countries to be able to plot them
rename_countries <- function(.df) {
  .df %>%
    # replace original country names with new country names (important for the plot_map() function!)
    mutate(across('country', str_replace, 'Antigua and Barbuda', 'Antigua'),
           across('country', str_replace, 'Congo, Dem. Rep.', 'Democratic Republic of the Congo'),
           across('country', str_replace, 'Congo, Rep.', 'Republic of Congo'),
           across('country', str_replace, 'Cote d\'Ivoire', 'Ivory Coast'),
           across('country', str_replace, 'Kyrgyz Republic', 'Kyrgyzstan'),
           across('country', str_replace, 'Lao', 'Laos'),
           across('country', str_replace, 'Macedonia, FYR', 'North Macedonia'),
           across('country', str_replace, 'Micronesia, Fed. Sts.', 'Micronesia'),
           across('country', str_replace, 'Slovak Republic', 'Slovakia'),
           across('country', str_replace, 'St. Vincent and the Grenadines', 'Saint Vincent'),
           across('country', str_replace, 'United Kingdom', 'UK'),
           across('country', str_replace, 'United States', 'USA')) %>%
    # add separate rows for countries that were originally grouped together
    add_row(country = 'Barbuda', cluster = filter(., country == 'Antigua') %>% getElement('cluster')) %>%
    add_row(country = 'Grenadines', cluster = filter(., country == 'Saint Vincent') %>% getElement('cluster'))
}

# plots the clusters onto the world map
plot_map <- function(.df) {
  # dataframe containing information (e.g. latitude, longitude) on all countries
  world <- map_data("world")
  
  world %>%
    # (left) join 'world' dataframe with another dataframe at columns with the country names
    left_join(.df, by = c("region" = "country")) %>%
    # plot the map
    ggplot() +
      geom_polygon(aes(x = long, y = lat, fill = cluster, group = group),
                   color = "white") +
      coord_fixed(1.3) +
      theme(legend.position = "top")
}


## -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# dataframe containing information (e.g. latitude, longitude) on all countries
world <- map_data("world")

# get unique countries in 'df' and 'world'
unique_countries_df <- row.names(df) %>% unique() %>% sort()
unique_countries_world <- world$region %>% unique() %>% sort()

# get all countries that occur in 'df' but not in 'world'
setdiff(unique_countries_df, unique_countries_world)


## ---- out.width='150%'--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# plot 2 clusters onto the world map
df %>%
  k_hclust(2) %>%
  clust_to_df() %>%
  rename_countries() %>%
  plot_map()


## ---- out.width='150%'--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# plot 3 clusters onto the world map
df %>%
  k_hclust(3) %>%
  clust_to_df() %>%
  rename_countries() %>%
  plot_map()


## ---- out.width='150%'--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# plot 4 clusters onto the world map
df %>%
  k_hclust(4) %>%
  clust_to_df() %>%
  rename_countries() %>%
  plot_map()


## ---- out.width='150%'--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# plot 5 clusters onto the world map
df %>%
  k_hclust(5) %>%
  clust_to_df() %>%
  rename_countries() %>%
  plot_map()


## -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# run model-based clustering algorithm
mb <- Mclust(df)

# output model and number of clusters chosen
summary(mb)


## -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# create BIC plot
plot(mb, what = "BIC")


## -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# create classification plots
plot(mb, what = "classification")


## -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# classification plot of life_expec against health
plot(mb, what = "classification", dimens = c(3, 7))


## -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# create uncertainty plots
plot(mb, what = "uncertainty")


## -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# uncertainty plot of life_expec against health
plot(mb, what = "uncertainty", dimens = c(3, 7))


## -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# create density plots
plot(mb, what = "density")


## -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# density plot of life_expec against health
plot(mb, what = "density", dimens = c(3, 7))


## ---- out.width='150%'--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# plot clusters onto the world map
mb$classification %>%
  clust_to_df() %>%
  rename_countries() %>%
  plot_map()


## ---- out.width='150%'--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# run the algorithm
mb2 <- Mclust(scaled.df)

# plot clusters onto the world map
mb2$classification %>%
  clust_to_df() %>%
  rename_countries() %>%
  plot_map()


## -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
kNNdistplot(scaled.df, k = 5) # plot k-distance graph
abline(h = 2.5, col = "red")  # best value of eps


## -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# create cluster with maximum radius of 3 for the neighborhood 
# with at least 18 points include in each cluster
set.seed(1)
db <- fpc::dbscan(scaled.df, eps = 3, MinPts = 18)

# visualize the clustering results
fviz_cluster(db, data = scaled.df, stand = FALSE,
             ellipse = FALSE, show.clust.cent = FALSE,
             geom = "point", palette = "jco", ggtheme = theme_classic())


## ---- warning = FALSE---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# create cluster with maximum radius of 3 for the neighborhood 
# with at least 5 points include in each cluster
set.seed(1)
db1 <- fpc::dbscan(scaled.df, eps = 3, MinPts = 5)

# visualize the clustering results
fviz_cluster(db1, data = scaled.df, stand = FALSE,
             ellipse = FALSE, show.clust.cent = FALSE,
             geom = "point", palette = "jco", ggtheme = theme_classic())


## -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# create cluster with maximum radius of 6 for the neighborhood 
# with at least 5 points include in each cluster
set.seed(1)
db <- fpc::dbscan(scaled.df, eps = 6, MinPts = 5)

# visualize the clustering result
fviz_cluster(db, data = scaled.df, stand = FALSE,
             ellipse = FALSE, show.clust.cent = FALSE,
             geom = "point", palette = "jco", ggtheme = theme_classic())


## -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# create cluster with maximum radius of 1 for the neighborhood 
# with at least 5 points include in each cluster
set.seed(1)
db <- fpc::dbscan(scaled.df, eps = 1, MinPts = 5)

# visualize the clustering result
fviz_cluster(db, data = scaled.df, stand = FALSE,
             ellipse = FALSE, show.clust.cent = FALSE,
             geom = "point", palette = "jco", ggtheme = theme_classic())


## -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# perform PCA on scaled data
pr.out <- prcomp(scaled.df,
                 scale = TRUE,
                 center = TRUE)

# plot the first 2 principal components
plot(pr.out$x[,1], pr.out$x[,2],
     xlab = 'PC1', ylab = 'PC2')


## ---- out.width='150%'--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# add country names to clusters
db_clust <- db1$cluster
names(db_clust) <- row.names(df)

# plot clusters onto the world map
db_clust %>%
  clust_to_df() %>%
  rename_countries() %>%
  plot_map()


## ---- include=FALSE-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# put just code in our R script
knitr::purl(input = 'vignette.Rmd', 
            output = 'scripts/vignette-script.R')

