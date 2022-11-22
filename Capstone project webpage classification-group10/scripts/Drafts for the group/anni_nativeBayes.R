

# Installing Packages
install.packages("e1071")
install.packages("caTools")
install.packages("caret")

# Loading package
library(e1071)
library(caTools)
library(caret)

# Splitting data into train
# and test data
# train_labels,train_dtm_projected and test_... from anni_logistic.R,
train_data <- bind_cols(train_labels,train_dtm_projected)
test_data <- bind_cols(test_labels,test_dtm_projected)
# Fitting Naive Bayes Model
# to training dataset
set.seed(120)  # Setting Seed
classifier_cl <- naiveBayes(bclass ~ .-.id-mclass,data = train_data)
classifier_cl

# Predicting on test data'
y_pred <- predict(classifier_cl, newdata = test_data)

# Confusion Matrix
cm <- table(test_data$bclass, y_pred)
cm

# Model Evaluation
confusionMatrix(cm)
# 56.9% accuracy