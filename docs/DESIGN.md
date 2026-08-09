# Design: DevOps SRE Assistant

**Project:** `devops-sre-assistant`  
**Parent system design:** `07-agent-runtime-containment.md`

## 1. What this POC demonstrates

Observe freely; prod mutations require approval and prefer PR/IaC over raw creds.

## 2. Architecture (POC)

```text
POST /observe → metrics
POST /act → ASK_USER on prod unless approved
```

## 3. Patterns used (and why)

| Pattern | Why used | Where in code |
|---------|----------|---------------|
| Env-scoped authorization | Prod ≠ dev. | `env=prod` gate. |
| Prefer IaC/PR | Auditable changes beat opaque apply. | `via=iac-simulated` / `prefer=open_pr`. |
| Mandatory approval | Dual control for destructive ops. | `ASK_USER`. |

## 4. Key endpoints

`GET /health`, `POST /observe`, `POST /act`

## 5. Tradeoffs / POC limits

No cloud IAM assume-role integration.

## 6. How to run

See the **Run (self-contained POC)** section in [`../README.md`](../README.md).

This folder is self-contained and can be published as its own GitHub repository.

## 7. Design walkthrough video

Narrated with **ElevenLabs Debpro voice** and Debpro still image (via [GitaProject](/Users/deb/Development/GenAI/GitaProject)):

- Video: [`video/design-overview.mp4`](./video/design-overview.mp4)
- Script: [`video/narration.txt`](./video/narration.txt)

