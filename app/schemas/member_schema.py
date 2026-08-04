from pydantic import BaseModel, EmailStr


class MemberCreate(BaseModel):

    name: str
    email: EmailStr
    password: str
    phone: str | None = None



class MemberResponse(BaseModel):

    user_id: int
    name: str
    email: EmailStr
    phone: str | None
    status: bool

    class Config:
        from_attributes = True



class MemberUpdate(BaseModel):

    name: str | None = None
    phone: str | None = None
    status: bool | None = None