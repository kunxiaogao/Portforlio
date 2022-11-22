library(tidyverse)
library(ggplot2)

# get names
var_names <- read_csv('data/biomarker-raw.csv', 
                      col_names = F, 
                      n_max = 2, 
                      col_select = -(1:2)) %>%
  t() %>%
  as_tibble() %>%
  rename(name = V1, 
         abbreviation = V2) %>%
  na.omit()

# read in data
biomarker_clean <- read_csv('data/biomarker-raw.csv', 
                            skip = 2,
                            col_select = -2L,
                            col_names = c('group', 
                                          'empty',
                                          pull(var_names, abbreviation),
                                          'ados'),
                            na = c('-', '')) %>%
  filter(!is.na(group)) %>%
  # log transform, center and scale
  mutate(across(.cols = -c(group, ados))) %>%
  # reorder columns
  select(group, ados, everything())

scale_fn <- function(.x){
  scale(log10(.x))[, 1]
}

# save outliers to a new df
biomarker_outliers <- biomarker_clean %>%
  # log transform, center and scale
  mutate(across(.cols = -c(group, ados), 
                scale_fn),
         subject = row_number()) %>%
  pivot_longer(cols = -c(group, ados, subject),
               names_to = 'variable',
               values_to = 'level')
  
biomarker_outliers2 <- biomarker_outliers %>%
  filter(abs(biomarker_outliers['level']) > 3)
  
# groupby subject to find which subject recorded most outliers
outlier_subjects <- biomarker_outliers2 %>%
  group_by(subject) %>%
  count()

max(outlier_subjects)

p<-ggplot(data=outlier_subjects, aes(x=subject, y=n)) +
  geom_bar(stat="identity") 
p

# it appears that there are some super-outliers among the outliers,
# lets isolate them

outlier_subjects2 <- outlier_subjects %>%
  filter(n > 50)

table(outlier_subjects2)

# let's find the group of the max outlier

maximum <- max(outlier_subjects2$n)
max_row_num <- which(outlier_subjects2$n == maximum)
subject_num <- outlier_subjects2$subject[max_row_num]
biomarker_outliers2$group[biomarker_outliers2$subject == subject_num][1]
# repeat the process to find group of all super-outliers

find_group <- function(x){
  y <- which(outlier_subjects2$n == x)
  z <- outlier_subjects2$subject[y]
  biomarker_outliers2$group[biomarker_outliers2$subject == z][1]
}

outlier_groups <- outlier_subjects2[,2] %>%
  apply(FUN = find_group, MARGIN = 1)

# tabulate results
table(outlier_groups)

# majority of super-outliers are typically developing

outlier_groups_df <- as.data.frame(outlier_groups)

mutate(outlier_subjects2, outlier_groups_df)

# it seems most of the "super-outliers" are typically developing
# let's repeat the process, this time for our original group of outliers

find_group2 <- function(x){
  y <- which(outlier_subjects$n == x)
  z <- outlier_subjects$subject[y]
  biomarker_outliers2$group[biomarker_outliers2$subject == z][1]
}

outlier_subjects3 <- outlier_subjects[,2] %>%
  apply(FUN = find_group2, MARGIN = 1)

# tabulate results
table(outlier_subjects3)

# surprisingly, our analysis uncovered that for the "regular outliers"
# the most common group was ASD, by a wide margin
# export as r binary
save(list = 'biomarker_clean', 
     file = 'data/biomarker-clean.RData')

