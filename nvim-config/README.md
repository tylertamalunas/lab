# My Neovim Configuration

Personal Neovim setup based on NvChad with custom plugins and configurations.

## Installation

1. Backup existing config:
   ```bash
   mv ~/.config/nvim ~/.config/nvim.backup
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/tylertamalunas/lab.git ~/.config/nvim
   ```

3. Start Neovim and let lazy.nvim install plugins:
   ```bash
   nvim
   ```

## Plugins Added

- precognition.nvim - Motion hints for better Vim navigation

## Features

- LSP support with Mason
- Autocompletion with nvim-cmp
- File explorer with nvim-tree
- Fuzzy finding with Telescope
- Git integration with Gitsigns
- Syntax highlighting with Treesitter
- And more from NvChad base configuration
