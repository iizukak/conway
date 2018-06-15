# conway

An implementation of "Conway's Game of Life" in [MicroPython](https://micropython.org/) for [micro:bit](http://microbit.org/).

## Demo

[Here](https://twitter.com/iizukak/status/1007429297689133056) is the demo.

## Usage 

You can use [Mu](https://codewith.mu/) or [uflash](https://github.com/ntoll/uflash) to flash conway to micro:bit.

AUTO and MANUAL mode are available. AUTO mode execute game automatically, and MANUAL mode need press a button to update states of the cells

- Press A and B button
	- Restart the game
- Press A button
	- Update cell states
- Press B button
	- Switch mode
	- AUTO -> MANUAL, MANUAL -> AUTO
