from openpyxl import load_workbook
import pyautogui as pg
import time
wb = load_workbook("data.xlsx")
ws = wb.active

def access(scene,object):   #mp3 or img
    '''
    x = scene no.
    y = 2(for img prompt) / 3(for Script)
    '''
    x = scene 
    if object=="mp3":
        value = ws.cell(row=x,column=3).value
        return value
    else:
        value = ws.cell(row=x,column=2).value
        return value


def insert(x,y,z):
    ws.cell(row=x, column=y, value=z)

    # File save karein
    wb.save("data.xlsx")

    print("Value inserted successfully!")
def inp():
    lines = []
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)

    text = "\n".join(lines)
    return text


def scene(n):
    def script():
        print(f"Script for Scene {n}:   ")
        a = inp()
        insert(n,3,a)
    def img_prompt():
        print(f"Image prompt for Scene {n}:     ")
        b = inp()
        insert(n,2,b)
    script()
    img_prompt()

no_of_scenes = int(input("how many scenes   :"))
def main():
    i = 1
    while i<=no_of_scenes:
        scene(i)
        i += 1
main()




def both(x):        #   x=scene number
    time.sleep(3)

    #GEMINI
    a = pg.locateCenterOnScreen('img/1.png')
    pg.click(a)     #click on gemini search
    pg.write("create a Image : " + access(x,"img"))
    pg.press('enter')
    time.sleep(1)

    #ELEVENLABS
    pg.click(1080, 540)
    pg.hotkey('ctrl', 'a')
    time.sleep(1)
    pg.press('backspace')
    time.sleep(2)
    pg.write(access(x,"mp3"))
    time.sleep(30)
    pg.click(1233,1005)
    #c = pg.locateCenterOnScreen('img/2.png')
    #time.sleep(1)

#SAVE GEMINI IMAGE
    pg.click(534,584)
    time.sleep(3)
    pg.click(740,114)
    time.sleep(25)
    name = f"{x}.png"
    pg.write(name)
    time.sleep(1)
    pg.press('enter')
    #pg.click(800,500)

#SAVE ELEVEN LABS
    time.sleep(1)
    pg.click(1244,928)
    time.sleep(17)
    pg.click(1836,1031)
    time.sleep(10)
    pg.write(f"{x}.mp3")
    time.sleep(1)
    pg.press('enter')
    
    #RESET
    time.sleep(3)
    pg.click(47,118)
    time.sleep(2)
    pg.click(892,114)
    time.sleep(3)

def main2():
    i = 1
    while i<=no_of_scenes:
        both(i)
        i += 1

main2()