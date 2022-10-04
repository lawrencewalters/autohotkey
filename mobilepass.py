from typing import Dict
from pywinauto.application import Application
import time

def get_code(token_name: str, pin: str) -> str:
    """Open the MobilePASS application, select the token based on `token_name` and enter the `pin` then retrieve the one time password.

    Expects Windows OS, and MobilePASS installed in C:\Program Files (x86)\SafeNet\Authentication\MobilePASS\MobilePASS.exe"""

    code = ""
    app = Application().start("C:\Program Files (x86)\SafeNet\Authentication\MobilePASS\MobilePASS.exe")

    app.MobilePASS[token_name].click()
    app.MobilePASS.Continue.wait("exists ready visible")
    time.sleep(1)
    app.MobilePASS.type_keys(pin)
    time.sleep(1)
    app.MobilePASS.Continue.click()
    app.MobilePASS['Copy Passcode'].click()

    code = app.MobilePASS.Edit.get_line(0)

    app.kill(True)
    app.wait_for_process_exit()
    return code
