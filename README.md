# 🧮 Simple Python Calculator

This is a calculator program written in Python that performs both basic arithmetic and scientific operations.

## 🚀 Features

### Basic Arithmetic Operations
- Add two numbers
- Subtract two numbers
- Multiply two numbers
- Divide two numbers (with division by zero handling)

### Scientific Operations
- Power (x^y)
- Square Root (√x)
- Sine (sin x)
- Cosine (cos x)
- Logarithm (natural log of x)

## 📦 Requirements

- Python 3.x
- Python's built-in `math` module (included in standard library)

## 🛠️ How to Run

1. Clone the repository or download the `calculator.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the calculator using:

```bash
python calculator.py
```

## 📋 Usage

1. When you run the calculator, you'll see a menu of available operations:
   ```
   Select operation:
   1. Add
   2. Subtract
   3. Multiply
   4. Divide
   5. Power
   6. Square Root
   7. Sine
   8. Cosine
   9. Logarithm
   ```

2. Enter the number corresponding to your desired operation.

3. For operations requiring two numbers (Add, Subtract, Multiply, Divide, Power):
   - Enter the first number when prompted
   - Enter the second number when prompted

4. For operations requiring one number (Square Root, Sine, Cosine, Logarithm):
   - Enter the number when prompted
   - For trigonometric functions (Sine, Cosine), input is in degrees

5. The calculator will display the result and then exit.

### Examples

#### Addition
```
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Square Root
7. Sine
8. Cosine
9. Logarithm
1
Enter first number: 5
Enter second number: 3
5.0 + 3.0 = 8.0
```

#### Square Root
```
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Square Root
7. Sine
8. Cosine
9. Logarithm
6
Enter a number: 16
Square root of 16.0 = 4.0
```

#### Sine
```
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Square Root
7. Sine
8. Cosine
9. Logarithm
7
Enter angle in degrees: 90
sin(90.0°) = 1.0
```