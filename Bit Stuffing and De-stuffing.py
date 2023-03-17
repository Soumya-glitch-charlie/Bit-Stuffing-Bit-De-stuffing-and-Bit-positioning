# Python code for  bit stuffing, bit de-stuffing, the bit positioning with starting and ending sequence
Bit_stuffing = input('Enter the sequence of bits:  ')
string1 = input('Starting Sequence: ')
string2 = input('Ending Sequence: ')
data_frame = list(Bit_stuffing)

# stuffing and bit positioning
i = 0
A = list()
bit_pos = []
count = 0
while i < len(data_frame):
    A.append(data_frame[i])
    if data_frame[i] == '1':
        count += 1
    else:
        count = 0

    if count == 5:
        A.append('0')
        count = 0
        bit_pos.append(len(string1) + len(A) - 1)
    i += 1
main_data = string1 + ''.join(A) + string2

print(f'The position of the stuffed bit: {bit_pos}')
print(f'After bit stuffing the final sequence: {main_data}')

# de-stuffing
i = 0
main_data2 = ""
while i < len(main_data):
    if i not in bit_pos:
        main_data2 += main_data[i]
    i += 1

print(f'The de-stuffed sequence: {main_data2}')
print("SOUMYADEEP DAS and RITURAJ PAUL")
