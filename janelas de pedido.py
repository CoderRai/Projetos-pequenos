import PySimpleGUI as sg

#Criar as janelas e estilos (layout)
def janela_login():

    sg.theme('reddit')
    layout = [
        [sg.Text('nome')],
        [sg.Input()],
        [sg.Button('continuar')]
    ]
    return sg.Window('login', layout=layout, finalize=True)

def janela_pedido():
    sg.theme('reddit')
    layout = [
        [sg.Text('fazer pedido')],
        [sg.Checkbox('pizza pepperoni',key='pizza1'), sg.Checkbox(
            'pizza frango c/ catupiry', key='pizza2')],
        [sg.Button('Voltar'), sg.Button('fazer pedido')]

    ]
    return sg.Window('Montar pedido',layout=layout, finalize=True)


#criar as janelas iniciais
janela1,janela2 = janela_login(), None
#Criar loop de leitura de eventos
while True:
    Window,event,values = sg.read_all_windows()
    #quando a janela for fechada
    if Window == janela1 and event ==sg.WIN_CLOSED:
        break
    # quando queremos ir para a proxima janela
    if Window == janela1 and event == 'continuar':
        janela2 = janela_pedido()
        janela1.hide()
    if Window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if Window == janela2 and event == 'fazer pedido':
        if values['pizza1'] == True and values ['pizza2'] == True:
            sg.popup('foram solicitados umapizza pepperoni e uma pizza Catupiry c/ frango')
        elif values['pizza1'] == True:
            sg.popup('foi solicitado uma pizza Pepperoni ')
        elif values['pizza2'] == True:
            sg.popup('foi solicitado uma pizza de Catupiry com frango ')




#lógica de o que deve acontecer ao clicar os botoes