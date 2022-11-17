library(tidyverse)
library(tidymodels)
library(modelr)
library(Matrix)
library(sparsesvd)
library(glmnet)

# can comment entire section out if no changes to preprocessing.R
source('scripts/drafts/dan-preprocessing.R')

# load raw data
load('data/claims-raw.RData')

# with header
claims_clean_header <- claims_raw %>%
  parse_data_header()

# without header
claims_clean <- claims_raw %>%
  parse_data()

# export
save(claims_clean, file = 'data/claims-clean-example.RData')
save(claims_clean_header, file = 'data/claims-clean-header.RData')

### NO HEADER ###

# partition data
set.seed(102722)
partitions <- claims_clean %>% initial_split(prop = 0.8)

url <- 'https://raw.githubusercontent.com/pstat197/pstat197a/main/materials/activities/data/'
source(paste(url, 'projection-functions.R', sep = ''))

# separate test and training data
test_dtm <- testing(partitions) %>%
  select(-.id, -bclass, -mclass)
test_labels <- testing(partitions) %>%
  select(.id, bclass, mclass)

train_dtm <- training(partitions) %>%
  select(-.id, -bclass, -mclass)
train_labels <- training(partitions) %>%
  select(.id, bclass, mclass)

# find projections based on training data
proj_out <- projection_fn(.dtm = train_dtm, .prop = 0.7)
train_dtm_projected <- proj_out$data

# binary classification
train <- train_labels %>%
  transmute(bclass = factor(bclass)) %>%
  bind_cols(train_dtm_projected)

test <- test_labels %>%
  transmute(bclass = factor(bclass)) %>%
  bind_cols(test_dtm_projected)

fit <- glm(bclass ~ ., data = train, family = 'binomial')

# compute predictions on test
test %>%
  add_predictions(fit)

# manually transform to probabilities
test %>%
  add_predictions(fit) %>%
  mutate(probs = 1/(1 + exp(-pred))) %>%
  select(bclass, pred, probs) %>%
  head(5)

# predict classes
test %>%
  add_predictions(fit, type = 'response') %>%
  mutate(pred.class = (pred > 0.5)) %>%
  select(bclass, pred, pred.class) %>%
  head(5)

# tabulate
test %>%
  add_predictions(fit, type = 'response') %>%
  mutate(pred.class = (pred > 0.5)) %>%
  select(bclass, pred.class) %>%
  table()

# store predictions as factors
pred_df <- test %>%
  add_predictions(fit, type = 'response') %>%
  mutate(pred.class = (pred > 0.5),
         group = factor(bclass, labels = c('N/A', 'Relevant')),
         pred.group = factor(pred.class, labels = c('N/A', 'Relevant'))) 



# define panel (arguments must be yardstick metric function names)
panel_fn <- metric_set(accuracy)

# compute
pred_df %>%
  panel_fn(truth = group,
           estimate = pred.group,
           event_level = 'second')

pred_df %>% conf_mat(truth = group, estimate = pred.group)

# Prediction N/A Relevant
# N/A      137       33
# Relevant  36      189

### WITH HEADER ###

# partition data
set.seed(102722)
partitions_header <- claims_clean_header %>% initial_split(prop = 0.8)


# separate test and training data
test_dtm_header <- testing(partitions_header) %>%
  select(-.id, -bclass, -mclass)
test_labels_header <- testing(partitions_header) %>%
  select(.id, bclass, mclass)

train_dtm_header <- training(partitions_header) %>%
  select(-.id, -bclass, -mclass)
train_labels_header <- training(partitions_header) %>%
  select(.id, bclass, mclass)

# find projections based on training data
proj_out <- projection_fn(.dtm = train_dtm_header, .prop = 0.7)
train_dtm_projected <- proj_out$data

# binary classification
train <- train_labels_header %>%
  transmute(bclass = factor(bclass)) %>%
  bind_cols(train_dtm_projected)

test <- test_labels_header %>%
  transmute(bclass = factor(bclass)) %>%
  bind_cols(test_dtm_projected)

fit <- glm(bclass ~ ., data = train, family = 'binomial')

# compute predictions on test
test %>%
  add_predictions(fit)

# manually transform to probabilities
test %>%
  add_predictions(fit) %>%
  mutate(probs = 1/(1 + exp(-pred))) %>%
  select(bclass, pred, probs) %>%
  head(5)

# predict classes
test %>%
  add_predictions(fit, type = 'response') %>%
  mutate(pred.class = (pred > 0.5)) %>%
  select(bclass, pred, pred.class) %>%
  head(5)

# tabulate
test %>%
  add_predictions(fit, type = 'response') %>%
  mutate(pred.class = (pred > 0.5)) %>%
  select(bclass, pred.class) %>%
  table()

# store predictions as factors
pred_df <- test %>%
  add_predictions(fit, type = 'response') %>%
  mutate(pred.class = (pred > 0.5),
         group = factor(bclass, labels = c('N/A', 'Relevant')),
         pred.group = factor(pred.class, labels = c('N/A', 'Relevant'))) 



# define panel (arguments must be yardstick metric function names)
panel_fn <- metric_set(accuracy)

# compute
pred_df %>%
  panel_fn(truth = group,
           estimate = pred.group,
           event_level = 'second')

pred_df %>% conf_mat(truth = group, estimate = pred.group)

# Prediction N/A Relevant
# N/A      137       33
# Relevant  36      189
