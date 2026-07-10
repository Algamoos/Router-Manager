import routeros_api


def connect_mikrotik(
    host,
    username,
    password,
    port=8728
):

    connection = routeros_api.RouterOsApiPool(
        host,
        username=username,
        password=password,
        port=port,
        plaintext_login=True
    )

    api = connection.get_api()

    return connection, api



def test_login(
    host,
    username,
    password
):

    connection = None

    try:

        connection, api = connect_mikrotik(
            host,
            username,
            password
        )

        api.get_resource(
            "/system/resource"
        ).get()

        return True


    except Exception:

        return False


    finally:

        if connection:
            connection.disconnect()



def get_system_info(
    host,
    username,
    password
):

    connection = None

    try:

        connection, api = connect_mikrotik(
            host,
            username,
            password
        )


        data = api.get_resource(
            "/system/resource"
        ).get()[0]


        return data


    finally:

        if connection:
            connection.disconnect()



def get_interfaces(
    host,
    username,
    password
):

    connection = None

    try:

        connection, api = connect_mikrotik(
            host,
            username,
            password
        )


        interfaces = api.get_resource(
            "/interface"
        )


        return interfaces.get()


    finally:

        if connection:
            connection.disconnect()


def get_ip_addresses(
    host,
    username,
    password
):

    connection = None

    try:

        connection, api = connect_mikrotik(
            host,
            username,
            password
        )


        return api.get_resource(
            "/ip/address"
        ).get()


    finally:

        if connection:
            connection.disconnect()



def change_interface_state(
    host,
    username,
    password,
    interface_id,
    action
):

    connection = None

    try:

        connection, api = connect_mikrotik(
            host,
            username,
            password
        )


        interface = api.get_resource(
            "/interface"
        )


        if action == "disable":

            interface.call(
                "disable",
                {
                    ".id": interface_id
                }
            )


        elif action == "enable":

            interface.call(
                "enable",
                {
                    ".id": interface_id
                }
            )


        return True


    except Exception as e:

        print(e)

        return False


    finally:

        if connection:
            connection.disconnect()



def get_ip_addresses(
    host,
    username,
    password
):

    connection = None

    try:

        connection, api = connect_mikrotik(
            host,
            username,
            password
        )


        addresses = api.get_resource(
            "/ip/address"
        )


        return addresses.get()


    finally:

        if connection:
            connection.disconnect()



def add_ip_address(
    host,
    username,
    password,
    address,
    interface
):

    connection = None

    try:

        connection, api = connect_mikrotik(
            host,
            username,
            password
        )


        ip_resource = api.get_resource(
            "/ip/address"
        )


        ip_resource.add(
            address=address,
            interface=interface
        )


        return True


    except Exception as e:

        print(e)

        return False


    finally:

        if connection:
            connection.disconnect()



def remove_ip_address(
    host,
    username,
    password,
    address_id
):

    connection = None

    try:

        connection, api = connect_mikrotik(
            host,
            username,
            password
        )


        ip_resource = api.get_resource(
            "/ip/address"
        )


        ip_resource.call(
            "remove",
            {
                ".id": address_id
            }
        )


        return True


    except Exception as e:

        print(e)

        return False


    finally:

        if connection:
            connection.disconnect()



def get_hotspot_users(
    host,
    username,
    password
):

    connection = None

    try:

        connection, api = connect_mikrotik(
            host,
            username,
            password
        )


        users = api.get_resource(
            "/ip/hotspot/user"
        )


        return users.get()


    finally:

        if connection:
            connection.disconnect()



def add_hotspot_user(
    host,
    username,
    password,
    user_profile,
    new_password
):

    connection = None

    try:

        connection, api = connect_mikrotik(
            host,
            username,
            password
        )


        users = api.get_resource(
            "/ip/hotspot/user"
        )


        users.add(
            name=username,
            password=new_password,
            profile=user_profile
        )


        return True


    except Exception as e:

        print(e)

        return False


    finally:

        if connection:
            connection.disconnect()