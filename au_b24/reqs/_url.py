import os
import logging

def get_url(method: str) -> str | None:
    """
    Get url by method 
    
    `method`: rest api b24 method. Method examples: *crm.lead.get*, *user.get*
    """
    if not method or not isinstance(method, str):
        return None
    if "." not in method:
        return None
    scope: str = method.split(".")[0]
    usertoken = os.getenv(f"{scope.upper()}_USERTOKEN")
    if not usertoken:
        logging.error(f"USERTOKEN for {scope} not found")
        return None
    bitrix_id = os.getenv("BITRIX_ID")
    if not bitrix_id:
        logging.error("BITRIX_ID not found")
        return None
    return f"https://{bitrix_id}.bitrix24.ru/rest{usertoken}/{method}.json"