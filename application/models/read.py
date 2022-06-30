from models import entity
from sqlalchemy import func, desc

def get_organizations():
    columns = [
        entity.Organizations.name,
        entity.Organizations.designation,
        entity.Organizations.is_current_org,
        func.to_char(
            func.to_timestamp(entity.Organizations.join_date), "Mon, YYYY"
            ),
        func.to_char(
            func.to_timestamp(entity.Organizations.exit_date), "Mon, YYYY"
            ),
        ]
    organizations = entity.Organizations.query.with_entities(*columns)\
                                        .order_by(desc(entity.Organizations.join_date))\
                                        .all()
    return organizations