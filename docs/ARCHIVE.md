# Archived Project Files

This document records files removed from the active IPcoll repository during the initial cleanup.

The original files are intentionally kept by the project owner in a separate local `archive` folder outside the Git repository. They are not part of the active project context, but may be useful later.

## Archived Files

| Original file | Why it was archived | Possible future use |
|---|---|---|
| Original `README.md` | The original version referenced many documents removed during cleanup. | Historical reference when expanding public project documentation. |
| `CHANGELOG.md` | No versioned release exists yet. | Restore when versioned releases begin. |
| `CONTRIBUTING.md` | The project currently has a single developer. | Restore if outside contributors are accepted. |
| `DOCUMENT_MANIFEST.json` | Added maintenance overhead for documentation that does not need a manifest. | Reconsider only if documentation grows substantially. |
| `create_structure.py` | One-time scaffolding utility; not needed for normal project operation. | Historical reference if repository scaffolding is revisited. |
| `requirements.txt` | Redundant because `pyproject.toml` is now the dependency source of truth. | Restore only if an exported requirements file becomes necessary for a specific deployment tool. |
| `tree.txt` | Static tree snapshots become outdated quickly. | Historical reference to the original generated structure. |
| `docs/DATA_MODEL.md` | Detailed schema was defined before implementation. | Reuse selectively while defining the normalized metadata model. |
| `docs/DEPLOYMENT.md` | Deployment does not exist yet. | Restore during the deployment stage if a separate guide becomes useful. |
| `docs/GITHUB_PROJECT.md` | A formal GitHub Project board is unnecessary at the current stage. | Restore if project-board management becomes useful. |
| `docs/MVP_SCOPE.md` | Considerable overlap with `docs/PROJECT.md`. | Mine for details when refining the MVP definition. |
| `docs/PROJECT_STRUCTURE.md` | Planned structure was more detailed than the current implementation requires. | Reference only if repository or server structure grows. |
| `docs/RISKS.md` | A separate risk register was premature during repository setup. | Restore only if concrete risks grow beyond what current documents can handle clearly. |
| `docs/SECURITY.md` | A separate security plan was premature before external integrations. | Reconsider before deployment if security requirements no longer fit existing documentation. |
| `docs/SOURCES.md` | A separate source-reference document was unnecessary during initial cleanup. | Restore only if source/API references become substantial enough to justify it. |
| `docs/STACK.md` | Technology choices overlap with architecture and decisions. | Reconsider only if the implemented stack becomes complex enough to need a dedicated document. |
| `docs/TESTING.md` | A standalone testing strategy was premature before code existed. Testing rules now live in `INSTRUCTIONS.md`, while executable configuration lives in `pyproject.toml` and tests live under `tests/`. | Restore only if testing strategy becomes complex enough to require separate documentation. |
| `docs/WORKFLOW.md` | The end-to-end flow had not yet been implemented. | Restore or reuse once the real pipeline differs enough from `ARCHITECTURE.md` to justify a separate operating document. |
| `docs/gptchat/gptchat-project-list.md` | Large ChatGPT workflow document added significant context overhead. | Historical reference only if the previous chat organization system is needed. |
| `examples/.gitkeep` | Empty directory with no current purpose. | Recreate `examples/` when real examples exist. |
| `scripts/.gitkeep` | Empty directory with no current purpose. | Recreate `scripts/` when the project needs committed utility scripts. |
| `frontend/index.html` | Empty placeholder. | Create when frontend implementation begins. |
| `frontend/post.html` | Empty placeholder. | Create when frontend implementation begins. |
| `frontend/assets/app.js` | Empty placeholder. | Create when frontend implementation begins. |
| `frontend/assets/styles.css` | Empty placeholder. | Create when frontend implementation begins. |
| `frontend/data/.gitkeep` | Placeholder for data that does not yet exist. | Recreate when the frontend receives generated catalog data. |

## Important Rule

The archive is historical reference, not a second source of truth.

Active project decisions must be reflected in files that remain in the repository. If an archived document is restored, it must first be reviewed against the current implementation and accepted project decisions.
