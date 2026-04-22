from app.services.factorization import prime_factorization

def euler_totient(n: int):
    if n <= 0:
        raise ValueError("Input must be a positive integer greater than 0.")

    if n == 1:
        return {
            "input": 1,
            "phi": 1,
            "formula": "φ(1) = 1",
            "steps": ["By definition, φ(1) = 1."]
        }

    factorization_result = prime_factorization(n)
    factors = factorization_result["factors"]

    phi_value = n
    steps = [f"Start with φ({n}) = {n}."]

    formula_parts = [str(n)]

    for factor in factors:
        p = factor["prime"]
        phi_value = phi_value * (p - 1) // p
        formula_parts.append(f"(1 - 1/{p})")
        steps.append(
            f"Since {p} is a distinct prime factor of {n}, multiply by (1 - 1/{p})."
        )

    formula = f"φ({n}) = " + " × ".join(formula_parts) + f" = {phi_value}"
    steps.append(f"Final result: φ({n}) = {phi_value}.")

    return {
        "input": n,
        "phi": phi_value,
        "formula": formula,
        "factors": factors,
        "steps": steps
    }