#### Problem definition

Check the Wolt_README.md for more information regarding the specifications of the task.

# HTTP Api submission
The project is really well unit tested.
For this project I did not incorporate end to end testing and there are three reasons why I did not.
1. Specifications stated that the solution should be well tested, but did not mention types of testing.
2. I could test the single API end point manually so essentially even the end to end functionality was tested.
3. I had other applications to focus on.
    
Wolt's position with required assignment part gathered around 840 applicants.

## Installation
Before executing any commands, remember to `cd` to the correct folder where the `.venv` directory is located.

## Virtual environment
Activate the virtual environment with one of the following commands:
*linux*
    .venv/Scripts/activate
*windows*
    .venv\Scripts\activate.bat
    .venv\Scripts\activate.ps1

## Running tests
To verify if all tests are discovered, run:
    pytest --collect-only

Ensure that 51 tests are successfully identified.

To execute the pytest tests, use:
    python -m pytest

Confirm that 51 tests pass successfully.

## Running the development server
To run the development server:
    python server.py
	
## Sending a POST request

Send a POST request to `http://127.0.0.1:5000/fee` with an example body as follows:
	{
		"cart_value": 500, 
		"delivery_distance": 2001, 
		"number_of_items": 4, 
		"time": "2024-01-15T13:00:00Z"
	}

The server should respond as follows:
	{
		"delivery_fee": 1000
	}

With cart value of 500 lacking, 5€ needs to get paid. 2001 meter distance
means starting cost 2€ and 
for additional full 2 times 500 meters = 2€, and the left over 1 meter adds 1€ more.
totalling 1000 or 10.00€ for the delivery

## Virtual environment deactivation

To deactivate the virtual environment on Windows, you can use:
    .venv\Scripts\deactivate.bat
