# setup
library(tidyverse)
library(tidytext)
library(tokenizers)
library(textstem)
library(stopwords)
library(modelr)
library(rsample)
library(yardstick)

# can comment entire section out if no changes to preprocessing.R
source('scripts/drafts/dan-preprocessing.R')

# load raw data
load('data/claims-raw.RData')

# preprocess (will take a minute or two)

# with header
claims_clean_header <- claims_raw %>%
  parse_data_header()

# without header
claims_clean <- claims_raw %>%
  parse_data()

# export
save(claims_clean, file = 'data/claims-clean-example.RData')
clean_df <- claims_clean %>%
  select(.id, bclass, text_clean)
# for reproducibility
set.seed(102022)

# partition data
partitions <- clean_df %>%
  initial_split(prop = 0.8)

# examine
partitions

clean_df %>% head()

stpwrd <- stop_words %>%
  pull(word) %>%
  str_remove_all('[[:punct:]]')

claims_tokens_long <- clean_df %>%
  unnest_tokens(output = token, # specifies new column name
                input = text_clean, # specifies column containing text
                token = 'words', # how to tokenize
                stopwords = stpwrd) %>% # optional stopword removal
  mutate(token = lemmatize_words(token)) 

# claims_tokens_long %>% head()


claims_tfidf <- claims_tokens_long %>%
  count(.id, token) %>%
  bind_tf_idf(term = token,
              document = .id,
              n = n) 

claims_df <- claims_tfidf %>%
  pivot_wider(id_cols = .id, 
              names_from = token,
              values_from = tf_idf,
              values_fill = 0)

claims_df %>% head()

claims_tfidf %>%
  group_by(.id) %>%
  slice_max(tf_idf, n = 2)

