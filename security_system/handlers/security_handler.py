import requests

from embedded_rasberry.settings import SECURITY_URL, SECURITY_ID


def send_image(thief_record):
    requests.post(SECURITY_URL + 'thief-records/', data={'raspberry': SECURITY_ID}, files={'image': thief_record.image})


def send_gas(smoke_record):
    requests.post(SECURITY_URL + 'smoke-records/', data={'smoke': smoke_record.smoke, 'methan': smoke_record.methan, 'lpg': smoke_record.lpg, 'hydrogen': smoke_record.hydrogen, 'raspberry': SECURITY_ID})
