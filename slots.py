import csv
import itertools
import os

# Fungsi untuk membaca data ruangan dari file CSV
def read_rooms_data(filename):
    rooms = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rooms.append({
                "id_ruangan": int(row["id_ruangan"]),
                "nama_ruangan": row["nama_ruangan"],
                "kapasitas": int(row["kapasitas"])
            })
    return rooms

# Path ke file ruangan.csv
ruangan_file_path = 'input_files/ruangan.csv'

# Generate slot waktu
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
start_time = '07:30'
end_time = '22:00'
time_slots = [(day, f"{hour:02d}:{minute:02d}") for day in days for hour in range(7, 22) for minute in range(0, 60, 30)]

# Baca data ruangan
rooms = read_rooms_data(ruangan_file_path)

# Generate slots berdasarkan data ruangan
slots = []
for room in rooms:
    for time_slot in time_slots:
        slots.append({
            "Day": time_slot[0],
            "Time": time_slot[1],
            "Classroom": room["nama_ruangan"],
            "Capacity": room["kapasitas"]
        })

# Path untuk menyimpan file schedule.csv
output_file_path = 'schedule.csv'

# Simpan data ke dalam file CSV
with open(output_file_path, 'w', newline='') as csvfile:
    fieldnames = ['Day', 'Time', 'Classroom', 'Capacity']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for slot in slots:
        writer.writerow(slot)

print(f"Data slot waktu telah disimpan dalam file {output_file_path}")
