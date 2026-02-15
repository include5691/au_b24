from ...aioreqs import post

async def get_dialog(dialog_id: int | str, limit: int | None = None) -> list[dict] | None:
    """Get dialog by given dialog_id"""
    data: dict = {"DIALOG_ID": dialog_id}
    if limit is not None:
        data["LIMIT"] = limit
    response = await post("im.dialog.messages.get", data)
    if not response or not isinstance(response, dict):
        return None
    return response

