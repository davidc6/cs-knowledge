# Vim

## Modes

- `Normal` - default / edit mode (no data is edited in normal mode)
- `Visual` - highlight text, perform an action (cut, paste, delete etc.)
- `Insert` - edit mode to insert new data into a document

## Shortcuts / commands

- `dd` - Delete a line
- `wq` / `ZZ` - Write and quit (save changes and quit). Adding `!` forces the command.
- `!` - force an action, no warnings.
- `x` - delete current character
- `Ctrl + r` - redo
- `dw` - delete a word
- `ea` - append at end of word
- `G + A` - append at the end of file
- `d0` - delete from cursor to end of line

### Editing in insert mode

- `<C-w>` - when in insert mode allows to delete one word back
- `<C-u>` - delete back to start line (whatever has been entered)
- `<C-o>` - insert normal mode

## Moving around

- `0` - go to beginning of line
- `^` or `_` - go to first non-whitespace char in the line
- `Shift + i` - go to beginning of line and drop into `INSERT` mode
- `$` - go to end of line
- `g_` - go to last non-whitespace char
- `Shift + a` (capital a) - go to end of line and append
- `Shift + g` (capital g) - go to end of file
- `gg` - go to start of file
- ??? jump to next blank line
- `<C-o>` - jump to the previous location in the jump list
- `<C-i>` - jump to the next location in the jump list
- `%` - jump to the matching parenthesis

## Actions

- (Normal) `dd` - delete whole line
- (Normal) `ddp` - deletes line and pastes from the register (swap)
- (Normal) `:m 0` - move current line to top
- (Normal) `:m $` - move current line to bottom
- (Visual) select a line up and down
- `y` - yank / copy data (to copy paste inside same vim session you will need to open a file inside vim `:e/ [file]`)
- `p` - paste data
- `d` - delete
- `:%/s/<what-to-find>/<what-to-replace>` - across all lines
- `ctlr + d` - shift left (tabs the whole line)
- `ctrl + t` - shift right (tabs the whole line)
- `o` or `O` - insert new empty line
- `ge` - back to end of word
- `ctrl + Q` - unfreeze program
- `V` - select the current line in one key stroke
- `gqG` - format text to fit the current screen width limit
- `ctlz + Z` - to switch to shell, suspends Vim and send process in the
  background. `jobs -l` to view jobs running in the background. `fg
  <process_num>` to bring job to the foreground - Ref:
  http://xahlee.info/linux/linux_job_control.html
- 

## Visual mode

- `shift + >>` - shift left (visual mode)
- `shift + <<` - shift right
- Fast scroll?

## Macros

- `qa` starts recording macro to buffer a (second letter is the buffer location)
- `@a` replay macro a 

## Frequent

- (Normal) `u` - undo previous action
- `<C-r>` - redo

## Modes

- Normal - for editor commands (move around the file, etc.)

## To reearch

- Vim buffers
- Vim tabs

## Ref

- https://www.shell-tips.com/linux/vi-vs-vim/n
- Avoid the escape key - https://vim.fandom.com/wiki/Avoid_the_escape_key
- Copy, cut and paste - https://vim.fandom.com/wiki/Copy,_cut_and_paste
- Undo and Redo - https://vim.fandom.com/wiki/Undo_and_Redo
- Graphical cheatsheet - https://stackoverflow.com/questions/4488979/how-to-move-one-word-left-in-the-vi-editor
- (Moving blazingly fast with the core VIM motions)(https://www.barbarianmeetscoding.com/boost-your-coding-fu-with-vscode-and-vim/moving-blazingly-fast-with-the-core-vim-motions/)
