def miller_rabin(n: int, a: int):
    if n < 3 or n % 2 == 0:
        raise ValueError("Input must be an odd integer greater than or equal to 3.")

    if a <= 1 or a >= n - 1:
        raise ValueError("Base a must satisfy 1 < a < n - 1.")

    steps = []

    q = n - 1
    k = 0
    while q % 2 == 0:
        q //= 2
        k += 1

    decomposition = f"{n - 1} = 2^{k} × {q}"
    steps.append(f"Write n - 1 as 2^k × q with q odd: {decomposition}.")

    aq_mod_n = pow(a, q, n)
    steps.append(f"Compute {a}^{q} mod {n} = {aq_mod_n}.")

    if aq_mod_n == 1:
        steps.append(f"Since {a}^{q} mod {n} = 1, the test returns maybe prime.")
        return {
            "input": n,
            "base": a,
            "k": k,
            "q": q,
            "decomposition": decomposition,
            "result": "maybe prime",
            "sequence": [
                {
                    "j": 0,
                    "expression": f"{a}^{q} mod {n}",
                    "value": aq_mod_n
                }
            ],
            "steps": steps
        }

    sequence = []
    for j in range(k):
        exponent = (2 ** j) * q
        value = pow(a, exponent, n)
        sequence.append({
            "j": j,
            "expression": f"{a}^({2 ** j} × {q}) mod {n}",
            "value": value
        })
        steps.append(f"For j = {j}, compute {a}^({2 ** j} × {q}) mod {n} = {value}.")

        if value == n - 1:
            steps.append(f"Since the value equals n - 1 = {n - 1}, the test returns maybe prime.")
            return {
                "input": n,
                "base": a,
                "k": k,
                "q": q,
                "decomposition": decomposition,
                "result": "maybe prime",
                "sequence": sequence,
                "steps": steps
            }

    steps.append(f"No value in the sequence equals {n - 1}, so the test returns composite.")

    return {
        "input": n,
        "base": a,
        "k": k,
        "q": q,
        "decomposition": decomposition,
        "result": "composite",
        "sequence": sequence,
        "steps": steps
    }