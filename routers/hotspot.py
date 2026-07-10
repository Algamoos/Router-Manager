from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import Form

from services.mikrotik import get_hotspot_users, add_hotspot_user
from config import MIKROTIK_HOST


router = APIRouter()


templates = Jinja2Templates(
    directory="templates"
)



@router.get("/hotspot/users")
async def hotspot_users(
    request: Request
):

    username = request.session.get("user")
    password = request.session.get("password")


    if not username:

        return RedirectResponse(
            "/",
            status_code=302
        )


    users = get_hotspot_users(
        MIKROTIK_HOST,
        username,
        password
    )


    return templates.TemplateResponse(
        request=request,
        name="hotspot_users.html",
        context={
            "users": users
        }
    )



@router.post("/hotspot/users/add")
async def create_hotspot_user(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    profile: str = Form(...)
):

    router_username = request.session.get("user")
    router_password = request.session.get("password")


    if not router_username:

        return RedirectResponse(
            "/",
            status_code=302
        )


    add_hotspot_user(
        MIKROTIK_HOST,
        router_username,
        router_password,
        profile,
        password
    )


    return RedirectResponse(
        "/hotspot/users",
        status_code=302
    )