from typing import Union
from fastapi import FastAPI
from fastapi import status

from github_data.infrastructure.routes.users import github__router

# FastAPI app
app = FastAPI()

# Routing registration
app.include_router(github__router)

# Exception handlers registration
#app.add_exception_handler(ValidationError, custom_validation_error_handler)
#app.add_exception_handler(RequestValidationError, custom_request_validation_error_handler)
#app.add_exception_handler(HTTPException, custom_not_authorized_exception_handler)
#app.add_exception_handler(NotImplementedError, custom_not_implemented_exception_handler)
#app.add_exception_handler(Exception, custom_internal_exception_error_handler)


# Main API endpoint
@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    summary="Main server",
    tags=["Main"]
)
def main():
    '''
    **Name:** Main Endpoint

    **Return:** JSON with message
    '''
    return {
        "server": "The server is already initialized!"
    }