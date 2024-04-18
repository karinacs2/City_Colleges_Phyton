# Dictionary patients
patients = {
    "P12345": {
        "name": "John Doe",
        "age": 35,
        "gender": "Male",
        "diagnosis": "Hypertension",
        "medications": ["Lisinopril", "Hydrochlorothiazide"],
        "allergies": ["Penicillin"],
        "blood_pressure_checks": [[130, 90], [146, 99], [138, 88], [128, 82]],
        "last_checkup_date": "2022-05-20",
        "next_appointment_date": "2023-11-15"
    },
    "P67890": {
        "name": "Jane Smith",
        "age": 41,
        "gender": "Female",
        "diagnosis": "Diabetes",
        "medications": ["Semaglutide", "Insulin"],
        "blood_pressure_checks": [[119, 79], [122, 77], [120, 81], [118, 85]],
        "allergies": ["Metformin"],
        "last_checkup_date": "2023-04-20",
        "next_appointment_date": "No-Date"
    },
    "P24680": {
        "name": "Robert Johnson",
        "age": 28,
        "gender": "Male",
        "diagnosis": "Asthma",
        "medications": ["Albuterol", "Prednisone"],
        "allergies": ["Peanuts"],
        "blood_pressure_checks": [[121, 80], [122, 78], [125, 80], [119, 83]],
        "last_checkup_date": "2022-06-08",
        "next_appointment_date": "2023-12-10"
    },
    "P18945": {
        "name": "Alice Davis",
        "age": 55,
        "gender": "Female",
        "diagnosis": "Diabetes",
        "medications": ["Metformin", "Insulin"],
        "allergies": ["Penicillin"],
        "blood_pressure_checks": [[122, 81], [122, 78], [123, 78], [119, 81]],
        "last_checkup_date": "2023-04-15",
        "next_appointment_date": "No-Date"
    },
    "P69918": {
        "name": "Michael Smith",
        "age": 42,
        "gender": "Male",
        "diagnosis": ["Hypertension", "Celiac Disease"],
        "medications": ["Lisinopril, Hydrochlorothiazide"],
        "allergies": [],
        "blood_pressure_checks": [[175, 95], [155, 89], [145, 100]],
        "last_checkup_date": "2023-05-20",
        "next_appointment_date": "2023-11-20"
    },
    "P13579": {
        "name": "Emily Johnson",
        "age": 33,
        "gender": "Female",
        "diagnosis": "Migraine",
        "medications": ["Sumatriptan", "Ibuprofen"],
        "allergies": ["Codeine"],
        "blood_pressure_checks": [[100, 72], [103, 76], [110, 69], [115, 68], [103, 76]],
        "last_checkup_date": "2023-01-05",
        "next_appointment_date": "2023-12-05"
    }
}

while True:
    # Printing patient data
    patients_ID = input("Insert Patient ID: ")
    if patients_ID in patients:
        print("Name:", patients[patients_ID]["name"])
        print("Age:", patients[patients_ID]["age"])
        print("Gender:", patients[patients_ID]["gender"])
        print("Diagnosis:", patients[patients_ID]["diagnosis"])

        medications = patients[patients_ID]["medications"]
        number_of_medications = len(patients[patients_ID]["medications"])
        print("Medications:", patients[patients_ID]["medications"])
        print("Number of Medications:", number_of_medications)

        allergies = patients[patients_ID]["allergies"]
        number_of_allergies = len(allergies)
        print("Allergies:", patients[patients_ID]["allergies"])
        print("Number of allergies:", number_of_allergies)

    # Patient avarage blood pressure
        bp_checks = patients[patients_ID]["blood_pressure_checks"]
        systolic = 0
        diastolic = 0
        for check in bp_checks:
            systolic += check[0]
            diastolic += check[1]
        systolic_avarage = systolic / len(bp_checks)
        diastolic_avarage = diastolic / len(bp_checks)
        print("Avarage blood pressure:", systolic_avarage, "/", diastolic_avarage)

        if systolic_avarage > 125 or diastolic_avarage > 85:
            print("High Body Pressure")
        elif 115 < systolic_avarage < 125 or 75 < diastolic_avarage < 85:
            print("Normal Body Pressure")
        elif systolic_avarage < 115 or diastolic_avarage < 75:
            print("Low Body Pressure")

    # Time difference between the patient last checkup and next appointment
        from datetime import datetime
        if patients[patients_ID]["next_appointment_date"] == "No-Date":
            print("Patient does not have an upcoming appointment.")
        else:
            last_checkup = datetime.strptime(
                patients[patients_ID]["last_checkup_date"], '%Y-%m-%d')
            next_appointment = datetime.strptime(
                patients[patients_ID]["next_appointment_date"], '%Y-%m-%d')
            time_difference = (next_appointment-last_checkup).days
            print("Time between appointments:", time_difference, "days")

    # Add medication
        while True:
            new_medication = input(
                "Enter the medication to be ADDED from the patient's list: ")
            if new_medication == "None" or new_medication.strip() == "":
                print("No medication included, the current medical prescription will be maintained.")
                break
            elif new_medication in allergies:
                print("The patient is allergic to the medication entered. Please change it or type 'Exit' to maintain the previous medical prescription.")
            elif new_medication in medications:
                print("The medication entered is already prescribed to the patient. If no additional medication is to be added, type 'Exit'.")
            elif new_medication == "Exit":
                break
            else:
                medications.append(new_medication)
                print("Medication(s) added successfully:", medications)
                break
          
    # Remove medication
        while True:
            old_medication = input("Enter the medication to be REMOVED from the patient's list:")
            if old_medication == "None" or old_medication.strip() == "":
                print("No medication removed, the current medical prescription will be maintained.")
                break
            elif old_medication in medications:
                medications.remove(old_medication)
                print("Medication(s) removed successfully:", medications)
                break
            else:
                print("Medication does not belong to the current medical prescription.")
                break

    elif patients_ID == "Exit":
        break
    else:
        print("Patient ID not found. To finish, type Exit.")