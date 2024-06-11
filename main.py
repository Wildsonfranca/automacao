# importação da biblioteca automação
import pyautogui as auto
#atrasar comando de uma unica linha
#import time
auto.PAUSE = 0.5

# abre o menu iniciar 
#time.sleep
auto.press('win')
# abre o chrome
auto.write('chrome')
auto.press('enter')
#maximiza a ela 
auto.write('alt','space')
# abre o github
auto.write('githube.com')
auto.press('enter')
# abre o classroom em uma nova guia
auto.hotkey('ctrl','t')
auto.write('classroom.google.com')
auto.press('enter')
