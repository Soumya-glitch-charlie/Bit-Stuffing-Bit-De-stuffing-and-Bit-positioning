# Bit_Stuffing
Bit Stuffing using Python in Computer Network


But at first what is bit stuffing ??
The data link layer is responsible for something called Framing, which is the division of stream of bits from network layer into manageable units (called frames). Frames could be of fixed size or variable size. In variable-size framing, we need a way to define the end of the frame and the beginning of the next frame. 

Bit stuffing is the insertion of non information bits into data. Note that stuffed bits should not be confused with overhead bits. 

Overhead bits are non-data bits that are necessary for transmission (usually as part of headers, checksums etc.). ![Bit_Byte_Stuffing_2](https://user-images.githubusercontent.com/127016329/225460997-6defae2e-7163-4bdd-b071-d613bf5ca1d5.jpg)


Applications of Bit Stuffing –

1)synchronize several channels before multiplexing
2)rate-match two single channels to each other
3)run length limited coding

Example of bit stuffing – 

Bit sequence: 110101111101011111101011111110 (without bit stuffing) 
Bit sequence: 110101111100101111101010111110110 (with bit stuffing) 

After 5 consecutive 1-bits, a 0-bit is stuffed.  
