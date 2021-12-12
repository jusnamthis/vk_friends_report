def save_friends(reader, writer):
    for row in reader.browse_friends():
        writer.write(row)
