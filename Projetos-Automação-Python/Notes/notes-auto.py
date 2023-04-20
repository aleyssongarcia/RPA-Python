import pyautogui as posicaoMouse
import keyboard

# Mesma coisa que precionar as teclas do teclado. WIN+R

posicaoMouse.hotkey('win', 'r')

# Aguarda um tempo para o computador processar.
posicaoMouse.sleep(2)


# Digita na caixa de executar " Notepad"
posicaoMouse.typewrite('notepad')

# Aguarda um tempo para o computador processar.
posicaoMouse.sleep(2)

# Apertar enter para abrir o bloco de notas.
posicaoMouse.press('enter')

# Aguarda um tempo para o computador processar.
posicaoMouse.sleep(4)

# Escrevendo dentro do bloco de notas.
posicaoMouse.typewrite('Abri o bloco de notas')

# Aguarda um tempo para o computador processar.
posicaoMouse.sleep(3)

# Me permite pegar a janela ativa.
fecharbloco = posicaoMouse.getActiveWindow()

# Aguarda um tempo para o computador processar.
posicaoMouse.sleep(2)

# Aciona a opção de fechar a janela ativa
fecharbloco.close()

# Aguarda um tempo para o computador processar.
posicaoMouse.sleep(2)

#Estou precionando tab, para ir para o botão não salvar.
keyboard.press('right')

# Aguarda um tempo para o computador processar.
posicaoMouse.sleep(2)

#Apertamos a tecla enter para fechar sem salvar.
posicaoMouse.press('enter')