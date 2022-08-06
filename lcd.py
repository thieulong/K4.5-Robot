from grove.factory import Factory

lcd = Factory.getDisplay("JHD1802")
rows, cols = lcd.size()

def write_lcd(first_line="", second_line=""):
    try:
        lcd.clear()
        lcd.setCursor(0, 0)
        lcd.write(first_line)
        lcd.setCursor(rows - 1, 0)
        lcd.write(second_line)
    except ModuleNotFoundError: pass
    
def clear_lcd():
    try:
        lcd.clear()
    except ModuleNotFoundError:
        pass
    
## Test LCD code
# write_lcd(first_line='Hello there!', second_line='Robotics project')
