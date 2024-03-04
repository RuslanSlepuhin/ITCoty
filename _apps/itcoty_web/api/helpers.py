from django.db.models import QuerySet


def add_numeration_to_response(query: list[QuerySet]) -> dict:
    result = {}
    for n in range(len(query)):
        result[str(n)] = query[n]

    return result
