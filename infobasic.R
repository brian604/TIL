### Statistical Computing ### ----

### Combinations and Permutations in R ----
## Author : Jiwon Kim 
# Probability 
p <- c(0.8, 0.6,0.2)
weather <- c(0.1,0.6,0.3)
p_vec <- c()
for (i in 1:3){
  p_vec[i] <- weather[i] * choose(10,4)*p[i]^4*(1-p[i])^(i)^6
}

# sigma of the series 
l <- c(0.16,0.84)
p_vec1 <- c()
for (i in 1:5){
  p_vec[i] <- (l[1]^i)*(l[2]^(5-i))
}

# Initiatlize the empty vector 
n <- c()
# How would I initiatize the empty data-frame?

for (i in 1:3){
  val <- c(8:10)
  n[i] <- choose(10,val[i])
}

expand_bn <- function(a,b,c){
  if (c = 1){  # c is power 
    return (paste(as.character(1),paste("-",b)))}
  else{
    
    b_p <- paste0(b,p)
  }
}

### Probability distribution in R ----
# NegBin = "finding # of trials on which rth success occur" 

# Bayesian Estimation
x <- c(0,0,1,0,0,2,0,0,5)
a <- 3.68 +10
b <- 8.42 + sum(x)
pbeta(0.4,shape1 = a, shape2 = b, lower.tail = T)



