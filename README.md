# Elemental Kingdom: Guardians of the Realm

Elemental Kingdom: Guardians of the Realm is a tower defense game in about wizards using elemental powers to protect their kingdom from a monster invasion.

## Game Screen ##

![gameScreen](https://github.com/OlgaTryk/magicTD/assets/127615584/1163dbdb-31a2-4744-ac5b-7868b42f1c9d)


## Towers ##
- magic tower - attacks one enemy, low damage, high speed and range
- ice tower - slows all enemies in range, doesn't do damage
- fire tower - attacks all enemies in range, high damage, low speed and range

## Controls ##
| | |
|---|---|
|Arrow keys | Controlling the cursor (white square)|
|Escape | Exit the game|
|Spacebar | Start next wave|
|1 | Place magic tower|
|2 | Place ice tower |
|3 | Place fire tower |

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

