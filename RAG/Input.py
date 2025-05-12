class Init_Input:
    def __init__(self, use_query : str = None, top_k : int = None) -> None:
        self.use_query : str = use_query
        self.top_k : int = top_k