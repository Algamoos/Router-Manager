from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from services.mikrotik import get_interfaces
from config import MIKROTIK_HOST

from fastapi.responses import RedirectResponse
from services.mikrotik import change_interface_state


router = APIRouter()


templates = Jinja2Templates(
    directory="templates"
)


@router.get("/interfaces")
async def interfaces_page(
    request: Request
):

    username = request.session.get("user")
    password = request.session.get("password")


    if not username:

        return RedirectResponse(
            "/",
            status_code=302
        )


    interfaces = get_interfaces(
        MIKROTIK_HOST,
        username,
        password
    )


    return templates.TemplateResponse(
        request=request,
        name="interfaces.html",
        context={
            "interfaces": interfaces
        }
    )



@router.get("/interfaces/{interface_id}/{action}")
async def interface_action(
    request: Request,
    interface_id: str,
    action: str
):

    username = request.session.get("user")
    password = request.session.get("password")


    if not username:

        return RedirectResponse(
            "/",
            status_code=302
        )


    if action not in [
        "enable",
        "disable"
    ]:

        return RedirectResponse(
            "/interfaces",
            status_code=302
        )


    change_interface_state(
        MIKROTIK_HOST,
        username,
        password,
        interface_id,
        action
    )


    return RedirectResponse(
        "/interfaces",
        status_code=302
    )