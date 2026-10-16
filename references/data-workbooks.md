# Data & workbooks — durable sources, regenerated views

Read setup for destination and source of truth. Keep evidence independently auditable and views reproducible; do not use a formatted workbook as the only copy of research.

## Append-only architecture
- Maintain append-only entity, fact, run and touch tables with **stable company/entity ID**, **fact ID hash**, and **run ID**. Preserve entity IDs across renames; hash canonical entity ID + source URL/locator + fact substance, not row position. Record hash rules.
- Store source URL, publication/event/access dates, evidence class, validation verdict and source fact IDs with derived insights. Append corrections/superseding records rather than silently overwriting history; derive current state by explicit status/version rules.
- Use a project build script to regenerate views from those tables. Give raw-table append/merge and view building one serial owner; agents write isolated batch artifacts.
- Preserve manual columns by **stable ID + column name** before rebuilding. Merge them back after generation; fail visibly on duplicate IDs or conflicting values. Keep orphaned manual values for review rather than dropping them.
- Validate unique entity IDs, fact/run links, counts by entity and evidence/validation class against source tables. Record input/output counts, rejects and unmatched manual values; count equality alone does not verify fact accuracy.

## Workbook views
Create a **one-row-per-entity overview** and a **one-entity card view** selected by stable ID. For lookups use **INDEX/MATCH only**, with ranges portable across the required docs/sheets tools; avoid XLOOKUP, dynamic arrays and macros. Check the exported workbook in the required target apps when available; mark unavailable compatibility checks NOT RUN.

Keep facts/touches in their own rows; link long evidence to source records/files. Example card lookup: `=INDEX(Overview!B2:B1000,MATCH(B1,Overview!A2:A1000,0))`, where B1 is the selected entity ID. Handle missing IDs explicitly without hiding broken links.

## XLSX repair and truncation checklist
- [ ] Use table names beginning `tbl_*`; names that resemble cell references (e.g. `CRM1`) can trigger repair warnings in spreadsheet apps.
- [ ] Keep a sheet-level autofilter from overlapping a table's own filter; use the table filter for that range.
- [ ] When writing data-validation formulas through a workbook library, omit the leading `=` in the serialized formula field; a leading `=` can cause repair warnings with some writers. This differs from ordinary worksheet formulas.
- [ ] Respect the XLSX format's **32,767-character cell limit**. Split long sections into linked fact/section rows or external files; detect excess before export and never silently truncate.
- [ ] Reopen the generated workbook; inspect repair warnings, filters, validation and representative card lookups. If an app is unavailable, report that check as unverified.

## Migration to a task tracker
1. Create **one task per entity**, embedding stable entity ID. **Description = summary (first sections); comments = remaining sections in source order**, labelled with section/order and evidence IDs. Agree the summary sections for the requested document and write remaining sections as ordered comments. Split long comments into numbered parts within field limits, never truncate. Make touches subtasks where applicable. Keep the **full long document in the project folder** and link its path/version as the full source.
2. Set all available fields at creation when `exec` cannot edit later. Budget connector calls and payload limits; consult `references/tooling-limits.md`.
3. Default to **create-only, idempotent** migration: search by **name/stable ID/external ID before creating**, verify entity identity and persist external task/subtask/comment IDs plus section/part keys in an import ledger. If search or matching is unavailable/ambiguous, stop that entity rather than create duplicates. Resume only missing sections after checking recorded IDs and existing section keys; a lost response requires reconciliation, not blind recreation.
4. Leave existing descriptions/fields untouched in create-only mode. Use specifically approved edits or an authorized interactive Codex session when requested; never treat create-only as permission to duplicate/update through a different unapproved route. Report **created task/subtask/comment IDs** and reused IDs separately, with full-source links and any pending sections.
5. Read back entity ID, description, fields, subtasks and long-section comments; compare entity/touch/section counts and representative contents to source. Split import from verification if quotas require it; mark exact unchecked records and verified resume time (UNKNOWN if not established).
