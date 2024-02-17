

# CMPS 2200 Assignment 1

**Name:**_________________________


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  
.  2^(n+1) is in O(2^n) because 2^(n+1) can be bounded above by 2^n multiplied by a constant for all n beyond a certain poiny (N0 = 1) This shows that 2^(n+1) grows at most as fast as some constant multiple of 2^n fitting the definition of Big O notation
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  
. 2^2^n is not in O(2^n) because the growth rate of 2^2^n is not upper-bounded by a constant multiple of the growth rate of 2^n The function 2^2^n grows much more rapidly and cannot be contained within the bounds defined by O(2^n)
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  
.  n^(1.01) is not in O(log^2n) because the growth rate of n^(1.01) is not bounded above by any constant multiple of log^2n for all sufficiently large The polynomial growth of n^(1.01) exceeds the growth of the squared logarithmic function, indicating that grows faster and cannot be contained within the bounds defined by O(log^2n)
  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  
  n^(1.01) is in Big omega(log^2n)because, for sufficiently large n, n^(1.01) is always greater than or equal to c * log^2n for some constant c>0 This means the growth rate of n^(1.01) is at least as fast as the growth rate of log^2n fulfilling the criteria for Big Omega notation. Essentially, n^(1.01) grows faster than log^2n making it a lower bound for n^(1.01)
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  
.  sqrt(n) is not in O((logn)^3) because there do not exist constants c > 0 and N0 such that for all n >= N0 as n becomes very large, the square root of n grows unboundedly faster than the cubic logarithm of n, indicating that sqrt(n) is not upper-bounded by (logn)^3


.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  
	sqrt(n) is in big omega((logn)^3) because sqrt(n) grows faster than (logn)^3 for all sufficiently large n this means that for large values of n, sqrt(n) will always be greater than or equal to c * (logn)^3 for some positive constant c, satisfying the criteria for big omega notation. Essentially the square root function provides a lower bound on the growth rate for omega((logn)^3) indcating that as n increases sqrt(n) grows at least as quickly, and in fact quicker than the cube of the logarithm of n.


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  
The foo function calculates the nth number in the Fibonacci sequence, where each number is the sum of the two before it. It starts with 0 and 1, then keeps adding the last two numbers to get the next one. If you ask for the first or second number, it gives back 0 or 1. For any other number, it keeps asking itself for the two previous numbers until it can add them up to get the answer you asked for. It's like climbing stairs, where to reach step n, you check how you got to steps n-1 and n-2, and then take one more step from there.
.  
.  
.  
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  
.  Work (W): The work done by the function is proportional to the length of the input list mylist because it iterates through each element exactly once. For each element, it performs a constant amount of work (comparisons, arithmetic operations, and possibly updating variables). Thus, if the length of mylist is n, the work is O(n).

Span (S): The span of this algorithm is also O(n) because the operations are inherently sequential. Each step (comparing the current value to the key and updating the current and maximum run lengths) depends on the completion of the previous step. There's no opportunity to parallelize this specific implementation because each iteration's actions depend on the result of the previous iteration (to maintain current_run and max_run). Therefore, even with infinite processors, you would still need to process each element one after the other, resulting in a span that is linear with respect to the size of the input list.
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  
.  
Work (W)
The algorithm divides the list in half at each step, processing sublists until it reaches base cases (an empty list or a single element).
The total work at each recursion level is proportional to the list's length at that level, leading to O(n) total work across all levels, as the algorithm effectively processes each element once.

Span (S)
The span includes the time to split the list and the time to merge results from recursive calls, both constant operations.
The recursion depth, O(logn), determines the span, reflecting the longest sequence of dependent operations.
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

Work (W)
The total computation, or work, remains O(n), consistent with the sequential version. This is because each element of the list is processed once, regardless of the distribution of work across threads.

Span (S)
The span, however, benefits from parallelism. With each recursive call operating in a new thread, the algorithm's span is governed by the depth of the recursion tree, O(logn). This depth reflects the maximum number of sequential operations, assuming optimal parallel execution.

In essence, while the work stays at O(n), indicating the total computational effort is unchanged, the span improves to O(logn) due to parallel execution, showcasing the potential for speedup in a parallel computing setting.
.  
.  
.  
.  

