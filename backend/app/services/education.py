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

    lessons = topic.get("lessons")

    if not lessons:
        lessons = [topic["lesson"]]

    return {
        "id": topic["id"],
        "title": topic["title"],
        "description": topic["description"],
        "lesson": lessons[0],
        "lessons": lessons
    }

def get_practice(topic_id: str):
    topic = get_topic(topic_id)

    return {
        "topic_id": topic["id"],
        "topic_title": topic["title"],
        "practice": [
            {
                "id": item["id"],
                "level": item.get("level", "easy"),
                "title": item.get("title", item["question"]),
                "question": item["question"],
                "interaction": item.get("interaction", "guided_steps"),
                "steps": [
                    {
                        "id": step["id"],
                        "type": step.get("type", "input"),
                        "prompt": step["prompt"],
                        "hint": step.get("hint", ""),
                        "options": step.get("options", [])
                    }
                    for step in item["steps"]
                ]
            }
            for item in topic["practice"]
        ]
    }

def check_practice_answer(topic_id: str, exercise_id: str, step_id: str, answer: str):
    topic = get_topic(topic_id)

    exercise = next(
        (item for item in topic["practice"] if item["id"] == exercise_id),
        None
    )

    if not exercise:
        raise ValueError("Practice exercise not found.")

    steps = exercise["steps"]

    step_index = next(
        (index for index, item in enumerate(steps) if item["id"] == step_id),
        None
    )

    if step_index is None:
        raise ValueError("Practice step not found.")

    step = steps[step_index]
    step_type = step.get("type", "input")

    if step_type == "choice":
        is_correct = answer == step["correct_option_id"]
    else:
        user_answer = normalize_answer(answer)
        accepted_answers = [
            normalize_answer(correct_answer)
            for correct_answer in step.get("accepted_answers", [])
        ]
        is_correct = user_answer in accepted_answers

    is_final_step = step_index == len(steps) - 1

    return {
        "topic_id": topic_id,
        "exercise_id": exercise_id,
        "step_id": step_id,
        "is_correct": is_correct,
        "is_final_step": is_final_step,
        "message": (
            "Correct! Move to the next step."
            if is_correct and not is_final_step
            else "Correct! Problem completed."
            if is_correct and is_final_step
            else "Not quite. Try again or reveal the answer."
        ),
        "correct_answer": step["correct_answer"],
        "explanation": step["explanation"]
    }



def get_quiz(topic_id: str):
    topic = get_topic(topic_id)

    questions = []

    for question in topic["quiz"]:
        safe_question = {
            "id": question["id"],
            "type": question.get("type", "mcq"),
            "question": question["question"]
        }

        if question.get("type", "mcq") == "mcq":
            safe_question["options"] = question["options"]

        questions.append(safe_question)

    return {
        "topic_id": topic["id"],
        "topic_title": topic["title"],
        "questions": questions
    }

def check_quiz_answers(topic_id: str, answers: list[dict]):
    topic = get_topic(topic_id)
    questions = topic["quiz"]

    answer_map = {
        answer["question_id"]: answer
        for answer in answers
    }

    results = []
    score = 0

    for question in questions:
        question_id = question["id"]
        question_type = question.get("type", "mcq")
        user_answer_data = answer_map.get(question_id, {})

        if question_type == "mcq":
            selected = user_answer_data.get("selected_option_id")
            is_correct = selected == question["correct_option_id"]

            result = {
                "question_id": question_id,
                "type": "mcq",
                "selected_option_id": selected,
                "correct_option_id": question["correct_option_id"],
                "is_correct": is_correct,
                "explanation": question["explanation"]
            }

        else:
            user_answer = user_answer_data.get("answer", "")
            normalized_user_answer = normalize_answer(user_answer)

            accepted_answers = [
                normalize_answer(correct_answer)
                for correct_answer in question.get("accepted_answers", [])
            ]

            is_correct = normalized_user_answer in accepted_answers

            result = {
                "question_id": question_id,
                "type": "input",
                "user_answer": user_answer,
                "correct_answer": question["correct_answer"],
                "is_correct": is_correct,
                "explanation": question["explanation"]
            }

        if is_correct:
            score += 1

        results.append(result)

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

def complete_lesson(user_id: int, topic_id: str, lesson_id: str):
    topic = get_topic(topic_id)

    lessons = topic.get("lessons", [topic["lesson"]])

    lesson_exists = any(lesson["id"] == lesson_id for lesson in lessons)

    if not lesson_exists:
        raise ValueError("Lesson not found.")

    save_education_attempt(
        user_id=user_id,
        mode="lesson",
        topic_id=topic_id,
        item_id=lesson_id,
        user_answer="completed",
        is_correct=True
    )

    return {
        "topic_id": topic_id,
        "lesson_id": lesson_id,
        "completed": True,
        "message": "Lesson completed."
    }


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