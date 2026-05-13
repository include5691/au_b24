import shlex
import json as json_module
from urllib.parse import urlencode

def build_curl(method: str, url: str, headers: dict | None = None, json: dict | None = None, params: dict | None = None) -> str:
    """Build a curl command string from request parts"""
    if params:
        sep = "&" if "?" in url else "?"
        url = f"{url}{sep}{urlencode(params, doseq=True)}"
    parts = ["curl", "-X", method.upper()]
    effective_headers = dict(headers or {})
    if json is not None and "Content-Type" not in effective_headers and "content-type" not in effective_headers:
        effective_headers["Content-Type"] = "application/json"
    for name, value in effective_headers.items():
        if name.lower() == "accept-encoding":
            continue
        parts.extend(["-H", f"{name}: {value}"])
    if json is not None:
        body = json_module.dumps(json, ensure_ascii=False)
        parts.extend(["--data-raw", body])
    parts.append(url)
    return " ".join(shlex.quote(str(p)) for p in parts)
