from ...reqs import post

def delete_product(product_id: str | int) -> bool | None:
    """Delete product by given product_id"""
    return post("crm.product.delete", {"id": product_id})