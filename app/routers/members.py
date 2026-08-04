from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.member_schema import (
    MemberCreate,
    MemberResponse,
    MemberUpdate
)
from app.services.member_service import MemberService


router = APIRouter(
    prefix="/members",
    tags=["Members"]
)



@router.get(
    "",
    response_model=list[MemberResponse]
)
def get_members(
    db: Session = Depends(get_db)
):

    return MemberService.get_all_members(db)



@router.get(
    "/{user_id}",
    response_model=MemberResponse
)
def get_member(
    user_id: int,
    db: Session = Depends(get_db)
):

    return MemberService.get_member_by_id(
        db,
        user_id
    )



@router.post(
    "",
    response_model=MemberResponse
)
def create_member(
    member: MemberCreate,
    db: Session = Depends(get_db)
):

    return MemberService.create_member(
        db,
        member
    )



@router.put(
    "/{user_id}",
    response_model=MemberResponse
)
def update_member(
    user_id: int,
    member: MemberUpdate,
    db: Session = Depends(get_db)
):

    return MemberService.update_member(
        db,
        user_id,
        member
    )