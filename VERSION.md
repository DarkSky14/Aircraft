
# V 0.2.7
Improvements
    - Splitting the monolith into smaller scripts.
    - Moving the main script from **Aircraft** to **Aircraft/src**.
    - Add **__init__** file.
    - Add **VERSION.MD** file.

Problems
    - Problems in clear RAM.

Bugfixes
    - Fixed a bug that occurred when exiting Settings by pressing a button, and which affected entering the game.

# V 0.2.6
Improvements
    - Automatic leveling of bonuses, opponents and player sizes.
    - Optimization of RAM usage.
    - Reduced CPU usage in some scenarios.
    - More information in the logs.
    - Transition from pygame library to pygame-ce.
    - Optimization of validation logic.

Bugfixes
    - Fixed some alignment issues.
    - Fixed a bug in the event flow clogging.
    - Fixed a bug with the button getting stuck when pressed.

# V 0.2.5
Improvements
    - Optimized RAM usage.
    - Better smoothness.
    - Minor improvements and optimizations.
    - Logs are now separated by startup time.
    - Mouse appearance change is now in the event class.

Bugfixes
    - Fix for loading mouse coordinates.
    - Fixed a bug where incorrect symbols were specified in the config, causing the settings to not work.
    - Fixed a bug where the fill would break when hovering over a button.

# V 0.2.4
Improvements
    - Add automatic text size alignment.

Bugfixes
    - Fixed a bug with button presses.
    - Fixed a bug in button animations.
    - Fixed a bug that caused the game to crash on small screens.

# V 0.2.3
Improvements
    - Added FPS display in the menu.
    - Animated dimming in settings.
    - Display refresh optimization (now black parts are not refreshed).
    - Real logging.
    - Menu optimization.
    - Automatic button size alignment.

Bugfixes
    - Fixed a bug with placing backgrounds on screens larger than (1373, 767) pixels.
    - Fixed a bug related to enemies and bonuses, and their clearing.
    - Fixes in text and button classes.

# V 0.2.2
    - Improvements
    - Improving the performance of the **Surface** class.

Bugfixes
    - Fix screen config.

# V 0.2.1
Improvements
    - Add event_pool.
    - Add logging class (print in console).
    - Improwed Formatter.
    - Improwed on/off music.
    - Add **draw** class.
    - Save appearance of a mouse.
    - Optimize CPU usage.
    - Buttons are in a separate class.
    - Optimization of file work.
    - Adding a class for languages.
    - Saving languages in **==.json==** files
    - Add expectation to a **click**.
    - Added sound effect when hovering over a button.
    - Delete library **winsound**.
    - Create file for class **Text** and **Button**.
    - Add animations to **Button** move.
    - Checking whether hardware optimization for the screen is supported.
    - Correct return when exiting menu and game functions.
    - Small improvement for FPS handling.

Bugfixes
    - Fixed in button.
    - Fixed a bug with leaving traces on a dark background.
    - Fixed a bug with incorrect mouse appearance change.
    - Fixed a bug with saving level progress.
    - Fixed a bug with the game crashing if the config file or folder is missing.

# V 0.1.1
Improvements
    - Added automatic adjustment to screen size.
    - A **temp** object has been created to store music.
    - There is now a separate link for specifying file names in **DLib**.
    - The classes are now in a separate file.

Bugfixes
    - Fix created **"internal/library/data"** in base directory.
    - Fixed issues with reading languages ​​to install them when logging into the game.

# V 0.1.0
Add.