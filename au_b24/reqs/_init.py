pause_ = 0 # pause for bitrix24 rate lims

def init_requests_pause(pause: float = 0) -> None:
    """
    Init requests
    
    :param pause: float, default 0, pause for bitrix24 rate lims
    """
    global pause_
    pause_ = pause

def get_pause() -> float:
    """
    Get requests pause
    
    :return: float, pause for bitrix24 rate lims
    """
    return pause_