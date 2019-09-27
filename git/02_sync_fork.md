#### Syncing a fork
To sync a fork repository with latest commit from the parent repository follow along.

- Clone the fork repository in the terminal
```bash
git clone https://github.com/FORK_REPOSITORY_USER/FORK_REPOSITROY.git
```

- Change directory to the FORK repository. Add the upstream to the local from remote repository
```bash
git remote add upstream git://github.com/PARENT_REPOSITORY_USER/PARENT_REPOSISTORY.git 
```

- Pull upstream from `master` branch
```bash
git pull upstream master
```

- Push changes to the remote fork repsitory
```bash
git pull
```
