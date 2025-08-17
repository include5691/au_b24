import os


class BitrixContext:

    def __init__(self, bitrix_id: str, **bitrix_tokens: dict):
        bitrix_data = bitrix_tokens.copy()
        bitrix_data["BITRIX_ID"] = bitrix_id
        self.bitrix_data = bitrix_data
        self._old_data = {}

    def __enter__(self):
        self._old_data = {k: os.getenv(k) for k in self.bitrix_data.keys()}
        for k, v in self.bitrix_data.items():
            os.environ[k] = v
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        for k, v in self._old_data.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
