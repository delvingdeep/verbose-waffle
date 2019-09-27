# Git Branching

- To view branch in a Git repository : `git branch`

- To view both remote-tracking branches and local branches : `git branch -a`

- To create and checkout a new branch
```bash
git checkout -b BRANCH_NAME
```

- To add a local branch to remote repository
```bash
git push -u origin BRANCH_NAME
```

- To delete a branch in local repository
```bash
git branch -d BRANCH_NAME
git branch -D BRANCH_NAME
```

- To delete a branch in remote repository
```bash
git push origin --delete BRANCH_NAME
```