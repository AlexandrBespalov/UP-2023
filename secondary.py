#GUI
window = Tk()

def btn_click():
    InputWindow = Input.get()

    info_str = f'Запрос на получение данных пользователя: {str(InputWindow)}'
    messagebox.showinfo(title='Получение JSON', message=info_str)

    #messagebox.showerrоr(title='Error!', Message='Ошибка')

#window['bg'] = '#8cc2ff'
window.title('Get JSON')
window.geometry('300x250')

window.resizable(width=False, height=False)

Canvas = Canvas(window, height=300, width=250)
Canvas.pack()

frame = Frame(window)
frame.place(relx = 0.15, rely = 0.15, relwidth = 0.7, relheight = 0.7)

title = Label(frame, text='Ввод имени', font='18')
title.pack(anchor=N)

Input = Entry(frame, bg='white')
Input.pack(anchor=CENTER)

btn = Button(frame, text = 'Получить', bg='#5991ff', command=lambda:[getData(), btn_click()])
btn.pack(anchor=S)

window.mainloop()

with open('log.txt') as f:
    for i in f.readlines():
        if 'необходимая фраза' in i:
            with open('log2.txt', 'a') as f2:
                f2.write(i)