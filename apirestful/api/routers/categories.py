from fastapi import Depends , APIRouter
from sqlalchemy.orm import Session
from api import categorycontroller,get_db
from api import CategorySchema

#Enrutador donde se definen los endpoints
router = APIRouter()
@router.get("/", response_model=list[CategorySchema])
async def read_categories(db: Session = Depends(get_db)):
    categories=categorycontroller.get_categories(db)
    return categories

@router.post("/")
async def write_category(db: Session = Depends(get_db)):
    return {"msg":"POST CATEGORY"}

@router.put("/")
async def update_category(db: Session = Depends(get_db)):
    return {"msg":"PUT CATEGORY"}

@router.delete("/")
async def delete_category(db: Session = Depends(get_db)):
    return {"msg":"DELETE CATEGORY"}
