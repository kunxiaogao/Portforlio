require(tidyverse)
require(keras)
require(tensorflow)
load('data/claims-test.RData')
load('data/claims-raw.RData')
source('scripts/preprocessing.R')
tf_model <- load_model_tf('results/example-model')

# apply preprocessing pipeline
clean_df <- claims_test %>%
  slice(1:100) %>%
  parse_data() %>%
  select(.id, text_clean)

# grab input
x <- clean_df %>%
  pull(text_clean)

# compute predictions
preds <- predict(tf_model, x) %>%
  as.numeric()

class_labels <- claims_raw %>% pull(bclass) %>% levels()

pred_classes <- factor(preds > 0.5, labels = class_labels)

# export (KEEP THIS FORMAT IDENTICAL)
pred_df <- clean_df %>%
  bind_cols(bclass.pred = pred_classes) %>%
  select(.id, bclass.pred)

save(pred_df, file = 'results/example-preds.RData')
