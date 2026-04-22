def fast_exponentiation(a: int, b: int, n: int):
    if n <= 0:
        raise ValueError("Modulus n must be a positive integer greater than 0.")

    if b < 0:
        raise ValueError("Exponent b must be a non-negative integer.")

    original_a = a
    original_b = b
    original_n = n

    steps = []
    result = 1
    base = a % n
    exponent = b

    steps.append(f"Start with result = 1, base = {a} mod {n} = {base}, exponent = {b}.")

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % n
            steps.append(
                f"Exponent is odd, so multiply: result = (result × base) mod {n} = {result}."
            )

        base = (base * base) % n
        exponent //= 2

        if exponent > 0:
            steps.append(
                f"Square the base and halve the exponent: base = {base}, exponent = {exponent}."
            )

    steps.append(f"Final result: {original_a}^{original_b} mod {original_n} = {result}.")

    return {
        "base": original_a,
        "exponent": original_b,
        "modulus": original_n,
        "result": result,
        "steps": steps
    }