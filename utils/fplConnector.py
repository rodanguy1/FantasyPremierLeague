import os
from fpl import FPL


async def get_connection(session):
    fpl = FPL(session)
    await fpl.login(email=os.getenv('EMAIL'), password=os.getenv('FPL_PWD'))
    return fpl
