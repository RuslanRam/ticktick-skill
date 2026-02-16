# TickTick Skill (OpenClaw)

Integrate with TickTick to **create, list, update, complete, move, and tag tasks**.

## Setup: create TickTick API keys
1. Go to the developer console: https://developer.ticktick.com/manage
2. Create an application.
3. Copy **Client ID** and **Client Secret**.
4. Complete OAuth to obtain access/refresh tokens.

## Typical commands
- "Создай задачу в TickTick: …"
- "Покажи мои задачи из TickTick"
- "Перенеси в нужную категорию"
- "Добавь тег …"
- "Удали тег …"
- "Пометить задачу как выполненную"

## Scripts
Set token:
```bash
export TICKTICK_TOKEN="<access_token>"
```

List projects:
```bash
python3 scripts/list_projects.py
```

List tasks in project:
```bash
python3 scripts/list_tasks.py --project-id <id>
```

Create task:
```bash
python3 scripts/create_task.py --project-id <id> --title "Task title" --content "..." --tags tag1,tag2
```

Update/move task:
```bash
python3 scripts/update_task.py --project-id <id> --task-id <id> --move-to <projectId>
```

Complete task:
```bash
python3 scripts/complete_task.py --project-id <id> --task-id <id>
```

Delete task:
```bash
python3 scripts/delete_task.py --project-id <id> --task-id <id>
```

## Install
```bash
npx skills add RuslanRam/ticktick-skill@ticktick-skill
```

## Notes
- Requires TickTick OAuth tokens.
- See API docs: https://developer.ticktick.com/docs#/openapi
