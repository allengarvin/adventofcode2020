#!/usr/bin/Rscript --vanilla

numbers <- scan("01-input.txt", numeric())
for (n in combn(numbers, 2, simplify=FALSE)) {
    if ( n[1] + n[2] == 2020 ) print(n[1] * n[2])
}
for (n in combn(numbers, 3, simplify=FALSE)) {
    if ( n[1] + n[2] + n[3] == 2020 ) print(n[1] * n[2] * n[3])
}
