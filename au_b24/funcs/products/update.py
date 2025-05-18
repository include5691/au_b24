from ...reqs import post

def update_product(product_id: int, fields: dict) -> bool:
    """Update a product with given id and fields"""
    return bool(post("crm.product.update", {"id": product_id, "fields": fields}))