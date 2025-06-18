# Algebra-Based Computation of Mobilized SIR Model Simulation

---

## 🧠 What is the SIR Model?

**S** = Susceptible People  
**I** = Infected People  
**R** = Recovered People

---

## 📈 Conceptual Understanding Over Time

### 🔹 Beginning:
- S: Decreasing, accelerating
- I: Increasing, accelerating
- R: Increasing (second derivative positive, linear rate)

### 🔹 Middle:
- S: Decreasing, slowing down
- I: Increasing, slowing down
- R: Increasing, accelerating

### 🔹 End:
- S′′ = 0  
- I′′ = 0  
- R′′ = 0

---

## 🧮 Formulas

- **β** = Infection Rate (%)
- **γ** = Recovery Rate (%)
- **N** = Total People = S + I + R

---

## 🧪 Simulation Equations

```python
new_recoveries = γ * I
new_infected = β * S * (I / N)

# Update equations:
S2 = S1 - new_infected
I2 = I1 + new_infected - new_recoveries
R2 = R1 + new_recoveries
```

---

## 🚚 Application of Matrices: Mobilization

We simulate population movement using a transition matrix:

### Matrix Setup

Matrix A is calculated as:

```
[245] * [
 [0.95, 0.025, 0.025],
 [0.025, 0.95, 0.025],
 [0.025, 0.025, 0.95]
] = A
```

### Sample Calculations:

```
A1 = (299 * 0.95) + (400 * 0.025) + (500 * 0.025)
A2 = (299 * 0.025) + (400 * 0.95) + (500 * 0.025)
A3 = (299 * 0.025) + (400 * 0.025) + (500 * 0.95)

A = [30, 39, 49]
```

---

## 🧑‍💻 Python Implementation

```python
# Perform mobilization using matrix multiplication:
susceptible_people = mobility_matrix @ susceptible_people
infected_people = mobility_matrix @ infected_people
recovered_people = mobility_matrix @ recovered_people
```

---

## 📝 Notes

- This simulation uses algebra-based update rules rather than solving differential equations.
- I wil be updating it in the future to be solving by differential equations

---
