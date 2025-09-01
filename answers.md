  # CMPS 6610 Problem Set 01
## Answers

**Name:**___Yifei Sun______________________
**Name:**_________________________


Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**

  - 1a 

The claim $2^{n+1} \in O(2^n)$ is correct, because there exist constants 
$c = 2$ and $n_0 = 1$ such that for all $n \geq 1$:

$$
2^{n+1} = 2 \cdot 2^n \leq c \cdot 2^n = 2 \cdot 2^n
$$

Therefore, $2^{n+1} \in O(2^n)$.

  - 1b    

We claim that $2^{2^n}\notin O(2^n)$. Suppose, to the contrary, that there exist
constants $c>0$ and $n_0$ such that for all $n\ge n_0$,
$$
2^{2^n}\le c\,2^n.
$$
Dividing by $2^n$ gives
$$
2^{\,2^n-n}\le c.
$$
Since $2^n-n\to\infty$, the left-hand side tends to $\infty$, a contradiction.
Hence $2^{2^n}\notin O(2^n)$.
Equivalently, $\displaystyle\lim_{n\to\infty}\frac{2^{2^n}}{2^n}=\infty$,
so $2^{2^n}=\omega(2^n)$.
 
  - 1c

  - 1d

  - 1e

  - 1f

  - 1g

2. **SPARC to Python**

  - 2b

3. **Parallelism and recursion**

  - 3b

  - 3d

  - 3e
  
4. **GCD**
