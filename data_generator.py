#This project analyzes manufacturing production data to identify patterns in defects across machines, shifts, 
# materials, tools, and process types. The goal is to understand which factors may be contributing to higher 
# defect rates and provide insights that could support process improvement and scrap reduction.
#creating a list to store as shifts and respective times

#import Pythonds random module so the program could generate realistic simulated manufacturing records by randomly 
#selecting values from the lists I created
import random
import csv

#create shifts
shifts = ['First 6:00AM-2:30PM', 
          'Second 1:30PM to 9:30PM']

#identify list for materials mostly used in manufacturing shop
materials = ['Steel', 
             '303 Stainless Steel', 
             '304 Stainless Steel', 
             '430 Stainless Steel', 
             '6061 Aluminum',
             '6063 Aluminum', 
             '7075 Aluminum']

#identify if part is a Mill or Lathe job
machine_type = ['Mill', 'Lathe']

#identify list of machines used at manufacturing ship
lathe_machines = ['Miyano_BND',
                  'Big_Wia',
                  'Small_Wia',
                  'Samsung_SL15E']
mill_machines = ['YCM_1',
                 'YCM_2',
                 'YCM_3',
                 'Matsuura_MAM72',
                 'Doosan_HC400_II',
                 'NFX400A']

#idenftify possible defects
defect_types = ['Dent',
                'Thread_Defect',
                'Incorrect_Hole_Size',
                'Incorrect_Depth',
                'Material_Cut_Too_Small',
                'Out_Of_Tolerance',
                'Damage_To_Surface',
                'Burrs_In_Part',
                'Missing_Feature',
                'Incorrect_Engraving',
                'Scratches']

#identify possible causes of defects
possible_causes = ['Tool_On_Machine_Broke',
                   'Incorrect_Print',
                   'Incorrect_Revision_Level',
                   'Operator_Mistake',
                   'Loaded_Part_On_Wrong_Size',
                   'Part_Lifted_On_Machine',
                   'Careless_Deburring',
                   'Programming_Error',
                   'Machine_Broke_Down',
                   'Incorrect_Tool_Used',
                   'Material_Defect',
                   'Measurement_Error',
                   'Improper_Setup',
                   'Damaged_When_Shipped_To_Customer']

#identify if the part has threads
has_threads = ['Yes', 'No']

#identify difficulty of part
process_types = ['Standard',
                 'Tight_Tolerance',
                 'Secondary_Operation',
                 'Surface_Finish_Critical',
                 'High_Precision']

#identify if part is manually deburred
deburr = ['Yes', 'No']

#identify if part has any outside process
outside_process = ['Yes', 'No']

#if part has outside process, which type
type_outside_process = ['Passivation',
                        'Beadblast',
                        'Grinding',
                        'Clear_Chromate',
                        'Clear_Hard_Anodize',
                        'Chem_Film',
                        'Colored_Hard_Anodize',
                        'Gold_Anodize',
                        'Heat_Treatment',
                        'Nickel_Plating',
                        'Electroless_Nickel_Plating',
                        'Zinc_Plating',
                        'White_Paint',
                        'Colored_Paint']

#identify if part needs hardware
hardware = ['Yes', 'No']

#if part needs hardware
hardware_type = ['Fasteners',
                 'Bolts',
                 'Screw',
                 'Dowel_Pins',
                 'Hinge']

# make an empty list to store all records
records = []

# loop to create n records
for i in range(5000):

    #randomize all variable choices
    selected_shift = random.choice(shifts)
    selected_material = random.choice(materials)

    selected_machine_type = random.choice(machine_type)

    if selected_machine_type == 'Lathe':
        selected_machine = random.choice(lathe_machines)
    else: 
        selected_machine = random.choice(mill_machines)

    selected_thread = random.choice(has_threads)

    if selected_thread == 'Yes':
        possible_defects_for_job = defect_types
    else:
        possible_defects_for_job = ['Dent',
                                    'Incorrect_Hole_Size',
                                    'Incorrect_Depth',
                                    'Material_Cut_Too_Small',
                                    'Out_Of_Tolerance',
                                    'Damage_To_Surface',
                                    'Burrs_In_Part',
                                    'Missing_Feature',
                                    'Incorrect_Engraving',
                                    'Scratches']

    selected_process = random.choice(process_types)

    selected_deburr = random.choice(deburr)

    if selected_deburr == 'Yes':
        selected_deburr = 'Manually Deburred'
    else:
        selected_deburr = 'Part_Deburred_On_Machine'

    selected_outside_process = random.choice(outside_process)

    if selected_outside_process == 'Yes':
        if 'Aluminum' in selected_material:
            possible_outside_process_for_job = type_outside_process.copy()
            possible_outside_process_for_job.remove('Heat_Treatment')
            possible_outside_process_for_job.remove('Grinding')
        else :
            possible_outside_process_for_job = type_outside_process
        selected_outside_process_type = random.choice(possible_outside_process_for_job)
    else :
        selected_outside_process_type = 'None'

    selected_hardware = random.choice(hardware)

    if selected_hardware == 'Yes':
        selected_hardware_type = random.choice(hardware_type)
    else:
        selected_hardware_type = 'None'

    #choosing number of parts
    total_parts = random.randint(10, 3000)
    #choosing defect percentage range
    defect_percentage = random.uniform(0.00, 0.05)
    #calculating total amount of defected parts
    defect_count = round(total_parts * defect_percentage)
    #identifying costs
    machine_cost = 75
    deburr_cost = 32 if selected_deburr == 'Manually Deburred' else 10
    outside_cost = 300 if selected_outside_process == 'Yes' else 0
    hardware_cost = 50 if selected_hardware == 'Yes' else 0
    scrap_cost = defect_count * 13
    production_cost = machine_cost + deburr_cost + outside_cost + hardware_cost + scrap_cost

    if defect_count > 0:
        selected_defect = random.choice(possible_defects_for_job)

        if selected_defect == 'Thread_Defect':
            possible_causes_for_defect = ['Tool_On_Machine_Broke',
                                        'Incorrect_Tool_Used',
                                        'Programming_Error',
                                        'Improper_Setup',
                                        'Measurement_Error']

        elif selected_defect == 'Scratches':
            possible_causes_for_defect = ['Careless_Deburring',
                                        'Operator_Mistake',
                                        'Damaged_When_Shipped_To_Customer']

        elif selected_defect == 'Incorrect_Hole_Size':
            possible_causes_for_defect = ['Incorrect_Tool_Used',
                                        'Tool_On_Machine_Broke',
                                        'Programming_Error',
                                        'Improper_Setup']

        elif selected_defect == 'Burrs_In_Part':
            possible_causes_for_defect = ['Careless_Deburring',
                                        'Tool_On_Machine_Broke',
                                        'Incorrect_Tool_Used',
                                        'Operator_Mistake']

        else:
            possible_causes_for_defect = possible_causes

        selected_cause = random.choice(possible_causes_for_defect)
    else:
        selected_defect = 'None'
        selected_cause = 'None'
    record = {
    'Shift': selected_shift,
    'Material': selected_material,
    'Department': selected_machine_type,
    'Machine': selected_machine,
    'Process Type': selected_process,
    'Outside Process': selected_outside_process,
    'Outside Process Type': selected_outside_process_type,
    'Hardware': selected_hardware,
    'Hardware Type': selected_hardware_type,
    'Deburr': selected_deburr,
    'Total Parts': total_parts,
    'Defect Count': defect_count,
    'Defect Rate': round(defect_percentage * 100, 2),
    'Thread': selected_thread,
    'Defect Type': selected_defect,
    'Possible Cause': selected_cause,
    'Production Cost': production_cost}

    records.append(record)

#prints n number of records
for record in records[:5]:
    print('\n------Part Summary-----')
    print('Shift:', record['Shift'])
    print('Material:', record['Material'])
    print('Department:', record['Department'])
    print('Machine:', record['Machine'])
    print('Outside Process:', record['Outside Process'])
    print('Outside Process Type:', record['Outside Process Type'])
    print('Hardware:', record['Hardware'])
    print('Hardware Type:', record['Hardware Type'])
    print('Deburr:', record['Deburr'])
    print('Total Parts:', record['Total Parts'])
    print('Defect Count:', record['Defect Count'])
    print('Defect Rate:', record['Defect Rate'])
    print('Thread:', record['Thread'])
    print('Defect Type:', record['Defect Type'])
    print('Possible Cause:', record['Possible Cause'])
    print('Process Type:', record['Process Type'])
    print('Production Cost:', record['Production Cost'])

#create and put data in csv (comma seperated values) file

with open('manufacturing_defect_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)

print('CSV file created: manufacturing_defect_data.csv')