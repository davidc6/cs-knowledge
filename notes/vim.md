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

## Moving around

- `0` - go to beginning of line
- `Shift + i` - go to beginning of line and drop into `INSERT` mode
- `$` - go to end of line
- `Shift + a` (capital a) - go to end of line and append
- `Shift + g` (capital g) - go to end of file
- `gg` - go to start of file
- ??? jump to next blank line

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

## Visual mode

- `shift + >>` - shift left (visual mode)
- `shift + <<` - shift right
- Fast scroll?

## Frequent

- (Normal) `u` - undo previous action

## Modes

- Normal - for editor commands (move around the file, etc.)

## Ref

- https://www.shell-tips.com/linux/vi-vs-vim/n
- Avoid the escape key - https://vim.fandom.com/wiki/Avoid_the_escape_key
- Copy, cut and paste - https://vim.fandom.com/wiki/Copy,_cut_and_paste
- Undo and Redo - https://vim.fandom.com/wiki/Undo_and_Redo
- Graphical cheatsheet - https://stackoverflow.com/questions/4488979/how-to-move-one-word-left-in-the-vi-editor
