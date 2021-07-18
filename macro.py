import pyautogui
import time
string =  input("What would you like to spam? ")
sleeptime = int(input("How long do I need to wait? "))
amount = int(input("How many times do you want to spam? "))
print("Countdown starting...")
for i in range(sleeptime, 0, -1):
   print(i)
   time.sleep(1)

print("Spam initiated")
for i in range(0,amount):
   pyautogui.write(string)
   pyautogui.press("Enter")
print("Spam ended")
    