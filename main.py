import os

if __name__ == '__main__':
    print("Welcome to lobo speaker1.1. Created my Mudit")
    while True:
        x = input("Enter what you want to speak")
        if x == "q":
            break
        command = f'powershell -Command "Add-Type -AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\');"'

        os.system(command)


