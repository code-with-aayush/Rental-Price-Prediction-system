# Sprint 1 — Project Planning & Foundation

**Sprint Duration:** Week 1–2
**Status:** 🟢 In Progress

---

## Sprint Goal

Establish the project scaffold, documentation, version control, and an initial notebook that can load and profile any raw dataset placed in `data/raw/`.

---

## Backlog Items

| ID | Task | Owner | Status |
|----|------|-------|--------|
| S1-01 | Define project directory structure | — | ✅ Done |
| S1-02 | Write `README.md` with problem statement, objectives, pipeline | — | ✅ Done |
| S1-03 | Write `docs/SRS.md` (Software Requirements Specification) | — | ✅ Done |
| S1-04 | Write `docs/SPRINT_1.md` (this document) | — | ✅ Done |
| S1-05 | Create `requirements.txt` with all planned dependencies | — | ✅ Done |
| S1-06 | Create `.gitignore` | — | ✅ Done |
| S1-07 | Create placeholder modules in `src/` | — | ✅ Done |
| S1-08 | Create `notebooks/01_initial_data_analysis.ipynb` | — | ✅ Done |
| S1-09 | Initialise Git repository with first commit | — | ✅ Done |
| S1-10 | Identify and download raw dataset(s) into `data/raw/` | — | ⬜ To Do |
| S1-11 | Create virtual environment and install dependencies | — | ⬜ To Do |

---

## Sprint 2 Preview

| Task |
|------|
| Data collection — scrape or download rental listings |
| Data cleaning pipeline (`src/preprocessing/`) |
| Full EDA notebook (`notebooks/02_eda.ipynb`) |
| Feature engineering module (`src/features/`) |

---

## Definition of Done

- [ ] All files listed above exist in the repository.
- [ ] `git log` shows at least one commit.
- [ ] Notebook runs without errors when no data file is present (graceful message).
- [ ] Notebook produces profiling output when a CSV is placed in `data/raw/`.
- [ ] `pip install -r requirements.txt` completes without errors.

---

## Notes

- The notebook uses **real data only** — no synthetic/fake data generation.
- Data files are excluded from Git via `.gitignore`; share via Google Drive or DVC.
