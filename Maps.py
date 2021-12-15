#https://coronavirus.data.gov.uk/details/developers-guide/main-api#structure-example
#https://covid-19.geohive.ie/datasets/a0e3a1c53ad8422faf00604ee08955db_0/api

from requests import get


def get_data(url):
    response = get(endpoint, timeout=10)

    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: {response.text}')

    return response.json()


if __name__ == '__main__':
    endpoint = (
        'https://api.coronavirus.data.gov.uk/v1/data?'
        'filters=areaType=nation;areaName=england&'
        'structure={"date":"date","newCases":"newCasesByPublishDate"}'
    )

    data = get_data(endpoint)
    print(data)