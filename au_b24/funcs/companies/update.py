from ...reqs import post


def update_company(company_id: str | int, fields: dict) -> bool:
    """Update a company with given id and fields"""
    return bool(post("crm.company.update", {"id": company_id, "fields": fields}))
