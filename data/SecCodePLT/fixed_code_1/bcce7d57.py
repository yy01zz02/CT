def parse_transformation_string(
    transformation_string: str = "a,b,c;0,0,0",
) -> tuple[list[list[float]] | np.ndarray, list[float]]:
    try:
        a, b, c = sp.symbols('a b c')
        b_change, o_shift = transformation_string.split(";")
        basis_change = b_change.split(",")
        origin_shift = o_shift.split(",")

        basis_change = [
            re.sub(r"(?<=\w|\))(?=\()|(?<=\))(?=\w)|(?<=(\d|a|b|c))(?=([abc]))", r"*", string, flags=re.X)
            for string in basis_change
        ]
        P = np.array([sp.sympify(x, locals={'a': a, 'b': b, 'c': c}) for x in basis_change])

        P = P.transpose()

        p = [float(Fraction(x)) for x in origin_shift]
        return P, p
    except Exception:
        raise ValueError("Failed to parse transformation string.")