# First Series Examination - August 2026

> [!question] ## 1. What are the set operations? Explain with venn diagram> 

> [!summary] 
> * **Union ($A \cup B$):** All elements in $A$, $B$, or both (Shade both circles entirely).
> * **Intersection ($A \cap B$):** Elements common to both $A$ and $B$ (Shade overlapping region).
> * **Difference ($A - B$):** Elements in $A$ but not in $B$ (Shade circle $A$ excluding the overlapping area).
> * **Complement ($A'$):** Elements in universal set $U$ not in $A$ (Shade outside circle $A$).

---

**2. Given $A=\{1,2,3,4,5\}$ and $B=\{0,3,6\}$**
a. $A \cup B = \{0, 1, 2, 3, 4, 5, 6\}$

b. $A \cap B = \{3\}$

c. $A - B = \{1, 2, 4, 5\}$

d. $B - A = \{0, 6\}$

---

**3. Symbolic Propositions**
a. $p \land q$

b. $p \land \neg q$

c. $\neg p \land \neg q$

d. $q \lor p$

---

**4. Truth Tables**

**a. $p \land \neg p$**

| $p$ | $\neg p$ | $p \land \neg p$ |
| --- | --- | --- |
| T | F | F |
| F | T | F |

**b. $(p \lor \neg q) \rightarrow q$**

| $p$ | $q$ | $\neg q$ | $p \lor \neg q$ | $(p \lor \neg q) \rightarrow q$ |
| --- | --- | --- | --- | --- |
| T | T | F | T | **T** |
| T | F | T | T | **F** |
| F | T | F | F | **T** |
| F | F | T | T | **F** |

**c. $(p \lor q) \rightarrow (p \land q)$**

| $p$ | $q$ | $p \lor q$ | $p \land q$ | $(p \lor q) \rightarrow (p \land q)$ |
| --- | --- | ---------- | ----------- | ------------------------------------ |
| T   | T   | T          | T           | **T**                                |
| T   | F   | T          | F           | **F**                                |
| F   | T   | T          | F           | **F**                                |
| F   | F   | F          | F           | **T**                                |

**d. $((p \rightarrow q) \land (q \rightarrow r)) \rightarrow (p \rightarrow r)$**

| $p$ | $q$ | $r$ | $p \rightarrow q$ | $q \rightarrow r$ | $(p \rightarrow q) \land (q \rightarrow r)$ | $p \rightarrow r$ | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T | T | T | T | T | T | T | **T** |
| T | T | F | T | F | F | F | **T** |
| T | F | T | F | T | F | T | **T** |
| T | F | F | F | T | F | F | **T** |
| F | T | T | T | T | T | T | **T** |
| F | T | F | T | F | F | T | **T** |
| F | F | T | T | T | T | T | **T** |
| F | F | F | T | T | T | T | **T** |

---

**5. Well-Formed Formula (WFF)**
A Well-Formed Formula (WFF) is a syntactically correct expression in propositional logic, constructed according to the logical language.
* **Examples:** $(p \land q) \rightarrow r$, $\neg(p \lor q)$

---

**PART - B (6 Marks Each)**

**6. DNF of $\neg(p \lor q) \leftrightarrow (p \land q)$**

Constructing the truth table to find minterms where result is True:

| $p$ | $q$ | $p \lor q$ | $\neg(p \lor q)$ | $p \land q$ | $\neg(p \lor q) \leftrightarrow (p \land q)$ | Minterm |
| --- | --- | --- | --- | --- | --- | --- |
| T | T | T | F | T | F | - |
| T | F | T | F | F | **T** | $p \land \neg q$ |
| F | T | T | F | F | **T** | $\neg p \land q$ |
| F | F | F | T | F | F | - |

**Disjunctive Normal Form (DNF):**

$$(p \land \neg q) \lor (\neg p \land q)$$

---

**7. Modus Ponens and Modus Tollens**

* **Modus Ponens (MP):** Rule stating if $p \rightarrow q$ is true and $p$ is true, then $q$ must be true. Formula: $[(p \rightarrow q) \land p] \rightarrow q$.
* **Modus Tollens (MT):** Rule stating if $p \rightarrow q$ is true and $q$ is false ($\neg q$), then $p$ must be false ($\neg p$). Formula: $[(p \rightarrow q) \land \neg q] \rightarrow \neg p$.

**Validity Check (Truth Table):**

| $p$ | $q$ | $p \rightarrow q$ | $(p \rightarrow q) \land p$ | **MP:** $[(p \rightarrow q) \land p] \rightarrow q$ | $\neg q$ | $(p \rightarrow q) \land \neg q$ | $\neg p$ | **MT:** $[(p \rightarrow q) \land \neg q] \rightarrow \neg p$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T | T | T | T | **T** | F | F | F | **T** |
| T | F | F | F | **T** | T | F | F | **T** |
| F | T | T | F | **T** | F | F | T | **T** |
| F | F | T | F | **T** | T | T | T | **T** |

Since the final columns for both MP and MT contain only **T** (tautologies), both inference rules are **valid**.

---

**8. Proof by Contradiction: "If $n^2$ is an even integer, then $n$ is also even"**

* **Assumption:** Assume the premise is true ($n^2$ is even) and the conclusion is false ($n$ is odd).
* Since $n$ is odd, it can be written as $n = 2k + 1$ for some integer $k$.
* Squaring both sides:

$$n^2 = (2k + 1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$$


* Let $m = 2k^2 + 2k$ (an integer). Then $n^2 = 2m + 1$, which means $n^2$ is odd.
* **Contradiction:** This contradicts our initial premise that $n^2$ is even.
* **Conclusion:** Therefore, $n$ must be an even integer.

---

**9. Proof by Mathematical Induction: $1 + 2 + 3 + \dots + n = \frac{n(n+1)}{2}$**

* **Base Step ($n = 1$):**

$$\text{LHS} = 1$$


$$\text{RHS} = \frac{1(1 + 1)}{2} = \frac{2}{2} = 1$$



LHS = RHS. Statement holds true for $n = 1$.
* **Inductive Hypothesis:** Assume statement is true for $n = k$:

$$1 + 2 + 3 + \dots + k = \frac{k(k + 1)}{2}$$


* **Inductive Step ($n = k + 1$):** Add $(k + 1)$ to both sides:

$$1 + 2 + 3 + \dots + k + (k + 1) = \frac{k(k + 1)}{2} + (k + 1)$$


$$= (k + 1) \left( \frac{k}{2} + 1 \right) = (k + 1) \left( \frac{k + 2}{2} \right) = \frac{(k + 1)((k + 1) + 1)}{2}$$



The statement holds for $n = k + 1$. By mathematical induction, the formula is true for all $n \ge 1$.
