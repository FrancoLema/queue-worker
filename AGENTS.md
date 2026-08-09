# queue-worker

Project-specific instructions for AI agents working on this repository.

---

## Purpose

**queue-worker** has a single responsibility: consume messages from RabbitMQ queues and forward them to a worker for processing.

Each component has a clearly defined responsibility. Consumers only connect to RabbitMQ, read messages, and delegate processing to a worker. The worker performs the required processing.

Both the consumers and the worker live in this application.

---

## Initial Version Scope

The first version is intentionally limited:

- **One queue per client** — each client gets its own RabbitMQ queue.
- **One shared worker** — all clients send messages to the same worker for processing.
- **Simple structure** — keep the codebase flat and minimal; avoid premature abstractions, extra layers, or features outside this scope.

Do not add multi-worker routing, complex orchestration, or per-client processing logic unless explicitly requested.

---

## Architecture

- Separate RabbitMQ consumption from worker invocation.
- Keep business logic independent from infrastructure.
- Keep configuration explicit and easy to follow.
- Prefer small, focused modules over a layered architecture in this initial version.
- Prefer composition over inheritance; depend on abstractions when useful.
- Reuse existing components before creating new ones.
- Do not introduce new patterns, layers, or abstractions unless they solve a clear need.

---

## Agent Behavior

How the AI agent should work in this repository.

### Scope and minimalism

- Implement **only** what was explicitly requested — the minimum indispensable to solve the task.
- Do not add extra features, anticipate future requirements, or solve unrelated problems.
- Avoid overengineering: no premature abstractions, unnecessary layers, or speculative designs.
- If you spot a possible improvement outside scope, mention it separately instead of implementing it.

### Before writing code

- Understand the request fully before implementing.
- Identify ambiguities, missing information, and assumptions.
- Never invent business rules. If something is unclear, ask before assuming.

### Code changes

- Keep changes as small as possible. Modify only the files required.
- Do not touch unrelated code, perform large rewrites, or refactor opportunistically.
- Assume existing code has a reason to exist. Do not rewrite working implementations or rename symbols for preference.
- Preserve existing behavior unless explicitly requested.
- Do not add dependencies unless they provide clear, justified value.

### Decisions and communication

- Never hide important decisions. Explain trade-offs before implementing choices that affect architecture, maintainability, performance, or security.
- When multiple valid solutions exist, explain the options, recommend one, and say why.
- Prefer the simplest correct solution. Minimize diff size. Prefer explicitness over cleverness.
- If you are unsure, stop, explain the uncertainty, and ask.

## Engineering Standards

### General

- Prioritize correctness, simplicity, and maintainability over cleverness.
- Follow existing project conventions and naming.
- Keep implementations focused on a single responsibility (SOLID, KISS, DRY, YAGNI).

### Python

- Follow PEP 8.
- Use type hints on all function parameters and return values.
- Prefer Pydantic models or dataclasses over unstructured dictionaries.
- Raise explicit exceptions instead of returning ambiguous values.
- Use context managers for resources. Avoid global mutable state and mutable default arguments.

### Error Handling

- Validate external inputs (messages, configuration, environment).
- Fail explicitly. Never swallow exceptions without justification.
- Provide meaningful error messages without exposing sensitive data in logs.

### Security

- Never hardcode secrets or credentials.
- Validate and sanitize all external input.
- Apply the principle of least privilege.

### Testing

- Every new behavior should be testable.
- Test behavior, not implementation details.
- Keep tests deterministic, simple, and isolated.
- Cover edge cases and error scenarios.
- Mock only external dependencies (RabbitMQ, HTTP calls, etc.).

### Documentation

- Explain non-obvious decisions in code or docs when needed.
- Keep `readme.md` up to date when behavior changes.
- Avoid comments that restate what the code already says.

---

## Out of Scope

Unless explicitly requested, do not implement:

- Message transformation or enrichment beyond what is needed to forward to the worker
- Retry policies, dead-letter handling, or advanced queue topologies
- Per-client workers or dynamic worker selection
- API endpoints beyond what is required to run or manage consumers

---

## Definition of Done

Before considering a task complete, verify that:

- The implementation satisfies the requested requirements.
- No unrelated behavior was modified.
- The solution is consistent with the existing codebase.
- The code is readable and maintainable.
- Appropriate tests have been added or updated.

---

## Related Documentation

- Setup and usage: `readme.md`
