# allester-bigrams.R

library(tokenizers)
source('scripts/drafts/allester-preprocessing.R')

clean_training_p_bigrams_df <- clean_training_p %>%
  nlp_fn()

set.seed(102722)
partitions <- clean_training_p_bigrams_df %>% 
  initial_split(prop = 0.8)

# separate DTM from labels
test_dtm <- testing(partitions) %>%
  select(-.id, -bclass)
test_labels <- testing(partitions) %>%
  select(.id, bclass)

# same, training set
train_dtm <- training(partitions) %>%
  select(-.id, -bclass)
train_labels <- training(partitions) %>%
  select(.id, bclass)

# find projections based on training data
proj_out <- projection_fn(.dtm = train_dtm, .prop = 0.7)
train_dtm_projected <- proj_out$data

train <- train_labels %>%
  transmute(bclass = factor(bclass)) %>%
  bind_cols(train_dtm_projected)


x_train <- train %>% select(-bclass) %>% as.matrix()
y_train <- train_labels %>% pull(bclass)

# fit enet model
alpha_enet <- 0.3
fit_reg <- glmnet(x = x_train, 
                  y = y_train, 
                  family = 'binomial',
                  alpha = alpha_enet)

# choose a strength by cross-validation
set.seed(102722)
cvout <- cv.glmnet(x = x_train, 
                   y = y_train, 
                   family = 'binomial',
                   alpha = alpha_enet)

# store optimal strength
lambda_opt <- cvout$lambda.min

# view results
cvout

# project test data onto PCs
test_dtm_projected <- reproject_fn(.dtm = test_dtm, proj_out)

# coerce to matrix
x_test <- as.matrix(test_dtm_projected)

# compute predicted probabilities
preds <- predict(fit_reg, 
                 s = lambda_opt, 
                 newx = x_test,
                 type = 'response')

# store predictions in a data frame with true labels
pred_df <- test_labels %>%
  transmute(bclass = factor(bclass)) %>%
  bind_cols(pred = as.numeric(preds)) %>%
  mutate(bclass.pred = factor(pred > 0.5, 
                              labels = levels(bclass)))

# define classification metric panel 
panel <- metric_set(sensitivity, 
                    specificity, 
                    accuracy, 
                    roc_auc)

# compute test set accuracy
pred_df %>% panel(truth = bclass, 
                  estimate = bclass.pred, 
                  pred, 
                  event_level = 'second')
