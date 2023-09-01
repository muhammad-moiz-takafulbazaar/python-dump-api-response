import requests
import pandas as pd

def main():
    url = "https://type.fit/api/quotes"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)  # Create a DataFrame from the JSON data
        
        csv_filename = "api_data.csv"
        df.to_csv(csv_filename, index=False)  # Save the DataFrame to a CSV file
    else:
        print("Failed to fetch data from the API")

if __name__ == "__main__":
    main()
