from fastapi import HTTPException, status


def raise_not_found_exception():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo was not found!")
