import strawberry
from typing import List

from controller import CreateMutation, Queries
from schema import UserType, PostType, CommentType


@strawberry.type
class Mutation:
    add_user: UserType = strawberry.mutation(resolver=CreateMutation.add_user)
    add_post: PostType = strawberry.mutation(resolver=CreateMutation.add_post)
    add_comment: CommentType = strawberry.mutation(
        resolver=CreateMutation.add_comment)


@strawberry.type
class Query:
    users: List[UserType] = strawberry.field(resolver=Queries.get_all_users)
    get_single_user: UserType = strawberry.field(
        resolver=Queries.get_single_user)
