import requests


def get_currency_rates(
    amount: int = 10,
    from_currency: str = "EUR",
    to_currency: str = "USD",
    date: str = "latest",
):
    """
    Retrieves the currency rates for converting an amount from one currency to another.

    Args:
        amount (int, optional): The amount to be converted. Defaults to 10.
        from_currency (str, optional): The currency to convert from. Defaults to "EUR".
        to_currency (str, optional): The currency to convert to. Defaults to "USD".
        date (str, optional): The date for which the currency rates are retrieved. Defaults to "latest".

    Returns:
        dict: The response containing the currency conversion rates.
    """
    host_url = "api.frankfurter.app"
    query_params = {"amount": amount, "from": from_currency, "to": to_currency}
    request = requests.get(f"https://{host_url}/{date}", params=query_params)
    response = request.json()
    return response


def get_currency_list():
    """
    Retrieves a list of supported currencies.

    Returns:
        dict: The response containing the list of supported currencies.
    """
    host_url = "api.frankfurter.app"
    request = requests.get(f"https://{host_url}/currencies")
    response = request.json()
    return response


def get_timeseries_rates(
    start_date: str = "2021-12-09",
    end_date: str = "2022-12-09",
    from_currency: str = "EUR",
    to_currency: str = "USD",
):
    """
    Retrieves the timeseries currency rates for a given date.

    Args:
        from_currency (str, optional): The currency to convert from. Defaults to "EUR".

    Returns:
        dict: The response containing the timeseries currency rates.
    """
    host_url = "api.frankfurter.app"
    query_params = {"from": from_currency, "to": to_currency}
    request = requests.get(
        f"https://{host_url}/{start_date}..{end_date}", params=query_params
    )
    response = request.json()
    return response
