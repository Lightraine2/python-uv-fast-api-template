from fastapi import APIRouter, Depends
from app.models import User
from app.auth import get_current_active_user

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    """Get current user information (protected route)."""
    return current_user


@router.get("/me/items")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    """Example protected endpoint that returns user-specific data."""
    return {
        "items": [
            {"item_id": 1, "owner": current_user.username},
            {"item_id": 2, "owner": current_user.username},
        ]
    }