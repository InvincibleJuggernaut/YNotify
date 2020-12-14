#Script to read channel IDs
filename='record.txt'

def read():
    with open(filename, 'r') as file:
        list_of_id=file.read().split('\n')[2::6]
        return list_of_id