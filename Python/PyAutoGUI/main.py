import pyautogui
from time import sleep, time



DELAY_BETWEEN_COMMANDS = 1.00


def main():

    InitializePyAutoGUI()
    CountdownTimer()

    GoToMerchant()
    TradeWithMerchant()
    ReturnToShip()

    #reportMousePosition()

    print("Bot is shuting down!")

def HoldKey(key, seconds=1.00):
    pyautogui.keyDown(key)
    sleep(seconds)
    pyautogui.keyUp(key)
    sleep(DELAY_BETWEEN_COMMANDS)

def reportMousePosition(seconds=5):
    for i in range(0,seconds):
        print(pyautogui.position())
        sleep(1)

def InitializePyAutoGUI():
    #Init PyAutoGUI
    pyautogui.FAILSAFE = True

def CountdownTimer():
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 5):
        print(".", end="", flush=True)
        sleep(1)
    print(" Go")

def TradeWithMerchant():
    #Click on Merchant
    pyautogui.moveTo(1256,498, 0.25)
    sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()

    #Wait for dialog to Appear
    sleep(3)
    
    #Click on "Trade" option
    pyautogui.moveTo(783,899,0.25)
    sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()

    #Wait for dialog to Appear
    sleep(3)
    
    #Click on "Manufactoring Robot" option
    pyautogui.moveTo(1332,453,0.25)
    sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()

    #Buy the Item
    numToBuy = 1
    pyautogui.keyDown('shiftleft')
    for i in range(0,numToBuy):
        pyautogui.click()
        sleep(0.5)
    pyautogui.keyUp('shiftleft')

    #Click the close button
    pyautogui.moveTo(1568,358,0.25)
    sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()

    #Wait for dialog to Appear
    sleep(3)

    #Click the done button
    pyautogui.moveTo(489,859,0.25)
    sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click()
    sleep(2.00)

def GoToMerchant():
    HoldKey('s', 6.00)
    HoldKey('a', 0.10)
    HoldKey('w', 7.00)
    HoldKey('d', 0.65)
    HoldKey('w', 5.60)
    HoldKey('d', 1.16)
    HoldKey('w', 1.50)

def ReturnToShip():
    HoldKey('a', 0.20)
    HoldKey('s', 2.65)
    HoldKey('d', 0.08)
    HoldKey('w', 5.76)
    HoldKey('a', 0.68)
    HoldKey('w', 6.20)
    HoldKey('a', 0.30)
    pyautogui.click(803, 269, duration=0.25)
    sleep(10.00)

if __name__ == "__main__":
    main()