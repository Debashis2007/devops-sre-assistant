# Use Case: DevOps / SRE Assistant

**Author fingerprint:** `DBHATT-Debashis2007-SystemDesignPOC-2026` — Debashis Bhattacharjee ([@Debashis2007](https://github.com/Debashis2007))

**YouTube walkthrough:** [Devops Sre Assistant — System Design #Shorts](https://youtu.be/FeXLIlbwWjs)

**Design doc:** [docs/DESIGN.md](./docs/DESIGN.md) — architecture, patterns, and why.


**Parent system design:** [07 — Agent Runtime with Hard Containment](../07-agent-runtime-containment.md)

## Users & problem

An assistant reads metrics/logs and proposes remediations. Read paths can be wide; write/prod-destructive paths must be tightly gated.

## Requirements & SLOs

| Requirement | Target |
|-------------|--------|
| Read tools | Scoped to user’s cloud permissions |
| Write tools | Default deny; break-glass approve |
| Blast radius | Env allowlists (dev/stage/prod) |
| Audit | Immutable change log |

## Design (from parent)

```
Observe (metrics/logs) → propose change
  → policy: prod mutate => mandatory human approve
  → execute via existing IaC/CI, not raw credentials in prompt
  → verify + rollback hooks
```

## Specializations

| Concern | SRE assistant choice |
|---------|----------------------|
| Identity | Assume roles via user’s IdP groups |
| Prefer | Generate PR/plan over direct apply |
| Kill switch | Disable write tools globally |
| Eval | Dry-run mode default |

## Failure modes

- Agent “fixes” prod outage wrongly → require dual control for prod.
- Secret exfiltration in logs tool → redact; DLP on observations.
- Confused deputy → bind actions to requester identity every call.




## Design walkthrough (opens on GitHub)

> **Watch on YouTube:** [Devops Sre Assistant — System Design #Shorts](https://youtu.be/FeXLIlbwWjs)


![Design overview](docs/video/design-overview.gif)

Full narrated video (download): [docs/video/design-overview.mp4](docs/video/design-overview.mp4)

## Run (self-contained POC)

This folder is a **standalone** project (safe to split into its own GitHub repo).

```bash
cd devops-sre-assistant
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
PYTHONPATH=. python -m uvicorn app.main:app --reload --port 8000
```

```bash
curl -s http://127.0.0.1:8000/health | jq
```

curl -s -X POST http://127.0.0.1:8000/act -H 'Content-Type: application/json' -d '{"action":"restart","env":"prod","approved":false}' | jq

---

**Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.**  
Unauthorized copying or redistribution of this material is prohibited.  
GitHub: [Debashis2007](https://github.com/Debashis2007)

