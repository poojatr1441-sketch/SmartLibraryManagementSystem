from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.user import User
from app.repositories.member_repository import MemberRepository
from app.schemas.member_schema import MemberCreate, MemberUpdate


class MemberService:


    @staticmethod
    def get_all_members(db: Session):

        return MemberRepository.get_all_members(db)



    @staticmethod
    def get_member_by_id(
        db: Session,
        user_id: int
    ):

        member = MemberRepository.get_member_by_id(
            db,
            user_id
        )

        if not member:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Member not found"
            )

        return member



    @staticmethod
    def create_member(
        db: Session,
        member_request: MemberCreate
    ):

        member = User(
            name=member_request.name,
            email=member_request.email,
            password=member_request.password,
            phone=member_request.phone,
            role_id=9
        )

        return MemberRepository.create_member(
            db,
            member
        )



    @staticmethod
    def update_member(
        db: Session,
        user_id: int,
        member_request: MemberUpdate
    ):

        member = MemberRepository.get_member_by_id(
            db,
            user_id
        )

        if not member:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Member not found"
            )


        if member_request.name:
            member.name = member_request.name

        if member_request.phone:
            member.phone = member_request.phone

        if member_request.status is not None:
            member.status = member_request.status


        return MemberRepository.update_member(
            db,
            member
        )