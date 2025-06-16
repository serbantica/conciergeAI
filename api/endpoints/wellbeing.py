from fastapi import APIRouter

router = APIRouter()

@router.get("/wellbeing/")
def get_wellbeing():
    return {"message": "Wellbeing area accessed!"}
                