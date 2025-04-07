from ...reqs import post

def get_deal_categories() -> dict[int, str] | None:
    "Get deals categories in `id: name` format"
    response = post("crm.category.list", {"entityTypeId": 2})
    if not response or not isinstance(response, dict):
        return
    categories = response.get("categories")
    if not categories or not isinstance(categories, list):
        return
    result = {}
    for category in categories:
        if not category or not isinstance(category, dict):
            continue
        category_id = category.get("id")
        if not category_id or not isinstance(category_id, int):
            continue
        category_name = category.get("name")
        if not category_name or not isinstance(category_name, str):
            continue
        result[str(category_id)] = category_name
    return result