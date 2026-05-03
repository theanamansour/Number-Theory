import json
from app.db import get_connection


def save_history_entry(user_id: int, operation: str, input_data: dict, result_data: dict):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO history (user_id, operation, input_data, result_data)
        VALUES (%s, %s, %s, %s)
        """,
        (
            user_id,
            operation,
            json.dumps(input_data),
            json.dumps(result_data)
        )
    )

    conn.commit()

    cursor.close()
    conn.close()


def get_user_history(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, operation, input_data, result_data, created_at
        FROM history
        WHERE user_id = %s
        ORDER BY created_at DESC, id DESC
        """,
        (user_id,)
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    history = []

    for row in rows:
        history.append({
            "id": row["id"],
            "operation": row["operation"],
            "input_data": json.loads(row["input_data"]),
            "result_data": json.loads(row["result_data"]),
            "created_at": row["created_at"]
        })

    return history

def clear_user_calculation_history(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM history WHERE user_id = %s",
        (user_id,)
    )

    conn.commit()
    deleted_count = cursor.rowcount
    conn.close()

    return deleted_count