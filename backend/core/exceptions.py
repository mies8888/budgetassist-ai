from fastapi import HTTPException

class AppError(HTTPException):
    def __init__(self, status_code: int = 400, detail: str = "Application error"):
        super().__init__(status_code=status_code, detail=detail)

# Add helper exception constructors as needed
def not_found(detail: str = "Not found"):
    return AppError(status_code=404, detail=detail)
