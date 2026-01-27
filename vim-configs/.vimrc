" Plugin management
call plug#begin('~/.vim/plugged')
Plug 'davidhalter/jedi-vim'           " Python autocompletion
Plug 'vim-syntastic/syntastic'       " Syntax checking
Plug 'preservim/nerdtree'            " File explorer
Plug 'jiangmiao/auto-pairs'          " Auto-close brackets
call plug#end()

" Python-specific settings
set tabstop=4
set shiftwidth=4
set expandtab
set autoindent
set smartindent

" General settings
set number
set relativenumber
set hlsearch
set incsearch
set ignorecase
set smartcase
set showmatch
set ruler
set wildmenu

" Syntastic configuration
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_check_on_wq = 0
let g:syntastic_python_checkers = ['flake8']

" Key mappings
map <C-n> :NERDTreeToggle<CR>
