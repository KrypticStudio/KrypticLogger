#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### Kryptic Studio ###

# Local Libraries
from KrypticLogger.logger import log
# Libraries

# Standard Libraries
import time
# Global Variables
logLog = True
writeLog = False
timeLog = True
# Function Definitions

# Main Function Definition
def main(): ### Uncomment if nessesary!
    while True:
        #log.OPTION("MESSAGE", True, Fasle, False)
        log.debug("Debugging Example", log = True, write = True, time = True)
        log.error("Error Example", log = True, write = True, time = True, code="Error Code", critical = True)
        log.info("Info Example", log = True, write = True, time = True)
        log.log("Logging Example", log = True, write = True, time = True)
        log.success("Success Example", log = True, write = True, time = True)
        log.track("Tracking Example", log = True, write = True, time = True)
        log.warn("Warning Example", log = True, write = True, time = True)
        time.sleep(5)

#    return ### Uncomment if nessesary!
# Call to main()
main() ### Uncomment if nessesary!

#or

#if __name__ == '__main__': ### Uncomment if nessesary!
#    main() ### Uncomment if nessesary!