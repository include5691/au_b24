from ...aioreqs import post

async def add_dialog_message(
    dialog_id: int | str,
    message: str,
    system: bool | str | None = None,
    attach: dict | list | None = None,
    url_preview: bool | str | None = None,
    keyboard: dict | None = None,
    menu: dict | None = None,
) -> int | None:
    """Send message to dialog"""
    data: dict = {"DIALOG_ID": dialog_id, "MESSAGE": message}
    if system is not None:
        data["SYSTEM"] = "Y" if system is True else "N" if system is False else system
    if attach is not None:
        data["ATTACH"] = attach
    if url_preview is not None:
        data["URL_PREVIEW"] = "Y" if url_preview is True else "N" if url_preview is False else url_preview
    if keyboard is not None:
        data["KEYBOARD"] = keyboard
    if menu is not None:
        data["MENU"] = menu
    result = await post("im.message.add", data)
    if not result or not isinstance(result, int):
        return None
    return result
