from fastapi import APIRouter, status
from car_api.db import USERS
from car_api.schemas.users import (
    UserListPublicSchema,
    UserSchema,
    UserPublicSchema
)


router = APIRouter ()

@router.post(
        path="/",
        status_code=status.HTTP_201_CREATED,
        response_model=UserPublicSchema
)
async def create_user(user:UserSchema):
    user_with_id = UserPublicSchema(**user.model_dump(), id=len(USERS) + 1)
    USERS.append(user_with_id)
    return user_with_id

@router.get(
        path="/",
        status_code=status.HTTP_200_OK,
        response_model=UserListPublicSchema)
async def list_user():
    return {
        'users': [
            {
                'id':1,
                'username': 'pycode',
                'email': 'pycode@email.com',
            },
            {
                'id':2,
                'username': 'joao',
                'email': 'joao@email.com',
            },
            {
                'id':3,
                'username': 'maria',
                'email': 'maria@email.com',
            }
        ]
    }