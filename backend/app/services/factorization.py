def prime_factorization(n: int):
    if n <= 0:
        raise ValueError("Input must be a positive integer greater than 0.")

    if n == 1:
        return {
            "input": 1,
            "factors": [],
            "formatted": "1",
            "steps": ["1 has no prime factors."]
        }

    original_n = n
    factors = []
    steps = []

    count = 0
    while n % 2 == 0:
        count += 1
        steps.append(f"{n} is divisible by 2, so divide by 2.")
        n //= 2

    if count > 0:
        factors.append({"prime": 2, "power": count})

    divisor = 3
    while divisor * divisor <= n:
        count = 0
        while n % divisor == 0:
            count += 1
            steps.append(f"{n} is divisible by {divisor}, so divide by {divisor}.")
            n //= divisor
        if count > 0:
            factors.append({"prime": divisor, "power": count})
        divisor += 2

    if n > 1:
        steps.append(f"{n} is prime, so it is the final factor.")
        factors.append({"prime": n, "power": 1})

    formatted_parts = []
    for factor in factors:
        if factor["power"] == 1:
            formatted_parts.append(str(factor["prime"]))
        else:
            formatted_parts.append(f'{factor["prime"]}^{factor["power"]}')

    formatted = " × ".join(formatted_parts)

    return {
        "input": original_n,
        "factors": factors,
        "formatted": formatted,
        "steps": steps
    }