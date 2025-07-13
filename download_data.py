from pathlib import Path
import csv

# addressing the path of file
path = Path('datasets/global_tourist_hotspot/cleaned_data_Iran.csv')
#"C:\Users\Dariush\Desktop\python_work\python-projects\data-visualization-project\datasets\global_tourist_hotspot\cleaned_data_Iran.csv"

# reading csv file
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
print(header_row)
