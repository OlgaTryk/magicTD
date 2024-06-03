# Elemental Kingdom: Guardians of the Realm

Elemental Kingdom: Guardians of the Realm is a tower defense game in about wizards using elemental powers to protect their kingdom from a monster invasion.

## Game Screen ##

![gameScreen](https://github.com/OlgaTryk/magicTD/assets/127615584/c8798407-3f4a-451d-8457-a9a029ae6e5b)

## Controls ##
| | |
|---|---|
|Arrow keys | Controlling the cursor (white square)|
|Escape | Exit the game|
|Spacebar | Start next wave|
|1 | Place magic tower|
|2 | Place ice tower |

## Threads ##
- _Main thread_ - draws the game window
- _Keyboard thread_ - reads and processes keyboard input
- _Wave thread_ - spawns enemies, checks if any remain or if a new wave can be started
- _Enemy threads_ - move the enemy they apply to, kill it and give money when it runs out of health, remove lives when it reaches the end
- _Tower threads_ - find and attack enemies in range

## Critical Sections ##
| Resource              | Type |
|-----------------------|---|
| Player lives          | Mutex |
| Player money          | Mutex |
| Enemy health          | Mutex |
| Enemy slow down timer | Mutex |

### External Modules ###
- pygame

