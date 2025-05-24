# 🧮 Sparse Matrix Operations – DSA Homework 01

This project is part of my coursework for **Data Structures and Algorithms (DSA) Homework 01**. It focuses on implementing a custom **sparse matrix** data structure in Python and performing the following operations:

- ✅ Matrix Addition  
- ✅ Matrix Subtraction  
- ✅ Matrix Multiplication  

Sparse matrices are efficient for storing large matrices that contain mostly zeroes. By storing only non-zero elements, we reduce memory usage and improve performance—especially with large datasets.

---

## 📁 Project Structure

The project is organized as follows:

```

dsa-hw01-sparse-matrix/
├── README.md                    # Project documentation
├── code/
│   └── src/
│       └── sparse\_matrix.py     # Main program with all logic
├── output/                      # Result files generated after operations
│   ├── add\_result.txt
│   ├── multiply\_result.txt
│   ├── result\_addition.txt
│   └── result\_subtraction.txt
└── sample\_inputs/               # Sample input matrix file
├── matrix1.txt
└── matrix2.txt

````

---

## 🚀 How to Run the Program

Follow these steps to run the program on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/ARIIK-ANTHONY/dsa-hw01-sparse-matrix.git
cd dsa-hw01-sparse-matrix
````

### 2. Navigate to the Source Code

```bash
cd code/src/
```

### 3. Run the Python Script

Make sure you have Python installed, then run:

```bash
python3 sparse_matrix.py
```

### 4. Follow the Prompts

You’ll be asked to choose the operation and provide paths to the input files:

```
Sparse Matrix Operations
1. Addition
2. Subtraction
3. Multiplication
Select operation (1/2/3): 1

Enter path to the first matrix file: ../../sample_inputs/matrix1.txt
Enter path to the second matrix file: ../../sample_inputs/matrix2.txt
```

After the operation is completed, the result will be saved in the `output/` folder.

---

## 📥 Input File Format

Each input matrix must follow this format:

```
rows=3
cols=3
0 0 5
0 2 8
1 1 4
```

* The first two lines specify the dimensions of the matrix.
* Each subsequent line represents a non-zero element in the form:
  `row_index column_index value`

This format ensures efficient storage of sparse matrices.

---

## 📤 Output

The output is saved to a `.txt` file in the `output/` directory. It follows the **same format** as the input file, so it can be reused for additional operations or verification.

Example:

```
rows=3
cols=3
0 0 10
1 1 5
```

---

## 🎯 Features

* Sparse matrix representation using Python dictionaries
* Clean command-line interface with input prompts
* Simple and modular Python code
* Custom input/output file support
* Efficient computation for sparse data


## ✅ Sample Run (Addition)

```
Select operation (1/2/3): 1
Enter path to the first matrix file: ../../sample_inputs/matrix1.txt
Enter path to the second matrix file: ../../sample_inputs/matrix2.txt
```

📂 Output saved at: `output/result_addition.txt`
