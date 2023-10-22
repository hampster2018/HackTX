import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.sidebar.write("# Manager Dashboard")


def display_team(team_number: int):
    print("displaying team: ", team_number)

    conn = st.experimental_connection("db", type="sql")

    with conn.session as s:
        sql_get_user_forms = f"""
        SELECT users.id, user_name, score, sending_time FROM users
        INNER JOIN form_responses
        ON users.id = form_responses.user_id
        WHERE sending_time >= DATE('now', '-7 days') AND team = {team_number}
    """  # for each user, get a record for each of their forms

        results = s.execute(sql_get_user_forms).fetchall()

        # convert the results to a dataframe
        df = pd.DataFrame(
            results, columns=["user_id", "user_name", "form_response", "sending_time"]
        )

        fig_users = px.bar(df, x="user_name", y="form_response")

        # convert the results to be of the following format:
        # Headers: [date, user1, user2, user3, ...]
        # Rows: [date1, score1, score2, score3, ...]
        # and continue this for the past 7 days

        # get the past 7 days
        sql_get_past_7_days = """
        SELECT DATE('now', '-7 days') as date
        UNION SELECT DATE('now', '-6 days')
        UNION SELECT DATE('now', '-5 days')
        UNION SELECT DATE('now', '-4 days')
        UNION SELECT DATE('now', '-3 days')
        UNION SELECT DATE('now', '-2 days')
        UNION SELECT DATE('now', '-1 days')
        UNION SELECT DATE('now')
        """
        dates = s.execute(sql_get_past_7_days).fetchall()

        # convert the dates to a dataframe
        df_dates = pd.DataFrame(dates, columns=["date"])

        # now add the user scores as columns to the dataframe based on their dates
        for index, row in df_dates.iterrows():
            date = row["date"]
            sql_get_user_scores = """
            SELECT user_name, score FROM users
            INNER JOIN form_responses
            ON users.id = form_responses.user_id
            WHERE sending_time = '{}' AND team = {}
            """.format(
                date,
                team_number,
            )
            scores = s.execute(sql_get_user_scores).fetchall()
            for score in scores:
                df_dates.loc[index, score[0]] = score[1]

        # fill in the missing values with 0
        df_dates = df_dates.fillna(0)

        # make the date column the index
        df_dates = df_dates.set_index("date")

        # make a multiple line graph
        multiple_line_fig = df_dates.plot()

        # make a pie chart and color it based on the scores
        sql_get_user_scores = """
            SELECT score FROM users
            INNER JOIN form_responses
            ON users.id = form_responses.user_id
            WHERE sending_time >= DATE('now', '-7 days') AND team = {}
            """.format(
            team_number,
        )

        scores = s.execute(sql_get_user_scores).fetchall()

        df_scores = pd.DataFrame(scores, columns=["score"])

        # group the df_scores by range of score. 0-0.5 is red, 0.5-0.75 is yellow, 0.75-1 is green
        df_scores["score"] = pd.cut(
            df_scores["score"],
            bins=[0, 0.5, 0.75, 1],
            labels=["red", "yellow", "green"],
        )

        # color_mapper = {"red": "#ff0000", "yellow": "#fdf200", "green": "#00ff00"}
        fig = px.pie(
            df_scores,
            names="score",
            color_discrete_sequence=["#1fd660", "#fdf200", "#e0615e"],
        )
        # fig.update_traces(marker=dict(colors=["red", "yellow", "green"]))

        st.write(f"# Team {team_number + 1}")
        # st.write(df)
        # st.write(df_dates)

        # use two columns to display the charts
        col1, col2 = st.columns(2)

        with col1:
            st.write("## User Scores")
            st.write(df)
            st.write("## User Scores Over Time")
            st.write(df_dates)

        with col2:
            st.write("## User Scores Over Time")
            pd.options.plotting.backend = "plotly"
            st.plotly_chart(multiple_line_fig)
            st.plotly_chart(fig_users)
            st.plotly_chart(fig)


selected_team = st.sidebar.selectbox(
    "Select a Team:",
    ["Team One", "Team Two"],
)

if selected_team == "Team One":
    display_team(0)
else:
    display_team(1)
