# Continue from the anni_logistic.R
# compute predicted probabilities
preds <- predict(fit_reg_word, 
                 s = lambda_opt, 
                 newx = x_train,
                 type = 'link')

preds_test <- predict(fit_reg_word, 
                      s = lambda_opt, 
                      newx = x_test,
                      type = 'link')

# Bigrams token
nlp_fn_bigram <- function(parse_data.out){
  out <- parse_data.out %>% 
    unnest_tokens(output = token, 
                  input = text_clean, 
                  token = 'ngrams',n=2,
                  stopwords = str_remove_all(stop_words$word, 
                                             '[[:punct:]]')) %>%
    mutate(token.lem = lemmatize_words(token)) %>%
    filter(str_length(token.lem) > 2) %>%
    count(.id, bclass,mclass, token.lem, name = 'n') %>%
    bind_tf_idf(term = token.lem, 
                document = .id,
                n = n) %>%
    pivot_wider(id_cols = c('.id', 'bclass','mclass'),
                names_from = 'token.lem',
                values_from = 'tf_idf',
                values_fill = 0)
  return(out)
}

out_bigrams <- nlp_fn_bigram(claims_clean)

set.seed(102722) # same seed, so this will give us the same split as in word token
partitions <- out_bigrams %>% initial_split(prop = 0.8)

# separate DTM from labels
test_dtm_bi <- testing(partitions) %>%
  select(-.id, -bclass, -mclass)
test_labels_bi <- testing(partitions) %>%
  select(.id, bclass, mclass)

# same, training set
train_dtm_bi <- training(partitions) %>%
  select(-.id, -bclass, -mclass)
train_labels_bi <- training(partitions) %>%
  select(.id, bclass, mclass)


# find projections based on training data
proj_out_bi <- projection_fn(.dtm = train_dtm_bi, .prop = 0.7)
train_dtm_projected_bi <- proj_out_bi$data

# how many components were used?
proj_out_bi$n_pc

train_bi <- train_labels_bi %>%
  transmute(bclass = factor(bclass)) %>%
  bind_cols(train_dtm_projected_bi) %>%
  bind_cols(preds[1])

# store predictors and response as matrix and vector
x_train_bigrams <- train_bi %>% select(-bclass) %>% as.matrix()
y_train_bigrams <- train_labels_bi %>% pull(bclass)

# fit enet model
alpha_enet <- 0.3
fit_reg_bigrams<- glmnet(x = x_train_bigrams, 
                       y = y_train_bigrams, 
                       family = 'binomial',
                       alpha = alpha_enet)

# choose a strength by cross-validation
set.seed(102722)
cvout <- cv.glmnet(x = x_train_bigrams, 
                   y = y_train_bigrams, 
                   family = 'binomial',
                   alpha = alpha_enet)

# store optimal strength
lambda_opt <- cvout$lambda.min


# project test data onto PCs
test_dtm_projected_bi <- reproject_fn(.dtm = test_dtm_bi, proj_out_bi)



# coerce to matrix
test_dtm_projected_bi <- test_dtm_projected_bi %>% bind_cols(preds_test[1])
x_test_bi <- as.matrix(test_dtm_projected_bi)



# compute predicted probabilities
preds <- predict(fit_reg_bigrams, 
                 s = lambda_opt, 
                 newx = x_test_bi,
                 type = 'response')

# store predictions in a data frame with true labels
pred_df <- test_labels_bi %>%
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
