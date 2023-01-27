import PySimpleGUI as sg


sg.theme('DarkTeal9')


menu = [
    ['Opções', ['Arquivar', 'Enviar', 'Ajuda']],
    ['Arquivo', ['Caixas', ['Arquivadas', 'Enviadas']]],
]
layout = [
    [sg.Menu(menu, text_color='black', pad=(1,1), font='Arial 8 italic bold ', key='MENU')],
    [sg.VPush()],
    [sg.Text("Ferramenta de Backup")],
    [sg.VPush()],
    [sg.Push(),sg.Button("Arquivar", font='Helvetica 12', pad=(0,0), border_width=1),sg.Push(), sg.Button("Enviar", font='Helvetica 12', pad=(0,0), border_width=1),sg.Push()],
    [sg.Text("")],
    [sg.VPush()],
    [sg.Button("Sair", font='Helvetica 12', pad=(0,0), border_width=1)],
    [sg.VPush()],


]


tela = sg.Window("Backup", layout, element_justification="c", resizable=True, font='Helvetica 14', titlebar_text_color='blue',)


while True:
    event, values = tela.read()
    if event in (sg.WIN_CLOSED, "Sair"):
        
        break
    if values['MENU']=="Arquivar" or event=="Arquivar":
        print("Selecionou a opção de Arquivamento")  
    if values['MENU']=="Enviar" or event=="Enviar":
        print("Selecionou a opção de Upload") 
    if values['MENU']=="Ajuda":
        sg.PopupNoTitlebar("Para facilitar o seu trabalho recomendamos unificar as senhas de todas as caixas para o arquivamento e envio simultaneo", font='Arial 10 bold', background_color='black', text_color='white', )
        print("Selecionou a opção de Ajuda")   
    if values['MENU']=='Arquivadas':
        sg.PopupNoTitlebar("Voce ja arquivou: ...", font='Arial 10 bold', background_color='black', text_color='white')
    if values['MENU']=='Enviadas':
        sg.PopupNoTitlebar("Voce ja enviou: ...", font='Arial 10 bold', background_color='black', text_color='white')

tela.close()





# DEPLOY == pyinstaller -wF my_program.py