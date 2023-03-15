The data link layer is responsible for something called Framing, which is the division of stream of bits from network layer into manageable units (called frames). Frames could be of fixed size or variable size. In variable-size framing, we need a way to define the end of the frame and the beginning of the next frame. 

But what BIT STUFFING actually is ??
Bit stuffing is the insertion of non information bits into data. Note that stuffed bits should not be confused with overhead bits. 

Overhead bits are non-data bits that are necessary for transmission (usually as part of headers, checksums etc.).


||The following image is the concept of bit stuffing||

![Bit_Byte_Stuffing_2](https://user-images.githubusercontent.com/127016329/225461630-9e29da49-48d5-4806-8f68-8afc0403389c.jpg)




Applications of Bit Stuffing –

i)synchronize several channels before multiplexing
ii)rate-match two single channels to each other
iii)run length limited coding

Disadvantages of Bit Stuffing:

i)The code rate is unpredictable; it depends on the data being transmitted. 
ii)The stuffed bits do not contain any information.

Example of bit stuffing – 
Bit sequence: 110101111101011111101011111110 (without bit stuffing) 
Bit sequence: 110101111100101111101010111110110 (with bit stuffing) 

After 5 consecutive 1-bits, a 0-bit is stuffed.
