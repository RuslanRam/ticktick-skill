#!/usr/bin/env python3
"""Complete a task.
Usage: TICKTICK_TOKEN=... python3 scripts/complete_task.py --project-id <id> --task-id <id>
"""
import os, requests, json, argparse

token=os.environ.get('TICKTICK_TOKEN')
if not token:
    raise SystemExit('TICKTICK_TOKEN env required')
parser=argparse.ArgumentParser()
parser.add_argument('--project-id', required=True)
parser.add_argument('--task-id', required=True)
args=parser.parse_args()
headers={'Authorization': f'Bearer {token}'}
url=f"https://api.ticktick.com/open/v1/project/{args.project_id}/task/{args.task_id}/complete"
resp=requests.post(url, headers=headers)
print(resp.status_code)
try:
    print(resp.json())
except Exception:
    print(resp.text)
