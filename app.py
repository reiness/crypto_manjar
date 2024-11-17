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
    st.image('soal.jpg')
    st.title("🕵️‍♂️ Crypt Room Challege ")
    st.write("""Karina terbangun dalam kegelapan, di sebuah ruangan sempit yang berbau busuk 
             dan juga dingin. Dinding-dinding kumuh di sekitarnya tampak ternodai, sementara 
             di depannya, sebuah pesan aneh terlihat mencolok, tertulis dengan apa yang tampak 
             seperti darah segar. Di ujung ruangan, sebuah pintu besi besar berdiri dengan megah 
             namun mengintimidasi, dilengkapi layar berkedip-kedip yang menunggu untuk diisi 
             dengan kode satu-satunya jalan keluar dari ruangan ini.
""")

    st.markdown("### Room 1: 44 Chamber")
    caesar_hint = st.checkbox("Clue Room 1")
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
        st.write("""Karina melangkah ragu memasuki ruangan kedua. Di tengah ruangan, 
                 hanya ada sebuah cermin besar yang memantulkan bayangan samar dirinya. Namun, 
                 ketika dia menatap lebih dalam, bayangannya perlahan menyeringai lebar, meskipun 
                 dia tidak bergerak sama sekali. Dari balik keheningan, terdengar bisikan mengerikan 
                 menggema di sekelilingnya: "Jangan berpaling... atau dia akan keluar.""")
        
        atbash_hint = st.checkbox("Clue Room 2")
        if atbash_hint:
            st.image('mrr.jpg')

        atbash_guess = st.text_input("Your decryption for Room 2:", "")
        if atbash_guess.lower() == "ymuz sqqkm":
            st.success("Benar! Ruang ketiga terbuka.")
            keyword_layer = True

    if keyword_layer:
        st.markdown("### Room 3: Arthropod")
        st.write("""Karina melangkah memasuki ruangan berikutnya, hanya untuk merasakan 
                 lantai di bawah kakinya bergerak perlahan, seolah hidup. Sensasi dingin 
                 menjalar dari bawah, sesuatu yang tak terlihat merayap mengitari kakinya. 
                 Seketika, dia menyadari ada makhluk-makhluk tak kasat mata yang melingkari 
                 tubuhnya, semakin rapat dengan setiap putaran. Cakaran tajam terasa menggores 
                 kulitnya, membuatnya menggigil ngeri saat rasa sakit itu perlahan menjalar, 
                 seakan mereka menikmati penderitaannya.""")
        
        keyword_hint = st.checkbox("Clue Room 3")
        if keyword_hint:
            st.write("Hewan tersebut hanya memiliki dua huruf")

        keyword_guess = st.text_input("Your decryption for Room 3:", "")
        if keyword_guess.lower() == "yoaz trrmo":
            st.success("Benar! Ruang keempat terbuka")
            vigenere_layer = True

    if vigenere_layer:
        st.markdown("### Room 4: Vengèful")
        st.write("""Dengan napas tersengal dan kaki yang terluka, Karina berhasil keluar 
                 dari ruangan sebelumnya, meninggalkan makhluk-makhluk yang nyaris melahapnya. 
                 Dia memasuki ruangan keempat, hanya untuk dihadapkan pada pemandangan yang tak 
                 kalah mengerikan dimana langit-langitnya dipenuhi angka-angka yang bercahaya 
                 merah seperti darah segar, seakan baru ditulis oleh tangan tak kasat mata. 
                 Angka-angka itu tampak hidup, bergerak perlahan-lahan, seolah mengawasi setiap gerakannya.""")

        vigenere_hint = st.checkbox("Clue Room 4")
        if vigenere_hint:
            st.image('number.jpg')

        vigenere_guess = st.text_input("Your decryption for Room 4:", "")
        if vigenere_guess.lower() == "uban perak":
            st.success("Benar! Ruang terakhir terbuka.")
            anagram_layer = True

    if anagram_layer:
        st.markdown("### Room 5: Missed Call")
        st.write("""Karina melangkah ke ruangan selanjutnya dengan berhati-hati. Di tengah 
                 ruangan yang remang-remang, sebuah telepon tua tergeletak di atas meja kayu tua. 
                 Kabelnya menggantung hampir terputus, namun suara deringnya masih menggema, mengisi 
                 keheningan dengan nada yang berulang-ulang. Setiap dentingnya terasa seperti panggilan 
                 dari sesuatu yang tak kasat mata, memutar suara seram yang merayap ke tulang belakangnya, 
                 seakan memanggilnya untuk mengangkat gagang telepon itu.""")

        morse_hint = st.checkbox("Clue Room 5")
        if morse_hint:
            st.audio('room5.mp3')

        anagram_guess = st.text_input("Your decryption for the last room:", "")
        if anagram_guess.lower() == "pekanbaru":
            st.balloons()
            st.success("🎉 Congratulations! You have solved the challenge!")



if __name__ == "__main__":
    cryptography_game()
