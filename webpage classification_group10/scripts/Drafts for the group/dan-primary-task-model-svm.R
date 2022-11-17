source('scripts/drafts/dan-preprocessing.R')

# load raw data
load('data/claims-raw.RData')

# preprocess (will take a minute or two)

# with header
claims_clean_header <- claims_raw %>%
  parse_data_header()

# without header
claims_clean <- claims_raw %>%
  parse_data()

# export
save(claims_clean, file = 'data/claims-clean-example.RData')
clean_df <- claims_clean %>%
  select(.id, bclass, text_clean)


## MODEL TRAINING (SVM)
######################
library(tidyverse)
library(tidymodels)
library(RTextTools)
library(yaml)
# library(e1071)
load('data/claims-raw.RData')

# load test data
load('data/claims-test.RData')

# preprocess (will take a minute or two)
claims_clean <- claims_raw %>%
  parse_data()

# export
save(claims_clean, file = 'data/claims-clean-example.RData')
save(claims_test_clean, file = 'data/claims-test-clean.RData')

# partition
set.seed(110122)
partitions <- claims_clean %>%
  initial_split(prop = 0.8)

# separate test and training data

train_text <- training(partitions) %>%
  pull(text_clean)
train_labels <- training(partitions) %>%
  pull(bclass) %>%
  as.numeric() - 1
train_labels_mu <- training(partitions) %>%
  pull(mclass) %>%
  as.numeric() - 1

# Create the document term matrix
dtMatrix <- create_matrix(clean_df["text_clean"])

# svm model for binary classification
# Configure the training data
container <- create_container(dtMatrix, train_labels, trainSize = 1:99, virgin=FALSE)

# train a SVM Model
model <- train_model(container, "SVM", kernel="linear", cost=1)

# preprocess for test
claims_test_clean <- claims_test %>%
  parse_data()
save(claims_test_clean, file = 'data/claims-test-clean.RData')
clean_df_test <- claims_test_clean %>%
  select(.id, text_clean)

dtMatrix_test <- create_matrix(clean_df["text_clean"], originalMatrix = dtMatrix)

# create the corresponding container
predSize = length(clean_df_test);
predictionContainer <- create_container(dtMatrix_test, labels=rep(0,1), testSize=1:915, virgin=FALSE)

results <- classify_model(predictionContainer, model)
results

write_yaml(model, "/scripts/drafts/dan-svm-model")



