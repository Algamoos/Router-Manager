from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from services.mikrotik import (
    get_ip_addresses,
    get_interfaces,
    add_ip_address,
    remove_ip_address
)

from config import MIKROTIK_HOST


router = APIRouter()


templates = Jinja2Templates(
    directory="templates"
)



@router.get("/ip-address")
async def ip_address_page(
    request: Request
):

    username = request.session.get("user")
    password = request.session.get("password")


    if not username:

        return RedirectResponse(
            "/",
            status_code=302
        )


    addresses = get_ip_addresses(
        MIKROTIK_HOST,
        username,
        password
    )


    interfaces = get_interfaces(
        MIKROTIK_HOST,
        username,
        password
    )


    return templates.TemplateResponse(
        request=request,
        name="ip_address.html",
        context={
            "addresses": addresses,
            "interfaces": interfaces
        }
    )



@router.post("/ip-address/add")
async def add_ip(
    request: Request,
    address: str = Form(...),
    interface: str = Form(...)
):

    username = request.session.get("user")
    password = request.session.get("password")


    if not username:

        return RedirectResponse(
            "/",
            status_code=302
        )


    add_ip_address(
        MIKROTIK_HOST,
        username,
        password,
        address,
        interface
    )


    return RedirectResponse(
        "/ip-address",
        status_code=302
    )


@router.get("/ip-address/delete/{address_id}")
async def delete_ip(
    request: Request,
    address_id: str
):

    username = request.session.get("user")
    password = request.session.get("password")


    if not username:

        return RedirectResponse(
            "/",
            status_code=302
        )


    remove_ip_address(
        MIKROTIK_HOST,
        username,
        password,
        address_id
    )


    return RedirectResponse(
        "/ip-address",
        status_code=302
    )