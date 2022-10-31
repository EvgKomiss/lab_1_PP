import json
import requests
import csv


def collect_data(url_parse):

    with open("C:/Users/evgen/Desktop/dataset.csv", "w", newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(
            (
                "Date",
                "Value"
            )
        )

    while True:
        json_parse = json.loads(requests.get(url_parse).text)

        url_parse = "http:" + json_parse["PreviousURL"]

        date = str(json_parse["Date"])[0:-15]

        value = json_parse["Valute"]["USD"]["Value"]

        with open("C:/Users/evgen/Desktop/dataset.csv", "a", newline="") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(
                (
                    date,
                    value
                )
            )


def main():
    collect_data("http://www.cbr-xml-daily.ru/archive/2022/10/29/daily_json.js")


if __name__ == '__main__':
    main()
