import os


PROD = os.getenv("PROD")

if PROD and PROD=="true":
    PROD=True
else:
    PROD = False

if PROD:
    from config_.prod import *
else:
    from config_.dev import *