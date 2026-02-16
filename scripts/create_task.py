#!/usr/bin/env python3
"""Create a task.
Usage: TICKTICK_TOKEN=... python3 scripts/create_task.py \
  --project-id <id> --title "Task title" [--content "..."] [--tags tag1,tag2]
"""
import os, requests, json, argparse

token=os.environ.get('TICKTICK_TOKEN')
if not token:
    raise SystemExit('TICKTICK_TOKEN env required')
parser=argparse.ArgumentParser()
parser.add_argument('--project-id', required=True)
parser.add_argument('--title', required=True)
parser.add_argument('--content', default='')
parser.add_argument('--tags', default='')
args=parser.parse_args()
headers={'Authorization': f'Bearer {token}'}
url='https://api.ticktick.com/open/v1/task'
payload={
    'projectId': args.project_id,
    'title': args.title,
    'content': args.content,
}
if args.tags:
    payload['tags']=[t.strip() for t in args.tags.split(',') if t.strip()]
resp=requests.post(url, headers=headers, json=payload)
print(resp.status_code)
print(json.dumps(resp.json(), ensure_ascii=False, indent=2))
