import pyautogui as posicaoMouse
# import time as tempoEspera
import pyautogui as tempoEspera

# Tempo de espera para que o computador possa pensar e processar.
tempoEspera.sleep(1)

# Movento o mouse ate o botão iniciar (x,y)
posicaoMouse.moveTo(509, 1061)


# Tempo de espera para que o computador possa pensar e processar.
tempoEspera.sleep(0)

# Clicando na posição do botão
posicaoMouse.click(509, 1061)

# Tempo de espera para que o computador possa pensar e processar.
tempoEspera.sleep(0)

# Estou escrevendo a palavra calc / calculadora.
posicaoMouse.typewrite('calc')

# Tempo de espera para que o computador possa pensar e processar.
tempoEspera.sleep(0)

# Movento o mouse ate o aplicativo da calculadora(x,y)
posicaoMouse.moveTo(747, 350)

# Tempo de espera para que o computador possa pensar e processar.
tempoEspera.sleep(0)

# Clicando na posição do botão da calculadora.
posicaoMouse.click(747, 350)


# print(posicaoMouse.position()) - codigo para verificar aonde está o mouse