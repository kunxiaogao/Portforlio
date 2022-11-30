data {
  int<lower=0> N1;
  int<lower=0> N2;
  vector[N1] y1;
  vector[N2] y2;
}

parameters {
  real mu1;
  real mu2;
  real<lower=0> sigma1;
  real<lower=0> sigma2;
}

model {
  sigma1 ~ uniform(0,1000);
  mu1 ~ uniform(0,2000);
  sigma2 ~ uniform(0,1000);
  mu2 ~ uniform(0,2000);
  y1 ~ normal(mu1, sigma1);
  y2 ~ normal(mu2, sigma2);
}
