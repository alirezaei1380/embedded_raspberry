import requests

from embedded_rasberry.settings import SECURITY_URL, SECURITY_ID


def send_image(thief_record):
    requests.post(SECURITY_URL + 'thief-records/', data={'raspberry': SECURITY_ID}, files={'image': thief_record.image})


def send_gas():
    requests.post(SECURITY_URL + 'smoke-records/', data={'raspberry': SECURITY_ID})


def send_motion():
    requests.post(SECURITY_URL + 'motion-records/', data={'raspberry': SECURITY_ID})
