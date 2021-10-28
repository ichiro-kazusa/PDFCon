# GUI

## concat

* list move
  * normal
  * list
    * buttons
      * add, remove, clear, move(*4)
    * move
      * single move, multiple move
      * up, down, top, bottom
      * up/down: non continuous error
    * key
      * ctrl+A, del, multiple del, move(alt + *)
    * drag and drop
      * single pdf
      * multiple pdf
      * included non-pdf -> reject
  * concat button
    * concat exec

## decrypt

* source drag and drop
  * pdf -> accept
  * multiple pdf -> accept first pdf
  * non-pdf -> reject
  * multiple file include non-pdf -> accept first pdf
* autofill button
  * same directory, file name with '_decrypt'
* decrypt button
  * concat decrypt

## log
* output every message
* log pane is read-only
* message style
  * log -> black
  * err -> red
* scroll
  * keep bottom (newest message)

# PDF Backend
## concat

* normal
  * multiple file
* error
  * encrypt file is included
  * source open error
  * no source
  * no output
  * no pdf -> File Read Error
* source file lock is released after concatenate
  * whether task is successed or failed.
    * error: already loaded files before the failed file
    * error: the file which is failed to concat

## decrypt

* normal
  * keeps metadata
* error
  * no source
  * source open error
  * no output
  * file is not encrypted
  * password failed
  * source file is not pdf
* source file lock is released after concatenate
  * whether task is successed or failed.

## encrypt

* normal
  * normal
  * normal with encrypted source
* error
  * encrypted source password failed
  * no source
  * no output
  * source file is not pdf


