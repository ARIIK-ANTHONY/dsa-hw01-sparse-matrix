import os

class SparseMatrix:
    """
    SparseMatrix represents a sparse matrix using a dictionary keyed by (row, col).
    Provides efficient storage and operations for large sparse matrices.
    """
    def __init__(self, matrixFilePath=None, numRows=None, numCols=None):
        self.values = {}
        if matrixFilePath:
            self._load_from_file(matrixFilePath)
        elif numRows is not None and numCols is not None:
            self.numRows = numRows
            self.numCols = numCols
        else:
            raise ValueError("Either file path or number of rows and columns must be provided.")

    def _load_from_file(self, file_path):
        """
        Reads the sparse matrix from a file.
        Validates input format strictly as per assignment instructions.
        Raises ValueError if format is wrong.
        """
        try:
            with open(file_path, 'r') as f:
                lines = [line.strip() for line in f if line.strip() != '']  # ignore empty lines
            if len(lines) < 2:
                raise ValueError("Input file has insufficient lines.")

            # Parse rows and columns
            if not lines[0].startswith("rows=") or not lines[1].startswith("cols="):
                raise ValueError("Input file has wrong format: missing rows= or cols= lines")
            self.numRows = int(lines[0].split('=')[1])
            self.numCols = int(lines[1].split('=')[1])

            # Parse matrix entries
            self.values = {}
            for line in lines[2:]:
                # Must start with '(' and end with ')'
                if not (line.startswith('(') and line.endswith(')')):
                    raise ValueError(f"Input file has wrong format: invalid parentheses in line: {line}")

                content = line[1:-1]  # remove parentheses
                parts = content.split(',')
                if len(parts) != 3:
                    raise ValueError(f"Input file has wrong format: expected 3 values in line: {line}")

                row_str, col_str, val_str = [p.strip() for p in parts]

                # Validate row and col as integers
                if not (row_str.isdigit() and col_str.isdigit()):
                    raise ValueError(f"Input file has wrong format: row and column must be integers in line: {line}")

                row = int(row_str)
                col = int(col_str)

                # Validate indices in bounds
                if not (0 <= row < self.numRows) or not (0 <= col < self.numCols):
                    raise ValueError(f"Input file has wrong format: index out of bounds in line: {line}")

                # Validate val as integer (no floats allowed)
                if val_str.startswith('-'):
                    val_int_part = val_str[1:]
                    if not val_int_part.isdigit():
                        raise ValueError(f"Input file has wrong format: value must be integer in line: {line}")
                else:
                    if not val_str.isdigit():
                        raise ValueError(f"Input file has wrong format: value must be integer in line: {line}")

                value = int(val_str)

                # Store non-zero values
                if value != 0:
                    self.values[(row, col)] = value
        except Exception as e:
            # Reraise as ValueError with specific message
            raise ValueError(f"Input file has wrong format: {e}")

    def getElement(self, row, col):
        """Return the element at (row, col), or zero if not set."""
        if row < 0 or row >= self.numRows or col < 0 or col >= self.numCols:
            raise IndexError(f"Index ({row},{col}) out of bounds.")
        return self.values.get((row, col), 0)

    def setElement(self, row, col, value):
        """Set the element at (row, col). Removes key if value is zero."""
        if row < 0 or row >= self.numRows or col < 0 or col >= self.numCols:
            raise IndexError(f"Index ({row},{col}) out of bounds.")
        if value == 0:
            self.values.pop((row, col), None)
        else:
            self.values[(row, col)] = value

    def add(self, other):
        """Return a new SparseMatrix that is the sum of self and other."""
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions must match for addition.")
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        # Add all non-zero from self
        for key, val in self.values.items():
            result.values[key] = val
        # Add all non-zero from other
        for key, val in other.values.items():
            result.values[key] = result.values.get(key, 0) + val
            if result.values[key] == 0:
                del result.values[key]
        return result

    def subtract(self, other):
        """Return a new SparseMatrix that is self minus other."""
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions must match for subtraction.")
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        # Add all non-zero from self
        for key, val in self.values.items():
            result.values[key] = val
        # Subtract all non-zero from other
        for key, val in other.values.items():
            result.values[key] = result.values.get(key, 0) - val
            if result.values[key] == 0:
                del result.values[key]
        return result

    def multiply(self, other):
        """Return a new SparseMatrix that is the product of self and other."""
        if self.numCols != other.numRows:
            raise ValueError("Number of columns of first matrix must equal number of rows of second for multiplication.")
        result = SparseMatrix(numRows=self.numRows, numCols=other.numCols)

        # For each non-zero in self, multiply by corresponding row in other
        for (row_a, col_a), val_a in self.values.items():
            # For each col_b in other for row col_a
            for col_b in range(other.numCols):
                val_b = other.getElement(col_a, col_b)
                if val_b != 0:
                    current_val = result.getElement(row_a, col_b)
                    new_val = current_val + val_a * val_b
                    result.setElement(row_a, col_b, new_val)
        return result

    def transpose(self):
        """Return a new SparseMatrix that is the transpose of self."""
        result = SparseMatrix(numRows=self.numCols, numCols=self.numRows)
        for (r, c), v in self.values.items():
            result.values[(c, r)] = v
        return result

    def save_to_file(self, file_path):
        """Save the sparse matrix to a file in the specified format."""
        with open(file_path, 'w') as f:
            f.write(f"rows={self.numRows}\n")
            f.write(f"cols={self.numCols}\n")
            for (row, col), val in sorted(self.values.items()):
                f.write(f"({row}, {col}, {val})\n")

def select_operation():
    """Display a menu and get user's choice of operation."""
    print("Select matrix operation to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    while True:
        choice = input("Enter choice (1/2/3): ").strip()
        if choice in {'1', '2', '3'}:
            return choice
        print("Invalid choice. Please enter 1, 2, or 3.")

def main():
    try:
        op = select_operation()
        # Get input file paths
        file1 = input("Enter path for first matrix file: ").strip()
        file2 = input("Enter path for second matrix file: ").strip()

        m1 = SparseMatrix(matrixFilePath=file1)
        m2 = SparseMatrix(matrixFilePath=file2)

        if op == '3':
            can_multiply = m1.numCols == m2.numRows
            can_multiply_transpose = m1.numCols == m2.numCols

            if can_multiply and can_multiply_transpose:
                print("Choose multiplication option:")
                print("1. Multiply with second matrix")
                print("2. Multiply with transpose of second matrix")
                choice = input("Enter choice (1/2): ").strip()
                if choice == '2':
                    m2 = m2.transpose()
                    op_name = 'multiplication_with_transpose'
                else:
                    op_name = 'multiplication'
                result = m1.multiply(m2)

            elif can_multiply:
                print("Multiplying with second matrix (transpose not possible due to incompatible dimensions).")
                result = m1.multiply(m2)
                op_name = 'multiplication'

            elif can_multiply_transpose:
                print("Multiplying with transpose of second matrix (original matrix dimensions incompatible).")
                m2 = m2.transpose()
                result = m1.multiply(m2)
                op_name = 'multiplication_with_transpose'

            else:
                raise ValueError("Cannot perform multiplication. Dimensions do not align with second matrix or its transpose.")

        elif op == '1':
            result = m1.add(m2)
            op_name = 'addition'
        else:
            result = m1.subtract(m2)
            op_name = 'subtraction'

        # Ensure output directory exists
        output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../output')
        os.makedirs(output_dir, exist_ok=True)

        output_file = os.path.join(output_dir, f'result_{op_name}.txt')
        result.save_to_file(output_file)
        print(f"Operation {op_name} completed successfully.")
        print(f"Result saved to: {output_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
