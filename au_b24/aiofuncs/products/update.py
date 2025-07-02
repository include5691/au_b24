from ...aioreqs import post

async def update_product(product_id: int, fields: dict) -> bool:
    """Update a product with given id and fields"""
    return bool(await post("crm.product.update", {"id": product_id, "fields": fields}))