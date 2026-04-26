EDUCATION_TOPICS = {
    "factorization": {
        "id": "factorization",
        "title": "Prime Factorization",
        "description": "Learn how to break a number into prime factors and use factorization to understand GCD.",

        "lessons": [
            {
                "id": "factorization_l1",
                "title": "What Is a Prime Number?",
                "summary": (
                    "A prime number is a positive integer greater than 1 whose only positive divisors are 1 and itself. "
                    "Prime numbers are central to number theory because they act like the building blocks of whole numbers. "
                    "For example, 2, 3, 5, and 7 are prime, while 4, 6, 8, 9, and 10 are not."
                ),
                "example": (
                    "7 is prime because its only divisors are 1 and 7. "
                    "9 is not prime because it can be divided by 1, 3, and 9."
                ),
                "steps": [
                    "A divisor is a number that divides another number exactly with no remainder.",
                    "A prime number must be greater than 1.",
                    "A prime number has exactly two positive divisors: 1 and itself.",
                    "For example, 13 is prime because only 1 and 13 divide it exactly.",
                    "15 is not prime because 3 and 5 also divide it exactly.",
                    "2 is the only even prime number. Every other even number is divisible by 2, so it cannot be prime."
                ]
            },
            {
                "id": "factorization_l2",
                "title": "What Is Prime Factorization?",
                "summary": (
                    "Prime factorization means writing a number as a product of prime numbers only. "
                    "For example, 84 = 2 x 42 is a factorization, but it is not a prime factorization because 42 is not prime. "
                    "We keep breaking composite factors until every factor left is prime."
                ),
                "example": "84 = 2 x 42 = 2 x 2 x 21 = 2 x 2 x 3 x 7 = 2^2 x 3 x 7",
                "steps": [
                    "Start with the number you want to factor.",
                    "Try dividing by the smallest prime number, 2.",
                    "If it divides evenly, keep 2 as a factor and continue factoring the quotient.",
                    "If it does not divide evenly, move to the next prime: 3, then 5, then 7, and so on.",
                    "Stop only when every remaining factor is prime.",
                    "Use exponents when a prime appears more than once."
                ]
            },
            {
                "id": "factorization_l3",
                "title": "Finding Prime Factors by Repeated Division",
                "summary": (
                    "Repeated division is a systematic way to find prime factorization. "
                    "We divide by prime numbers step by step, starting from the smallest prime. "
                    "Each time a prime divides the current number exactly, we record it as a factor."
                ),
                "example": "60 ÷ 2 = 30, 30 ÷ 2 = 15, 15 ÷ 3 = 5, and 5 ÷ 5 = 1, so 60 = 2^2 x 3 x 5.",
                "steps": [
                    "Begin with the smallest prime number, 2.",
                    "Divide by 2 as many times as possible.",
                    "Then try 3, then 5, then 7, and so on.",
                    "Every time the division is exact, record the prime factor.",
                    "Stop when the remaining value becomes 1.",
                    "Combine repeated factors using exponents."
                ]
            },
            {
                "id": "factorization_l4",
                "title": "Using Prime Factorization to Find GCD",
                "summary": (
                    "Prime factorization can help us find the greatest common divisor, or GCD, of two numbers. "
                    "The GCD is the largest number that divides both numbers exactly. "
                    "To find it using prime factorization, compare the prime factors and keep only the common primes with the smallest powers."
                ),
                "example": (
                    "18 = 2 x 3^2 and 300 = 2^2 x 3 x 5^2. "
                    "The common primes are 2 and 3, with smallest powers 2^1 and 3^1. "
                    "So GCD(18, 300) = 2 x 3 = 6."
                ),
                "steps": [
                    "Write the prime factorization of both numbers.",
                    "Identify the primes that appear in both factorizations.",
                    "For each common prime, choose the smaller exponent.",
                    "Multiply these chosen prime powers together.",
                    "The result is the greatest common divisor."
                ]
            }
        ],

        "lesson": {
            "id": "factorization_l1",
            "title": "What Is a Prime Number?",
            "summary": "A prime number has only divisors 1 and itself.",
            "example": "7 is prime, but 9 is not prime.",
            "steps": [
                "Check the divisors.",
                "If only 1 and the number itself divide it, it is prime."
            ]
        },

        "practice": [
            {
                "id": "factorization_easy_1",
                "level": "easy",
                "title": "Prime factorize 60",
                "question": "Find the prime factorization of 60 step by step.",
                "interaction": "guided_steps",
                "steps": [
                    {
                        "id": "s1",
                        "type": "input",
                        "prompt": "Step 1: What is the smallest prime number that divides 60?",
                        "hint": "60 is even.",
                        "accepted_answers": ["2"],
                        "correct_answer": "2",
                        "explanation": "Since 60 is even, the smallest prime factor is 2."
                    },
                    {
                        "id": "s2",
                        "type": "input",
                        "prompt": "Step 2: Compute 60 ÷ 2.",
                        "hint": "Half of 60.",
                        "accepted_answers": ["30"],
                        "correct_answer": "30",
                        "explanation": "60 ÷ 2 = 30."
                    },
                    {
                        "id": "s3",
                        "type": "input",
                        "prompt": "Step 3: What is the smallest prime number that divides 30?",
                        "hint": "30 is still even.",
                        "accepted_answers": ["2"],
                        "correct_answer": "2",
                        "explanation": "30 is even, so divide by 2 again."
                    },
                    {
                        "id": "s4",
                        "type": "input",
                        "prompt": "Step 4: Compute 30 ÷ 2.",
                        "hint": "Half of 30.",
                        "accepted_answers": ["15"],
                        "correct_answer": "15",
                        "explanation": "30 ÷ 2 = 15."
                    },
                    {
                        "id": "s5",
                        "type": "input",
                        "prompt": "Step 5: Factor 15.",
                        "hint": "15 is divisible by 3.",
                        "accepted_answers": ["3*5", "3 x 5", "3 x 5"],
                        "correct_answer": "15 = 3 x 5",
                        "explanation": "15 = 3 x 5, and both 3 and 5 are prime."
                    },
                    {
                        "id": "s6",
                        "type": "input",
                        "prompt": "Final Step: Write the prime factorization of 60.",
                        "hint": "You found 2, 2, 3, and 5.",
                        "accepted_answers": ["2^2*3*5", "2^2 x 3 x 5", "2^2 x 3 x 5", "2*2*3*5"],
                        "correct_answer": "60 = 2^2 x 3 x 5",
                        "explanation": "Combining the prime factors gives 60 = 2 x 2 x 3 x 5 = 2^2 x 3 x 5."
                    }
                ]
            },
            {
                "id": "factorization_easy_2",
                "level": "easy",
                "title": "Prime factorize 84",
                "question": "Find the prime factorization of 84 step by step.",
                "interaction": "guided_steps",
                "steps": [
                    {
                        "id": "s1",
                        "type": "input",
                        "prompt": "Step 1: What is the smallest prime number that divides 84?",
                        "hint": "84 is even.",
                        "accepted_answers": ["2"],
                        "correct_answer": "2",
                        "explanation": "Since 84 is even, divide by 2."
                    },
                    {
                        "id": "s2",
                        "type": "input",
                        "prompt": "Step 2: Compute 84 ÷ 2.",
                        "hint": "Half of 84.",
                        "accepted_answers": ["42"],
                        "correct_answer": "42",
                        "explanation": "84 ÷ 2 = 42."
                    },
                    {
                        "id": "s3",
                        "type": "input",
                        "prompt": "Step 3: What prime divides 42 next?",
                        "hint": "42 is still even.",
                        "accepted_answers": ["2"],
                        "correct_answer": "2",
                        "explanation": "42 is even, so divide by 2 again."
                    },
                    {
                        "id": "s4",
                        "type": "input",
                        "prompt": "Step 4: Compute 42 ÷ 2.",
                        "hint": "Half of 42.",
                        "accepted_answers": ["21"],
                        "correct_answer": "21",
                        "explanation": "42 ÷ 2 = 21."
                    },
                    {
                        "id": "s5",
                        "type": "input",
                        "prompt": "Step 5: Factor 21.",
                        "hint": "21 is divisible by 3.",
                        "accepted_answers": ["3*7", "3 x 7", "3 x 7"],
                        "correct_answer": "21 = 3 x 7",
                        "explanation": "21 = 3 x 7."
                    },
                    {
                        "id": "s6",
                        "type": "input",
                        "prompt": "Final Step: Write the prime factorization of 84.",
                        "hint": "You found 2, 2, 3, and 7.",
                        "accepted_answers": ["2^2*3*7", "2^2 x 3 x 7", "2^2 x 3 x 7", "2*2*3*7"],
                        "correct_answer": "84 = 2^2 x 3 x 7",
                        "explanation": "84 = 2 x 2 x 3 x 7 = 2^2 x 3 x 7."
                    }
                ]
            },
            {
                "id": "factorization_medium_1",
                "level": "medium",
                "title": "Choose the factorization path for 84",
                "question": "Prime factorize 84 by choosing the correct next steps.",
                "interaction": "choice_steps_final",
                "steps": [
                    {
                        "id": "s1",
                        "type": "choice",
                        "prompt": "Step 1: What should you divide 84 by first?",
                        "options": [
                            {"id": "a", "text": "2"},
                            {"id": "b", "text": "3"},
                            {"id": "c", "text": "5"},
                            {"id": "d", "text": "7"}
                        ],
                        "correct_option_id": "a",
                        "correct_answer": "2",
                        "explanation": "84 is even, so the smallest prime factor is 2."
                    },
                    {
                        "id": "s2",
                        "type": "choice",
                        "prompt": "Step 2: After 84 ÷ 2 = 42, what should you do next?",
                        "options": [
                            {"id": "a", "text": "Stop because 42 is prime"},
                            {"id": "b", "text": "Divide by 2 again"},
                            {"id": "c", "text": "Divide by 5"},
                            {"id": "d", "text": "Write 84 = 42"}
                        ],
                        "correct_option_id": "b",
                        "correct_answer": "Divide by 2 again",
                        "explanation": "42 is still even, so divide by 2 again."
                    },
                    {
                        "id": "s3",
                        "type": "choice",
                        "prompt": "Step 3: After reaching 21, what is the correct factorization of 21?",
                        "options": [
                            {"id": "a", "text": "2 x 10.5"},
                            {"id": "b", "text": "3 x 7"},
                            {"id": "c", "text": "4 x 5"},
                            {"id": "d", "text": "21 is prime"}
                        ],
                        "correct_option_id": "b",
                        "correct_answer": "3 x 7",
                        "explanation": "21 = 3 x 7."
                    },
                    {
                        "id": "s4",
                        "type": "input",
                        "prompt": "Final Step: Enter the prime factorization of 84.",
                        "hint": "You found 2, 2, 3, and 7.",
                        "accepted_answers": ["2^2*3*7", "2^2 x 3 x 7", "2^2 x 3 x 7", "2*2*3*7"],
                        "correct_answer": "84 = 2^2 x 3 x 7",
                        "explanation": "Combining all factors gives 84 = 2^2 x 3 x 7."
                    }
                ]
            },
            {
                "id": "factorization_medium_2",
                "level": "medium",
                "title": "Choose the factorization path for 90",
                "question": "Prime factorize 90 by choosing the correct next steps.",
                "interaction": "choice_steps_final",
                "steps": [
                    {
                        "id": "s1",
                        "type": "choice",
                        "prompt": "Step 1: What should you divide 90 by first?",
                        "options": [
                            {"id": "a", "text": "2"},
                            {"id": "b", "text": "7"},
                            {"id": "c", "text": "11"},
                            {"id": "d", "text": "13"}
                        ],
                        "correct_option_id": "a",
                        "correct_answer": "2",
                        "explanation": "90 is even, so 2 is the first prime factor."
                    },
                    {
                        "id": "s2",
                        "type": "choice",
                        "prompt": "Step 2: After 90 ÷ 2 = 45, what should you divide by next?",
                        "options": [
                            {"id": "a", "text": "2"},
                            {"id": "b", "text": "3"},
                            {"id": "c", "text": "8"},
                            {"id": "d", "text": "45 is prime"}
                        ],
                        "correct_option_id": "b",
                        "correct_answer": "3",
                        "explanation": "45 is divisible by 3."
                    },
                    {
                        "id": "s3",
                        "type": "choice",
                        "prompt": "Step 3: After 45 ÷ 3 = 15, what is the factorization of 15?",
                        "options": [
                            {"id": "a", "text": "3 x 5"},
                            {"id": "b", "text": "2 x 7.5"},
                            {"id": "c", "text": "15 is prime"},
                            {"id": "d", "text": "4 x 4"}
                        ],
                        "correct_option_id": "a",
                        "correct_answer": "3 x 5",
                        "explanation": "15 = 3 x 5."
                    },
                    {
                        "id": "s4",
                        "type": "input",
                        "prompt": "Final Step: Enter the prime factorization of 90.",
                        "hint": "You found 2, 3, 3, and 5.",
                        "accepted_answers": ["2*3^2*5", "2 x 3^2 x 5", "2 x 3^2 x 5", "2*3*3*5"],
                        "correct_answer": "90 = 2 x 3^2 x 5",
                        "explanation": "90 = 2 x 45 = 2 x 3 x 15 = 2 x 3 x 3 x 5 = 2 x 3^2 x 5."
                    }
                ]
            },
            {
                "id": "factorization_hard_1",
                "level": "hard",
                "title": "Prime factorize 3600",
                "question": "Find the prime factorization of 3600.",
                "interaction": "final_answer",
                "steps": [
                    {
                        "id": "final",
                        "type": "input",
                        "prompt": "Enter the final prime factorization of 3600.",
                        "hint": "3600 = 36 x 100.",
                        "accepted_answers": ["2^4*3^2*5^2", "2^4 x 3^2 x 5^2", "2^4 x 3^2 x 5^2", "2*2*2*2*3*3*5*5"],
                        "correct_answer": "3600 = 2^4 x 3^2 x 5^2",
                        "explanation": "3600 = 36 x 100 = (2^2 x 3^2)(2^2 x 5^2) = 2^4 x 3^2 x 5^2."
                    }
                ]
            },
            {
                "id": "factorization_hard_2",
                "level": "hard",
                "title": "Find a GCD using prime factorization",
                "question": "Use prime factorization to find GCD(18, 300).",
                "interaction": "final_answer",
                "steps": [
                    {
                        "id": "final",
                        "type": "input",
                        "prompt": "Enter the final value of GCD(18, 300).",
                        "hint": "Compare 18 = 2 x 3^2 and 300 = 2^2 x 3 x 5^2.",
                        "accepted_answers": ["6", "gcd=6", "gcd(18,300)=6"],
                        "correct_answer": "GCD(18, 300) = 6",
                        "explanation": "The common primes are 2 and 3. Use the smaller powers: 2^1 x 3^1 = 6."
                    }
                ]
            }
        ],

        "quiz": [
            {
                "id": "factorization_q1",
                "type": "mcq",
                "question": "Which statement correctly describes a prime number?",
                "options": [
                    {"id": "a", "text": "A number divisible by many values."},
                    {"id": "b", "text": "A number whose only divisors are 1 and itself."},
                    {"id": "c", "text": "A number that is always even."},
                    {"id": "d", "text": "A number that is always composite."}
                ],
                "correct_option_id": "b",
                "explanation": "A prime number has exactly two positive divisors: 1 and itself."
            },
            {
                "id": "factorization_q2",
                "type": "mcq",
                "question": "Which is the correct prime factorization of 84?",
                "options": [
                    {"id": "a", "text": "2 x 3 x 14"},
                    {"id": "b", "text": "2^2 x 3 x 7"},
                    {"id": "c", "text": "4 x 21"},
                    {"id": "d", "text": "6 x 14"}
                ],
                "correct_option_id": "b",
                "explanation": "84 = 2 x 2 x 3 x 7 = 2^2 x 3 x 7."
            },
            {
                "id": "factorization_q3",
                "type": "input",
                "question": "Enter the prime factorization of 60.",
                "accepted_answers": ["2^2*3*5", "2^2 x 3 x 5", "2^2 x 3 x 5", "2*2*3*5"],
                "correct_answer": "60 = 2^2 x 3 x 5",
                "explanation": "60 = 2 x 30 = 2 x 2 x 15 = 2^2 x 3 x 5."
            },
            {
                "id": "factorization_q4",
                "type": "mcq",
                "question": "What is the only even prime number?",
                "options": [
                    {"id": "a", "text": "1"},
                    {"id": "b", "text": "2"},
                    {"id": "c", "text": "4"},
                    {"id": "d", "text": "8"}
                ],
                "correct_option_id": "b",
                "explanation": "2 is the only even prime. Every other even number is divisible by 2."
            },
            {
                "id": "factorization_q5",
                "type": "input",
                "question": "Find GCD(18, 300).",
                "accepted_answers": ["6"],
                "correct_answer": "6",
                "explanation": "18 = 2 x 3^2 and 300 = 2^2 x 3 x 5^2. The common part is 2 x 3 = 6."
            },
            {
                "id": "factorization_q6",
                "type": "mcq",
                "question": "Which number is composite?",
                "options": [
                    {"id": "a", "text": "13"},
                    {"id": "b", "text": "17"},
                    {"id": "c", "text": "21"},
                    {"id": "d", "text": "19"}
                ],
                "correct_option_id": "c",
                "explanation": "21 is composite because 21 = 3 x 7."
            },
            {
                "id": "factorization_q7",
                "type": "input",
                "question": "Enter the prime factorization of 90.",
                "accepted_answers": ["2*3^2*5", "2 x 3^2 x 5", "2 x 3^2 x 5", "2*3*3*5"],
                "correct_answer": "90 = 2 x 3^2 x 5",
                "explanation": "90 = 2 x 45 = 2 x 3 x 15 = 2 x 3 x 3 x 5."
            },
            {
                "id": "factorization_q8",
                "type": "mcq",
                "question": "In prime factorization, why do we keep factoring 42 in 84 = 2 x 42?",
                "options": [
                    {"id": "a", "text": "Because 42 is not prime."},
                    {"id": "b", "text": "Because 42 is already prime."},
                    {"id": "c", "text": "Because we must always divide by 10."},
                    {"id": "d", "text": "Because 84 is odd."}
                ],
                "correct_option_id": "a",
                "explanation": "Prime factorization only stops when every factor is prime."
            },
            {
                "id": "factorization_q9",
                "type": "mcq",
                "question": "Two numbers are relatively prime when:",
                "options": [
                    {"id": "a", "text": "They are both prime."},
                    {"id": "b", "text": "Their only common divisor is 1."},
                    {"id": "c", "text": "They are both even."},
                    {"id": "d", "text": "They have the same prime factorization."}
                ],
                "correct_option_id": "b",
                "explanation": "Relatively prime numbers have no common divisor except 1."
            },
            {
                "id": "factorization_q10",
                "type": "input",
                "question": "Enter the prime factorization of 3600.",
                "accepted_answers": ["2^4*3^2*5^2", "2^4 x 3^2 x 5^2", "2^4 x 3^2 x 5^2", "2*2*2*2*3*3*5*5"],
                "correct_answer": "3600 = 2^4 x 3^2 x 5^2",
                "explanation": "3600 = 36 x 100 = 2^4 x 3^2 x 5^2."
            }
        ]
    },

    "totient": {
        "id": "totient",
        "title": "Euler's Totient Function",
        "description": "Learn how to count integers that are relatively prime to n.",

        "lessons": [
            {
                "id": "totient_l1",
                "title": "Complete and Reduced Residue Sets",
                "summary": (
                    "When working modulo n, the complete residue set is 0, 1, 2, ..., n - 1. "
                    "The reduced residue set keeps only the values that are relatively prime to n."
                ),
                "example": (
                    "For n = 10, the complete residue set is {0,1,2,3,4,5,6,7,8,9}. "
                    "The reduced residue set is {1,3,7,9}."
                ),
                "steps": [
                    "List all residues from 0 to n - 1.",
                    "Check which residues are relatively prime to n.",
                    "Keep only the residues whose GCD with n is 1.",
                    "The remaining set is the reduced residue set."
                ]
            },
            {
                "id": "totient_l2",
                "title": "Definition of φ(n)",
                "summary": (
                    "Euler's totient function φ(n) counts how many positive integers up to n are relatively prime to n. "
                    "Equivalently, it counts the number of elements in the reduced residue set modulo n."
                ),
                "example": "φ(10) = 4 because 1, 3, 7, and 9 are relatively prime to 10.",
                "steps": [
                    "Choose n.",
                    "List the numbers from 1 to n.",
                    "Keep the numbers whose GCD with n is 1.",
                    "Count them.",
                    "That count is φ(n)."
                ]
            },
            {
                "id": "totient_l3",
                "title": "φ(p) and φ(pq)",
                "summary": (
                    "If p is prime, then φ(p) = p - 1. "
                    "If p and q are different primes, then φ(pq) = (p - 1)(q - 1)."
                ),
                "example": "φ(37) = 36 and φ(21) = φ(3 x 7) = (3 - 1)(7 - 1) = 12.",
                "steps": [
                    "If n is prime, use φ(n) = n - 1.",
                    "If n = pq with p and q prime, use φ(pq) = (p - 1)(q - 1).",
                    "Substitute the prime factors.",
                    "Multiply to get the result."
                ]
            },
            {
                "id": "totient_l4",
                "title": "Euler's Theorem",
                "summary": (
                    "Euler's theorem says that if GCD(a,n)=1, then a^φ(n) ≡ 1 mod n. "
                    "It generalizes Fermat's Little Theorem and helps simplify modular powers."
                ),
                "example": "Since φ(10)=4 and GCD(3,10)=1, 3^4 = 81 ≡ 1 mod 10.",
                "steps": [
                    "Check that GCD(a,n)=1.",
                    "Compute φ(n).",
                    "Use a^φ(n) ≡ 1 mod n.",
                    "Reduce the power modulo n."
                ]
            }
        ],

        "lesson": {
            "id": "totient_l1",
            "title": "Complete and Reduced Residue Sets",
            "summary": "φ(n) counts the numbers relatively prime to n.",
            "example": "φ(10)=4 because {1,3,7,9} are relatively prime to 10.",
            "steps": ["List residues.", "Keep only coprime values.", "Count them."]
        },

        "practice": [
            {
                "id": "totient_easy_1",
                "level": "easy",
                "title": "Compute φ(10)",
                "question": "Compute φ(10) step by step.",
                "interaction": "guided_steps",
                "steps": [
                    {
                        "id": "s1",
                        "type": "input",
                        "prompt": "Step 1: List the numbers from 1 to 10 that are relatively prime to 10.",
                        "hint": "They must not share a factor 2 or 5 with 10.",
                        "accepted_answers": ["1,3,7,9", "1 3 7 9", "{1,3,7,9}"],
                        "correct_answer": "1, 3, 7, 9",
                        "explanation": "The numbers relatively prime to 10 are 1, 3, 7, and 9."
                    },
                    {
                        "id": "s2",
                        "type": "input",
                        "prompt": "Final Step: How many numbers are in that list?",
                        "hint": "Count 1, 3, 7, and 9.",
                        "accepted_answers": ["4"],
                        "correct_answer": "φ(10) = 4",
                        "explanation": "There are 4 numbers relatively prime to 10, so φ(10)=4."
                    }
                ]
            },
            {
                "id": "totient_easy_2",
                "level": "easy",
                "title": "Compute φ(7)",
                "question": "Compute φ(7) step by step.",
                "interaction": "guided_steps",
                "steps": [
                    {
                        "id": "s1",
                        "type": "input",
                        "prompt": "Step 1: Is 7 prime?",
                        "hint": "7 has divisors 1 and 7 only.",
                        "accepted_answers": ["yes", "prime", "7 is prime"],
                        "correct_answer": "Yes, 7 is prime.",
                        "explanation": "7 is prime because only 1 and 7 divide it exactly."
                    },
                    {
                        "id": "s2",
                        "type": "input",
                        "prompt": "Step 2: For prime p, what is φ(p)?",
                        "hint": "Use p - 1.",
                        "accepted_answers": ["p-1", "p - 1"],
                        "correct_answer": "φ(p) = p - 1",
                        "explanation": "For a prime p, every number from 1 to p-1 is relatively prime to p."
                    },
                    {
                        "id": "s3",
                        "type": "input",
                        "prompt": "Final Step: Compute φ(7).",
                        "hint": "7 - 1 = ?",
                        "accepted_answers": ["6"],
                        "correct_answer": "φ(7) = 6",
                        "explanation": "Since 7 is prime, φ(7)=7-1=6."
                    }
                ]
            },
            {
                "id": "totient_medium_1",
                "level": "medium",
                "title": "Choose the totient method for 21",
                "question": "Compute φ(21) by choosing the correct next steps.",
                "interaction": "choice_steps_final",
                "steps": [
                    {
                        "id": "s1",
                        "type": "choice",
                        "prompt": "Step 1: How should we factor 21?",
                        "options": [
                            {"id": "a", "text": "3 x 7"},
                            {"id": "b", "text": "2 x 10"},
                            {"id": "c", "text": "5 x 5"},
                            {"id": "d", "text": "21 is prime"}
                        ],
                        "correct_option_id": "a",
                        "correct_answer": "21 = 3 x 7",
                        "explanation": "21 factors into the primes 3 and 7."
                    },
                    {
                        "id": "s2",
                        "type": "choice",
                        "prompt": "Step 2: Which formula should we use for n = pq?",
                        "options": [
                            {"id": "a", "text": "φ(pq) = p + q"},
                            {"id": "b", "text": "φ(pq) = (p - 1)(q - 1)"},
                            {"id": "c", "text": "φ(pq) = pq"},
                            {"id": "d", "text": "φ(pq) = p - q"}
                        ],
                        "correct_option_id": "b",
                        "correct_answer": "φ(pq) = (p - 1)(q - 1)",
                        "explanation": "For two primes p and q, φ(pq) = (p - 1)(q - 1)."
                    },
                    {
                        "id": "s3",
                        "type": "input",
                        "prompt": "Final Step: Compute φ(21).",
                        "hint": "(3 - 1)(7 - 1)",
                        "accepted_answers": ["12"],
                        "correct_answer": "φ(21) = 12",
                        "explanation": "φ(21) = (3 - 1)(7 - 1) = 2 x 6 = 12."
                    }
                ]
            },
            {
                "id": "totient_medium_2",
                "level": "medium",
                "title": "Choose the Euler theorem path",
                "question": "Use Euler's theorem to compute 3^4 mod 10.",
                "interaction": "choice_steps_final",
                "steps": [
                    {
                        "id": "s1",
                        "type": "choice",
                        "prompt": "Step 1: What is φ(10)?",
                        "options": [
                            {"id": "a", "text": "2"},
                            {"id": "b", "text": "4"},
                            {"id": "c", "text": "5"},
                            {"id": "d", "text": "10"}
                        ],
                        "correct_option_id": "b",
                        "correct_answer": "4",
                        "explanation": "The reduced residue set modulo 10 is {1,3,7,9}, so φ(10)=4."
                    },
                    {
                        "id": "s2",
                        "type": "choice",
                        "prompt": "Step 2: Since GCD(3,10)=1, what does Euler's theorem say?",
                        "options": [
                            {"id": "a", "text": "3^4 ≡ 1 mod 10"},
                            {"id": "b", "text": "3^4 ≡ 0 mod 10"},
                            {"id": "c", "text": "3 + 10 = 13"},
                            {"id": "d", "text": "φ(10)=10"}
                        ],
                        "correct_option_id": "a",
                        "correct_answer": "3^4 ≡ 1 mod 10",
                        "explanation": "Euler's theorem gives a^φ(n) ≡ 1 mod n."
                    },
                    {
                        "id": "s3",
                        "type": "input",
                        "prompt": "Final Step: Enter 3^4 mod 10.",
                        "hint": "3^4 = 81.",
                        "accepted_answers": ["1"],
                        "correct_answer": "1",
                        "explanation": "81 mod 10 = 1."
                    }
                ]
            },
            {
                "id": "totient_hard_1",
                "level": "hard",
                "title": "Compute φ(12)",
                "question": "Compute φ(12).",
                "interaction": "final_answer",
                "steps": [
                    {
                        "id": "final",
                        "type": "input",
                        "prompt": "Enter the final value of φ(12).",
                        "hint": "The coprime numbers are 1, 5, 7, and 11.",
                        "accepted_answers": ["4"],
                        "correct_answer": "φ(12) = 4",
                        "explanation": "The numbers relatively prime to 12 are 1, 5, 7, and 11, so φ(12)=4."
                    }
                ]
            },
            {
                "id": "totient_hard_2",
                "level": "hard",
                "title": "Compute φ(33)",
                "question": "Compute φ(33).",
                "interaction": "final_answer",
                "steps": [
                    {
                        "id": "final",
                        "type": "input",
                        "prompt": "Enter the final value of φ(33).",
                        "hint": "33 = 3 x 11.",
                        "accepted_answers": ["20"],
                        "correct_answer": "φ(33) = 20",
                        "explanation": "φ(33) = (3 - 1)(11 - 1) = 2 x 10 = 20."
                    }
                ]
            }
        ],

        "quiz": [
            {
                "id": "totient_q1",
                "type": "mcq",
                "question": "What does φ(n) count?",
                "options": [
                    {"id": "a", "text": "The number of prime factors of n."},
                    {"id": "b", "text": "The numbers up to n that are relatively prime to n."},
                    {"id": "c", "text": "The powers of n."},
                    {"id": "d", "text": "Only the even numbers less than n."}
                ],
                "correct_option_id": "b",
                "explanation": "φ(n) counts how many positive integers up to n are relatively prime to n."
            },
            {
                "id": "totient_q2",
                "type": "input",
                "question": "Compute φ(10).",
                "accepted_answers": ["4"],
                "correct_answer": "4",
                "explanation": "The numbers relatively prime to 10 are 1, 3, 7, and 9."
            },
            {
                "id": "totient_q3",
                "type": "mcq",
                "question": "What is φ(p) when p is prime?",
                "options": [
                    {"id": "a", "text": "p"},
                    {"id": "b", "text": "p - 1"},
                    {"id": "c", "text": "p + 1"},
                    {"id": "d", "text": "1"}
                ],
                "correct_option_id": "b",
                "explanation": "If p is prime, φ(p)=p-1."
            },
            {
                "id": "totient_q4",
                "type": "input",
                "question": "Compute φ(37).",
                "accepted_answers": ["36"],
                "correct_answer": "36",
                "explanation": "37 is prime, so φ(37)=37-1=36."
            },
            {
                "id": "totient_q5",
                "type": "mcq",
                "question": "What is the reduced residue set modulo 10?",
                "options": [
                    {"id": "a", "text": "{0,1,2,3}"},
                    {"id": "b", "text": "{1,3,7,9}"},
                    {"id": "c", "text": "{2,4,6,8}"},
                    {"id": "d", "text": "{5,10}"}
                ],
                "correct_option_id": "b",
                "explanation": "The numbers relatively prime to 10 are 1, 3, 7, and 9."
            },
            {
                "id": "totient_q6",
                "type": "input",
                "question": "Compute φ(21).",
                "accepted_answers": ["12"],
                "correct_answer": "12",
                "explanation": "φ(21)=(3-1)(7-1)=12."
            },
            {
                "id": "totient_q7",
                "type": "mcq",
                "question": "Euler's theorem says that if GCD(a,n)=1, then:",
                "options": [
                    {"id": "a", "text": "a^φ(n) ≡ 1 mod n"},
                    {"id": "b", "text": "a + n = φ(n)"},
                    {"id": "c", "text": "a must be prime"},
                    {"id": "d", "text": "n must be even"}
                ],
                "correct_option_id": "a",
                "explanation": "Euler's theorem states that a^φ(n) ≡ 1 mod n."
            },
            {
                "id": "totient_q8",
                "type": "input",
                "question": "Compute 3^4 mod 10.",
                "accepted_answers": ["1"],
                "correct_answer": "1",
                "explanation": "3^4=81 and 81 mod 10 = 1."
            },
            {
                "id": "totient_q9",
                "type": "mcq",
                "question": "Which pair is relatively prime?",
                "options": [
                    {"id": "a", "text": "8 and 15"},
                    {"id": "b", "text": "6 and 12"},
                    {"id": "c", "text": "10 and 20"},
                    {"id": "d", "text": "9 and 27"}
                ],
                "correct_option_id": "a",
                "explanation": "8 and 15 share no common divisor except 1."
            },
            {
                "id": "totient_q10",
                "type": "input",
                "question": "Compute φ(33).",
                "accepted_answers": ["20"],
                "correct_answer": "20",
                "explanation": "33=3x11, so φ(33)=(3-1)(11-1)=20."
            }
        ]
    },

    "fastexp": {
        "id": "fastexp",
        "title": "Fast Modular Exponentiation",
        "description": "Learn how to compute large powers modulo n efficiently.",

        "lessons": [
            {
                "id": "fastexp_l1",
                "title": "Why Modular Powers Matter",
                "summary": (
                    "Modular exponentiation means computing a^b mod n. "
                    "It appears in Fermat's theorem, Euler's theorem, primality testing, and cryptography. "
                    "The goal is to avoid computing huge powers directly."
                ),
                "example": "Instead of computing 7^100 directly, reduce intermediate results modulo n.",
                "steps": [
                    "Start with a^b mod n.",
                    "Notice that a^b can become very large.",
                    "Reduce intermediate results modulo n.",
                    "Keep the numbers small while preserving the final modular result."
                ]
            },
            {
                "id": "fastexp_l2",
                "title": "Repeated Squaring",
                "summary": (
                    "Repeated squaring computes powers like a, a^2, a^4, a^8, and so on. "
                    "This is faster than multiplying by a one step at a time."
                ),
                "example": "3^2 ≡ 4 mod 5, 3^4 ≡ 1 mod 5, and 3^8 ≡ 1 mod 5.",
                "steps": [
                    "Square the base.",
                    "Reduce modulo n.",
                    "Square again.",
                    "Continue until you build the powers you need."
                ]
            },
            {
                "id": "fastexp_l3",
                "title": "Binary Exponentiation",
                "summary": (
                    "Binary exponentiation writes the exponent as a sum of powers of 2. "
                    "Then we multiply only the powers that are needed."
                ),
                "example": "13 = 8 + 4 + 1, so 2^13 = 2^8 x 2^4 x 2^1.",
                "steps": [
                    "Write the exponent in powers of 2.",
                    "Compute a^1, a^2, a^4, a^8, and so on.",
                    "Multiply only the needed powers.",
                    "Reduce modulo n after each step."
                ]
            },
            {
                "id": "fastexp_l4",
                "title": "Using Fermat and Euler",
                "summary": (
                    "Fermat's theorem and Euler's theorem help reduce large powers. "
                    "If p is prime, Fermat gives a^(p-1) ≡ 1 mod p. "
                    "Euler generalizes this to a^φ(n) ≡ 1 mod n when GCD(a,n)=1."
                ),
                "example": "Since 11 is prime, 2^10 ≡ 1 mod 11.",
                "steps": [
                    "Check whether the base and modulus are relatively prime.",
                    "Use Fermat if the modulus is prime.",
                    "Use Euler if you know φ(n).",
                    "Reduce the exponent using the theorem."
                ]
            }
        ],

        "lesson": {
            "id": "fastexp_l1",
            "title": "Why Modular Powers Matter",
            "summary": "Fast modular exponentiation computes a^b mod n without building huge numbers.",
            "example": "2^13 mod 7 can be computed using repeated squaring.",
            "steps": ["Square repeatedly.", "Reduce modulo n.", "Multiply needed powers."]
        },

        "practice": [
            {
                "id": "fastexp_easy_1",
                "level": "easy",
                "title": "Compute 2^5 mod 7",
                "question": "Compute 2^5 mod 7 step by step.",
                "interaction": "guided_steps",
                "steps": [
                    {
                        "id": "s1",
                        "type": "input",
                        "prompt": "Step 1: Compute 2^5.",
                        "hint": "2 x 2 x 2 x 2 x 2.",
                        "accepted_answers": ["32"],
                        "correct_answer": "32",
                        "explanation": "2^5 = 32."
                    },
                    {
                        "id": "s2",
                        "type": "input",
                        "prompt": "Final Step: Compute 32 mod 7.",
                        "hint": "32 = 7 x 4 + ?",
                        "accepted_answers": ["4"],
                        "correct_answer": "4",
                        "explanation": "32 = 7 x 4 + 4, so 2^5 mod 7 = 4."
                    }
                ]
            },
            {
                "id": "fastexp_easy_2",
                "level": "easy",
                "title": "Compute 3^4 mod 5",
                "question": "Compute 3^4 mod 5 step by step.",
                "interaction": "guided_steps",
                "steps": [
                    {
                        "id": "s1",
                        "type": "input",
                        "prompt": "Step 1: Compute 3^4.",
                        "hint": "3 x 3 x 3 x 3.",
                        "accepted_answers": ["81"],
                        "correct_answer": "81",
                        "explanation": "3^4 = 81."
                    },
                    {
                        "id": "s2",
                        "type": "input",
                        "prompt": "Final Step: Compute 81 mod 5.",
                        "hint": "81 = 5 x 16 + ?",
                        "accepted_answers": ["1"],
                        "correct_answer": "1",
                        "explanation": "81 mod 5 = 1."
                    }
                ]
            },
            {
                "id": "fastexp_medium_1",
                "level": "medium",
                "title": "Choose the repeated squaring path",
                "question": "Compute 3^4 mod 5 by choosing the correct steps.",
                "interaction": "choice_steps_final",
                "steps": [
                    {
                        "id": "s1",
                        "type": "choice",
                        "prompt": "Step 1: What is 3^2 mod 5?",
                        "options": [
                            {"id": "a", "text": "4"},
                            {"id": "b", "text": "2"},
                            {"id": "c", "text": "0"},
                            {"id": "d", "text": "5"}
                        ],
                        "correct_option_id": "a",
                        "correct_answer": "4",
                        "explanation": "3^2 = 9 and 9 mod 5 = 4."
                    },
                    {
                        "id": "s2",
                        "type": "choice",
                        "prompt": "Step 2: Since 3^4 = (3^2)^2, what is 4^2 mod 5?",
                        "options": [
                            {"id": "a", "text": "0"},
                            {"id": "b", "text": "1"},
                            {"id": "c", "text": "2"},
                            {"id": "d", "text": "4"}
                        ],
                        "correct_option_id": "b",
                        "correct_answer": "1",
                        "explanation": "4^2 = 16 and 16 mod 5 = 1."
                    },
                    {
                        "id": "s3",
                        "type": "input",
                        "prompt": "Final Step: Enter 3^4 mod 5.",
                        "hint": "Use the result from the previous step.",
                        "accepted_answers": ["1"],
                        "correct_answer": "1",
                        "explanation": "3^4 mod 5 = 1."
                    }
                ]
            },
            {
                "id": "fastexp_medium_2",
                "level": "medium",
                "title": "Use Fermat's theorem",
                "question": "Compute 2^10 mod 11 using Fermat's theorem.",
                "interaction": "choice_steps_final",
                "steps": [
                    {
                        "id": "s1",
                        "type": "choice",
                        "prompt": "Step 1: Is 11 prime?",
                        "options": [
                            {"id": "a", "text": "Yes"},
                            {"id": "b", "text": "No"}
                        ],
                        "correct_option_id": "a",
                        "correct_answer": "Yes",
                        "explanation": "11 is prime."
                    },
                    {
                        "id": "s2",
                        "type": "choice",
                        "prompt": "Step 2: What does Fermat's theorem say for base 2 and prime 11?",
                        "options": [
                            {"id": "a", "text": "2^10 ≡ 1 mod 11"},
                            {"id": "b", "text": "2^10 ≡ 0 mod 11"},
                            {"id": "c", "text": "2^11 ≡ 10 mod 11"},
                            {"id": "d", "text": "2 + 11 = 13"}
                        ],
                        "correct_option_id": "a",
                        "correct_answer": "2^10 ≡ 1 mod 11",
                        "explanation": "Fermat says a^(p-1) ≡ 1 mod p."
                    },
                    {
                        "id": "s3",
                        "type": "input",
                        "prompt": "Final Step: Enter 2^10 mod 11.",
                        "hint": "Use Fermat's theorem.",
                        "accepted_answers": ["1"],
                        "correct_answer": "1",
                        "explanation": "2^10 mod 11 = 1."
                    }
                ]
            },
            {
                "id": "fastexp_hard_1",
                "level": "hard",
                "title": "Compute 7^2 mod 19",
                "question": "Compute 7^2 mod 19.",
                "interaction": "final_answer",
                "steps": [
                    {
                        "id": "final",
                        "type": "input",
                        "prompt": "Enter the final answer.",
                        "hint": "7^2 = 49.",
                        "accepted_answers": ["11"],
                        "correct_answer": "11",
                        "explanation": "49 mod 19 = 11."
                    }
                ]
            },
            {
                "id": "fastexp_hard_2",
                "level": "hard",
                "title": "Compute 5^3 mod 13",
                "question": "Compute 5^3 mod 13.",
                "interaction": "final_answer",
                "steps": [
                    {
                        "id": "final",
                        "type": "input",
                        "prompt": "Enter the final answer.",
                        "hint": "5^3 = 125.",
                        "accepted_answers": ["8"],
                        "correct_answer": "8",
                        "explanation": "125 mod 13 = 8."
                    }
                ]
            }
        ],

        "quiz": [
            {
                "id": "fastexp_q1",
                "type": "mcq",
                "question": "Why do we reduce intermediate results modulo n?",
                "options": [
                    {"id": "a", "text": "To keep numbers small."},
                    {"id": "b", "text": "To make numbers bigger."},
                    {"id": "c", "text": "To avoid multiplication forever."},
                    {"id": "d", "text": "Because modulo always gives 0."}
                ],
                "correct_option_id": "a",
                "explanation": "Reducing modulo n keeps numbers manageable."
            },
            {
                "id": "fastexp_q2",
                "type": "input",
                "question": "Compute 2^5 mod 7.",
                "accepted_answers": ["4"],
                "correct_answer": "4",
                "explanation": "2^5 = 32 and 32 mod 7 = 4."
            },
            {
                "id": "fastexp_q3",
                "type": "mcq",
                "question": "Repeated squaring computes powers like:",
                "options": [
                    {"id": "a", "text": "a, a^2, a^4, a^8"},
                    {"id": "b", "text": "a, a+1, a+2"},
                    {"id": "c", "text": "n, n-1, n-2"},
                    {"id": "d", "text": "Only odd powers"}
                ],
                "correct_option_id": "a",
                "explanation": "Repeated squaring doubles the exponent each time."
            },
            {
                "id": "fastexp_q4",
                "type": "input",
                "question": "Compute 3^4 mod 5.",
                "accepted_answers": ["1"],
                "correct_answer": "1",
                "explanation": "3^4=81 and 81 mod 5 = 1."
            },
            {
                "id": "fastexp_q5",
                "type": "mcq",
                "question": "13 = ? as a sum of powers of 2",
                "options": [
                    {"id": "a", "text": "8 + 4 + 1"},
                    {"id": "b", "text": "8 + 2"},
                    {"id": "c", "text": "4 + 4 + 4"},
                    {"id": "d", "text": "16 - 1 only"}
                ],
                "correct_option_id": "a",
                "explanation": "13 = 8 + 4 + 1."
            },
            {
                "id": "fastexp_q6",
                "type": "input",
                "question": "Compute 7^2 mod 19.",
                "accepted_answers": ["11"],
                "correct_answer": "11",
                "explanation": "7^2=49 and 49 mod 19=11."
            },
            {
                "id": "fastexp_q7",
                "type": "mcq",
                "question": "Fermat's theorem says that if p is prime and GCD(a,p)=1:",
                "options": [
                    {"id": "a", "text": "a^(p-1) ≡ 1 mod p"},
                    {"id": "b", "text": "a+p=1"},
                    {"id": "c", "text": "p must divide a"},
                    {"id": "d", "text": "a must be 0"}
                ],
                "correct_option_id": "a",
                "explanation": "This is Fermat's Little Theorem."
            },
            {
                "id": "fastexp_q8",
                "type": "input",
                "question": "Compute 2^10 mod 11.",
                "accepted_answers": ["1"],
                "correct_answer": "1",
                "explanation": "By Fermat's theorem, 2^10 ≡ 1 mod 11."
            },
            {
                "id": "fastexp_q9",
                "type": "input",
                "question": "Compute 5^3 mod 13.",
                "accepted_answers": ["8"],
                "correct_answer": "8",
                "explanation": "5^3=125 and 125 mod 13=8."
            },
            {
                "id": "fastexp_q10",
                "type": "mcq",
                "question": "Fast exponentiation is useful because:",
                "options": [
                    {"id": "a", "text": "It avoids working with unnecessarily huge powers."},
                    {"id": "b", "text": "It only works for number 2."},
                    {"id": "c", "text": "It removes the need for modulus."},
                    {"id": "d", "text": "It works only when n is even."}
                ],
                "correct_option_id": "a",
                "explanation": "Fast exponentiation keeps calculations efficient by reducing and squaring."
            }
        ]
    },

    "millerrabin": {
        "id": "millerrabin",
        "title": "Miller-Rabin Primality Test",
        "description": "Learn how probabilistic primality testing works.",

        "lessons": [
            {
                "id": "millerrabin_l1",
                "title": "Why Primality Testing Matters",
                "summary": (
                    "We often need large prime numbers in number theory and cryptography. "
                    "Trial division works for small numbers but becomes too slow for large ones. "
                    "Miller-Rabin is a fast probabilistic primality test."
                ),
                "example": "Testing 29 by trial division is easy, but testing huge numbers needs faster methods.",
                "steps": [
                    "A prime number has no divisors except 1 and itself.",
                    "Trial division checks possible divisors one by one.",
                    "For large numbers, this becomes inefficient.",
                    "Miller-Rabin uses modular arithmetic to test primality faster."
                ]
            },
            {
                "id": "millerrabin_l2",
                "title": "Writing n - 1 = 2^k x q",
                "summary": (
                    "The first step of Miller-Rabin is to write n - 1 as 2^k x q, where q is odd. "
                    "This is possible for every odd n ≥ 3 because n - 1 is even."
                ),
                "example": "For n = 29, n - 1 = 28 = 2^2 x 7.",
                "steps": [
                    "Compute n - 1.",
                    "Divide by 2 repeatedly.",
                    "Count the number of divisions. This is k.",
                    "Stop when the remaining value is odd. This is q."
                ]
            },
            {
                "id": "millerrabin_l3",
                "title": "Witnesses",
                "summary": (
                    "A witness is a base a that proves n is composite. "
                    "If Miller-Rabin finds a witness, then n is definitely composite."
                ),
                "example": "For n = 221 and a = 5, Miller-Rabin returns composite.",
                "steps": [
                    "Choose a base a.",
                    "Run the Miller-Rabin checks.",
                    "If the checks fail, a is a witness.",
                    "A witness proves that n is composite."
                ]
            },
            {
                "id": "millerrabin_l4",
                "title": "Maybe Prime vs Composite",
                "summary": (
                    "If Miller-Rabin returns composite, the number is definitely composite. "
                    "If it returns maybe prime, the number passed that test but is not proven prime with only one base."
                ),
                "example": "For n = 29 and a = 10, the test returns maybe prime.",
                "steps": [
                    "Composite means definitely not prime.",
                    "Maybe prime means the number passed for the chosen base.",
                    "Repeat with different bases to increase confidence."
                ]
            },
            {
                "id": "millerrabin_l5",
                "title": "Miller-Rabin Algorithm Steps",
                "summary": (
                    "Miller-Rabin chooses a random base a, computes a^q mod n, then checks a sequence of powers. "
                    "If the sequence behaves like it should for a prime, the result is maybe prime. Otherwise, it is composite."
                ),
                "example": "For n = 29, 28 = 2^2 x 7. With a = 10, 10^14 mod 29 = 28, so maybe prime.",
                "steps": [
                    "Write n - 1 = 2^k x q.",
                    "Choose a base a.",
                    "Compute a^q mod n.",
                    "Check whether the result is 1.",
                    "Check whether any later power is n - 1.",
                    "If none pass, return composite."
                ]
            }
        ],

        "lesson": {
            "id": "millerrabin_l1",
            "title": "Why Primality Testing Matters",
            "summary": "Miller-Rabin checks whether a number is composite or probably prime.",
            "example": "A witness proves compositeness.",
            "steps": ["Write n-1 as 2^kq.", "Choose a base.", "Check powers modulo n."]
        },

        "practice": [
            {
                "id": "millerrabin_easy_1",
                "level": "easy",
                "title": "Decompose n - 1 for n = 29",
                "question": "For n = 29, write n - 1 as 2^k x q.",
                "interaction": "guided_steps",
                "steps": [
                    {
                        "id": "s1",
                        "type": "input",
                        "prompt": "Step 1: Compute n - 1.",
                        "hint": "29 - 1.",
                        "accepted_answers": ["28"],
                        "correct_answer": "28",
                        "explanation": "29 - 1 = 28."
                    },
                    {
                        "id": "s2",
                        "type": "input",
                        "prompt": "Step 2: Write 28 as 2^k x q with q odd.",
                        "hint": "28 = 4 x 7.",
                        "accepted_answers": ["2^2*7", "2^2 x 7", "2^2 x 7", "4*7"],
                        "correct_answer": "28 = 2^2 x 7",
                        "explanation": "28 = 2 x 2 x 7 = 2^2 x 7."
                    },
                    {
                        "id": "s3",
                        "type": "input",
                        "prompt": "Final Step: What are k and q?",
                        "hint": "Compare 28 = 2^2 x 7.",
                        "accepted_answers": ["k=2,q=7", "k = 2, q = 7", "2,7"],
                        "correct_answer": "k = 2, q = 7",
                        "explanation": "From 28 = 2^2 x 7, k = 2 and q = 7."
                    }
                ]
            },
            {
                "id": "millerrabin_easy_2",
                "level": "easy",
                "title": "Understand witnesses",
                "question": "Understand what a Miller-Rabin witness proves.",
                "interaction": "guided_steps",
                "steps": [
                    {
                        "id": "s1",
                        "type": "input",
                        "prompt": "Step 1: If Miller-Rabin finds a witness, what does it prove?",
                        "hint": "It proves the number is not prime.",
                        "accepted_answers": ["composite", "n is composite", "the number is composite"],
                        "correct_answer": "The number is composite.",
                        "explanation": "A witness proves that n is composite."
                    },
                    {
                        "id": "s2",
                        "type": "input",
                        "prompt": "Final Step: If the test returns maybe prime, is the number definitely prime?",
                        "hint": "Think about pseudoprimes.",
                        "accepted_answers": ["no", "not necessarily", "no it is not definitely prime"],
                        "correct_answer": "No",
                        "explanation": "Maybe prime means the number passed this test, but it is not a full proof with one base."
                    }
                ]
            },
            {
                "id": "millerrabin_medium_1",
                "level": "medium",
                "title": "Choose the Miller-Rabin setup",
                "question": "Set up Miller-Rabin for n = 29.",
                "interaction": "choice_steps_final",
                "steps": [
                    {
                        "id": "s1",
                        "type": "choice",
                        "prompt": "Step 1: What is n - 1 when n = 29?",
                        "options": [
                            {"id": "a", "text": "28"},
                            {"id": "b", "text": "29"},
                            {"id": "c", "text": "30"},
                            {"id": "d", "text": "14"}
                        ],
                        "correct_option_id": "a",
                        "correct_answer": "28",
                        "explanation": "29 - 1 = 28."
                    },
                    {
                        "id": "s2",
                        "type": "choice",
                        "prompt": "Step 2: Which decomposition is correct?",
                        "options": [
                            {"id": "a", "text": "28 = 2^2 x 7"},
                            {"id": "b", "text": "28 = 2^3 x 7"},
                            {"id": "c", "text": "28 = 2 x 15"},
                            {"id": "d", "text": "28 = 3 x 9"}
                        ],
                        "correct_option_id": "a",
                        "correct_answer": "28 = 2^2 x 7",
                        "explanation": "28 = 4 x 7 = 2^2 x 7."
                    },
                    {
                        "id": "s3",
                        "type": "input",
                        "prompt": "Final Step: Enter q.",
                        "hint": "28 = 2^2 x q.",
                        "accepted_answers": ["7"],
                        "correct_answer": "q = 7",
                        "explanation": "q is the odd part, so q = 7."
                    }
                ]
            },
            {
                "id": "millerrabin_medium_2",
                "level": "medium",
                "title": "Composite or maybe prime?",
                "question": "Understand Miller-Rabin outputs.",
                "interaction": "choice_steps_final",
                "steps": [
                    {
                        "id": "s1",
                        "type": "choice",
                        "prompt": "If Miller-Rabin returns composite, what can we conclude?",
                        "options": [
                            {"id": "a", "text": "Definitely composite"},
                            {"id": "b", "text": "Definitely prime"},
                            {"id": "c", "text": "Need to divide by 2"},
                            {"id": "d", "text": "The test crashed"}
                        ],
                        "correct_option_id": "a",
                        "correct_answer": "Definitely composite",
                        "explanation": "Composite is a definite result."
                    },
                    {
                        "id": "s2",
                        "type": "choice",
                        "prompt": "If Miller-Rabin returns maybe prime, what should we do for more confidence?",
                        "options": [
                            {"id": "a", "text": "Repeat with different bases"},
                            {"id": "b", "text": "Stop forever"},
                            {"id": "c", "text": "Assume it is even"},
                            {"id": "d", "text": "Change n"}
                        ],
                        "correct_option_id": "a",
                        "correct_answer": "Repeat with different bases",
                        "explanation": "Repeating with different bases reduces the chance of being fooled."
                    },
                    {
                        "id": "s3",
                        "type": "input",
                        "prompt": "Final Step: What does a witness prove?",
                        "hint": "One word.",
                        "accepted_answers": ["composite"],
                        "correct_answer": "Composite",
                        "explanation": "A witness proves that the number is composite."
                    }
                ]
            },
            {
                "id": "millerrabin_hard_1",
                "level": "hard",
                "title": "Decompose 220",
                "question": "Write 220 as 2^k x q where q is odd.",
                "interaction": "final_answer",
                "steps": [
                    {
                        "id": "final",
                        "type": "input",
                        "prompt": "Enter the decomposition of 220.",
                        "hint": "220 = 4 x 55.",
                        "accepted_answers": ["2^2*55", "2^2 x 55", "2^2 x 55", "4*55"],
                        "correct_answer": "220 = 2^2 x 55",
                        "explanation": "220 = 2 x 110 = 2 x 2 x 55 = 2^2 x 55."
                    }
                ]
            },
            {
                "id": "millerrabin_hard_2",
                "level": "hard",
                "title": "Factor 221",
                "question": "Show why 221 is composite.",
                "interaction": "final_answer",
                "steps": [
                    {
                        "id": "final",
                        "type": "input",
                        "prompt": "Enter a nontrivial factorization of 221.",
                        "hint": "221 is divisible by 13.",
                        "accepted_answers": ["13*17", "13 x 17", "13 x 17", "221=13*17"],
                        "correct_answer": "221 = 13 x 17",
                        "explanation": "Since 221 = 13 x 17, it is composite."
                    }
                ]
            }
        ],

        "quiz": [
            {
                "id": "millerrabin_q1",
                "type": "mcq",
                "question": "Miller-Rabin is mainly used for:",
                "options": [
                    {"id": "a", "text": "Primality testing"},
                    {"id": "b", "text": "Sorting arrays"},
                    {"id": "c", "text": "Drawing graphs"},
                    {"id": "d", "text": "Solving linear equations only"}
                ],
                "correct_option_id": "a",
                "explanation": "Miller-Rabin is a primality test."
            },
            {
                "id": "millerrabin_q2",
                "type": "input",
                "question": "For n = 29, compute n - 1.",
                "accepted_answers": ["28"],
                "correct_answer": "28",
                "explanation": "29 - 1 = 28."
            },
            {
                "id": "millerrabin_q3",
                "type": "mcq",
                "question": "The first step writes n - 1 as:",
                "options": [
                    {"id": "a", "text": "2^k x q, q odd"},
                    {"id": "b", "text": "p + q"},
                    {"id": "c", "text": "n^2"},
                    {"id": "d", "text": "a x b x c only"}
                ],
                "correct_option_id": "a",
                "explanation": "Miller-Rabin writes n-1 = 2^kq with q odd."
            },
            {
                "id": "millerrabin_q4",
                "type": "input",
                "question": "For 28 = 2^k x q, enter q.",
                "accepted_answers": ["7"],
                "correct_answer": "7",
                "explanation": "28 = 2^2 x 7."
            },
            {
                "id": "millerrabin_q5",
                "type": "mcq",
                "question": "If Miller-Rabin finds a witness, the number is:",
                "options": [
                    {"id": "a", "text": "Definitely composite"},
                    {"id": "b", "text": "Definitely prime"},
                    {"id": "c", "text": "Always odd"},
                    {"id": "d", "text": "Always 1"}
                ],
                "correct_option_id": "a",
                "explanation": "A witness proves compositeness."
            },
            {
                "id": "millerrabin_q6",
                "type": "mcq",
                "question": "If the test says maybe prime, this means:",
                "options": [
                    {"id": "a", "text": "The number passed this test but is not fully proven prime."},
                    {"id": "b", "text": "The number is definitely composite."},
                    {"id": "c", "text": "The number is 2."},
                    {"id": "d", "text": "The number has no residues."}
                ],
                "correct_option_id": "a",
                "explanation": "Maybe prime is probabilistic."
            },
            {
                "id": "millerrabin_q7",
                "type": "input",
                "question": "Write 220 as 2^k x q with q odd.",
                "accepted_answers": ["2^2*55", "2^2 x 55", "2^2 x 55", "4*55"],
                "correct_answer": "220 = 2^2 x 55",
                "explanation": "220 = 4 x 55."
            },
            {
                "id": "millerrabin_q8",
                "type": "mcq",
                "question": "Why repeat Miller-Rabin with different bases?",
                "options": [
                    {"id": "a", "text": "To increase confidence in a maybe-prime result"},
                    {"id": "b", "text": "To make n bigger"},
                    {"id": "c", "text": "To change the definition of prime"},
                    {"id": "d", "text": "To avoid modular arithmetic"}
                ],
                "correct_option_id": "a",
                "explanation": "More bases reduce the chance that a composite number passes."
            },
            {
                "id": "millerrabin_q9",
                "type": "input",
                "question": "Give a nontrivial factorization of 221.",
                "accepted_answers": ["13*17", "13 x 17", "13 x 17"],
                "correct_answer": "221 = 13 x 17",
                "explanation": "221 is composite because 221 = 13 x 17."
            },
            {
                "id": "millerrabin_q10",
                "type": "mcq",
                "question": "A pseudoprime is:",
                "options": [
                    {"id": "a", "text": "A composite number that passes a prime-like test for some base"},
                    {"id": "b", "text": "A prime number under 10"},
                    {"id": "c", "text": "A number with no divisors"},
                    {"id": "d", "text": "A number equal to 1"}
                ],
                "correct_option_id": "a",
                "explanation": "Some composite numbers can pass certain primality tests and are called pseudoprimes."
            }
        ]
    },

    "crt": {
        "id": "crt",
        "title": "Chinese Remainder Theorem",
        "description": "Learn how to reconstruct numbers from remainders.",

        "lessons": [
            {
                "id": "crt_l1",
                "title": "CRT Intuition",
                "summary": (
                    "The Chinese Remainder Theorem lets us work modulo smaller pairwise coprime moduli instead of one large modulus. "
                    "This is useful because modular computations are easier with smaller numbers."
                ),
                "example": "Instead of working modulo 1813, we can work modulo 37 and modulo 49 separately.",
                "steps": [
                    "Start with a modulus M that is a product of smaller moduli.",
                    "Make sure the smaller moduli are pairwise coprime.",
                    "Represent a number by its residues modulo the smaller moduli.",
                    "Use CRT to recover the original value modulo M."
                ]
            },
            {
                "id": "crt_l2",
                "title": "Residues and Moduli",
                "summary": (
                    "For each modulus mi, compute ai = A mod mi. "
                    "The number A can then be represented by the tuple (a1, a2, ..., ak)."
                ),
                "example": "If A = 973, then 973 mod 37 = 11 and 973 mod 49 = 42.",
                "steps": [
                    "Choose A and the moduli.",
                    "Compute A mod each modulus.",
                    "Write the residues as a tuple.",
                    "This tuple represents A modulo the product M."
                ]
            },
            {
                "id": "crt_l3",
                "title": "Recovering A from Residues",
                "summary": (
                    "To recover A, compute M, then Mi = M / mi for each modulus. "
                    "Use modular inverses to build constants ci, then combine the residues."
                ),
                "example": "A ≡ Σ ai ci mod M, where ci = Mi x (Mi^-1 mod mi).",
                "steps": [
                    "Compute M.",
                    "Compute each Mi = M / mi.",
                    "Find each inverse Mi^-1 mod mi.",
                    "Build ci.",
                    "Add the terms ai ci.",
                    "Reduce modulo M."
                ]
            },
            {
                "id": "crt_l4",
                "title": "CRT Worked Example",
                "summary": (
                    "The slides use M = 1813 = 37 x 49. "
                    "For A = 973, the residues are 11 modulo 37 and 42 modulo 49."
                ),
                "example": "973 corresponds to the pair (11, 42).",
                "steps": [
                    "Let M = 1813 = 37 x 49.",
                    "Compute 973 mod 37 = 11.",
                    "Compute 973 mod 49 = 42.",
                    "So 973 is represented by (11, 42)."
                ]
            }
        ],

        "lesson": {
            "id": "crt_l1",
            "title": "CRT Intuition",
            "summary": "CRT solves systems of congruences with pairwise coprime moduli.",
            "example": "x ≡ 2 mod 3 and x ≡ 3 mod 5 gives x ≡ 8 mod 15.",
            "steps": ["Check coprime moduli.", "Work with residues.", "Recover the value modulo M."]
        },

        "practice": [
            {
                "id": "crt_easy_1",
                "level": "easy",
                "title": "Solve x ≡ 2 mod 3 and x ≡ 3 mod 5",
                "question": "Solve the CRT system step by step.",
                "interaction": "guided_steps",
                "steps": [
                    {
                        "id": "s1",
                        "type": "input",
                        "prompt": "Step 1: List a few numbers congruent to 2 mod 3.",
                        "hint": "Start with 2 and add 3.",
                        "accepted_answers": ["2,5,8,11", "2 5 8 11", "2, 5, 8, 11"],
                        "correct_answer": "2, 5, 8, 11",
                        "explanation": "Numbers congruent to 2 mod 3 include 2, 5, 8, 11, ..."
                    },
                    {
                        "id": "s2",
                        "type": "input",
                        "prompt": "Step 2: Which of these is congruent to 3 mod 5?",
                        "hint": "Check 2, 5, 8, 11.",
                        "accepted_answers": ["8"],
                        "correct_answer": "8",
                        "explanation": "8 mod 5 = 3."
                    },
                    {
                        "id": "s3",
                        "type": "input",
                        "prompt": "Final Step: Enter the CRT solution modulo 15.",
                        "hint": "The product of the moduli is 3 x 5 = 15.",
                        "accepted_answers": ["8 mod 15", "x=8 mod 15", "x ≡ 8 mod 15", "8"],
                        "correct_answer": "x ≡ 8 mod 15",
                        "explanation": "The solution is x ≡ 8 mod 15."
                    }
                ]
            },
            {
                "id": "crt_easy_2",
                "level": "easy",
                "title": "Compute CRT residues of 973",
                "question": "Compute the residues of 973 modulo 37 and 49.",
                "interaction": "guided_steps",
                "steps": [
                    {
                        "id": "s1",
                        "type": "input",
                        "prompt": "Step 1: Compute 973 mod 37.",
                        "hint": "37 x 26 = 962.",
                        "accepted_answers": ["11"],
                        "correct_answer": "11",
                        "explanation": "973 - 962 = 11."
                    },
                    {
                        "id": "s2",
                        "type": "input",
                        "prompt": "Step 2: Compute 973 mod 49.",
                        "hint": "49 x 19 = 931.",
                        "accepted_answers": ["42"],
                        "correct_answer": "42",
                        "explanation": "973 - 931 = 42."
                    },
                    {
                        "id": "s3",
                        "type": "input",
                        "prompt": "Final Step: Enter the residue pair.",
                        "hint": "Use the format (a1, a2).",
                        "accepted_answers": ["(11,42)", "11,42", "(11, 42)"],
                        "correct_answer": "(11, 42)",
                        "explanation": "973 corresponds to the residue pair (11, 42)."
                    }
                ]
            },
            {
                "id": "crt_medium_1",
                "level": "medium",
                "title": "Choose the CRT setup",
                "question": "Set up CRT for moduli 3 and 5.",
                "interaction": "choice_steps_final",
                "steps": [
                    {
                        "id": "s1",
                        "type": "choice",
                        "prompt": "Step 1: Are 3 and 5 pairwise coprime?",
                        "options": [
                            {"id": "a", "text": "Yes"},
                            {"id": "b", "text": "No"}
                        ],
                        "correct_option_id": "a",
                        "correct_answer": "Yes",
                        "explanation": "GCD(3,5)=1, so they are pairwise coprime."
                    },
                    {
                        "id": "s2",
                        "type": "choice",
                        "prompt": "Step 2: What is M?",
                        "options": [
                            {"id": "a", "text": "8"},
                            {"id": "b", "text": "15"},
                            {"id": "c", "text": "2"},
                            {"id": "d", "text": "5"}
                        ],
                        "correct_option_id": "b",
                        "correct_answer": "15",
                        "explanation": "M = 3 x 5 = 15."
                    },
                    {
                        "id": "s3",
                        "type": "input",
                        "prompt": "Final Step: Solve x ≡ 2 mod 3 and x ≡ 3 mod 5.",
                        "hint": "Try 8.",
                        "accepted_answers": ["8", "8 mod 15", "x ≡ 8 mod 15"],
                        "correct_answer": "x ≡ 8 mod 15",
                        "explanation": "8 mod 3 = 2 and 8 mod 5 = 3."
                    }
                ]
            },
            {
                "id": "crt_medium_2",
                "level": "medium",
                "title": "Choose the residue pair",
                "question": "Represent 973 using moduli 37 and 49.",
                "interaction": "choice_steps_final",
                "steps": [
                    {
                        "id": "s1",
                        "type": "choice",
                        "prompt": "Step 1: What is 973 mod 37?",
                        "options": [
                            {"id": "a", "text": "11"},
                            {"id": "b", "text": "42"},
                            {"id": "c", "text": "37"},
                            {"id": "d", "text": "49"}
                        ],
                        "correct_option_id": "a",
                        "correct_answer": "11",
                        "explanation": "973 mod 37 = 11."
                    },
                    {
                        "id": "s2",
                        "type": "choice",
                        "prompt": "Step 2: What is 973 mod 49?",
                        "options": [
                            {"id": "a", "text": "11"},
                            {"id": "b", "text": "42"},
                            {"id": "c", "text": "37"},
                            {"id": "d", "text": "0"}
                        ],
                        "correct_option_id": "b",
                        "correct_answer": "42",
                        "explanation": "973 mod 49 = 42."
                    },
                    {
                        "id": "s3",
                        "type": "input",
                        "prompt": "Final Step: Enter the residue pair.",
                        "hint": "Use (a1, a2).",
                        "accepted_answers": ["(11,42)", "(11, 42)", "11,42"],
                        "correct_answer": "(11, 42)",
                        "explanation": "973 corresponds to (11, 42)."
                    }
                ]
            },
            {
                "id": "crt_hard_1",
                "level": "hard",
                "title": "Solve a CRT system",
                "question": "Solve x ≡ 1 mod 4 and x ≡ 2 mod 5.",
                "interaction": "final_answer",
                "steps": [
                    {
                        "id": "final",
                        "type": "input",
                        "prompt": "Enter the solution modulo 20.",
                        "hint": "Try numbers congruent to 1 mod 4.",
                        "accepted_answers": ["17", "17 mod 20", "x ≡ 17 mod 20"],
                        "correct_answer": "x ≡ 17 mod 20",
                        "explanation": "17 mod 4 = 1 and 17 mod 5 = 2."
                    }
                ]
            },
            {
                "id": "crt_hard_2",
                "level": "hard",
                "title": "Compute M1 and M2",
                "question": "For M = 1813, m1 = 37, and m2 = 49, compute M1 and M2.",
                "interaction": "final_answer",
                "steps": [
                    {
                        "id": "final",
                        "type": "input",
                        "prompt": "Enter M1 and M2.",
                        "hint": "Mi = M / mi.",
                        "accepted_answers": ["M1=49,M2=37", "m1=49,m2=37", "49,37", "M1 = 49, M2 = 37"],
                        "correct_answer": "M1 = 49, M2 = 37",
                        "explanation": "M1 = 1813/37 = 49 and M2 = 1813/49 = 37."
                    }
                ]
            }
        ],

        "quiz": [
            {
                "id": "crt_q1",
                "type": "mcq",
                "question": "CRT usually requires the moduli to be:",
                "options": [
                    {"id": "a", "text": "Pairwise coprime"},
                    {"id": "b", "text": "All equal"},
                    {"id": "c", "text": "All even"},
                    {"id": "d", "text": "Negative"}
                ],
                "correct_option_id": "a",
                "explanation": "The standard CRT requires pairwise coprime moduli."
            },
            {
                "id": "crt_q2",
                "type": "input",
                "question": "Solve x ≡ 2 mod 3 and x ≡ 3 mod 5.",
                "accepted_answers": ["8", "8 mod 15", "x ≡ 8 mod 15"],
                "correct_answer": "x ≡ 8 mod 15",
                "explanation": "8 satisfies both congruences."
            },
            {
                "id": "crt_q3",
                "type": "mcq",
                "question": "If M = m1m2...mk, CRT lets us work:",
                "options": [
                    {"id": "a", "text": "Modulo each mi separately"},
                    {"id": "b", "text": "Only with decimal numbers"},
                    {"id": "c", "text": "Without modular arithmetic"},
                    {"id": "d", "text": "Only with prime numbers less than 10"}
                ],
                "correct_option_id": "a",
                "explanation": "CRT lets us work modulo each smaller modulus separately."
            },
            {
                "id": "crt_q4",
                "type": "input",
                "question": "Compute 973 mod 37.",
                "accepted_answers": ["11"],
                "correct_answer": "11",
                "explanation": "973 = 37 x 26 + 11."
            },
            {
                "id": "crt_q5",
                "type": "input",
                "question": "Compute 973 mod 49.",
                "accepted_answers": ["42"],
                "correct_answer": "42",
                "explanation": "973 = 49 x 19 + 42."
            },
            {
                "id": "crt_q6",
                "type": "mcq",
                "question": "If M = 1813 and m1 = 37, what is M1?",
                "options": [
                    {"id": "a", "text": "49"},
                    {"id": "b", "text": "37"},
                    {"id": "c", "text": "1813"},
                    {"id": "d", "text": "11"}
                ],
                "correct_option_id": "a",
                "explanation": "M1 = M/m1 = 1813/37 = 49."
            },
            {
                "id": "crt_q7",
                "type": "input",
                "question": "Enter the residue pair for 973 modulo 37 and 49.",
                "accepted_answers": ["(11,42)", "(11, 42)", "11,42"],
                "correct_answer": "(11, 42)",
                "explanation": "973 mod 37 = 11 and 973 mod 49 = 42."
            },
            {
                "id": "crt_q8",
                "type": "mcq",
                "question": "Why is CRT useful?",
                "options": [
                    {"id": "a", "text": "It can make modular computations smaller and faster."},
                    {"id": "b", "text": "It removes all remainders."},
                    {"id": "c", "text": "It works only for fractions."},
                    {"id": "d", "text": "It avoids multiplication completely."}
                ],
                "correct_option_id": "a",
                "explanation": "Working modulo smaller numbers can be more efficient."
            },
            {
                "id": "crt_q9",
                "type": "input",
                "question": "Solve x ≡ 1 mod 4 and x ≡ 2 mod 5.",
                "accepted_answers": ["17", "17 mod 20", "x ≡ 17 mod 20"],
                "correct_answer": "x ≡ 17 mod 20",
                "explanation": "17 mod 4 = 1 and 17 mod 5 = 2."
            },
            {
                "id": "crt_q10",
                "type": "mcq",
                "question": "In CRT, Mi means:",
                "options": [
                    {"id": "a", "text": "M divided by mi"},
                    {"id": "b", "text": "M multiplied by mi"},
                    {"id": "c", "text": "Only the final answer"},
                    {"id": "d", "text": "The smallest prime"}
                ],
                "correct_option_id": "a",
                "explanation": "Mi = M / mi."
            }
        ]
    }
}