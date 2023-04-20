import pyautogui as escolhas

opcao = escolhas.confirm('Clique no butão desejado',
                         buttons=['Excel', 'Word', 'Notepad'])

# if = se
if opcao == 'Excel':

    escolhas.hotkey('win', 'r')
    escolhas.sleep(1)
    escolhas.typewrite('Excel')
    escolhas.sleep(1)
    escolhas.press('enter')
    print('Você escolheu abrir o Excel')

elif opcao == 'Word':

    escolhas.hotkey('win', 'r')
    escolhas.sleep(1)
    escolhas.typewrite('winword ')
    escolhas.sleep(1)
    escolhas.press('enter')
    escolhas.sleep(1)
    escolhas.press('enter')
    print('Você escolheu abrir o Word')

else:

    escolhas.hotkey('win', 'r')
    escolhas.sleep(1)
    escolhas.typewrite('notepad')
    escolhas.sleep(1)
    escolhas.press('enter')
    print('Você escolheu abrir o Bloco de Notas')

