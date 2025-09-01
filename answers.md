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

Yes. 

Choose $c=1$ and $n_0=16$. First check at $n=16$ (any logarithm base is fine up to a constant):

$$ 16^{1.01} > 16 = (\log_2 16)^2. $$

Now define $f(n)=\dfrac{n^{1.01}}{(\log n)^2}$ with natural logarithm in the denominator (bases differ by constants only). Then

$$ \frac{d}{dn}\big(\ln f(n)\big)=\frac{1.01}{n}-\frac{2}{n\ln n}=\frac{1}{n}\left(1.01-\frac{2}{\ln n}\right). $$

Hence $f^'(n)\ge 0$ whenever $\ln n \ge \dfrac{2}{1.01}$, i.e. for all $n\ge 8$. Therefore $f(n)$ is increasing on $[8,\infty)$, so for all $n\ge16$,

$$ \frac{n^{1.01}}{(\log n)^2}\ \ge\ \frac{16^{1.01}}{(\log 16)^2}\ >\ 1. $$

Thus, for all $n\ge16$,

$$ n^{1.01} \ge 1\cdot(\log n)^2, $$

which (with $c=1,\ n_0=16$) proves

$$ n^{1.01} \in \Omega \big((\log n)^2\big). $$

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
