# Sparse Matrix Operations – DSA Homework 01
Python project, reflecting my folder structure, usage steps, and operations:
This project implements a custom sparse matrix data structure and performs key matrix operations—**Addition**, **Subtraction**, and **Multiplication**—on sparse matrices efficiently. Designed as part of **DSA Homework 01**, it demonstrates how to represent and manipulate large matrices with minimal memory overhead using a dictionary-based sparse representation.

---

## 📁 Project Structure

```
dsa/
└── sparse_matrix/
    └── code/
        └── src/
            ├── main.py
            ├── matrix.py
            ├── utils.py
            └── ... (other supporting files)
    └── sample_inputs/
        ├── small_matrix_1.txt
        ├── small_matrix_2.txt
        └── multiply_result.txt
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone the repo
cd sparse-matrix-dsa-assignment
```

### 2. Navigate to the Source Directory

```bash
cd dsa/sparse_matrix/code/src/
```

### 3. Run the Program

Execute the program using Python:


### 4. Provide Input and Select Operation

When prompted, select the matrix operation you'd like to perform:

```
Select operation:
1. Addition
2. Subtraction
3. Multiplication
Enter your choice (1/2/3): 3
```

Then provide paths to your input matrix files (use relative paths as shown below):

```
Enter path to the first input file: ../../sample_inputs/small_matrix_1.txt
Enter path to the second input file: ../../sample_inputs/small_matrix_2.txt
Enter path to the result output file: ../../sample_inputs/multiply_result.txt
```

---

## 📌 Features

* Sparse matrix representation using dictionaries for memory efficiency.
* Clean command-line interaction and input validation.
* Modular code structure for readability and future extension.

---

## 📚 Sample Input Format

Each input matrix file should be in the following format:

rows=5
cols=5
0 0 1
0 2 3
1 1 5
2 3 7
4 4 9

Each line represents a non-zero entry in the sparse matrix.

---

## 🧑‍💻 Author

**Anthony Ariik Mathiang Ariik**
DSA Homework 01 – Sparse Matrix Operations
