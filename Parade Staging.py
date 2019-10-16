#make sure there is standardized input data (length and width in feet)

import math

print('Parade Staging\n')
print('a - Walking')
print('s - Vehicle or Float')
print('d - Animal')
print('f - Animal and Vehicle/Float')
print('g - Animal and Walking')
print('')

group_name = input('Enter entry SOE name.\n')

print('')

prompt = input('Choose an entry type.\n')

#calculating walking group, will add dimensions to a dictionary
if prompt == 'a':
    walk_len = int(input('Enter length of walking group in feet.'))
    walk_width = int(input('Enter width of walking group in feet.'))
    print(group_name, (walk_len * walk_width), 'square feet')

#calculating vehicle or float group 
if prompt == 's':
    park = 171
    vf_len = int(input('Enter length of vehicle or float group in feet.'))
    vf_width = int(input('Enter width of vehicle or float group in feet.'))
    vf_staging = math.ceil(int((vf_len * vf_width) / park))
    print(vf_staging, 'spaces')

#calculating animal group
if prompt == 'd':
    a_park = 171
    a_len = int(input('Enter length of animal group in feet.'))
    a_width = int(input('Enter width of animal group in feet.'))
    print(math.ceil(int((a_len * a_width) / a_park) + 2), 'spaces')
    # +2 gives cushion space

#calculating animal and vehicle / float group
if prompt == 'f':
    avf_park = 171
    avf_len = int(input('Enter length of animal and vehicle / float group in feet.'))
    avf_width = int(input('Enter width of animal and vehicle / float group in feet.'))
    print(math.ceil(int((avf_len * avf_width) / avf_park) + 4), 'spaces')
    # +4 gives cushion space
    
#calculating animal and walking group
if prompt == 'g':
    aw_park = 171
    aw_len = int(input('Enter length of animal and walking group in feet.'))
    aw_width = int(input('Enter width of animal and walking group in feet.'))
    print(math.ceil(int((aw_len * aw_width) / aw_park) + 2), 'spaces')

    


    


