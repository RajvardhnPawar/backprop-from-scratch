# Backpropagation From Scratch

This repository documents my journey of understanding **backpropagation** from first principles before implementing automatic differentiation.

Instead of using machine learning libraries like PyTorch or TensorFlow, I manually compute gradients using **numerical differentiation** and the **chain rule**.

## Goal

Understand **why backpropagation works**, not just how to code it.

The objective is to derive every gradient manually and build intuition before writing an automatic backward pass.

---

## Computation Graph

The current example computes:

```text
m = 2
x = 5
c = 10

a = m * x
b = a + c
y = b
```

Graph representation:

```text
m ----\
       * ---> a ----\
x ----/             + ---> b (= y)
                    /
c -----------------/
```

---

## Gradients Computed

Using finite differences and the chain rule, the following gradients are calculated:

| Gradient | Value |
| -------- | ----: |
| dy/dy    |     1 |
| dy/db    |     1 |
| dy/da    |     1 |
| dy/dm    |     5 |
| dy/dx    |     2 |
| dy/dc    |     1 |

---

## Concepts Covered

* Numerical differentiation
* Finite difference approximation
* Computational graphs
* Local derivatives
* Chain rule
* Gradient propagation
* Manual backpropagation

---

## Technologies

* Python 3
* No external libraries

---

## Motivation

This project is part of my journey to deeply understand the mathematics behind neural networks instead of treating automatic differentiation as a black box.

The long-term goal is to build a complete neural network framework from scratch using only Python and mathematics.

---

## Current Status

* ✅ Computational graph
* ✅ Manual gradient calculation
* ✅ Chain rule implementation
* ⏳ Automatic backward propagation
* ⏳ Complete autograd engine
* ⏳ Neural network implementation
