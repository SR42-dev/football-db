import pandas as pd
import streamlit as st
from database import view_all_data, view_only_dealer_names, get_dealer, edit_dealer_data


def update():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['league_id', 'league_name', 'country', 'sponsors', 'current_champions', 'top_scorer'])
    with st.expander("Current data"):
        st.dataframe(df)
    list_of_leagues = [i[0] for i in view_only_dealer_names()]
    selected_leagues = st.selectbox("Leagues to edit", list_of_leagues)
    selected_result = get_dealer(selected_leagues)
    
    if selected_result:
        league_id, league_name, country, current_champion, sponsor, top_scorer = selected_result[0][0], selected_result[0][1], selected_result[0][2], selected_result[0][3], selected_result[0][4], selected_result[0][5]
        
        col1, col2 = st.columns(2)

        '''
        with col1:
            player_id = st.text_input('Player ID', player_id)
            player_name_surname = st.text_input("Player Name", player_name_surname)
            position = st.selectbox("Type: ", ["Forward", "Midfield", "Defender", "Goalkeeper"])
            nationality = st.text_input("Nationality", nationality)

        with col2:
            player_contract_start_date = st.text_input("Contract Start Date (YYYY-MM-DD)", player_contract_start_date)
            player_contract_end_date = st.text_input("Contract End Date (YYYY-MM-DD)", player_contract_end_date)
            age = st.text_input('Age', age)
            current_market_value = st.text_input("Current Market Value (In Millions of USD)", current_market_value)
            
        team_id = st.text_input('Team ID', team_id)
        '''

        col1, col2 = st.columns(2)

        with col1:
            league_id1 = st.text_input('League ID', league_id)
            league_name1 = st.text_input("League Name", league_name)
            country1 = st.text_input("Country of Origin", country)

        with col2:
            sponsor1 = st.text_input("Primary Sponsor", sponsor)
            current_champion1 = st.text_input("Current Champion (Team)", current_champion)
            top_scorer1 = st.text_input('Top Scorer (Player)', top_scorer)

        if st.button("Update League"):
            edit_dealer_data(league_id, league_name, country, sponsor, current_champion, top_scorer, league_id1, league_name1, country1, sponsor1, current_champion1, top_scorer1)
            st.success("Successfully updated record")

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['league_id', 'league_name', 'country', 'sponsor', 'current_champions', 'top_scorer'])
    with st.expander("Updated data"):
        st.dataframe(df2)
