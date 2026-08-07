import os
import sys
import tkinter as tk
from PIL import Image, ImageTk

# Configuration
IMAGE_FOLDER = "images"  # Put your image directory here
DELAY = 60000  # Time in milliseconds (600 seconds)


class SlideshowApp:

  def __init__(self, root, folder):
    self.root = root
    self.root.title("Python Automatic Slideshow")
    self.root.attributes('-fullscreen', True)
    self.root.lift()
    self.root.attributes('-topmost', True)
    # Kill Windows Explorer to hide taskbar and desktop
    os.system("taskkill /f /im explorer.exe")

    # Bind the Escape key to close the app
    self.root.bind('<Escape>', self.close_app)

    self.images = []
    self.load_images(folder)

    self.index = 0
    self.label = tk.Label(self.root)
    self.label.pack(fill=tk.BOTH, expand=True)

    if self.images:
      self.show_image()
      self.auto_loop()
      
   
  def load_images(self, folder):
    valid_exts = (".png", ".jpg", ".jpeg", ".gif", ".bmp")
    try:
        for file in sorted(os.listdir(folder)):
            if file.lower().endswith(valid_exts):
                path = os.path.join(folder, file)
                img = Image.open(path)
                self.images.append(img)
    except OSError:
        print("Error reading image file(s) or image folder (",
              os.getcwd(), "\\", IMAGE_FOLDER, ") does not exist")
        input("Press Enter to exit...")  # Execution halts here until Enter is pressed
        sys.exit()

  def show_image(self):
    img = self.images[self.index]
    # Resize image to fit window (optional)
    self.photo = ImageTk.PhotoImage(img)
    self.label.config(image=self.photo)

  def auto_loop(self):
    self.index = (self.index + 1) % len(self.images)
    self.show_image()
    self.root.after(DELAY, self.auto_loop)
  
  def close_app(self, event=None):
    self.root.destroy()

if __name__ == "__main__":
  root = tk.Tk()
  root.geometry("800x600")
  app = SlideshowApp(root, IMAGE_FOLDER)
  root.mainloop()
