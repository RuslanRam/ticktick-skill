---
name: ticktick-skill
description: Integrate with TickTick to create, list, update, complete, move, and tag tasks. Use when the user asks to manage TickTick tasks (create, show, update, delete, move to list/category, add/remove tags, mark completed).
---

# TickTick Skill

## Overview

Create, read, update, complete, and organize TickTick tasks via the TickTick API. Supports moving tasks between lists/categories, adding/removing tags, and deleting tasks.

## Setup (one-time)

1) Create a TickTick developer app and get **Client ID** + **Client Secret**:
   - https://developer.ticktick.com/manage
2) Authenticate via OAuth and store tokens for API calls.
3) Save credentials in environment variables or a local `.env` file.

## Quick Start (typical requests)

- "Создай задачу в TickTick: …"
- "Покажи мои задачи из TickTick"
- "Перенеси в нужную категорию"
- "Добавь тег …"
- "Удали тег …"
- "Пометить задачу как выполненную"

## Core Tasks

### 1) Create task
- Required: title
- Optional: content/description, due date, priority, listId, tags

### 2) List tasks
- By list/category, status (active/completed), or due range

### 3) Update task
- Update title, content, due date, priority, tags, list

### 4) Complete task
- Mark task as completed (by taskId)

### 5) Move to list/category
- Update listId for the task

### 6) Tags
- Add tag / remove tag on a task

### 7) Delete task
- Remove by taskId

## References

- TickTick OpenAPI: https://developer.ticktick.com/docs#/openapi

## Notes

- This skill assumes OAuth access tokens are stored securely.
- If tokens expire, refresh via OAuth.
