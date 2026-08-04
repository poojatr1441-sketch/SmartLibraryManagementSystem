from sqlalchemy.orm import Session

from app.models.user import User


class MemberRepository:


    @staticmethod
    def get_all_members(db: Session):

        return db.query(User).filter(
            User.role_id == 9
        ).all()



    @staticmethod
    def get_member_by_id(
        db: Session,
        user_id: int
    ):

        return db.query(User).filter(
            User.user_id == user_id,
            User.role_id == 9
        ).first()



    @staticmethod
    def create_member(
        db: Session,
        member: User
    ):

        db.add(member)
        db.commit()
        db.refresh(member)

        return member



    @staticmethod
    def update_member(
        db: Session,
        member: User
    ):

        db.commit()
        db.refresh(member)

        return member