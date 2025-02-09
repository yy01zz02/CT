"""
write a function to extract the 3x3 linear transformation matrix from the linear expressions containing `a, b, c` as basis and separated by semicolons. For example, "a;b;c" to a np.eye(3), "3a+4b;2a+3b;4c" to [[3, 2, 0], [4, 3, 0], [0, 0, 4]]
"""

def parse_transformation_string(
    transformation_string: str = "a,b,c;0,0,0",
) -> tuple[list[list[float]] | np.ndarray, list[float]]:
    """
    Parse a transformation string to obtain the transformation matrix and vector.

    Args:
        transformation_string (str, optional): Transformation string in the format "a,b,c;0,0,0".
            Defaults to "a,b,c;0,0,0".

    Raises:
        ValueError: If the transformation string fails to parse.

    Returns:
        tuple[list[list[float]] | np.ndarray, list[float]]: The transformation matrix & vector.
    """
    try:
        a, b, c = sp.symbols('a b c')
        b_change, o_shift = transformation_string.split(";")
        basis_change = b_change.split(",")
        origin_shift = o_shift.split(",")

        # Add implicit multiplication operators using regular expressions
        basis_change = [
            re.sub(r"(?<=\w|\))(?=\() | (?<=\))(?=\w) | (?<=(\d|a|b|c))(?=([abc]))", r"*", string, flags=re.X)
            for string in basis_change
        ]
        P = np.array([eval(x, {"__builtins__": None}, {"a": a, "b": b, "c": c}) for x in basis_change])

        P = P.transpose()  # by convention

        p = [float(Fraction(x)) for x in origin_shift]
        return P, p
    except Exception:
        raise ValueError("Failed to parse transformation string.")