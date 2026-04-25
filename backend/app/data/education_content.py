EDUCATION_TOPICS = {
    "factorization": {
        "id": "factorization",
        "title": "Prime Factorization",
        "description": "Learn how to break a number into prime factors.",
        "lesson": {
            "summary": "Prime factorization expresses a number as a product of prime numbers.",
            "example": "84 = 2^2 × 3 × 7",
            "steps": [
                "Start with the smallest prime number, 2.",
                "Divide repeatedly while possible.",
                "Move to the next prime number.",
                "Continue until the remaining value is 1."
            ]
        },
        "practice": [
            {
                "id": "factorization_p1",
                "question": "Find the prime factorization of 60.",
                "hint": "Start by dividing by 2.",
                "accepted_answers": ["2^2 * 3 * 5", "2^2×3×5", "2*2*3*5"],
                "solution": "60 = 2 × 30 = 2 × 2 × 15 = 2^2 × 3 × 5",
                "steps": [
                    "60 is even, so divide by 2.",
                    "30 is even, so divide by 2 again.",
                    "15 = 3 × 5.",
                    "Therefore, 60 = 2^2 × 3 × 5."
                ]
            }
        ],
        "quiz": [
            {
                "id": "factorization_q1",
                "question": "Which is the correct prime factorization of 84?",
                "options": [
                    {"id": "a", "text": "2 × 3 × 14"},
                    {"id": "b", "text": "2^2 × 3 × 7"},
                    {"id": "c", "text": "4 × 21"},
                    {"id": "d", "text": "6 × 14"}
                ],
                "correct_option_id": "b",
                "explanation": "84 = 2 × 42 = 2 × 2 × 21 = 2^2 × 3 × 7."
            }
        ]
    },

    "totient": {
        "id": "totient",
        "title": "Euler's Totient Function",
        "description": "Learn how to count integers that are relatively prime to n.",
        "lesson": {
            "summary": "Euler's totient function φ(n) counts how many positive integers less than or equal to n are coprime with n.",
            "example": "φ(9) = 6 because 1, 2, 4, 5, 7, and 8 are coprime with 9.",
            "steps": [
                "Factorize n.",
                "Use the formula φ(n) = n × Π(1 - 1/p).",
                "Apply the formula using distinct prime factors."
            ]
        },
        "practice": [
            {
                "id": "totient_p1",
                "question": "Compute φ(12).",
                "hint": "The numbers coprime to 12 are 1, 5, 7, and 11.",
                "accepted_answers": ["4"],
                "solution": "φ(12) = 4",
                "steps": [
                    "12 = 2^2 × 3.",
                    "φ(12) = 12 × (1 - 1/2) × (1 - 1/3).",
                    "φ(12) = 12 × 1/2 × 2/3 = 4."
                ]
            }
        ],
        "quiz": [
            {
                "id": "totient_q1",
                "question": "What is φ(10)?",
                "options": [
                    {"id": "a", "text": "2"},
                    {"id": "b", "text": "4"},
                    {"id": "c", "text": "5"},
                    {"id": "d", "text": "10"}
                ],
                "correct_option_id": "b",
                "explanation": "The numbers coprime to 10 are 1, 3, 7, and 9, so φ(10) = 4."
            }
        ]
    },

    "fastexp": {
        "id": "fastexp",
        "title": "Fast Modular Exponentiation",
        "description": "Learn how to compute large powers modulo n efficiently.",
        "lesson": {
            "summary": "Fast modular exponentiation computes a^b mod n efficiently using repeated squaring.",
            "example": "2^13 mod 7 = 2",
            "steps": [
                "Write the exponent in binary or repeatedly square.",
                "Reduce each intermediate result modulo n.",
                "Multiply only the needed powers.",
                "Take the final result modulo n."
            ]
        },
        "practice": [
            {
                "id": "fastexp_p1",
                "question": "Compute 2^5 mod 7.",
                "hint": "2^5 = 32, and 32 mod 7 = ?",
                "accepted_answers": ["4"],
                "solution": "2^5 mod 7 = 32 mod 7 = 4",
                "steps": [
                    "Compute 2^5 = 32.",
                    "Divide 32 by 7.",
                    "32 = 7 × 4 + 4.",
                    "So 2^5 mod 7 = 4."
                ]
            }
        ],
        "quiz": [
            {
                "id": "fastexp_q1",
                "question": "What is 3^4 mod 5?",
                "options": [
                    {"id": "a", "text": "1"},
                    {"id": "b", "text": "2"},
                    {"id": "c", "text": "3"},
                    {"id": "d", "text": "4"}
                ],
                "correct_option_id": "a",
                "explanation": "3^4 = 81 and 81 mod 5 = 1."
            }
        ]
    },

    "millerrabin": {
        "id": "millerrabin",
        "title": "Miller-Rabin Primality Test",
        "description": "Learn how probabilistic primality testing works.",
        "lesson": {
            "summary": "Miller-Rabin tests whether a number is composite or probably prime using modular arithmetic.",
            "example": "If a witness proves n is composite, then n is definitely not prime.",
            "steps": [
                "Write n - 1 as 2^s × d where d is odd.",
                "Choose a base a.",
                "Compute a^d mod n.",
                "Square repeatedly and check conditions.",
                "Decide whether n is composite or probably prime."
            ]
        },
        "practice": [
            {
                "id": "millerrabin_p1",
                "question": "For Miller-Rabin, what does a witness prove?",
                "hint": "Think about whether it proves primality or compositeness.",
                "accepted_answers": ["composite", "that the number is composite", "n is composite"],
                "solution": "A witness proves that n is composite.",
                "steps": [
                    "Miller-Rabin can prove a number is composite.",
                    "If no witness is found, the number is probably prime.",
                    "It does not always prove primality with one base."
                ]
            }
        ],
        "quiz": [
            {
                "id": "millerrabin_q1",
                "question": "If Miller-Rabin finds a witness, what can we conclude?",
                "options": [
                    {"id": "a", "text": "The number is definitely prime."},
                    {"id": "b", "text": "The number is definitely composite."},
                    {"id": "c", "text": "The number is even."},
                    {"id": "d", "text": "The test failed."}
                ],
                "correct_option_id": "b",
                "explanation": "A Miller-Rabin witness proves that the tested number is composite."
            }
        ]
    },

    "crt": {
        "id": "crt",
        "title": "Chinese Remainder Theorem",
        "description": "Learn how to reconstruct numbers from remainders.",
        "lesson": {
            "summary": "CRT solves systems of congruences when the moduli are pairwise coprime.",
            "example": "x ≡ 2 mod 3 and x ≡ 3 mod 5 has solution x ≡ 8 mod 15.",
            "steps": [
                "Check that moduli are pairwise coprime.",
                "Multiply all moduli to get M.",
                "Build partial products.",
                "Find modular inverses.",
                "Combine all terms and reduce modulo M."
            ]
        },
        "practice": [
            {
                "id": "crt_p1",
                "question": "Find x where x ≡ 2 mod 3 and x ≡ 3 mod 5.",
                "hint": "Try numbers that are 2 mod 3: 2, 5, 8, 11...",
                "accepted_answers": ["8", "x = 8", "8 mod 15", "x ≡ 8 mod 15"],
                "solution": "x ≡ 8 mod 15",
                "steps": [
                    "Numbers congruent to 2 mod 3 are 2, 5, 8, 11, 14...",
                    "Check which one is congruent to 3 mod 5.",
                    "8 mod 5 = 3.",
                    "So x ≡ 8 mod 15."
                ]
            }
        ],
        "quiz": [
            {
                "id": "crt_q1",
                "question": "CRT usually requires the moduli to be:",
                "options": [
                    {"id": "a", "text": "All even"},
                    {"id": "b", "text": "Pairwise coprime"},
                    {"id": "c", "text": "Prime only"},
                    {"id": "d", "text": "Equal"}
                ],
                "correct_option_id": "b",
                "explanation": "The standard CRT requires moduli to be pairwise coprime."
            }
        ]
    }
}