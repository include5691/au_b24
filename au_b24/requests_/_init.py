pause_ = 0 # pause for bitrix24 rate lims

def init_requests(pause: float = 0) -> None:
    """
    Init requests
    
    ``pause``: float, default 0, pause for bitrix24 rate lims
    """
    global pause_
    pause_ = pause