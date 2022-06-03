data = open('Task_1_RecordedData.txt', 'rt', encoding='UTF-8')
messages_raw = [line.strip() for line in data]
data.close()
message_serial = []
for line in messages_raw:
    line_li = [z for z in line.split()]
    message_serial.append(line_li)

key = [222, 162, 247, 145, 216, 75, 68, 138, 120, 246, 168, 168, 54, 103, 200, 16, 248, 199, 39, 89, 119, 174, 95, 21, 94, 227, 202, 223]

with open('decoded_text.txt', 'w') as message_file:
    for line in message_serial:
        for i, c in enumerate(line):
            message_file.write(chr(key[i] ^ int(c, 16)))
        message_file.write("\n")