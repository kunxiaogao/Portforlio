# train_labels,train_dtm_projected and test_... from anni_logistic.R,
train_data <- bind_cols(train_labels,train_dtm_projected)
test_data <- bind_cols(test_labels,test_dtm_projected)
svm_model_b <- svm(bclass ~ .-.id-mclass,data = train_data,
                 kernel = "radial", cost = 35, scale = TRUE)

pred_test_b <- predict(svm_model_b,test_data)
# Check accuracy:
m_test_b <- table(pred_test_b, test_labels$bclass) #
confusionMatrix(m_test_b) 

svm_model_m <- svm(mclass ~ .-.id-bclass,data = train_data,
                 kernel = "radial", cost = 40, scale = TRUE)

pred_test_m <- predict(svm_model_m,test_data)
save(pred_test, file = 'results/multiclass-preds.RData')
# Check accuracy:
m_test_m<- table(pred_test_m, test_labels$mclass) #
confusionMatrix(m_test_m) 

df <- bind_rows(train_data,test_data)
label <- bind_rows(train_labels,test_labels)
prediction <- bind_cols(label,predict(svm_model_b,df),predict(svm_model_m,df))
save(prediction, file = 'results/preds-group10.RData')

save(pred_test_b, file = 'results/binary_svm_model')
save(pred_test_m, file = 'results/multiclass_svm_model')