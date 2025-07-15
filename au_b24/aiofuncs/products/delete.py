from ...aioreqs import post

async def delete_product(product_id: str | int) -> bool | None:
    """Delete product by given product_id"""
    return await post("crm.product.delete", {"id": product_id})