from fastapi import APIRouter

router = APIRouter()

@router.get("/knowledge/")
def get_knowledge():
    return {"message": "Knowledge area accessed!"}
                