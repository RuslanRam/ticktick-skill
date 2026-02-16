#!/usr/bin/env python3
"""Update a task (title/content/tags/project).
Usage: TICKTICK_TOKEN=... python3 scripts/update_task.py \
  --project-id <id> --task-id <id> \
  [--title "..."] [--content "..."] [--tags tag1,tag2] [--move-to <projectId>]
"""
import os, requests, json, argparse

token=os.environ.get('TICKTICK_TOKEN')
if not token:
    raise SystemExit('TICKTICK_TOKEN env required')
parser=argparse.ArgumentParser()
parser.add_argument('--project-id', required=True)
parser.add_argument('--task-id', required=True)
parser.add_argument('--title')
parser.add_argument('--content')
parser.add_argument('--tags')
parser.add_argument('--move-to')
args=parser.parse_args()
headers={'Authorization': f'Bearer {token}'}
url=f"https://api.ticktick.com/open/v1/task/{args.task_id}"
payload={'projectId': args.project_id}
if args.title is not None:
    payload['title']=args.title
if args.content is not None:
    payload['content']=args.content
if args.tags is not None:
    payload['tags']=[t.strip() for t in args.tags.split(',') if t.strip()]
if args.move_to:
    payload['projectId']=args.move_to
resp=requests.put(url, headers=headers, json=payload)
print(resp.status_code)
print(json.dumps(resp.json(), ensure_ascii=False, indent=2))
