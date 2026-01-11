# Instructions for Agents

---   DO NOT EDIT  ---
- The main purpose of this project is to plan a trip from 2026-02-10 to 2026-02-28, especially focusing on food and sightseeing.
- All flights, trains, and accommodations have already been booked and are FINAL.

Agents MUST NOT:
- Suggest changing flights, trains, accommodations, or travel dates
- Suggest alternative hotels or rebooking transport
- Reorder cities or modify the travel route

## Flight Itinerary (Immutable)
TPE→VIE BR61
2/10 22:30 TPE
2/11 08:25 VIE
VIE→FCO OS557
2/13 17:40 VIE
2/13 19:15 FCO
MXP→TPE BR96
2/27 11:00 MXP
2/28 05:55 TPE

## Train Itinerary (Immutable)
2/19 Roma Tiburtina(10:45 → Firenze S. M. Novella(12:11)
2/22 Firenze S. M. Novella(10:20 → Venezia Mestre(12:23)
2/25 Venezia Mestre(12:00 → Milano Centrale(14:15)
--- END DO NOT EDIT---

## Agent Mission

Build and maintain a **high-quality, evidence-based food shortlist** for each city, covering:
- Restaurants
- Cafes
- Dessert shops

All recommendations must be:
- Traceable (sources linked)
- Comparable (shared scoring rubric)
- Auditable (decisions and exclusions recorded)
- Actionable (clear top picks and backups)

---

## Required Repository Structure (Per City)

Each city directory under `gourmet/` MUST contain:

- overview.md  
- inbox.md  
- candidates.md  
- top-places.md  
- excluded.md  

Agents MUST respect this structure and naming.

---

## Workflow (Must Follow)

### 1 Discovery — Candidate Collection

- Search broadly for food, coffee, and dessert places in the city.
- Record raw findings in:
  - inbox.md (unstructured, fast capture)
  - and/or candidates.md (structured list)

Minimum fields per candidate:
- name
- category (restaurant | cafe | dessert)
- area / neighborhood
- type (e.g. pasta, steak, espresso, gelato)
- google_maps_url
- status: inbox | researching | shortlisted | rejected | top

---

### 2 Evidence Collection — Per Place

For each candidate promoted to research:
- Add an evidence section for the place in `candidates.md` (keep it skimmable; link sources).
- Summarize evidence from multiple independent sources.

Required source types:
- Google Maps (rating, review count, recurring pros/cons)
- Reddit (threads/comments; summarize patterns)
- One or more reputable food or travel guides

Optional sources:
- PTT / Dcard / Chinese-language travel blogs (cite clearly if used)

Rules:
- Do NOT fabricate facts or reviews
- Clearly distinguish:
  - What sources report
  - Your synthesis or inference

---

### 3 Scoring — Standard Rubric

Each place MUST include a 50-point total score:

- Taste / Quality (0–10)
- Value (0–10)
- Convenience (0–10)
- Consistency (0–10)
- Risk (0–10; 10 = low risk)

Also record:
- reservation requirement (required | optional | none | unknown)
- best visiting time (if applicable)

---

### 4 Triage — Exclusion with Reasons

- Do NOT delete entries silently.
- Mark excluded places with:
  - status: rejected
  - a documented reason

Record exclusions in:
- excluded.md
- and/or `candidates.md` (if keeping all notes in one file)

Hard exclusion triggers:
- Strong multi-source signals of tourist traps
- Repeated hygiene or safety concerns
- Repeated severe service issues

Soft exclusion trigger:
- Total score < 30 / 50 (justification required)

---

### 5 Final Output — Top Picks

Maintain top-places.md with:
- Top Picks (high-confidence)
- Backups (good alternatives)

Each entry MUST include:
- name
- type
- area
- total score
- google maps link
- one-line justification
- constraints (reservation, queues, closed days)

---

## Documentation & Naming Rules

- `AGENTS.md` is written in English.
- Other documents in this repo MUST be primarily in Traditional Chinese (Taiwan).
- Use English for structured fields and keys
- Dates must follow ISO format (YYYY-MM-DD)
- Unknown information must be labeled as `unknown`
- Place filenames MUST follow:
  <city>-<normalized-place-name>.md

---

## Quality Bar

- Prefer fewer, higher-confidence picks
- Avoid relying on a single platform
- Preserve traceability at all times

## MCP

- You will leverage MCP tools to search for the information you need.
- Document design will consider progressive disclosure.
