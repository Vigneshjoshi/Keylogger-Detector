
import keyboard
import time

def detect_keylogger():
    suspicious_keys = ['F12', 'Ctrl', 'Alt', 'Shift']
    detected = False
    
    while True:
        for key in suspicious_keys:
            if keyboard.is_pressed(key):
                print(f"Detected potential keylogger activity: {key} key pressed.")
                detected = True
                # Additional actions can be added here, such as alerting or logging.
                
        time.sleep(0.1)  # Adjust sleep time as needed for performance
        
        if detected:
            break

if __name__ == "__main__":
    print("Starting keylogger detector...")
    detect_keylogger()
