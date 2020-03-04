import string
import os, json

def update_pupil_json(pupil_json_file, autumn_census_dict):
    print("in update_pupil_json")
    pupil_data_dict = {}
    with open(pupil_json_file, 'r') as fp:
        pupil_data_dict = json.load(fp)
        #print(pupil_data_dict)
    
    fp.close()
  
    census_found = False

    # Modify Autumn Census
    for census in pupil_data_dict['census']:
        if census['CensusTerm'] == 'Autumn':
            census.update(autumn_census_dict)
            census_found = True
    
    # Write the new Pupil Json File
    pupil_data_json = json.dumps(pupil_data_dict)
    print(census_found)
    with open(pupil_json_file, 'w') as fp:
        fp.write(pupil_data_json)
    fp.close()
      


    
    
    #pupil_data_dict = json.loads(pupil_data_string)

def create_pupil_json(pupil_json_file, autumn_census_dict):
    print("in Create Pupil json")
    pupil_data_dict = {}
    pupil_data_dict['PupilMatchingRef'] = autumn_census_dict['PupilMatchingRef']
    pupil_data_dict['LA']               = autumn_census_dict['LA']
    pupil_data_dict['Estab']            = autumn_census_dict['Estab']
    pupil_data_dict['URN']              = autumn_census_dict['URN']
    pupil_data_dict['UPN']              = autumn_census_dict['UPN']
    pupil_data_dict['Surname']          = autumn_census_dict['Surname']
    pupil_data_dict['Forename']         = autumn_census_dict['Forename']
    pupil_data_dict['Gender']           = autumn_census_dict['Gender']
    pupil_data_dict['DOB']              = autumn_census_dict['DOB']
    census                              = [autumn_census_dict]
    pupil_data_dict['census'] = census
    
    # Convert dictiorany to json
    pupil_data_json = json.dumps(pupil_data_dict, indent= 2)
    #print(pupil_data_json)
    with open(pupil_json_file, 'w') as fp:
        fp.write(pupil_data_json)
    fp.close()




if __name__ == "__main__":
    # Open Autumn Census file
    filepath = '/Users/arunabhamidipati/ArunProjects/python/KTS/'
    filename = 'AutumnCensus.csv'
    with open(filepath+filename, 'r') as fp:
        # Store line1 as header
        
        # Read File in a loop
        count = 0
        header_list = []
        data_list = []
        data_dict = {}
        #pupil_dict = {}
        pupil_json_filename = ''

        for line in fp:
            filtered_line = ''.join(filter(lambda x: x in string.printable, line))
            #print(filtered_line, end = '')

        
            if count == 0 :
                header_list = filtered_line.split(',')
                #print(header_list)
                count += 1
            else:
                data_list = filtered_line.split(',')
                #print(data_list)
            
                # Create json String from header and line
                data_dict = dict(zip(header_list, data_list))
                

                # Use PupilMatchingRef to search for PupilMatchingRef_pupil.json file
                pupil_json_filename = data_dict['PupilMatchingRef'] + "_pupil.json"
                print(pupil_json_filename)
                if os.path.exists(filepath+pupil_json_filename):
                    update_pupil_json(filepath + pupil_json_filename, data_dict)
                else:
                    create_pupil_json(filepath + pupil_json_filename, data_dict)
                    

    fp.close()





    # if exists update the file else create the file

