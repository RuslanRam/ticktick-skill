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

## Install (for others)
```bash
npx skills add <owner>/<repo>@ticktick-skill
```

## Notes
- Requires TickTick OAuth tokens.
- See API docs: https://developer.ticktick.com/docs#/openapi
