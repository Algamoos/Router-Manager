from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from services.mikrotik import get_system_info
from config import MIKROTIK_HOST

from services.mikrotik import (
    get_system_info,
    get_interfaces,
    get_ip_addresses
)

router = APIRouter()


templates = Jinja2Templates(
    directory="templates"
)



@router.get("/dashboard")
async def dashboard(
    request: Request
):

    username = request.session.get("user")
    password = request.session.get("password")


    if not username:

        return RedirectResponse(
            "/",
            status_code=302
        )


    system = get_system_info(
        MIKROTIK_HOST,
        username,
        password
    )

    interfaces = get_interfaces(
    MIKROTIK_HOST,
    username,
    password
    )

    addresses = get_ip_addresses(
        MIKROTIK_HOST,
        username,
        password
        )


    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "username": username,
            "system": system,
            "interfaces": interfaces,
            "addresses": addresses
        }
    )