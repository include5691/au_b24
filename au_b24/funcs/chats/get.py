from ...reqs import post

def get_dialog(dialog_id: int | str, limit: int | None = None) -> list[dict] | None:
    """Get dialog by given dialog_id

    Identifier of the dialog. Format:

        chatXXX – chat of the recipient, if the message is for chats
        XXX – identifier of the recipient, if the message is for a private dialog
    """
    data: dict = {"DIALOG_ID": dialog_id}
    if limit is not None:
        data["LIMIT"] = limit
    response = post("im.dialog.messages.get", data)
    if not response or not isinstance(response, dict):
        return None
    return response
