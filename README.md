#Python file for bit stuffing
Bit_stuffing = input('Enter the sequence of bits: ')
data_frame = list(Bit_stuffing)

count = 0
i = 0
while(i<len(data_frame)):
    if data_frame[i]=='1':
          count+=1
    else: 
          count=0
    
    if count==6:
          data_frame.insert(i,'0')  
          count = 0
    i+=1
string = ''
string = ''.join(data_frame)
print(f'After bit stuffing the final sequence:{string}')

