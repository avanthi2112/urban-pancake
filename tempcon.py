from tkinter import *
import random
class Converter:
    def __init__(self, parent):
        background_colour = "light blue"
        # frame
        self.converter_frame=Frame(parent, bg=background_colour,
                                   padx=10, pady=10)
        self.converter_frame.grid()
        # GUI
        self.heading_label = Label(self.converter_frame, bg=background_colour,
                                   text="Temperature Converter",
                                   font=("Arial", "16", "bold"))
        self.heading_label.grid(row=0, columnspan=2, padx=10, pady=10)
        self.text_label = Label(self.converter_frame, bg=background_colour,
                                text="Enter Temperature")
        self.text_label.grid(row=1, column=0, padx=10, pady=10)
        self.input_entry = Entry(self.converter_frame, bg="white")
        self.input_entry.grid(row=1, column=1)
        self.b1 = Button(self.converter_frame,
                         text="To Degrees C",
                         font=("Arial", "10"),
                         command = self.to_deg)
        self.b1.grid(row=2, column=0, sticky=E)
        
        self.b2 = Button(self.converter_frame,
                         text="To Degrees F",
                         font=("Arial", "10"),
                         command = self.to_far)
        self.b2.grid(row=2, column=1, sticky=W)
        
        self.answer_label = Label(self.converter_frame,
                                  text="choose an option",
                                  bg=background_colour)
        self.answer_label.grid(row=3, columnspan=2, padx=10, pady=10)
        
        self.help_button = Button(self.converter_frame,
                                  text="Help/Info",
                                  command=self.help)
        
        self.help_button.grid(row=4, columnspan=2)
        
    def change(self, which):
        to_convert = self.input_entry.get()
        try:
            to_convert = float(to_convert)
            
            if which == 1 and to_convert < -459.4:
                self.answer_label.configure(text="too cold",
                                            foreground="red")
            elif which == 2 and to_convert < -273:
                self.answer_label.configure(text="too cold",
                                            foreground="red")
            else:
                if which == 1:
                    from_f = (to_convert - 32) * 5 / 9
                    choice = ("{} degrees F is {:.2f} "
                              "degrees C".format(to_convert, from_f))
                else:
                    from_c = (9 / 5)*to_convert + 32
                    choice = ("{} degrees C is {:2f} "
                              "degrees F".format(to_convert, from_c))
                    
                    self.answer_label.configure(text=choice)
                    
        except ValueError:
            self.answer_label.configure(text="thats not a number",
                                        foreground="red")
            
    def to_deg(self):
        which = 1
        self.change(which)
        
    def to_far(self):
        which = 2
        self.change(which)
            
    def help(self):
        get_help = Help()
                        
class Help:
    def __init__(self):
        
        background = "light blue"
        self.help_box = Toplevel()
        self.help_frame = Frame(self.help_box, width=300,
                                height=200, bg=background)
        self.help_frame.grid()
        
        how_heading = Label(self.help_frame,
                            text="help / Instructions",
                            font="arial 10 bold", bg=background)
        how_heading.grid(row=0)
        
        self.help_text = Label(self.help_frame,
                               text="", justify=LEFT,
                               width=40, bg=background, wrap=250)
        self.help_text.grid(column=0, row=1)
        
        dismiss_button = Button(self.help_frame, text="Dismiss",
                                width=10, bg="orange",
                                font="arial 10 bold",
                                command=self.close_help)
        dismiss_button.grid(row=2, pady=10)
        
    def close_help(self):
        self.help_box.destroy()
        
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    convert_it = Converter(root)
    root.mainloop()