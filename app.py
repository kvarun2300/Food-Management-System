import streamlit as st

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}
h1, h2, h3 {
    font-weight: 700;
}
.stSelectbox, .stTextInput, .stNumberInput {
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Food Wastage System", layout="wide")

# ---------------- SIDEBAR ----------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Project Introduction",
        "View Tables",
        "CRUD Operations",
        "SQL Queries & Visualization",
        "Learn SQL Queries",
        "User Introduction",
    ],
)

# ---------------- MAIN CONTENT ----------------

# 1️⃣ PROJECT INTRODUCTION
if page == "Project Introduction":
    st.title("Local Food Wastage Management System")

    st.write("""
    This project helps manage manage surplus food and reduce wastage by connecting providers and receivers.
    """)

    st.markdown("""
    - **Providers:** Restaurants, households, and businesses list surplus food.
    - **Receivers:** NGOs and individuals claim available food.
    - **Geolocation:** Helps locate nearby food.
    - **SQL Analysis:** Powerful insights using SQL queries.
    """)

elif page == "View Tables":
    st.title("📊 View Tables")

    import pandas as pd

    table = st.selectbox(
            "Select Table",
            ["Providers", "Receivers", "Food Listings", "Claims"]
        )

    if table == "Providers":
        df = pd.read_csv("/content/sample_data/providers.csv")
    elif table == "Receivers":
        df = pd.read_csv("/content/sample_data/receivers.csv")
    elif table == "Food Listings":
        df = pd.read_csv("/content/sample_data/food_listings.csv")
    else:
        df = pd.read_csv("/content/sample_data/claims.csv")

    st.dataframe(df, use_container_width=True)

elif page == "CRUD Operations":
    st.title("CRUD Operations")

    import pandas as pd

    table = st.selectbox(
        "Select Table",
        ["providers", "receivers", "food_listings", "claims"]
    )

    file_map = {
        "providers": "/content/sample_data/providers.csv",
        "receivers": "/content/sample_data/receivers.csv",
        "food_listings": "/content/sample_data/food_listings.csv",
        "claims": "/content/sample_data/claims.csv"
    }

    df = pd.read_csv(file_map[table])

    operation = st.selectbox("Select Operation", ["Add", "Update", "Delete"])

    st.divider()

    # ---------------- ADD ----------------
    if operation == "Add":
        st.subheader("Add Record")

        with st.form("add_form"):
            inputs = {}
            for col in df.columns:
                inputs[col] = st.text_input(col)

            submitted = st.form_submit_button("Add")

            if submitted:
                df = pd.concat([df, pd.DataFrame([inputs])], ignore_index=True)
                df.to_csv(file_map[table], index=False)
                st.success("Record Added Successfully!")

    # ---------------- UPDATE ----------------
    elif operation == "Update":
        st.subheader("Update Record")

        index = st.number_input("Row Index", 0, len(df)-1)

        with st.form("update_form"):
            updated = {}
            for col in df.columns:
                updated[col] = st.text_input(col, value=str(df.loc[index, col]))

            submitted = st.form_submit_button("Update")

            if submitted:
                for col in df.columns:
                    df.loc[index, col] = updated[col]

                df.to_csv(file_map[table], index=False)
                st.success("Updated Successfully!")

    # ---------------- DELETE ----------------
    elif operation == "Delete":
        st.subheader("Delete Record")

        index = st.number_input("Row Index to Delete", 0, len(df)-1)

        if st.button("Delete"):
            df = df.drop(index)
            df.to_csv(file_map[table], index=False)
            st.success("Deleted Successfully!")

elif page == "SQL Queries & Visualization":
    st.title("SQL Analysis")

    import pandas as pd

    query_option = st.selectbox(
        "Choose a Query",
        [
            "1. Providers & Receivers per City",
            "2. Provider Type Contributing Most Food",
            "3. Provider Contact by City",
            "4. Top Receivers by Food Claimed",
            "5. Total Food Available",
            "6. City with Most Listings",
            "7. Most Common Food Types",
            "8. Claims per Food Item",
            "9. Provider with Most Successful Claims",
            "10. Claim Status Percentage",
            "11. Avg Food Claimed per Receiver",
            "12. Most Claimed Meal Type",
            "13. Food Donated per Provider"
        ]
    )

    # Load datasets
    providers = pd.read_csv("/content/sample_data/providers.csv")
    receivers = pd.read_csv("/content/sample_data/receivers.csv")
    food = pd.read_csv("/content/sample_data/food_listings.csv")
    claims = pd.read_csv("/content/sample_data/claims.csv")

    # ---------------- QUERY 1 ----------------
    if query_option.startswith("1"):
        p = providers.groupby("City").size().reset_index(name="Providers")
        r = receivers.groupby("City").size().reset_index(name="Receivers")
        result = pd.merge(p, r, on="City", how="outer").fillna(0)

    # ---------------- QUERY 2 ----------------
    elif query_option.startswith("2"):
        result = food.groupby("Provider_Type")["Quantity"].sum().reset_index().sort_values(by="Quantity", ascending=False)

    # ---------------- QUERY 3 ----------------
    elif query_option.startswith("3"):
        city = st.text_input("Enter City")
        if city:
            result = providers[providers["City"].str.lower() == city.lower()][["Name", "Contact"]]
        else:
            result = pd.DataFrame()

    # ---------------- QUERY 4 ----------------
    elif query_option.startswith("4"):
        merged = claims.merge(food, on="Food_ID").merge(receivers, on="Receiver_ID")
        result = merged[merged["Status"] == "Completed"].groupby("Name")["Quantity"].sum().reset_index().sort_values(by="Quantity", ascending=False)

    # ---------------- QUERY 5 ----------------
    elif query_option.startswith("5"):
        result = pd.DataFrame({"Total Food Available": [food["Quantity"].sum()]})

    # ---------------- QUERY 6 ----------------
    elif query_option.startswith("6"):
        result = food["Location"].value_counts().reset_index()
        result.columns = ["City", "Total Listings"]

    # ---------------- QUERY 7 ----------------
    elif query_option.startswith("7"):
        result = food["Food_Type"].value_counts().reset_index()
        result.columns = ["Food Type", "Count"]

    # ---------------- QUERY 8 ----------------
    elif query_option.startswith("8"):
        merged = food.merge(claims, on="Food_ID", how="left")
        result = merged.groupby("Food_Name")["Claim_ID"].count().reset_index()
        result.columns = ["Food Name", "Total Claims"]

    # ---------------- QUERY 9 ----------------
    elif query_option.startswith("9"):
        merged = providers.merge(food, on="Provider_ID").merge(claims, on="Food_ID")
        result = merged[merged["Status"] == "Completed"].groupby("Name")["Claim_ID"].count().reset_index().sort_values(by="Claim_ID", ascending=False)

    # ---------------- QUERY 10 ----------------
    elif query_option.startswith("10"):
        total = len(claims)
        result = claims["Status"].value_counts().reset_index()
        result.columns = ["Status", "Count"]
        result["Percentage"] = (result["Count"] / total * 100).round(2)

    # ---------------- QUERY 11 ----------------
    elif query_option.startswith("11"):
        merged = claims.merge(food, on="Food_ID")
        temp = merged[merged["Status"] == "Completed"].groupby("Receiver_ID")["Quantity"].sum()
        result = pd.DataFrame({"Average Food per Receiver": [temp.mean()]})

    # ---------------- QUERY 12 ----------------
    elif query_option.startswith("12"):
        merged = claims.merge(food, on="Food_ID")
        result = merged[merged["Status"] == "Completed"]["Meal_Type"].value_counts().reset_index()
        result.columns = ["Meal Type", "Count"]

    # ---------------- QUERY 13 ----------------
    elif query_option.startswith("13"):
        result = food.groupby("Provider_ID")["Quantity"].sum().reset_index()

    # ---------------- DISPLAY ----------------
    st.divider()
    st.subheader("Result")

    if 'result' in locals():
        st.dataframe(result, use_container_width=True)

elif page == "Learn SQL Queries":
    st.title("Learn SQL Queries")
    st.write("This section will provide resources to learn SQL queries.")

elif page == "User Introduction":
    st.title("About the Creator")

    st.write("**Name:** Varun")
    st.write("**Role:** Data Analyst")
