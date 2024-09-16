import graphene
from graphene_django import DjangoObjectType
from banks.models import Bank, Branch

class BankType(DjangoObjectType):
    class Meta:
        model = Bank

class BranchType(DjangoObjectType):
    class Meta:
        model = Branch

class Query(graphene.ObjectType):
    all_banks = graphene.List(BankType)
    all_branches = graphene.List(BranchType, limit = graphene.Int())
    
    branch_by_ifsc = graphene.Field(BranchType, ifsc=graphene.String(required=True))

    def resolve_all_banks(self, info):
        return Bank.objects.all()

    def resolve_all_branches(self, info, limit=None):
        return Branch.objects.select_related('bank')[:limit]

    def resolve_branch_by_ifsc(self, info, ifsc):
        return Branch.objects.get(ifsc=ifsc)

class CreateBranch(graphene.Mutation):
    class Arguments:
        bank_id = graphene.Int(required=True)
        ifsc = graphene.String(required=True)
        branch = graphene.String(required=True)
        address = graphene.String(required=True)
        city = graphene.String(required=True)
        district = graphene.String(required=True)
        state = graphene.String(required=True)

    branch = graphene.Field(BranchType)

    def mutate(self, info, bank_id, ifsc, branch, address, city, district, state):
        bank = Bank.objects.get(id=bank_id)
        branch_obj = Branch(
            bank=bank,
            ifsc=ifsc,
            branch=branch,
            address=address,
            city=city,
            district=district,
            state=state
        )
        branch_obj.save()
        return CreateBranch(branch=branch_obj)

class Mutation(graphene.ObjectType):
    create_branch = CreateBranch.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)