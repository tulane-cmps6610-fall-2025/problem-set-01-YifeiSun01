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

Hence $f^{'} (n)\ge 0$ whenever $\ln n \ge \dfrac{2}{1.01}$, i.e. for all $n\ge 8$. Therefore $f(n)$ is increasing on $[8,\infty)$, so for all $n\ge16$,

$$ \frac{n^{1.01}}{(\log n)^2}\ \ge\ \frac{16^{1.01}}{(\log 16)^2}\ >\ 1. $$

Thus, for all $n\ge16$,

$$ n^{1.01} \ge 1\cdot(\log n)^2, $$

which (with $c=1,\ n_0=16$) proves

$$ n^{1.01} \in \Omega \big((\log n)^2\big). $$

  - 1e

No. 

Suppose there exist $c>0$ and $n_0$ such that for all $n\ge n_0$,

$$ \sqrt{n} \le c (\log n)^3. $$

Taking logs gives

$$ \tfrac12 \log n \le \log c + 3\log\log n, $$

which cannot hold for large $n$ since $\log n / \log\log n \to \infty$. Hence $\sqrt{n}\notin O((\log n)^3)$.

  - 1f

Yes. 
Let $f(n)=\dfrac{\sqrt{n}}{(\log n)^3}$ (natural log). For $n\ge e^6$,

$$ \frac{d}{dn}\ln f(n)=\frac{1}{2n}-\frac{3}{n\ln n}\ge 0, $$

so $f$ is increasing on $[e^6,\infty)$. Hence with $n_0=\lceil e^6\rceil=404$,

$$ f(n)\ge f(n_0)=\frac{\sqrt{e^6}}{6^3}=\frac{e^3}{216}\approx 0.0929. $$

Therefore, choosing $c=0.09$ and $n_0=404$,

$$ \sqrt{n} \ge c (\log n)^3 \quad\text{for all } n\ge n_0, $$

which proves $\sqrt{n}\in\Omega((\log n)^3)$.

  - 1g

Suppose $f \in o(g)$ and $f \in \omega(g)$.  
From $f \in o(g)$, for every $c>0$ there is $N_1$ s.t. for all $n\ge N_1$,

$$ |f(n)| \le c |g(n)|. $$

Taking $c=1$ gives some $N_1$ with

$$ |f(n)| \le |g(n)| \quad (n\ge N_1). $$

From $f \in \omega(g)$, for every $c>0$ there is $N_2$ s.t. for all $n\ge N_2$,

$$ |f(n)| \ge c |g(n)|. $$

Taking $c=2$ gives some $N_2$ with

$$ |f(n)| \ge 2 |g(n)| \quad (n\ge N_2). $$

Let $N=\max\{N_1,N_2\}$. Then for all $n\ge N$,

$$ |f(n)| \le |g(n)| \quad\text{and}\quad |f(n)| \ge 2 |g(n)|, $$

a contradiction. Hence $o(g(n)) \cap \omega(g(n)) = \varnothing$. $\square$


2. **SPARC to Python**

  - 2b

If there is no typo, the foo just gives the larger value out of a and b.

If the y in the function foo returned is actually x, the foo gives the gcd of a and bm using Euclid's algorithm.

  - 2c



Work/Span of `foo` (Euclid’s GCD; unit-cost arithmetic)

$$ W(n) = T_1 = \Theta(\log n) $$

$$ S(n) = T_\infty = \Theta(\log n) $$

$$n=max(a,b)$$

If here we mean the literal pseudocode which is finding the larger value out of a and b

$$ W(n) = T_1 = \Theta(n) $$

$$ S(n) = T_\infty = \Theta(n) $$

$$n=min(a,b)$$

Because we can construct a worst case, like the following  

Let the first step fix the larger number as

$$ y = lcm(1,2,\dots,m) - 1 $$

and set the other parameter (the current divisor/remainder) to

$$ r_0 = m. $$

Since every integer $1 \le r \le m$ divides $lcm(1,\dots,m)$, we have

$$ lcm(1,\dots,m) \equiv 0 \pmod r \;\Rightarrow\; y = lcm - 1 \equiv -1 \pmod r. $$

The congruence $a \equiv -1 \pmod r$ means the remainder of $a$ upon division by $r$ is $r-1$, i.e.

$$ a \bmod r = r - 1. $$

Therefore each step satisfies

$$ r_{k+1} = y \bmod r_k = r_k - 1 \quad (k=0,1,\dots), $$

so the remainder sequence is

$$ m,\, m-1,\, \dots,\, 1,\, 0. $$

Hence it takes exactly $m$ steps to reach $0$, i.e. the number of steps is

$$ \Theta(m). $$

If we denote the input size by $n \approx m$ (e.g., n=min(a,b)), then

$$ W(n) = \Theta(n) $$

$$ S(n) = \Theta(n) $$

because each step depends on the previous remainder; the critical path is the entire sequence, so the span is the same order as the number of steps.


3. **Parallelism and recursion**

  - 3b

work

$$ W(n) = T_1 = \Theta(n) $$

span

$$ S(n) = T_\infty = \Theta(n) $$

  - 3d

  - 3e
  
4. **GCD**
