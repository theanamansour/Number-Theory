def gcd(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(a: int, b: int):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y


def mod_inverse(a: int, m: int):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"No modular inverse exists for {a} mod {m}.")
    return x % m


def validate_moduli(moduli):
    if len(moduli) == 0:
        raise ValueError("Please provide at least one modulus.")

    for m in moduli:
        if m <= 1:
            raise ValueError("Each modulus must be greater than 1.")

    for i in range(len(moduli)):
        for j in range(i + 1, len(moduli)):
            if gcd(moduli[i], moduli[j]) != 1:
                raise ValueError("Moduli must be pairwise relatively prime.")


def crt_compute_residues(A: int, moduli: list[int]):
    validate_moduli(moduli)

    residues = []
    steps = []

    for m in moduli:
        residue = A % m
        residues.append(residue)
        steps.append(f"Compute {A} mod {m} = {residue}.")

    return {
        "mode": "A_to_residues",
        "A": A,
        "moduli": moduli,
        "residues": residues,
        "steps": steps
    }


def crt_recover_A(residues: list[int], moduli: list[int]):
    if len(residues) != len(moduli):
        raise ValueError("Residues and moduli must have the same length.")

    validate_moduli(moduli)

    M = 1
    for m in moduli:
        M *= m

    steps = [f"Compute M = " + " × ".join(str(m) for m in moduli) + f" = {M}."]
    terms = []
    total = 0

    for i in range(len(moduli)):
        ai = residues[i]
        mi = moduli[i]
        Mi = M // mi
        inverse = mod_inverse(Mi, mi)
        term = ai * Mi * inverse
        total += term

        terms.append({
            "a_i": ai,
            "m_i": mi,
            "M_i": Mi,
            "inverse": inverse,
            "term": term
        })

        steps.append(
            f"For modulus {mi}: M{i+1} = {M}/{mi} = {Mi}, "
            f"and ({Mi}^-1 mod {mi}) = {inverse}."
        )
        steps.append(
            f"Term {i+1} = {ai} × {Mi} × {inverse} = {term}."
        )

    A = total % M
    steps.append(f"Add all terms: total = {total}.")
    steps.append(f"Reduce modulo M: A = {total} mod {M} = {A}.")

    return {
        "mode": "residues_to_A",
        "residues": residues,
        "moduli": moduli,
        "M": M,
        "terms": terms,
        "A": A,
        "steps": steps
    }