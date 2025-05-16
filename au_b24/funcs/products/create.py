from typing import Literal
from ...reqs import post

def create_product(name: str, fields: dict | None = None) -> int | None:
    """
    Create a new product with the given fields.
    """
    fields = fields or {}
    fields["NAME"] = name
    return post("crm.product.add", {"fields": fields})