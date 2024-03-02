#!/usr/bin/env python3

from inventree.api import InvenTreeAPI
import os

token = os.getenv("INVENTREE_API")
server = os.getenv("INVENTREE_SERVER")
api = InvenTreeAPI(server, token=token)

print(api.server_details)

