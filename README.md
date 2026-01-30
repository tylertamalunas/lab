# Lab Repository

Personal development environment, configurations, and learning projects.

## Quick Setup

Clone this repository:
```bash
git clone https://github.com/tylertamalunas/lab.git ~/lab
```

## Contents

### 🚀 Neovim Configuration (`nvim-config/`)

Complete Neovim setup based on NvChad with custom plugins including precognition.nvim for motion hints.

**Install:**
```bash
# Backup existing config
mv ~/.config/nvim ~/.config/nvim.backup

# Install configuration
cp -r ~/lab/nvim-config ~/.config/nvim

# Start Neovim (plugins auto-install)
nvim
```

### 🐍 Python Learning (`pythonStuff/`)

Python scripts and exercises including:
- Basic syntax and concepts (loops, conditionals, functions)
- Data structures (lists, dictionaries, collections)
- File interaction and utilities
- **100 Days of Code** challenge projects
  

### 🐳 Docker Examples (`dockerStuff/`)

Collection of Dockerfiles and containerization examples:
- Basic container setups (Python, Node.js)
- Multi-stage builds and optimization
- Port configuration and networking
- Stateful applications and logging
- Volume mounting examples

### ⚙️ Vim Configuration (`vim-configs/`)

Traditional Vim setup with plugins and custom `.vimrc` configuration.

### ☸️ Kubernetes Resources (`kubernetesStuff/`)

Kubernetes manifests and configuration files for container orchestration.

## Usage

Each directory contains specific tools and configurations for different development environments. See individual README files in subdirectories for detailed setup instructions.

## Repository Structure

```
lab/
├── nvim-config/          # Modern Neovim setup
├── vim-configs/          # Traditional Vim setup  
├── pythonStuff/          # Python learning and projects
├── dockerStuff/          # Docker examples and configs
├── kubernetesStuff/      # Kubernetes manifests
└── test.yaml            # Test configuration file
```
