#!/usr/bin/env python3

from inventree.api import InvenTreeAPI

import os

from prestashop.client import Client


token = os.getenv("INVENTREE_API")
server = os.getenv("INVENTREE_SERVER")
api = InvenTreeAPI(server, token=token)
from invantree.part import part
from prestashop.client import Client
import yaml

pstoken = os.getenv("PS_TOKEN")
psserver = os.getenv("PS_SERVER")
client = Client(pstoken,psserver)




