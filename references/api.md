# TickTick API Notes

Docs: https://developer.ticktick.com/docs#/openapi
App management: https://developer.ticktick.com/manage

## OAuth
- Create app to get Client ID / Client Secret
- Use OAuth flow to obtain access/refresh tokens
- Store tokens securely (env or local file)

## Common operations
- Create task
- List tasks
- Update task (move list, update tags, etc.)
- Complete task
- Delete task

(See OpenAPI docs for exact endpoints, payloads, and scopes.)
