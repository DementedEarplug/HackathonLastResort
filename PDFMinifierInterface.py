from Tkinter import *
import tkFileDialog
import os
def main():
    root = Tk()
    root.title('ImposibruPDF')
    root.filename= tkFileDialog.askopenfilename(filetypes=( ("All Files", "*.*"), (",pdf files","*.pdf") ))
    root.minsize(width=300, height=300)
    root.maxsize(width=300, height=300)
    downsize(root.filename)
    finished = Label(text="Optimization Finished!!", anchor='e')
    finished.pack()
    root.mainloop()


    

def downsize(name):
    cmd = 'cd pdfminify-master/; ./pdfminify '+str(name)+' ../output.pdf'
    print cmd
    os.system(cmd)

    

if __name__=="__main__":
    main()

