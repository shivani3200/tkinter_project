import tkinter as tk
from tkinter import messagebox
import re

def analyze_sentiment():
    # Get the YouTube video link from the entry widget
    youtube_link = link_entry.get()

    # Check if the link is a valid YouTube link
    if not is_valid_youtube_link(youtube_link):
        messagebox.showerror("Error", "Invalid YouTube link. Please enter a valid link.")
        return

    # Perform sentiment analysis (placeholder - actual analysis can be more complex)
    sentiment = perform_sentiment_analysis()

    # Show sentiment result in a message box
    messagebox.showinfo("Sentiment Analysis Result", f"The sentiment of the video is {sentiment}.")

def is_valid_youtube_link(link):
    # Check if the link matches a typical YouTube video link pattern
    youtube_pattern = re.compile(r'(https?://)?(www\.)?youtube\.(com|be)/.+/watch\?v=.+')
    return bool(re.match(youtube_pattern, link))

def perform_sentiment_analysis():
    # Placeholder function for sentiment analysis
    # In a real application, you would use a more sophisticated sentiment analysis approach
    return "Positive"  # Placeholder result

# Create the main window
window = tk.Tk()
window.title("YT Sentiment Analysis")

# Styling
window_width = 500
window_height = 300
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

window.configure(bg="#F8F8F8")  # Set background color

# Create and pack widgets with enhanced styling
info_label = tk.Label(window, text="Enter YouTube Video Link:", bg="#F8F8F8", font=("Arial", 14))
info_label.pack(pady=15)

link_entry = tk.Entry(window, width=40, font=("Arial", 12))
link_entry.pack(pady=15)

submit_button = tk.Button(window, text="Submit", command=analyze_sentiment, bg="#4CAF50", fg="white", font=("Arial", 12))
submit_button.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()
