from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from services.mikrotik import test_login
from config import (
    MIKROTIK_HOST
)


router = APIRouter()


templates = Jinja2Templates(
    directory="templates"
)



@router.get("/")
async def login_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )



@router.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):

    success = test_login(
        MIKROTIK_HOST,
        username,
        password
    )


    if success:

        request.session["user"] = username
        request.session["password"] = password


        return RedirectResponse(
            "/dashboard",
            status_code=302
        )


    return RedirectResponse(
        "/?error=1",
        status_code=302
    )

@router.get("/logout")
async def logout(request: Request):

    request.session.clear()

    return RedirectResponse(
        "/",
        status_code=302
    )