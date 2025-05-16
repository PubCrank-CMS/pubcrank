---
title: Installing Tmux plugins on Ubuntu
date: 2023-08-14 00:00:00 -0600
categories:
  - tmux
  - terminal
  - command line
  - cli
cover: /img/Tmux.png
---

I learned about Tmux plugins this weekend and they are pretty awesome! However, I didn't find the correct instructions for setting them up quickly in Ubuntu. Most of the directions I found centered around installing manaully from Github. Below I listed the instructions for Ubuntu/Debian installation.

See the [list of plugins on Github](https://github.com/tmux-plugins/list).

### Installation

```
sudo apt install tmux-plugin-manager

echo "run '/usr/share/tmux-plugin-manager/tpm'" >> ~/.tmux.conf

# exit and start tmux again
```

### Installing plugins

1. Add new plugin to `~/.tmux.conf` with `set -g @plugin '...'`
    - Example: `set -g @plugin 'tmux-plugins/tmux-yank'`
2. Press `ctrl-b (or prefix)` + <kbd>I</kbd> (capital i, as in **I**nstall) to fetch the plugin.

You're good to go! The plugin was cloned to `~/.tmux/plugins/` dir and sourced.

### Uninstalling plugins

1. Remove (or comment out) plugin from the list.
2. Press `prefix` + <kbd>alt</kbd> + <kbd>u</kbd> (lowercase u as in **u**ninstall) to remove the plugin.

All the plugins are installed to `~/.tmux/plugins/` so alternatively you can
find plugin directory there and remove it.

### More Docs

For more docs on plugins see [TPM - Tmux Plugin Manager](https://github.com/tmux-plugins/tpm).
