# Ciphers
This is a project to implement different crypto systems.
The crypto system ciphers would be gradually added and a short notes on how they are implemented would be updated below

# Preprocess Data
The preprocess function is to read data from a file and performs a regular expression search to do below 
remove special characters, convert the upper case to lower case remove spaces 
Finally returns a string of lower case alphabetic characters (a-z)


# Shift Cipher 
This is a special case of substitution cipher. Decrypt and encrypt functions would accept a key and a text as params
Encrypt and Decrypt functions would return encrypted text and decrypted text respectively


# Affine Cipher
This is another special case of substitution cipher. Decrypt and Encrypt functions would take 2 keys and a text as params
Encrypt and Decrypt functions would return encrypted text and decrypted text respectively


# Vigenere Cipher
This is also another special case of subsitution cipher. Decrypt and Encrypt functions would take a string as key and a text
Encrypt and Decrypt functions would return encrypted text and decrypted text respectively


# Permutation Cipher
This is a subset of substitution cipher method where we would encrypt using a permutation p(array) and a value m indicating the length of the key i.e array p. Encrypt and Decrypt functions are implemented. Inverse of the permutation is calculated which is used for decryption.

# Involutory keys
The number of involutory keys for affine cipher and permutation cipher are calculated for any given size i.e m value for affine and any permuatation for permutation cipher. A key is called involutory key if the encryption key is the same as decryption key. These calls fall under the same mathemtical group, quite useful during cryptanalysis, studying of the strenght of the various crypto systems implemented so far.
