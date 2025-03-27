import numpy as np
import cmath


# Function to solve a quadratic equation (Ax^2 + Bx + C = 0)
def solve_quadratic(A, B, C):
    discriminant = B ** 2 - 4 * A * C
    if discriminant > 0:
        root1 = (-B + cmath.sqrt(discriminant)) / (2 * A)
        root2 = (-B - cmath.sqrt(discriminant)) / (2 * A)
        return root1, root2
    elif discriminant == 0:
        root = -B / (2 * A)
        return root,
    else:
        root1 = (-B + cmath.sqrt(discriminant)) / (2 * A)
        root2 = (-B - cmath.sqrt(discriminant)) / (2 * A)
        return root1, root2


# Function to solve a cubic equation (Ax^3 + Bx^2 + Cx + D = 0)
def solve_cubic(A, B, C, D):
    coefficients = [A, B, C, D]
    roots = np.roots(coefficients)
    return roots


# Function to solve a quartic equation (Ax^4 + Bx^3 + Cx^2 + Dx + E = 0)
def solve_quartic(A, B, C, D, E):
    coefficients = [A, B, C, D, E]
    roots = np.roots(coefficients)
    return roots


# Main program logic
def main():
    print("Welcome to the Equation Solver!")

    # Ask the user which type of equation they want to solve
    equation_type = input("Which equation do you want to solve? (quadratic, cubic, quartic): ").strip().lower()

    if equation_type == "quadratic":
        A = float(input("Enter coefficient A (for Ax^2 + Bx + C = 0): "))
        B = float(input("Enter coefficient B: "))
        C = float(input("Enter coefficient C: "))
        roots = solve_quadratic(A, B, C)
        print(f"The roots of the quadratic equation are: {roots}")

    elif equation_type == "cubic":
        A = float(input("Enter coefficient A (for Ax^3 + Bx^2 + Cx + D = 0): "))
        B = float(input("Enter coefficient B: "))
        C = float(input("Enter coefficient C: "))
        D = float(input("Enter coefficient D: "))
        roots = solve_cubic(A, B, C, D)
        print(f"The roots of the cubic equation are: {roots}")

    elif equation_type == "quartic":
        A = float(input("Enter coefficient A (for Ax^4 + Bx^3 + Cx^2 + Dx + E = 0): "))
        B = float(input("Enter coefficient B: "))
        C = float(input("Enter coefficient C: "))
        D = float(input("Enter coefficient D: "))
        E = float(input("Enter coefficient E: "))
        roots = solve_quartic(A, B, C, D, E)
        print(f"The roots of the quartic equation are: {roots}")

    else:
        print("Invalid equation type. Please choose either 'quadratic', 'cubic', or 'quartic'.")


if __name__ == "__main__":
    main()
