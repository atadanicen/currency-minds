# Currency Minds

Currency Minds is a simple yet powerful currency converter and time series data visualization tool. It leverages the Frankfurter API to provide accurate and up-to-date foreign exchange reference rates published by the European Central Bank. The data is refreshed around 16:00 CET every working day, ensuring that users have access to the latest currency information.

## Features

1. **Currency Conversion**: Convert currencies easily with the intuitive interface. Select the source currency, target currency, enter the amount, and get the converted value instantly.

2. **Time Series Data Visualization**: Visualize historical currency exchange rates over time. Track trends, analyze patterns, and make informed decisions based on the historical performance of different currencies.

3. **CSV Download**: Download time series currency data in CSV format for further analysis or record-keeping. This feature allows users to save and share historical exchange rate data seamlessly.

## Technologies Used

- **[Frankfurter API](https://www.frankfurter.app)**: The project relies on the Frankfurter API to fetch accurate and timely foreign exchange reference rates published by the European Central Bank.

- **[Streamlit](https://streamlit.io)**: The user interface is built using Streamlit, a Python library for creating interactive web applications with minimal effort.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/atadanicen/currency-minds.git
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
3. Run the Streamlit app:
     ```bash
    streamlit run app.py
This will launch the app in your default web browser.

# Usage

1. ### Currency Conversion:
    - Choose the source and target currencies from the dropdown menus.
    - Enter the amount you want to convert.
    - Click the "Convert" button to see the converted amount.
2. ### Time Series Data Visualization:
    - Navigate to the "Time Series" section.
    - Select the currencies and time range for the data.
    - Visualize the historical exchange rates using the interactive plot.
3. ### CSV Download:
    - In the "Time Series" section, after visualizing the data, click on the "Download CSV" button to download the time series data in CSV format.

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, feel free to open an issue or submit a pull request.