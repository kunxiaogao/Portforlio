# train_labels,train_dtm_projected and test_... from anni_logistic.R,
train_data <- bind_cols(train_labels,train_dtm_projected)
test_data <- bind_cols(test_labels,test_dtm_projected)
svm_model_b <- svm(bclass ~ .-.id-mclass,data = train_data,
                   kernel = "radial", cost = 35, scale = TRUE)

pred_test <- predict(svm_model_b,test_data)
# Check accuracy:
m_test_b <- table(pred_test, test_labels$bclass) #
confusionMatrix(m_test_b) # 82.44% accuracy

svm_model_m <- svm(mclass ~ .-.id-bclass,data = train_data,
                   kernel = "radial", cost = 40, scale = TRUE)

pred_test <- predict(svm_model_m,test_data)
# Check accuracy:
m_test_m<- table(pred_test, test_labels$mclass) #
confusionMatrix(m_test_m) # 81.03% overall accuracy 
