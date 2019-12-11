# truck_chatbot
The chatbot helps identifing trucks, their specification and number in particular fleet. Customer is Fleet Owner or Fleet manager. End result of conversation is a list of trucks with their specifications and numbers. All conversations are recorded in CSV files timestamped for future analysis.

## Getting Started
Just run the script. Input the data interactively. You can then get the result.
The specifications of the trucks are axle configuration, weight and load.
Possible axle configurations are 4x2, 4x4, 6x2, 6x4, 8x2, 8x4, 10x2, 10x4.
Weight and load are in kg.
The chat log files are saved in CSV format with the name as the timestamp of the end of the chat.
For example: 20191211114311.csv

### Prerequisites
Pandas,csv and datetime library are used.
