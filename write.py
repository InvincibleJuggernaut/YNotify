filename='record.txt'

def store(title, description, channel_id):
    with open(filename, 'a') as file:
        file.write(title+"\n")
        file.write(description+"\n")
        file.write(channel_id+"\n\n")
        file.write("-X-X-X-X-\n\n")
