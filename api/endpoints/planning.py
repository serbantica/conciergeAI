from fastapi import APIRouter

router = APIRouter()

@router.get("/planning/")
def get_planning():
    return {"message": "Planning area accessed!"}
                