# 4.  Use any method to find either: 
# a simpler panel that achieves comparable classification accuracy,
# or an alternative panel that achieves improved classification accuracy.
# Benchmark your results against the in-class analysis.

# From class -> you can fit a lasso model to find a simpler panel
library(tidymodels)
library(tidyverse)
library(ISLR) 
library(glmnet) 
library(dplyr) 
library(tidyr)
library(yardstick)

# load in clean data
biomarker_clean_noAdos = biomarker_clean %>% select(-ados) 
biomarker <- biomarker_clean_noAdos %>%
  mutate(class = as.numeric(group == 'ASD'))

# partition
x <- biomarker %>%
  select(-group, -class) %>%
  as.matrix()
y <- biomarker %>%
  pull(class)

# create training and testing datasets
set.seed(1234)
train = sample(1:nrow(x), 123)
test = (-train)

x.train = x[train,]
y.train = y[train]
x.test = x[test,]
y.test = y[test]

# perform cross-validation to get test error
cv.out.lasso = cv.glmnet(x.train, y.train, alpha = 1) 
plot(cv.out.lasso)
abline(v = log(cv.out.lasso$lambda.min), col="red", lwd=3, lty=2)

# get best value of lambda and test mse
bestlam = cv.out.lasso$lambda.min

# get coefficient values from best lambda
out=glmnet(x,y,alpha=1,lambda = bestlam) 
coef <- coef(out)[,1]
coef_df <- as.data.frame(coef)
panel <- coef_df %>% filter(coef_df != 0)
panel

# get the accuracy of our prediction model by finding mse
lasso.pred = predict(out, s=bestlam, newx=x.test) 
test.mse = mean((lasso.pred-y.test)^2)
test.mse

class_metrics <- metric_set(sensitivity, specificity, accuracy)
test.data <- cbind(x.test, y.test)
test.data %>%
  add_predictions(out, type = 'response') %>%
  class_metrics(estimate = factor(pred > 0.5),
                truth = factor(group == "ASD"), 
                event_level = 'second')
  
  