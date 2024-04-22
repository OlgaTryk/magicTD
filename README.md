# Elemental Kingdom: Guardians of the Realm

Elemental Kingdom: Guardians of the Realm is a tower defense game in about wizards using elemental powers to protect their kingdom from a monster invasion.

## Game Screen ##

![gameScreen](https://github.com/OlgaTryk/magicTD/assets/127615584/bec89cd4-fdb5-46d0-a1c6-82c7fe3bd73b)

## Controls ##
| | |
|---|---|
|Arrow keys | Controlling the cursor (white square)|
|Escape | Exit the game|
|Spacebar | Start next wave|

## Threads ##
- _Main thread_ - draws the game window
- _Keyboard thread_ - reads and processes keyboard input
- _Wave thread_ - spawns enemies, checks if any remain or if a new wave can be started
- _Enemy threads_ - moves the enemy it applies to, kills it when it runs out of health and removes lives when it reaches the end

### Modules ###
- pygame

