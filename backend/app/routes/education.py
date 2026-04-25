from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.dependencies import get_current_user_optional, get_current_user_required
from app.services.education import (
    get_all_topics,
    get_lesson,
    get_practice,
    check_practice_answer,
    get_quiz,
    check_quiz_answers,
    save_education_attempt,
    get_user_education_progress
)

router = APIRouter()


class PracticeCheckRequest(BaseModel):
    topic_id: str
    exercise_id: str
    answer: str

    def validate_input(self):
        if not self.topic_id.strip():
            raise ValueError("Topic is required.")
        if not self.exercise_id.strip():
            raise ValueError("Exercise is required.")
        if not self.answer.strip():
            raise ValueError("Answer cannot be empty.")


class QuizAnswer(BaseModel):
    question_id: str
    selected_option_id: str


class QuizCheckRequest(BaseModel):
    topic_id: str
    answers: list[QuizAnswer]

    def validate_input(self):
        if not self.topic_id.strip():
            raise ValueError("Topic is required.")
        if len(self.answers) == 0:
            raise ValueError("At least one quiz answer is required.")


@router.get("/topics")
def topics():
    return {
        "topics": get_all_topics()
    }


@router.get("/topics/{topic_id}")
def lesson(topic_id: str):
    try:
        return get_lesson(topic_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/practice/{topic_id}")
def practice(topic_id: str):
    try:
        return get_practice(topic_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/practice/check")
def check_practice(
    request: PracticeCheckRequest,
    current_user=Depends(get_current_user_optional)
):
    try:
        request.validate_input()

        result = check_practice_answer(
            request.topic_id,
            request.exercise_id,
            request.answer
        )

        if current_user:
            save_education_attempt(
                user_id=current_user["id"],
                mode="practice",
                topic_id=request.topic_id,
                item_id=request.exercise_id,
                user_answer=request.answer,
                is_correct=result["is_correct"]
            )

        return result

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/quiz/{topic_id}")
def quiz(topic_id: str):
    try:
        return get_quiz(topic_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/quiz/check")
def check_quiz(
    request: QuizCheckRequest,
    current_user=Depends(get_current_user_optional)
):
    try:
        request.validate_input()

        answers_as_dicts = [
            {
                "question_id": answer.question_id,
                "selected_option_id": answer.selected_option_id
            }
            for answer in request.answers
        ]

        result = check_quiz_answers(request.topic_id, answers_as_dicts)

        if current_user:
            save_education_attempt(
                user_id=current_user["id"],
                mode="quiz",
                topic_id=request.topic_id,
                item_id=None,
                user_answer=str(answers_as_dicts),
                is_correct=result["score"] == result["total"],
                score=result["score"],
                total=result["total"]
            )

        return result

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/progress/me")
def my_education_progress(current_user=Depends(get_current_user_required)):
    return {
        "user": current_user,
        "progress": get_user_education_progress(current_user["id"])
    }