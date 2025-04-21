# # run.py

# import os
# from rasa import run

# def start_rasa_server():
#     # Start the Rasa server using rasa.run() for core NLU and conversations
#     print("Starting Rasa server...")
#     os.system("rasa run --enable-api --cors '*' --debug")

# if __name__ == "__main__":
#     start_rasa_server()
from rasa.__main__ import main

if __name__ == "__main__":
    main()
