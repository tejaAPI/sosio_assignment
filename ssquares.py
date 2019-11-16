n=int(input())
#Find the sum of squares of n natural numbers 
sum_of_squares=(n*(n+1)*(2*n+1))//6
#Find the sum of n natural numbers and square the result
square_of_sum=((n*(n+1))//2)**2
#Print the difference 
print(abs(sum_of_squares-square_of_sum))
