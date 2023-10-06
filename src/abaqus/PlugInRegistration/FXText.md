Multiline text widget

![](https://help.3ds.com/2023/English/DSSIMULIA_Established/SIMACAERefImages/gui-fxtext.png)

### FXText(p, tgt=None, sel=0, opts=0, x=0, y=0, w=0, h=0)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Construct multi-line text widget.

| **Argument** | **Type** | **Default** | **Description** |
| p | FXComposite |   |   |
| tgt | FXObject | None |   |
| sel | Int | 0 |   |
| opts | Int | 0 |   |
| x | Int | 0 |   |
| y | Int | 0 |   |
| w | Int | 0 |   |
| h | Int | 0 |   |

### appendText(text, n, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Append n characters of text at the end of the buffer.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   |   |
| n | Int |   |   |
| notify | Bool | False |   |

### canFocus()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Returns True because a text widget can receive focus.

Reimplemented from FXWindow.

### create()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Create server-side resources.

Reimplemented from FXComposite.

### detach()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Detach server-side resources.

Reimplemented from FXComposite.

### disable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Disable the text widget.

Reimplemented from FXWindow.

### enable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Enable the text widget.

Reimplemented from FXWindow.

### getBarColor()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return bar color.

### getBarColumns()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return number of columns used for line numbers.

### getChar(pos)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get character at position in text buffer.

| **Argument** | **Type** | **Default** | **Description** |
| pos | Int |   |   |

### getContentHeight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get default height.

Reimplemented from FXScrollArea.

### getContentWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Get default width.

Reimplemented from FXScrollArea.

### getCursorCol()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return cursor row, i.e. indent position.

### getCursorColor()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return cursor color.

### getCursorPos()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return the cursor position.

### getCursorRow()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return cursor row.

### getDefaultHeight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return default height.

Reimplemented from FXScrollArea.

### getDefaultWidth()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return default width.

Reimplemented from FXScrollArea.

### getFont()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return text font.

### getLength()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return length of buffer.

### getMarginBottom()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return bottom margin.

### getMarginLeft()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return left margin.

### getMarginRight()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return right margin.

### getMarginTop()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return top margin.

### getNumberColor()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return line number color.

### getPosAt(x, y)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return text position at given visible x,y coordinate.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int |   |   |
| y | Int |   |   |

### getSelBackColor()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return selected background color.

### getSelEndPos()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return selendpos.

### getSelStartPos()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return selstartpos.

### getSelTextColor()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return selected text color.

### getText()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return text in the widget.

### getText(text, n)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Retrieve text into buffer.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   |   |
| n | Int |   |   |

### getTextColor()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return text color.

### getTopLine()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return position of top line.

### getVisCols()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return number of visible columns.

### getVisRows()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return number of visible rows.

### insertText(pos, text, n, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Insert n characters of text at position pos into the buffer.

| **Argument** | **Type** | **Default** | **Description** |
| pos | Int |   |   |
| text | String |   |   |
| n | Int |   |   |
| notify | Bool | False |   |

### isEditable()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if text is editable.

### isModified()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if text was modified.

### isPosSelected(pos)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return True if position pos is selected.

| **Argument** | **Type** | **Default** | **Description** |
| pos | Int |   |   |

### killSelection(notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Unselect the text.

| **Argument** | **Type** | **Default** | **Description** |
| notify | Bool | False |   |

### lineEnd(pos)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return position of end of line containing position pos.

| **Argument** | **Type** | **Default** | **Description** |
| pos | Int |   |   |

### lineStart(pos)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return position of begin of line containing position pos.

| **Argument** | **Type** | **Default** | **Description** |
| pos | Int |   |   |

### makePositionVisible(pos)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Scroll text to make the given position visible.

| **Argument** | **Type** | **Default** | **Description** |
| pos | Int |   |   |

### moveContents(x, y)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Scroll the contents.

Reimplemented from FXScrollArea.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int |   |   |
| y | Int |   |   |

### nextLine(pos, nl=1)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return start of next line.

| **Argument** | **Type** | **Default** | **Description** |
| pos | Int |   |   |
| nl | Int | 1 |   |

### nextRow(pos, nr=1)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return start of next row.

| **Argument** | **Type** | **Default** | **Description** |
| pos | Int |   |   |
| nr | Int | 1 |   |

### position(x, y, w, h)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Move and resize this window in the parent's coordinates.

Reimplemented from FXWindow.

| **Argument** | **Type** | **Default** | **Description** |
| x | Int |   |   |
| y | Int |   |   |
| w | Int |   |   |
| h | Int |   |   |

### prevLine(pos, nl=1)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return start of previous line.

| **Argument** | **Type** | **Default** | **Description** |
| pos | Int |   |   |
| nl | Int | 1 |   |

### prevRow(pos, nr=1)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return start of previous row.

| **Argument** | **Type** | **Default** | **Description** |
| pos | Int |   |   |
| nr | Int | 1 |   |

### recalc()  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Need to recalculate size.

Reimplemented from FXWindow.

### removeText(pos, n, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Remove n characters of text at position pos from the buffer.

| **Argument** | **Type** | **Default** | **Description** |
| pos | Int |   |   |
| n | Int |   |   |
| notify | Bool | False |   |

### replaceText(pos, m, text, n, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Replace m characters at pos by n characters.

| **Argument** | **Type** | **Default** | **Description** |
| pos | Int |   |   |
| m | Int |   |   |
| text | String |   |   |
| n | Int |   |   |
| notify | Bool | False |   |

### resize(w, h)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Resize this window to the specified width and height.

Reimplemented from FXWindow.

| **Argument** | **Type** | **Default** | **Description** |
| w | Int |   |   |
| h | Int |   |   |

### rowEnd(pos)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return row end.

| **Argument** | **Type** | **Default** | **Description** |
| pos | Int |   |   |

### rowStart(pos)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Return row start.

| **Argument** | **Type** | **Default** | **Description** |
| pos | Int |   |   |

### setBarColor(clr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change bar color.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor |   |   |

### setBarColumns(cols)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change number of columns used for line numbers.

| **Argument** | **Type** | **Default** | **Description** |
| cols | Int |   |   |

### setBottomLine(pos)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Make line containing pos the bottom line.

| **Argument** | **Type** | **Default** | **Description** |
| pos | Int |   |   |

### setCursorCol(col, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set cursor column.

| **Argument** | **Type** | **Default** | **Description** |
| col | Int |   |   |
| notify | Bool | False |   |

### setCursorColor(clr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change cursor color.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor |   |   |

### setCursorPos(pos, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set the cursor position.

| **Argument** | **Type** | **Default** | **Description** |
| pos | Int |   |   |
| notify | Bool | False |   |

### setCursorRow(row, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set cursor row.

| **Argument** | **Type** | **Default** | **Description** |
| row | Int |   |   |
| notify | Bool | False |   |

### setEditable(edit=True)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set editable flag.

| **Argument** | **Type** | **Default** | **Description** |
| edit | Bool | True |   |

### setFont(fnt)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change text font.

| **Argument** | **Type** | **Default** | **Description** |
| fnt | FXFont |   |   |

### setMarginBottom(pb)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change bottom margin.

| **Argument** | **Type** | **Default** | **Description** |
| pb | Int |   |   |

### setMarginLeft(pl)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change left margin.

| **Argument** | **Type** | **Default** | **Description** |
| pl | Int |   |   |

### setMarginRight(pr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change right margin.

| **Argument** | **Type** | **Default** | **Description** |
| pr | Int |   |   |

### setMarginTop(pt)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change top margin.

| **Argument** | **Type** | **Default** | **Description** |
| pt | Int |   |   |

### setModified(mod=True)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Set modified flag.

| **Argument** | **Type** | **Default** | **Description** |
| mod | Bool | True |   |

### setNumberColor(clr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change line number color.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor |   |   |

### setSelBackColor(clr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change selected background color.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor |   |   |

### setSelection(pos, len, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Select len characters starting at given position pos.

| **Argument** | **Type** | **Default** | **Description** |
| pos | Int |   |   |
| len | Int |   |   |
| notify | Bool | False |   |

### setSelTextColor(clr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change selected text color.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor |   |   |

### setText(text, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change the text.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   |   |
| notify | Bool | False |   |

### setText(text, n, notify=False)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change the text in the buffer to new text.

| **Argument** | **Type** | **Default** | **Description** |
| text | String |   |   |
| n | Int |   |   |
| notify | Bool | False |   |

### setTextColor(clr)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change text color.

| **Argument** | **Type** | **Default** | **Description** |
| clr | FXColor |   |   |

### setTopLine(pos)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Make line containing pos the top line.

| **Argument** | **Type** | **Default** | **Description** |
| pos | Int |   |   |

### setVisCols(cols)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change number of visible columns.

| **Argument** | **Type** | **Default** | **Description** |
| cols | Int |   |   |

### setVisRows(rows)  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)

Change number of visible rows.

| **Argument** | **Type** | **Default** | **Description** |
| rows | Int |   |   |

### Global flags  
![](https://help.3ds.com/2023/English/DSSIMULIA_Established/IconsReference/butix_top_wline.png)


**Text widget options**

| **TEXT_READONLY** | 

Text is NOT editable.

 |
| **TEXT_WORDWRAP** | 

Wrap at word breaks.

 |
| **TEXT_OVERSTRIKE** | 

Overstrike mode.

 |
| **TEXT_FIXEDWRAP** | 

Fixed wrap columns.

 |
| **TEXT\_NO\_TABS** | 

Insert spaces for tabs.

 |
| **TEXT_AUTOINDENT** | 

Autoindent.

 |
| **TEXT_SHOWACTIVE** | 

Show active line.

 |


**Selection modes**

| **SELECT_CHARS** | 

Select characters.

 |
| **SELECT_WORDS** | 

Select words.

 |
| **SELECT_LINES** | 

Select lines.

 |