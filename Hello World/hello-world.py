# Import datetime to enable time functionality.
from datetime import datetime

def main():
    # Display "Hello World!"
    print("Hello World!")
    # Ask the user for their name.
    name = input("What is your name? \n> ")
    # Note the current date and time from their computer. 
    time = datetime.now()
    # Greet the user.
    print(f"It's nice to meet you, {name}!")
    # Acknowledge when the user entered their name.
    print(f"{time.strftime('I met you on %A, %B %d at %I:%M %p.')} ")
    

# Enable testing with pytest.
if __name__ == "__main__":
    main()