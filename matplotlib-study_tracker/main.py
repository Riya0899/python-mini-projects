import csv
import matplotlib.pyplot as plt
import os

FILE_NAME = 'study_data.csv'

def save_data(date, hours, focus):
    # Check if file exists to write headers
    file_exists = os.path.isfile(FILE_NAME)
    
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Date', 'Hours', 'Focus_Level']) # Header
        writer.writerow([date, hours, focus])
    print(f"✅ Data saved for {date}!")

def visualize_data():
    dates, hours, focus_levels = [], [], []
    
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                dates.append(row['Date'])
                hours.append(float(row['Hours']))
                focus_levels.append(int(row['Focus_Level']))
    except FileNotFoundError:
        print("No data found! Please add some entries first.")
        return

    # Create a dual-axis plot
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Bar chart for Hours
    ax1.bar(dates, hours, color='skyblue', label='Hours Studied')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Hours', color='blue')
    
    # Line plot for Focus Level (on a second Y-axis)
    ax2 = ax1.twinx()
    ax2.plot(dates, focus_levels, color='red', marker='o', label='Focus Level (1-10)')
    ax2.set_ylabel('Focus Level', color='red')
    ax2.set_ylim(0, 10)

    plt.title('My Study Progress Over Time')
    plt.show()

# --- Main Interaction ---
print("--- 📚 Personal Study Tracker ---")
user_date = input("Enter Date (e.g., Oct-24): ")
user_hours = input("How many hours did you study? ")
user_focus = input("Focus Level (1-10)? ")

save_data(user_date, user_hours, user_focus)

if input("View progress chart? (y/n): ").lower() == 'y':
    visualize_data()