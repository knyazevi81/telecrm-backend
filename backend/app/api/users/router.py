from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.service.session import (
    get_session_with_commit,
    get_session_without_commit
)

from app.api.users.dependencies import get_ip_address

router = APIRouter(
    tags=["users"]
)

@router.get("/users/me",response_model=None)
async def read_current_user(
    ip_address: str = Depends(get_ip_address),
    session: AsyncSession = Depends(get_session_with_commit)
):
    return {"ip_address": ip_address}
