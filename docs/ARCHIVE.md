# Archived Project Files

This document records files removed from the active IPcoll repository during the initial cleanup.

The original files are intentionally kept by the project owner in a separate local `archive` folder outside the Git repository. They are not part of the active project context, but may be useful later.

## Archived Files

| Original file | Why it was archived | Possible future use |
|---|---|---|
| `README.md` | Original version referenced many documents removed during cleanup. | Historical reference when expanding public project documentation. |
| `CHANGELOG.md` | No released implementation exists yet. | Restore when versioned releases begin. |
| `CONTRIBUTING.md` | The project currently has a single developer. | Restore if outside contributors are accepted. |
| `DOCUMENT_MANIFEST.json` | Added maintenance overhead for documentation that does not yet need a manifest. | Reconsider only if documentation grows substantially. |
| `create_structure.py` | One-time scaffolding utility; not needed for normal project operation. | Reference if the repository structure needs to be regenerated. |
| `requirements.txt` | Empty and redundant while `pyproject.toml` is intended as the Python project configuration. | Restore only if a separate requirements export becomes necessary. |
| `tree.txt` | Static tree snapshots become outdated quickly. | Historical reference to the original generated structure. |
| `docs/DATA_MODEL.md` | Detailed schema was defined before implementation. | Restore or reuse when the persistent data model is implemented. |
| `docs/DEPLOYMENT.md` | Deployment does not exist yet. | Restore during the deployment stage. |
| `docs/GITHUB_PROJECT.md` | GitHub Project board/process is unnecessary before active development. | Restore if issue/project-board management becomes useful. |
| `docs/MVP_SCOPE.md` | Considerable overlap with `docs/PROJECT.md`. | Mine for details when refining the MVP definition. |
| `docs/PROJECT_STRUCTURE.md` | Planned structure was more detailed than the current implementation requires. | Reference when the repository and FTP structure grow. |
| `docs/RISKS.md` | Separate risk register is premature at this stage. | Restore when technical discovery reveals concrete risks worth tracking. |
| `docs/SECURITY.md` | Security plan is more detailed than the current implementation. | Restore and update before secrets/external services/deployment are introduced. |
| `docs/SOURCES.md` | Reference list is not required in the active context yet. | Restore during technical discovery and integration work. |
| `docs/STACK.md` | Technology choices overlap with architecture and are not yet implemented. | Reference when selecting dependencies and finalizing the stack. |
| `docs/TESTING.md` | Detailed testing strategy precedes actual code. | Restore when implementation and automated tests begin. |
| `docs/WORKFLOW.md` | Describes an end-to-end flow that has not yet been implemented. | Restore or reuse once the pipeline is built. |
| `docs/gptchat/gptchat-project-list.md` | Large ChatGPT workflow document added significant context overhead. | Historical reference only if the previous chat organization system is needed. |
| `examples/.gitkeep` | Empty directory with no current purpose. | Recreate `examples/` when real examples exist. |
| `scripts/.gitkeep` | Empty directory with no current purpose. | Recreate `scripts/` when the project needs utility scripts. |
| `frontend/index.html` | Empty placeholder. | Create when frontend implementation begins. |
| `frontend/post.html` | Empty placeholder. | Create when frontend implementation begins. |
| `frontend/assets/app.js` | Empty placeholder. | Create when frontend implementation begins. |
| `frontend/assets/styles.css` | Empty placeholder. | Create when frontend implementation begins. |
| `frontend/data/.gitkeep` | Placeholder for data that does not yet exist. | Recreate when the frontend receives generated catalog data. |

## Important Rule

The archive is historical reference, not a second source of truth.

Active project decisions must be reflected in the files that remain in the repository. If an archived document is restored, it should first be reviewed against the current implementation and project decisions.
