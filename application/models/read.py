from models import entity

def get_organizations():
    return entity.Organizations.query.all()