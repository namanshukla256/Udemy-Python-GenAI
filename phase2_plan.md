# Neurologix Phase 2 Roadmap

## 1. Objectives for the Next Phase
- Onboard additional affiliates safely by scaling multi-tenant data access, governance, and observability.
- Improve end-to-end performance (LLM latency, SQL execution, Streamlit responsiveness) to support heavier clinical workloads.
- Introduce domain-specific modules that surface proactive clinical insights, workflow automation, and compliance tooling.
- Set the foundation for production-grade operations: resilience, monitoring, CI/CD, and auditability.

## 2. Current State Snapshot
- **Strengths:** Stable FastAPI/Streamlit stack, schema-aware DB access, LLM guardrails (SQL validation, Langfuse prompts), automated test suite with coverage.
- **Gaps for scale:** In-memory session history, static schema mapping, manual prompt/config management, limited offline analytics, no shared caching layer, minimal operational insights.

## 3. Feature Themes & Proposed Modules

### 3.1 Multi-Affiliate Readiness
- Implement a **schema registry service** backed by the database to store affiliate metadata (schema name, contact info, feature flags, quotas).
- Build an **Affiliate Admin module** (FastAPI endpoints + Streamlit admin panel) for onboarding, suspending, and configuring affiliates.
- Add **per-affiliate prompt sets and guardrails** stored in S3/DB with runtime caching so each affiliate can tune tone, disclaimers, and SQL constraints.
- Extend authentication/authorization (header token, API key, or IAM) with affiliate scoping and rate limits.

### 3.2 Performance & Caching Layer
- Introduce **Redis or ElastiCache** for:
  - Chat session persistence (replace in-memory deque).
  - Metadata caching (data dictionary, table schemas, prompt templates).
  - Short-lived SQL result caching for repeated physician questions with invalidation rules (TTL + cache key derived from schema + normalized query).
- Add **async job queue** (RQ/Celery) for long-running analysis, generating reports, and nightly cache warm-ups.
- Instrument query timings and cache hit ratios to drive tuning.

### 3.3 Clinical Intelligence Modules
- **Visit Summary Module:** generate structured encounter summaries (symptoms, deviations, red flags) with clinician review workflow and PDF export.
- **Trend Insights Module:** surface longitudinal metrics (reaction times, balance scores) with configurable lookback windows; leverage pre-aggregated views/materialized tables.
- **Care Plan Assistant:** provide guideline-aligned next steps, templated discharge notes, and educational content referencing affiliate-specific policies.
- Optional **Alerting Module:** trigger notifications (email/SMS/Slack) when thresholds are breached (e.g., symptom spikes, overdue follow-ups).

### 3.4 Data & Integration Enhancements
- Build **ETL connectors** (AWS DMS, Lambda, or scheduled scripts) to refresh affiliate schemas and keep a denormalized analytics store in sync.
- Create **field lineage & documentation portal** to map C3Logix fields to natural language terminology; host in Streamlit or static docs.
- Define **data quality checks** (dbt/Great Expectations) that run nightly and block stale/incorrect data before it reaches the LLM workflow.

### 3.5 Frontend & UX Investments
- Implement **multi-affiliate selection** with RBAC (users see only permitted affiliates); persist choice in session state.
- Add **conversation bookmarks**, search, and tagging for quick recall of prior answers.
- Provide **LLM transparency cues** (source tables, confidence scores, fallback reasons) and inline feedback capture to audit responses.
- Optimize Streamlit performance: lazy-load large responses, skeleton loaders, WebSocket-based streaming.

### 3.6 Observability & Operations
- Expand Langfuse usage for **trace analytics**, prompt versioning, and regression alerts when LLM behavior shifts.
- Add **structured logging** (JSON) shipped to CloudWatch/ELK, plus metrics (Prometheus/OpenTelemetry) for request volumes, errors, cache hits, DB latency.
- Configure **incident playbooks**: automated health-check dashboard, pager rules, and runbooks for schema outages or LLM degradation.
- Harden security posture: secrets manager integration, infrastructure-as-code (Terraform/CDK) for repeatable deployments, and penetration testing plan.

## 4. Delivery Plan (Indicative)
- **Phase 2A – Foundation (Weeks 1-4):**
  - Stand up Redis/cache infrastructure, refactor session history, and cache prompts/metadata.
  - Implement schema registry service, admin APIs, and automated schema validation.
  - Add observability baseline (structured logs, metrics, expanded Langfuse traces).
- **Phase 2B – Feature Expansion (Weeks 5-8):**
  - Deliver visit summary and trend insights modules with background jobs and PDF exports.
  - Launch Streamlit admin panel, RBAC, and affiliate-specific configuration flows.
  - Introduce data quality checks and start ETL pipeline for analytics views.
- **Phase 2C – Hardening & Rollout (Weeks 9-12):**
  - Stress-test caching, affiliate onboarding, and LLM workflows; add load/perf tests.
  - Finalize alerting/notification integrations and incident playbooks.
  - Conduct security review, finalize documentation, and pilot with initial new affiliates.

## 5. Technical Considerations
- **Cache invalidation:** define per-table change signals (CDC, timestamp columns) to bust cached SQL results; fall back to short TTL where change detection is unavailable.
- **Prompt management:** store prompt variants in S3/DB with hash-based versioning; preload into cache at startup with hot reload capability for updates without redeploy.
- **Job orchestration:** choose serverless (AWS Step Functions/Lambda) vs containerized worker based on existing infrastructure; ensure idempotency.
- **Testing strategy:** expand integration suite for multi-affiliate scenarios, add contract tests for new modules, and mock Redis/queue layers in unit tests.
- **Deployment pipeline:** adopt GitHub Actions (or similar) for CI/CD with environment promotion (dev → staging → prod) and automated config sync.

## 6. Risks & Open Questions
- Availability of affiliate-specific data dictionaries and whether schemas stay homogeneous.
- Requirement for PHI/PII handling may necessitate additional encryption and auditing.
- Expected real-time load (concurrent clinicians) to size cache/DB pools appropriately.
- Confirmation on notification channels and integrations (existing provider systems, EHR hooks, etc.).
- Decision on hosting model (AWS-managed vs on-prem) affects cache/queue technology choices.

---
**Next Steps:** validate priorities with stakeholders, size engineering effort, and align on infrastructure budget (Redis, job queue, observability tooling). Once approved, translate roadmap items into user stories and update the project backlog.
