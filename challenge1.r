# challenge 1 using R
input = "998"
counter <- function(digits, n){
    if(n<=0){
        return (digits)
    }
    else{
        digit.array <- as.integer(strsplit(digits, "")[[1]]) + 1
        digit.array <- paste(digit.array, sep = '', collapse = '')
        counter(digit.array, n - 1)
    }
}

result <- counter(input, 3)
print(result)
