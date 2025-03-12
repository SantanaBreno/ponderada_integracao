from fastapi import HTTPException

class GoogleAPIException(HTTPException):
    def __init__(self, detail: str = "Erro na API Google Maps"):
        super().__init__(status_code=500, detail=detail)