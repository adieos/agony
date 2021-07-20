import pyautogui
import time
amogus = True
string =  input("What would you like to spam? ")

while amogus:
   try:
      sleeptime = int(input("How long do I need to wait? "))
      break
   except ValueError:
      print("Please enter a valid number!")

while amogus:
   try:
      amount = int(input("How many times do you want to spam? "))
      break
   except ValueError:
      print("Please enter a valid number!")
   
while amogus:
   try:
      interval = int(input("How long does the interval will last? "))
      break
   except ValueError:
      print("Please print a valid number!")

print("Countdown starting...")


for i in range(sleeptime, 0, -1):
   print(i)
   time.sleep(1)

print("Spam initiated")
for i in range(0,amount):
   pyautogui.write(string)
   pyautogui.press("Enter")
   time.sleep(interval)
print("Spam ended")

    