import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models.user import User as UserModel
from database import db

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (graphene.relay.Node, )

class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
    
    user = graphene.Field(lambda: User)
    
    def mutate(self, info, username, password):
        user = UserModel(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return CreateUser(user=user)

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
