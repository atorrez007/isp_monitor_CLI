
# ISP Monitor CLI

This repository contains a command-line interface (CLI) tool for monitoring your internet service provider (ISP). The tool provides functionality to greet users and run continuous speed tests.

## Installation

 Clone this repository to your local machine:
   ```
   git clone https://github.com/atorrez007/isp_monitor_CLI.git
  ```

Navigate to isp_monitor_CLI directory:
```
cd isp_monitor_CLI
```
Install the necessary dependencies:
```
pip install -r requirements.txt
```
## Usage
To use the ISP Monitor CLI, follow these steps:

Execute the main script:

```
python main.py
```
or
```
python main.py [OPTIONS]
```
You'll be prompted to choose an option:

* hello: Greets the user. Test function that will be replaced later.
* speedtest: Runs a continuous speed test.
  
Choose the desired option by typing either hello or speedtest and pressing Enter.

The speedtest option will run continuous speed tests until you manually stop it (by pressing Ctrl+Z).

Speed test results will be displayed and generated into a test.csv file. Future release will contain chart data of internet improvement and/or degradation performance over time.


## Contributing
* Contributions are welcome! 
* If you have any ideas, enhancements, or bug fixes, feel free to open an issue or submit a pull request.
