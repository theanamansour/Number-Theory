from app.db import get_connection
from app.data.education_content import EDUCATION_TOPICS


def normalize_answer(answer: str) -> str:
    return (
        str(answer)
        .lower()
        .replace(" ", "")
        .replace("×", "*")
        .replace("≡", "=")
        .strip()
    )


def get_all_topics():
    return [
        {
            "id": topic["id"],
            "title": topic["title"],
            "description": topic["description"]
        }
        for topic in EDUCATION_TOPICS.values()
    ]


def get_topic(topic_id: str):
    topic = EDUCATION_TOPICS.get(topic_id)
    if not topic:
        raise ValueError("Topic not found.")
    return topic


def get_lesson(topic_id: str):
    topic = get_topic(topic_id)
    return {
        "id": topic["id"],
        "title": topic["title"],
        "description": topic["description"],
        "lesson": topic["lesson"]
    }


def get_practice(topic_id: str):
    topic = get_topic(topic_id)
    return {
        "topic_id": topic["id"],
        "topic_title": topic["title"],
        "practice": [
            {
                "id": item["id"],
                "question": item["question"],
                "hint": item["hint"]
            }
            for item in topic["practice"]
        ]
    }


def check_practice_answer(topic_id: str, exercise_id: str, answer: str):
    topic = get_topic(topic_id)

    exercise = next(
        (item for item in topic["practice"] if item["id"] == exercise_id),
        None
    )

    if not exercise:
        raise ValueError("Practice exercise not found.")

    user_answer = normalize_answer(answer)
    accepted_answers = [
        normalize_answer(correct_answer)
        for correct_answer in exercise["accepted_answers"]
    ]

    is_correct = user_answer in accepted_answers

    return {
        "topic_id": topic_id,
        "exercise_id": exercise_id,
        "is_correct": is_correct,
        "message": "Correct answer!" if is_correct else "Not quite. Review the explanation and try again.",
        "correct_answer": exercise["solution"],
        "steps": exercise["steps"]
    }


def get_quiz(topic_id: str):
    topic = get_topic(topic_id)

    return {
        "topic_id": topic["id"],
        "topic_title": topic["title"],
        "questions": [
            {
                "id": question["id"],
                "question": question["question"],
                "options": question["options"]
            }
            for question in topic["quiz"]
        ]
    }


def check_quiz_answers(topic_id: str, answers: list[dict]):
    topic = get_topic(topic_id)
    questions = topic["quiz"]

    answer_map = {
        answer["question_id"]: answer["selected_option_id"]
        for answer in answers
    }

    results = []
    score = 0

    for question in questions:
        selected = answer_map.get(question["id"])
        is_correct = selected == question["correct_option_id"]

        if is_correct:
            score += 1

        results.append({
            "question_id": question["id"],
            "selected_option_id": selected,
            "correct_option_id": question["correct_option_id"],
            "is_correct": is_correct,
            "explanation": question["explanation"]
        })

    return {
        "topic_id": topic_id,
        "score": score,
        "total": len(questions),
        "percentage": round((score / len(questions)) * 100, 2) if questions else 0,
        "results": results
    }


def save_education_attempt(
    user_id,
    mode: str,
    topic_id: str,
    item_id: str,
    user_answer: str,
    is_correct: bool,
    score=None,
    total=None
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO education_attempts
        (user_id, mode, topic_id, item_id, user_answer, is_correct, score, total)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        user_id,
        mode,
        topic_id,
        item_id,
        user_answer,
        1 if is_correct else 0,
        score,
        total
    ))

    conn.commit()
    conn.close()


def get_user_education_progress(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, mode, topic_id, item_id, user_answer, is_correct, score, total, created_at
        FROM education_attempts
        WHERE user_id = ?
        ORDER BY created_at DESC, id DESC
    """, (user_id,))

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row["id"],
            "mode": row["mode"],
            "topic_id": row["topic_id"],
            "item_id": row["item_id"],
            "user_answer": row["user_answer"],
            "is_correct": bool(row["is_correct"]),
            "score": row["score"],
            "total": row["total"],
            "created_at": row["created_at"]
        }
        for row in rows
    ]