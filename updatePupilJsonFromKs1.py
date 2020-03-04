import string
import os, json, sys

def update_pupil_json(pupil_json_file, ks1_dict, update_key):
    print("in update_pupil_json")
    pupil_data_dict = {}
    with open(pupil_json_file, 'r') as fp:
        pupil_data_dict = json.load(fp)
        #print(pupil_data_dict)
    
    fp.close()


    pupil_data_dict[update_key] = ks1_dict
    
    pupil_data_json = json.dumps(pupil_data_dict, indent= 2)
    
    with open(pupil_json_file, 'w') as fp:
        fp.write(pupil_data_json)
    fp.close()
    



if __name__ == "__main__":
    
    #update_key = sys.argv[1]
    #filepath = sys.argv[2]
    #filename = sys.argv[3]
    update_key = 'ks1'
    filepath = '/Users/arunabhamidipati/ArunProjects/python/KTS/'
    filename = 'Ks1.csv'

    if update_key == None:
        update_key = 'ks1'

    if filepath == None:
        filepath = '/Users/arunabhamidipati/ArunProjects/python/KTS/'
    
    if filepath == None:
        filename = 'Ks1.csv'

    # Open Autumn Census file
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
                    update_pupil_json(filepath + pupil_json_filename, data_dict, update_key)
                else:
                    print("Pupil Json not found for PupilMatchingRef: {}".format(data_dict['PupilMatchingRef']))
                    raise
                    

    fp.close()





    # if exists update the file else create the file

