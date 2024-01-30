"""
This is a Streamlit app for visualizing happiness data with customization options.
"""
import streamlit as st
import pandas as pd
import plotly.express as px


def main():
    """
    Streamlit app for visualizing happiness data with customization options.
    """
    # Load the dataset (assuming it has a 'year' column)
    df = pd.read_csv("./happy.csv")

    # Set the title for the app
    st.title("Happiness Data Visualization Project")

    # Sidebar for customization options
    st.sidebar.subheader("Customization Options")

    # Create selectboxes for X and Y axis options
    option_x = st.sidebar.selectbox("Select X-axis", ["happiness", "gdp", "generosity"])
    option_y = st.sidebar.selectbox("Select Y-axis", ["happiness", "gdp", "generosity"])

    # Create a selectbox for chart type
    chart_type = st.sidebar.selectbox("Select Chart Type", ["scatter", "line", "bar"])

    # Create a color picker
    selected_color = st.sidebar.color_picker("Select Color", "#1f77b4")

    # Display the subheader with selected axes and chart type
    st.subheader(f"{option_x} vs {option_y} ({chart_type.capitalize()} Chart)")

    # Filter the data based on year (if a 'year' column exists)
    if "year" in df.columns:
        min_year = int(df["year"].min())
        max_year = int(df["year"].max())
        selected_year = st.sidebar.slider(
            "Select Year", min_year, max_year, (min_year, max_year)
        )
        filtered_df = df[
            (df["year"] >= selected_year[0]) & (df["year"] <= selected_year[1])
        ]
    else:
        filtered_df = df

    # Create the chart based on the selected options
    if chart_type == "scatter":
        fig = px.scatter(
            data_frame=filtered_df,
            x=option_x,
            y=option_y,
            color_discrete_sequence=[selected_color],
        )
    elif chart_type == "line":
        fig = px.line(
            data_frame=filtered_df,
            x=option_x,
            y=option_y,
            color_discrete_sequence=[selected_color],
        )
    else:
        fig = px.bar(
            data_frame=filtered_df,
            x=option_x,
            y=option_y,
            color_discrete_sequence=[selected_color],
        )

    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig)


if __name__ == "__main__":
    main()
