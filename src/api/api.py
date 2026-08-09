from fastapi import APIRouter

router = APIRouter(prefix="/api/v1", tags=["api"])


@router.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
