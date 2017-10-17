'''
    this make use of a concept called recursion to effectively 
    solve the problem of moving the disk from the source tower
    to destination tower using an helper ( auxilliary tower)
'''

def tower_of_hanoi(disk, source, destination, auxilliary):
    if disk == 1:
        print ('move disk from {} to {}'.format(source, destination))
    else:
        tower_of_hanoi(disk-1, source, auxilliary, destination)
        print ('move disk from {} to {}'.format(source, destination))
        tower_of_hanoi(disk-1, auxilliary, destination, source)


tower_of_hanoi(3, 'source', 'destination', 'auxilliary')

