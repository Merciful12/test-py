# tt Run and Publish

This worflow provides the following functionality for GitHub Actions users:

- Setup Python (3.x by default) environment using [setup-python](https://github.com/actions/setup-python)
- Install deps
- Run the shell command
- Push produced files to a branch (gh-pages by default)

# Usage

Provide **access-token**: [GitHub Personal Access Token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) with
  the `repo` scope. This is **required** to push the site to the repo after
  script finish. You should store this as a [secret](https://docs.github.com/en/actions/reference/encrypted-secrets#creating-encrypted-secrets) called `ACCESS_TOKEN`
  in your repository.

The worflow has two inputs:
- glossaryDefFile
- branch (the branch to publish)

**Manual Run**

[Manually running the workflow](https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow)

**Automation Run**

Change the trigger event in the next lines if it is needed
```yaml
on:
  push:
    branches: [main]
```
**Variables**

Change default input values `DEFAULT_GLOSSARY_DEF_FILE` and/or `DEFAULT_BRANCH` in the next lines if it is needed
```yaml
- name: Set variables
  env:
    DEFAULT_GLOSSARY_DEF_FILE: test
    DEFAULT_BRANCH: gh-pages
```

Change the shell command if it is needed
```yaml
- name: Run script
  run: tt glossary ${{ env.GLOSSARY_DEF_FILE }} >index.html
```
