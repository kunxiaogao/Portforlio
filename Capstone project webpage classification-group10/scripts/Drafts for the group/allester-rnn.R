library(tidyverse)
library(tidymodels)
library(tidytext)
library(keras)
library(tensorflow)
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

train_dtm <- training(partitions) %>%
  unnest_tokens(output = 'token', 
                input = text_clean) %>%
  group_by(.id, bclass) %>%
  count(token) %>%
  bind_tf_idf(term = token, 
              document = .id, 
              n = n) %>%
  pivot_wider(id_cols = c(.id, bclass), 
              names_from = token, 
              values_from = tf_idf,
              values_fill = 0) %>%
  ungroup()

# specify model type
rnn_model <- keras_model_sequential() %>%
  layer_simple_rnn(units = 64, dropout = 0.2, recurrent_dropout = 0.2) %>% 
  layer_dense(units = 1, activation = 'sigmoid')
  
