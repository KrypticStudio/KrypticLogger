# Kryptic Studio - KrypticLogger

KrypticLogger is a tool to help better organize and minimizing the amount of code while logging!

## Required Libraries

1. sty
```bash
$ pip install sty
```

## Installation

1. Clone Repository to Project Folder.


```bash
$ git clone https://github.com/KrypticStudio/KrypticLogger.git
```

## Usage
1. Import KrypticLogger!
```python
import from KrypticLogger.logger import log
```
2. Call it anywhere!
```python
### Parameters
    # log = True #Logs to terminal or cmd
    # write = Ture #Writes log to file
    # time = True #Adds current time to log
log.LOG_EXAMPLE("Message", log = True, write = True, time = True)
```
3. EXAMPLE
```python
# Example
import from KrypticLogger.logger import log

# Calling Logs
log.debug("Debugging Example", log = True, write = True, time = True)
log.error("Error Example", log = True, write = True, time = True, code="Error Code", critical = True)
log.info("Info Example", log = True, write = True, time = True)
log.log("Logging Example", log = True, write = True, time = True)
log.success("Success Example", log = True, write = True, time = True)
log.track("Tracking Example", log = True, write = True, time = True)
log.warn("Warning Example", log = True, write = True, time = True)
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
