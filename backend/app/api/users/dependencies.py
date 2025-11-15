from fastapi import Request

async def get_ip_address(
    request: Request
) -> str:
    ip_address = request.headers.get("X-Real-IP")
    return ip_address