# OSMStats

OSMStats is a Python bot for tweeting OpenStreetMap statistics.

## Features

- Scrape OpenStreetMap statistics from websites
- Format the data
- Tweet statistics automatically

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/sammyhawkrad/osmstats.git
    ```
2. Navigate to the project directory:
    ```sh
    cd osmstats
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
   ```
4. Set up your environment variables for Twitter API credentials:

    ```sh
    export CONSUMER_KEY="your_consumer_key"
    export CONSUMER_SECRET="your_consumer_secret"
    export ACCESS_TOKEN="your_access_token"
    export ACCESS_TOKEN_SECRET="your_access_token_secret"
    ```
5. Specify the period (Day, Week, Month) you want to tweet for:

    ```sh
    export SCHEDULE = "Day"
    ```

## Usage

Run script to Tweet:
```sh
python tweet.py
```


## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Licence

This project is licensed under the MIT Licence. See the [LICENCE](LICENCE) file for details.


