import streamlit as st

# Cipher decryption functions
def caesar_cipher_decrypt(ciphertext, shift):
    shift = shift % 26
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[-shift:] + alphabet[:-shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return ciphertext.translate(table)

def atbash_cipher_decrypt(ciphertext):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    reversed_alphabet = alphabet[::-1]
    table = str.maketrans(alphabet, reversed_alphabet)
    return ciphertext.translate(table)

def keyword_cipher_decrypt(ciphertext, key):
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher_alphabet = key + ''.join([char for char in alphabet if char not in key])
    table = str.maketrans(cipher_alphabet, alphabet)
    return ciphertext.translate(table)

def vigenere_cipher_decrypt(ciphertext, key):
    key = key.lower()
    ciphertext = ciphertext.lower()
    plaintext = []
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            plaintext.append(decrypted_char)
            key_index += 1
        else:
            plaintext.append(char)

    return ''.join(plaintext)

def cryptography_game():
    st.title("🕵️‍♂️ Crypt Room Challege ")
    st.write("""Karina terbangun di sebuah ruangan gelap.
            Dinding-dindingnya dipenuhi dengan simbol-simbol aneh dan satu-satunya cahaya berasal dari sebuah lilin yang berkedip-kedip. 
             Di seberang ruangan, sebuah pintu besi besar terpasang kokoh. Di atas pintu, terukir kode misterius: ykcx eggmk.""")

    st.markdown("### Room 1: 44 Chamber")
    caesar_hint = st.checkbox("Minta bantuan makhluk halus")
    if caesar_hint:
        st.write("Kaisar tahun depan")

    caesar_guess = st.text_input("Your decryption for Room 1:", "")
    if caesar_guess.lower() == "bnfa hjjpn":
        st.success("Benar! Ruang kedua terbuka.")
        atbash_layer = True
    else:
        atbash_layer = False

    # Ensure variables are initialized before usage
    keyword_layer = False
    vigenere_layer = False
    anagram_layer = False

    if atbash_layer:
        st.markdown("### Room 2: Looking Glass")
        st.write("""Karina melangkah ke ruangan kedua. Hanya ada sebuah cermin besar di tengah ruangan dengan bingkai penuh ukiran simbol aneh. 
                 Saat dia melihat ke dalam cermin, bayangannya tiba-tiba tersenyum sendiri, meski dia tak bergerak. 
                 Suara berbisik terdengar: 'Jangan berpaling, atau dia akan keluar'""")
        
        atbash_hint = st.checkbox("Minta bantuan pada cermin")
        if atbash_hint:
            st.image('mrr.jpg')

        atbash_guess = st.text_input("Your decryption for Room 2:", "")
        if atbash_guess.lower() == "ymuz sqqkm":
            st.success("Benar! Ruang ketiga terbuka.")
            keyword_layer = True

    if keyword_layer:
        st.markdown("### Room 3: Arthropod")
        st.write("""Karina memasuki ruangan berikutnya dengan lantai yang bergerak sendirinya. 
                 Makhluk seperti serangga besar berbentuk kunci mulai mengelilinginya. 
                 Di sudut ruangan, terlihat pintu kayu kecil, satu-satunya jalan keluar.
                 """)
        
        keyword_hint = st.checkbox("Minta bantuan pada makhluk misterius")
        if keyword_hint:
            st.write("Dua huruf apa yang hewan?")

        keyword_guess = st.text_input("Your decryption for Room 3:", "")
        if keyword_guess.lower() == "yoaz trrmo":
            st.success("Benar! Ruang keempat terbuka")
            vigenere_layer = True

    if vigenere_layer:
        st.markdown("### Room 4: Vengèful")
        st.write("""Karina berhasil mencapai pintu kayu dan masuk ke ruangan keempat. 
                 Di sana, dindingnya dipenuhi angka yang berwarna merah darah. 
                 Di tengah ruangan, sebuah meja kecil dengan secarik kertas bergambarkan kunci yang berulang.
        """)

        vigenere_hint = st.checkbox("Lihat darah pada dinding")
        if vigenere_hint:
            st.write("1, 2, 3, 4, 5, ..., 7, 8, 9")

        vigenere_guess = st.text_input("Your decryption for Room 4:", "")
        if vigenere_guess.lower() == "uban perak":
            st.success("Benar! Ruang terakhir terbuka.")
            anagram_layer = True

    if anagram_layer:
        st.markdown("### Room 5: Missed Call")
        st.write("""Karina melangkah ke ruangan selanjutnya. Di sana, sebuah telepon tua tergeletak di meja. 
                 Meski tidak terhubung dengan apapun, telepon itu terus berdering, memutar suara yang sama berulang-ulang.""")
        

        morse_hint = st.checkbox("Dengarkan suara pada telepon")
        if morse_hint:
            st.audio('room5.mp3')

        anagram_guess = st.text_input("Your decryption for the last room:", "")
        if anagram_guess.lower() == "pekanbaru":
            st.balloons()
            st.success("🎉 Congratulations! You have solved the challenge!")
        else:
            st.error("Try again!")


if __name__ == "__main__":
    cryptography_game()
