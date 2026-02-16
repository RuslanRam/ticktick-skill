#!/usr/bin/env python3
"""Exchange authorization code for access token.
Usage:
  python3 scripts/auth_exchange.py \
    --client-id <id> --client-secret <secret> \
    --code <auth_code> --redirect-uri <uri>
"""
import argparse, requests

parser = argparse.ArgumentParser()
parser.add_argument('--client-id', required=True)
parser.add_argument('--client-secret', required=True)
parser.add_argument('--code', required=True)
parser.add_argument('--redirect-uri', required=True)
args = parser.parse_args()

resp = requests.post('https://ticktick.com/oauth/token', data={
    'grant_type':'authorization_code',
    'code': args.code,
    'redirect_uri': args.redirect_uri,
    'client_id': args.client_id,
    'client_secret': args.client_secret,
})
print(resp.status_code)
print(resp.text)
