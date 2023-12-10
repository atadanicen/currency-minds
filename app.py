from datetime import datetime, timedelta

import pandas as pd
import streamlit as st

from utils import (
    get_currency_list,
    get_currency_rates,
    get_timeseries_rates,
)

st.set_page_config(
    page_title="Currency Converter",
    page_icon="💸",
    layout="wide",
)

st.title("Currency Minds 💸")
currency_list = get_currency_list()
today = datetime.now()
month_ago = today - timedelta(days=365)

tab1, tab2, tab3 = st.tabs(
    ["Currency Converter", "Time Series Data", "Supported Currencies"]
)

with tab1:
    st.title("Currency Converter")
    col1, col2, col3 = st.columns(3)
    amount = col1.number_input("Amount:", min_value=1)
    from_currency = col2.selectbox("From:", list(currency_list.keys()))
    to_currency_list = list(currency_list.keys())
    to_currency_list.remove(from_currency)
    to_currency = col3.selectbox("To:", to_currency_list)

    if from_currency and to_currency:
        currency_data = get_currency_rates(
            amount=amount,
            from_currency=from_currency,
            to_currency=to_currency,
        )
        currency_date = datetime.strptime(currency_data["date"], "%Y-%m-%d").date()
        day_ago = currency_date - timedelta(days=1)

        day_ago_currency_data = get_currency_rates(
            amount=amount,
            from_currency=from_currency,
            to_currency=to_currency,
            date=day_ago.strftime("%Y-%m-%d"),
        )

        rate_current = currency_data["rates"][to_currency]
        rate_day_ago = day_ago_currency_data["rates"][to_currency]
        delta_rate = ((rate_current - rate_day_ago) / rate_day_ago) * 100

        col2.metric(
            label="%s %s =" % (amount, currency_list[from_currency]),
            value="%s %s"
            % (currency_data["rates"][to_currency], currency_list[to_currency]),
            delta="%.3f %%" % delta_rate,
        )
with tab2:
    st.title("Time Series Currency Data")
    col1, col2 = st.columns(2)

    start_date = col1.date_input("Start Date", value=month_ago)
    end_date = col2.date_input("End Date", max_value=today)

    # Validate start date and end date
    if start_date >= end_date:
        st.error(
            "Oops! The adventure of time awaits, but remember, the Start Date cannot be greater or equal to the End Date. Let's choose some valid dates for this journey through currency history!"
        )
    else:
        from_currency = col1.selectbox("From", list(currency_list.keys()))

        to_currency_list = list(currency_list.keys())
        to_currency_list.remove(from_currency)

        to_currency = col2.multiselect(
            "To", to_currency_list, placeholder="You can select multiple currencies"
        )

        if from_currency and to_currency:
            timeseries_data = get_timeseries_rates(
                start_date=start_date,
                end_date=end_date,
                from_currency=from_currency,
                to_currency=",".join(to_currency),
            )
            df = pd.DataFrame.from_dict(timeseries_data["rates"], orient="index")
            df = 1 / df
            if len(to_currency) == 1:
                st.line_chart(df)
            else:
                st.area_chart(df)

            col2.download_button(
                label="Download CSV",
                data=df.to_csv(),
                file_name=f"{from_currency}_{to_currency}_{start_date}_{end_date}.csv",
                mime="text/csv",
            )
with tab3:
    st.title("Supported Currencies")
    df = pd.DataFrame()
    df["Symbol"] = list(currency_list.keys())
    df["Currency"] = list(currency_list.values())
    st.table(df)
