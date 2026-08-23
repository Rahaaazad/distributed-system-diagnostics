# Git Workflow

This project uses a branch-based workflow to keep the main branch stable and
to make changes reviewable.

## Workflow

1. Update the local main branch.
2. Create a focused feature or documentation branch.
3. Make and review the required changes.
4. Stage and commit the changes with a meaningful message.
5. Push the branch to GitHub.
6. Open and review a pull request.
7. Merge the pull request into main.
8. Update the local main branch.

## Branch Naming

- `feature/<name>` for new functionality
- `fix/<name>` for bug fixes
- `docs/<name>` for documentation
- `test/<name>` for test changes

## Commit Examples

- `feat: add heartbeat monitor`
- `fix: handle missing service response`
- `docs: describe system architecture`
- `test: add health-check unit tests`