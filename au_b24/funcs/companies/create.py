from ...reqs import post


def create_company(fields: dict) -> int | None:
    """
    Create a company with given fields
    Accepts phone in "PHONE": [{"VALUE": "555888", "VALUE_TYPE": "WORK"}] format
    """
    return post("crm.company.add", {"fields": fields})
