from fastapi import Request


class HeadersCache:
    def __init__(self):
        self.headers_cache = {}

    def get_headers(self, request: Request):
        key = request.client.host
        headers = self.headers_cache.get(key, {})
        if not headers.get("cookie"):
            headers["cookie"] = request.headers.get("cookie") or ""
            headers["user-agent"] = request.headers.get("user-agent") or ""
            self.headers_cache[key] = headers
        return headers
