# Copyright (c) 2026 Debashis Bhattacharjee. All Rights Reserved.
# Unauthorized copying, modification, or distribution is prohibited.
# https://github.com/Debashis2007

"""DevOps SRE Assistant — thin self-contained FastAPI POC."""

from __future__ import annotations

from typing import Optional

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

from poc_core import MockLLM, TokenBucket, health_payload
from poc_core.safety import SafetyPlane
from poc_core.stores import InMemoryStore, MockVectorIndex

USE_CASE = "DevOps SRE Assistant"
app = FastAPI(title=USE_CASE)
llm = MockLLM()
store = InMemoryStore()
safety = SafetyPlane()

@app.get("/health")
def health():
    return health_payload(USE_CASE)


class ActIn(BaseModel):
    action: str
    env: str = "dev"
    approved: bool = False

@app.post("/observe")
def observe():
    return {"cpu": 0.82, "error_rate": 0.03, "hint": "elevated errors"}

@app.post("/act")
def act(body: ActIn):
    if body.env == "prod" and not body.approved:
        return {"status": "ASK_USER", "reason": "prod_mutate_requires_approval", "prefer": "open_pr"}
    return {"status": "applied", "action": body.action, "env": body.env, "via": "iac-simulated"}
