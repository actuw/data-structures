# Data Structures and Algorithms Challenges 

Table of Contents 
============
- [Beginner]()
    - [Challenge #1]()

Beginner 
============
- [ ] Challenge 1

    ##### Print a new number by adding one to each of its digit
    ---

    ###### Description 
    *A number is input in computer then a new no should get printed by adding one to each of its digit. If you encounter a 9, insert a 10 (don't carry over, just shift things around). For example, 998 becomes 10109.* 

    ###### Bonus 
    *Using recursion implement a function where the output described in the challenge above is used as an input in the same function (using recursion) for N times. For example, if N = 3 and input is 998 the output should be 10109, 212110, 323221, so the final output (returned value) should be 323221.*
    
    ###### Credit
    *This challenge was taken from [reddit/r/dailyprogrammer](https://www.reddit.com/r/dailyprogrammer/comments/aphavc/20190211_challenge_375_easy_print_a_new_number_by/), thanks to [/u/chetvishal](https://www.reddit.com/user/chetvishal). The bonus part was suggested by [achmand](https://github.com/achmand), many thanks for both suggestions.*


- [ ] Challenge 2

    ##### Hailstone Sequence 
    ---
    
    ###### Description 
    *Given a positive integer as an input to a function, apply these two different rules to the input; if the input is an even number divide it by 2, if it is an odd number multiply it by 3 and subtract 1. Apply these rules until the number reaches 1. The function must return an array/list of all the numbers in the sequence, so for example if the input is 3 the returned array/list must contain [3, 10, 5, 16, 8, 4, 2, 1].*
    
    *For this challenge implement two functions one using a loop and the other using recursion. To test your output for different inputs you can visit [dcode](https://www.dcode.fr/collatz-conjecture).* 
    
    *For more information on the Hail Stone Sequence/Collatz Conjecture visit [Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture) or [On the 3x + 1 problem](http://www.ericr.nl/wondrous/). This problem is still unsolved in mathematics and there is no proof which shows that the sequence will converge to 1 for all positive integers. A recent [paper](https://ieeexplore.ieee.org/abstract/document/8560077) was published in 2018 which proposed an interesting algorithm which could verify 2^100000-1 positive integers.*
    
    ###### Bonus 
    
    *For the sequence generated output the number of steps taken for the sequence to be less than the input (also known as the Glide Time). So, in the example above the sequence returned was [3, 10, 5, 16, 8, 4, 2, 1], so the Glide Time for this sequence is 6, since it took 6 steps for the number to be lower than the input (2 < 3). For this bonus challenge write two new functions (one using a loop and the other using recursion) which takes an array/list as an input and outputs the Glide Time.*
