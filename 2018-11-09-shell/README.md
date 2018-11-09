# highlights from customizing bash

- The PS1 environment variable sets your prompt
  and can include things like the current directory,
  git branch, time, etc.
  My PS1:

  ```bash
  \[\]\u\[\033[0;31m\][\A]\[\]\w \[\033[0;32m\]$(_git_branch_paren)\[\]$
  ```

  which produces:

  ```
  minrk[20:02]~/dev/simula/tools-meetup (master) $
  ```

- aliases are simple shortcuts for common commands, e.g.

  ```
  alias b="git checkout --branch"
  alias clone="git clone --recursive"
  ```

- functions allow you to have more logic.

- completion is super useful. Check out a package called `bash_completion`
  and see if your favorite programs have completion snippets to add
  to your bashrc file or completion.d directory.

- [hub](https://hub.github.com) is a handy wrapper around git
  to make it github-aware (it adds commands like 'fork' and 'pull-request').
- [autojump](https://github.com/wting/autojump)
  is a handy tool that defines `j` a command to quickly
  change to common directories.
  autojump remembers which directories you visit most often,
  and lets you do things like `j fenics` to change
  to your most-visited directory with a name *similar to* fenics
  from anywhere.

My personal favorite aliases and functions that I use:

```bash
# psg shows all processes matching a pattern
psg () {
    ps aux | grep -e "$@" | grep -v "grep -e $@"
}

# mp makes sure I am on master and up-to-date
alias mp='git checkout master && git pull'
# fork creates a fork on github and adds it as a remote called `mine`
alias fork='hub fork && hub remote add -p mine $(hub config --get github.user)'
# pr opens a pull request from my current branch
alias pr='git push mine && hub pull-request'
# nb starts the notebook
alias nb='jupyter notebook'
```

`awk` is a super powerful program for parsing text,
but I *always* use it to pick a single item out of columnar output like `ps`,
which looks like:

```bash
ps ax | grep notebook | awk '{print $1}'
```

to get the pid of processes matching `notebook`.
So I made an alias and a function to make
these common actions:

```bash
alias awk1="awk '{print \$1}'"
function awkn {
  n="$1"
  shift
  awk "{print \$$n}" "$@"
}
```

So now I can do `| awk1` or `| awkn 3` to get the first or third item.
