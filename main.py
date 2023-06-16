from stegano import lsb
import time

def hideMessage(imagePath, secretMessage, outputPath):
    try:
        start_time = time.time()
        secretImage = lsb.hide(imagePath, secretMessage)
        secretImage.save(outputPath)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Wiadomość została ukryta w obrazie.")
        print("Czas szyfrowania: {:.4f} sekundy".format(elapsed_time))
    except Exception as e:
        print("Wystąpił błąd podczas ukrywania wiadomości:", str(e))

def revealMessage(imagePath):
    try:
        start_time = time.time()
        secretMessage = lsb.reveal(imagePath)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Ukryta wiadomość:", secretMessage)
        print("Czas odszyfrowania: {:.4f} sekundy".format(elapsed_time))
        print(secretMessage)
    except Exception as e:
        print("Wystąpił błąd podczas odkrywania wiadomości:", str(e))


imagePath = "12mb.jpg"
secretMessage = "alamakota"
outputPath = "12mb_with_message.jpg"

hideMessage(imagePath, secretMessage, outputPath)
# revealMessage(outputPath)
