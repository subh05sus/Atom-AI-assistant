import tkinter as tk
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure




class AudioVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title('Atom Voice Assistant')

        # Create a frame to hold the visualizer and button
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        # Create the start/stop button
        self.start_button = tk.Button(self.frame, text='Start', command=self.toggle_audio_capture)
        self.start_button.pack(side=tk.LEFT, padx=10)

        # Initialize the PyAudio object
        self.pa = pyaudio.PyAudio()

        # Initialize the audio stream
        self.stream = None

        # Initialize the visualizer figure
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_ylim(-2**15, 2**15)
        self.ax.set_xlim(0, 1024)
        self.ax.set_title('Atom AI Assistant')
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.line, = self.ax.plot(np.zeros(1024))


        self.ax.xaxis.set_visible(False)
        self.ax.yaxis.set_visible(False)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['bottom'].set_visible(False)
        self.ax.spines['left'].set_visible(False)

        # Initialize the canvas to display the visualizer
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Set the initial state of the audio capture
        self.is_capturing = False
    def toggle_audio_capture(self):
        if self.is_capturing:
            # Stop capturing audio
            self.is_capturing = False
            self.start_button.config(text='Start')
            self.stream.stop_stream()
            self.stream.close()
            self.pa.terminate()
            
        else:
            # Start capturing audio
            self.is_capturing = True
            self.start_button.config(text='Stop')
            self.stream = self.pa.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
            self.update_visualizer()

    def update_visualizer(self):
        if self.is_capturing:
            # Read the audio data from the stream
            data = self.stream.read(1024)

            # Convert the audio data to a numpy array
            data_np = np.frombuffer(data, dtype=np.int16)

            # Update the visualizer display
            self.line.set_ydata(data_np)
            self.fig.canvas.draw()

            # Repeat the update after 10 milliseconds
            self.master.after(10, self.update_visualizer)

    
# Create the Tkinter window and run the main event loop
root = tk.Tk()
app = AudioVisualizer(root)
root.mainloop()
