from fastapi import APIRouter

router = APIRouter()

@router.get("/nutrition/")
def get_nutrition():
    return {"message": "Nutrition area accessed!"}
                