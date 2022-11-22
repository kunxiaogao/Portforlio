###### svm-allester.R
library(tidyverse)
library(RTextTools) #train_model
library(caret)
library(rnn)#trainr
source('scripts/drafts/allester-preprocessing.R')
###### run once
load('data/claims-raw.RData')
claims_clean <- claims_raw %>%
  parse_data_p_title()
######

# main

set.seed(110122)
partitions <- claims_clean %>%
  initial_split(prop = 0.8)

train_text <- training(partitions) %>%
  pull(text_clean)
train_labels <- training(partitions) %>%
  pull(bclass) %>%
  as.numeric() - 1


dtMatrix_train <- create_matrix(train_text) %>%
  removeSparseTerms(0.99)

nrow(dtMatrix_train)


# Configure the training data
container <- create_container(dtMatrix_train,
                              train_labels,
                              trainSize=1:nrow(dtMatrix_train),
                              virgin=FALSE)

# train a SVM Model
model <- train_model(container, "SVM", kernel="radial", cost=5)

test_text <- testing(partitions) %>%
  pull(text_clean)
test_labels <- testing(partitions) %>%
  pull(bclass) %>%
  as.numeric() - 1
# prediction matrix
dtMatrix_test <- create_matrix(test_text, originalMatrix=dtMatrix_train)

predictionContainer <- create_container(dtMatrix_test, 
                                        labels=seq(1:length(test_labels)), 
                                        testSize=1:nrow(dtMatrix_test), 
                                        virgin=FALSE)



results <- classify_model(predictionContainer, model)
glimpse(results)
glimpse(test_labels)

sum(test_labels==results['SVM_LABEL'])/length(test_labels)