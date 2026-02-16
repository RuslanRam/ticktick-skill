#!/usr/bin/env python3
"""List TickTick projects.
Usage: TICKTICK_TOKEN=... python3 scripts/list_projects.py
"""
import os, requests, json

token=os.environ.get('TICKTICK_TOKEN')
if not token:
    raise SystemExit('TICKTICK_TOKEN env required')

headers={'Authorization': f'Bearer {token}'}
resp=requests.get('https://api.ticktick.com/open/v1/project', headers=headers)
print(resp.status_code)
print(json.dumps(resp.json(), ensure_ascii=False, indent=2))
