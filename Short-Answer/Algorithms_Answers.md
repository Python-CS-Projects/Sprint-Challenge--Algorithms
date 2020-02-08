#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)Since the first and last lines are constants O(1) and the while loop is linear O(n) then we drop constants and the total is O(n)
O(1) + O(n2) + O(1) = O(n)

a = 0 # constant T O(1)
while (a < n _ n _ n): # linear T O(n)
a = a + n \* n # constant T O(1)

```


b)In this case with the inner while loop and after dropping the constants the result would be O(n2)

O(1) + O(n) + O(1) + O(n) + O(1) + O(1) = O(n2)

 sum = 0 # constant T O(1)
    for i in range(n): # Linear T O(n)
      j = 1 # constant T O(1)
      while j < n: # Linear T O(n)
        j *= 2 # constant T O(1)
        sum += 1 # constant amount of operations T O(1)
```

c)The amount of operations increases dramatically as the in relation to n so this would be O(n2)

def bunnyEars(bunnies):
if bunnies == 0: # constant T O(1)
return 0 # constant T O(1)

      return 2 + bunnyEars(bunnies-1) #Quadratic  T O(n2)

## Exercise II

```
# 1.An egg gets broken if it is thrown off floor f or higher

# 2.Doesn't get broken if dropped off a floor less than floor f.

# 3.Determine the value of f such that the number of dropped + broken eggs is minimized

```

def find_h_floor(n):
num_of_eggs = 100
#1.Split n in two and assign the miffle to f (floor f = n // 2) and throw and egg
f = n // 2
low_list = list(range(1,f))
high_list = list(range(f,n+1))
#base case if length of low_list = 0 return f
#2.if the egg breaks reasign f to the middle of smaller half
f = low_list // 2
#3.if the egg does not break reasign f to the middle of higher half
f = high_list // 2

        #4.Recurse till the the length of low_list = 0

```

Finally the runtime of this algorithm would be O(nlogn) mainly because we are dividing the arrays till we get to the base case


```
