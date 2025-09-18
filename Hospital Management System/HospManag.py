import pymysql

# ✅ Connect to MySQL using pymysql
try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="hospital_management_db",
        cursorclass=pymysql.cursors.Cursor
    )
    cursor = conn.cursor()
    print("✅ Connected to MySQL successfully.")
except pymysql.MySQLError as err:
    print(f"❌ Connection error: {err}")
    exit()

# ---------------- Helper Function ----------------
def record_exists(table, column, value):
    cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE {column} = %s", (value,))
    return cursor.fetchone()[0] > 0

# ---------------- Patients ----------------
def add_patient():
    try:
        name = input("Enter patient name: ")
        age = int(input("Enter age: "))
        gender = input("Enter gender: ")
        diagnosis = input("Enter diagnosis: ")
        cursor.execute("INSERT INTO patients (name, age, gender, diagnosis) VALUES (%s, %s, %s, %s)",
                       (name, age, gender, diagnosis))
        conn.commit()
        print("✅ Patient added.")
    except Exception as e:
        print(f"❌ Error: {e}")

def view_patients():
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    print("\n📋 Patient Records:")
    for row in rows:
        print(row)

def update_patient():
    try:
        pid = int(input("Enter patient ID to update: "))
        diagnosis = input("Enter new diagnosis: ")
        cursor.execute("UPDATE patients SET diagnosis = %s WHERE patient_id = %s", (diagnosis, pid))
        conn.commit()
        print("✅ Patient updated.")
    except Exception as e:
        print(f"❌ Error: {e}")

def delete_patient():
    try:
        pid = int(input("Enter patient ID to delete: "))
        cursor.execute("DELETE FROM patients WHERE patient_id = %s", (pid,))
        conn.commit()
        print("🗑️ Patient deleted.")
    except Exception as e:
        print(f"❌ Error: {e}")

# ---------------- Doctors ----------------
def add_doctor():
    try:
        name = input("Enter doctor name: ")
        speciality = input("Enter specialty: ")
        phone = input("Enter phone number: ")

        cursor.execute(
            "INSERT INTO doctors (name, speciality, phone) VALUES (%s, %s, %s)",
            (name, speciality, phone)
        )
        conn.commit()
        print("✅ Doctor added.")
    except Exception as e:
        print(f"❌ Error: {e}")


def view_doctors():
    cursor.execute("SELECT * FROM doctors")
    rows = cursor.fetchall()
    print("\n📋 Doctor Records:")
    for row in rows:
        print(row)

def update_doctor():
    try:
        did = int(input("Enter doctor ID to update: "))
        phone = input("Enter new phone number: ")
        cursor.execute("UPDATE doctors SET phone = %s WHERE doctor_id = %s", (phone, did))
        conn.commit()
        print("✅ Doctor updated.")
    except Exception as e:
        print(f"❌ Error: {e}")

def delete_doctor():
    try:
        did = int(input("Enter doctor ID to delete: "))
        cursor.execute("DELETE FROM doctors WHERE doctor_id = %s", (did,))
        conn.commit()
        print("🗑️ Doctor deleted.")
    except Exception as e:
        print(f"❌ Error: {e}")

# ---------------- Appointments ----------------
def add_appointment():
    try:
        pid = int(input("Enter patient ID: "))
        did = int(input("Enter doctor ID: "))
        date = input("Enter appointment date (YYYY-MM-DD): ")
        notes = input("Enter notes: ")

        if not record_exists("patients", "patient_id", pid):
            print("❌ Patient ID does not exist.")
            return
        if not record_exists("doctors", "doctor_id", did):
            print("❌ Doctor ID does not exist.")
            return

        cursor.execute("INSERT INTO appointments (patient_id, doctor_id, appointment_date, notes) VALUES (%s, %s, %s, %s)",
                       (pid, did, date, notes))
        conn.commit()
        print("✅ Appointment added.")
    except Exception as e:
        print(f"❌ Error: {e}")

def view_appointments():
    cursor.execute("SELECT * FROM appointments")
    rows = cursor.fetchall()
    print("\n📋 Appointment Records:")
    for row in rows:
        print(row)

def update_appointment():
    try:
        aid = int(input("Enter appointment ID to update: "))
        notes = input("Enter updated notes: ")

        # Execute the update
        cursor.execute("UPDATE appointments SET notes = %s WHERE appointment_id = %s", (notes, aid))

        # Check if any row was updated
        if cursor.rowcount == 0:
            print("⚠️ No appointment found with that ID.")
        else:
            conn.commit()
            print("✅ Appointment updated.")
    except Exception as e:
        print(f"❌ Error: {e}")

def delete_appointment():
    try:
        aid = int(input("Enter appointment ID to delete: "))
        cursor.execute("DELETE FROM appointments WHERE appointment_id = %s", (aid,))
        conn.commit()
        print("🗑️ Appointment deleted.")
    except Exception as e:
        print(f"❌ Error: {e}")

# ---------------- Menu System ----------------
def main_menu():
    print("\n🚀 Hospital Management System Started")
    while True:
        print("\n📋 Main Menu")
        print("1. Manage Patients")
        print("2. Manage Doctors")
        print("3. Manage Appointments")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            patient_menu()
        elif choice == '2':
            doctor_menu()
        elif choice == '3':
            appointment_menu()
        elif choice == '4':
            print("👋 Exiting system. Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

def patient_menu():
    while True:
        print("\n👤 Patient Menu")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            update_patient()
        elif choice == '4':
            delete_patient()
        elif choice == '5':
            break
        else:
            print("❌ Invalid choice.")

def doctor_menu():
    while True:
        print("\n🩺 Doctor Menu")
        print("1. Add Doctor")
        print("2. View Doctors")
        print("3. Update Doctor")
        print("4. Delete Doctor")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            add_doctor()
        elif choice == '2':
            view_doctors()
        elif choice == '3':
            update_doctor()
        elif choice == '4':
            delete_doctor()
        elif choice == '5':
            break
        else:
            print("❌ Invalid choice.")

def appointment_menu():
    while True:
        print("\n📅 Appointment Menu")
        print("1. Add Appointment")
        print("2. View Appointments")
        print("3. Update Appointment")
        print("4. Delete Appointment")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            add_appointment()
        elif choice == '2':
            view_appointments()
        elif choice == '3':
            update_appointment()
        elif choice == '4':
            delete_appointment()
        elif choice == '5':
            break
        else:
            print("❌ Invalid choice.")

# 🔁 Start the program
main_menu()
cursor.close()
conn.close()
