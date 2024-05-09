from fastapi import Depends , APIRouter
from sqlalchemy.orm import Session
from api import categorycontroller,get_db
from api import CategorySchema, CategoryCreateSchema

#Enrutador donde se definen los endpoints
router = APIRouter()
@router.get("/", response_model=list[CategorySchema])
async def read_categories(db: Session = Depends(get_db)):
    categories=categorycontroller.get_categories(db)
    return categories

@router.post("/", response_model=CategorySchema)
async def write_category(category:CategoryCreateSchema,db: Session = Depends(get_db)):
    categoryResult=categorycontroller.write_category(db,category)
    return categoryResult

@router.put("/{cat_id}", response_model=CategorySchema)
async def update_category(cat_id:int,category:CategoryCreateSchema,db: Session = Depends(get_db)):
    categoryResult = categorycontroller.update_category(db, cat_id,category)
    return categoryResult

@router.delete("/")
async def delete_category(db: Session = Depends(get_db)):
    return {"msg":"DELETE CATEGORY"}
