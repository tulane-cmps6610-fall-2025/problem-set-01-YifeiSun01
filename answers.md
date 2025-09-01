  # CMPS 6610 Problem Set 01
## Answers

**Name:**___Yifei Sun______________________
**Name:**_________________________


Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**

  - 1a 

Yes, because there exist constants 
$c = 2$ and $n_0 = 1$ such that for all $n \geq 1$:

$$
2^{n+1} = 2 \cdot 2^n \leq c \cdot 2^n = 2 \cdot 2^n
$$

Therefore, $2^{n+1} \in O(2^n)$.

  - 1b    

No. 

Suppose, for contradiction, that $2^{2^n} \in O(2^n)$.  
Then there exist constants $c>0$ and $n_0$ such that for all $n \ge n_0$:

$$ 2^{2^n} \le c \cdot 2^n $$

Dividing both sides by $2^n$ gives:

$$ 2^{2^n - n} \le c $$

But since $2^n - n \to \infty$, the left-hand side satisfies:

$$ 2^{2^n - n} \to \infty $$

which cannot be bounded by a constant $c$. This is a contradiction. Therefore:

$$ 2^{2^n} \notin O(2^n) $$

Equivalently, taking $\log_2$ on both sides of the inequality would give:

$$ 2^n \le n + \log_2 c $$

but the left-hand side grows exponentially while the right-hand side grows only linearly, so the inequality cannot hold for sufficiently large $n$. Thus:

$$ \lim_{n \to \infty} \frac{2^{2^n}}{2^n} = \infty $$

so:

$$ 2^{2^n} = \omega(2^n) $$

 
  - 1c

No. 

Suppose there exist $c>0$ and $n_0$ such that for all $n\ge n_0$,

$$ n^{1.01} \le c(\log n)^2. $$

Taking logs gives

$$ 1.01\log n \le \log c + 2\log\log n, $$

which cannot hold for large $n$ since $\log n / \log\log n \to \infty$. Hence $n^{1.01}\notin O((\log n)^2)$.


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
