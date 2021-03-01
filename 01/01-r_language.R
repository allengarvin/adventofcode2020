#!/usr/bin/Rscript --vanilla

library(purrr)

numbers <- scan("01-input.txt", numeric())
for (comb in c(2, 3))
    for (n in combn(numbers, comb, simplify=FALSE)) 
        if ( sum(n) == 2020 ) 
            print(reduce(n, `*`))
