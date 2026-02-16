#!/usr/bin/env python3
"""List tasks in a project.
Usage: TICKTICK_TOKEN=... python3 scripts/list_tasks.py --project-id <id>
"""
import os, requests, json, argparse

token=os.environ.get('TICKTICK_TOKEN')
if not token:
    raise SystemExit('TICKTICK_TOKEN env required')
parser=argparse.ArgumentParser()
parser.add_argument('--project-id', required=True)
args=parser.parse_args()
headers={'Authorization': f'Bearer {token}'}
url=f"https://api.ticktick.com/open/v1/project/{args.project_id}/data"
resp=requests.get(url, headers=headers)
print(resp.status_code)
print(json.dumps(resp.json(), ensure_ascii=False, indent=2))
