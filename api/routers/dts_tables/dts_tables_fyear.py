from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.models.models import User
from api.crud.user_operations import UserOperations
from api.crud.dts_table_operations import DTSTableOperations
from api.user_dependencies import init_db

router = APIRouter()


@router.get("/")
def dts_table_fyear(table_name: str, fiscal_year: str,
                    db: Session = Depends(init_db)):
    """Filter data by fiscal year"""
    # userOps = UserOperations(db)
    # current_user: User = userOps.get_current_active_user()
    # if current_user:
    #     dts_table_operations = DTSTableOperations(db)
    #     data = dts_table_operations.get_data_using_fyear(table_name, fiscal_year)
    #     return data
    # return None
    dts_table_operations = DTSTableOperations(db)
    data = dts_table_operations.get_data_using_fyear(table_name, fiscal_year)
    return data
