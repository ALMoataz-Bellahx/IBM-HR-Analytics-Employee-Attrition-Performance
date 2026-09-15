# Import the streamlit library to build the web application framework
import streamlit as st 
# Import pandas to load and manipulate the dataset
import pandas as pd 
# Import plotly.express to generate the interactive charts for the web page
import plotly.express as px 

# Set the initial configuration of the webpage (Must be the very first Streamlit command)
# We give it a title, set the layout to take up the full screen width, and expand the sidebar
st.set_page_config(page_title="HR Attrition Dashboard", layout="wide", initial_sidebar_state="expanded") 

# Use Streamlit's cache decorator to store the dataset in memory so it doesn't reload on every click
@st.cache_data 
# Define a function to load the dataset
def load_data(): 
    # Read the cleaned CSV file we generated in the Jupyter notebook
    df = pd.read_csv(r'D:\Machine Learning Epsilon 2\Python Notes\IBM HR Analytics Employee Attrition & Performance\Cleaned_HR_Employee_Attrition.csv') 
    # Return the loaded DataFrame so it can be used
    return df 

# Call the function to load the data and store it in the variable 'df'
df = load_data() 

# Add a large main heading to the top of the dashboard
st.title("🛡️ HR Employee Attrition Command Center") 
# Add a smaller subheader using markdown text formatting
st.markdown("### Tactical Overview of Workforce Dynamics") 
# Add a standard text paragraph explaining the dashboard's purpose
st.markdown("This dashboard analyzes employee retention and identifies key risk factors driving attrition.") 

# Create a header text specifically for the left-hand sidebar
st.sidebar.header("Filter Controls") 

# Create a multi-select dropdown menu in the sidebar for users to filter by Department
# 'options' provides the list of unique departments. 'default' pre-selects all of them.
selected_departments = st.sidebar.multiselect(
    "Select Department(s):", 
    options=df['Department'].unique(), 
    default=df['Department'].unique()
)

# Filter the main DataFrame to only include rows where the Department matches the user's sidebar selection
filtered_df = df[df['Department'].isin(selected_departments)] 

# Create three vertical columns side-by-side to display top-level metrics
col1, col2, col3 = st.columns(3) 

# Calculate the total number of employees currently filtered
total_employees = len(filtered_df) 
# Calculate the total number of employees who have 'Yes' in the Attrition column
total_attrition = len(filtered_df[filtered_df['Attrition'] == 'Yes']) 
# Calculate the percentage of attrition, with a fallback to 0 to prevent division by zero errors
attrition_rate = (total_attrition / total_employees) * 100 if total_employees > 0 else 0 

# Open the first column context
with col1:
    # Display a metric card showing the total personnel count
    st.metric("Total Personnel", total_employees) 
# Open the second column context
with col2:
    # Display a metric card showing the total attrition count
    st.metric("Total Attrition", total_attrition) 
# Open the third column context
with col3:
    # Display a metric card showing the attrition percentage, formatted to one decimal place
    st.metric("Attrition Rate", f"{attrition_rate:.1f}%") 

# Draw a horizontal line across the screen to separate sections
st.markdown("---") 

# Create two columns side-by-side for the first row of visual charts
chart_col1, chart_col2 = st.columns(2) 

# Open the first chart column context
with chart_col1:
    # Add a title above the chart
    st.subheader("Attrition by Job Role") 
    # Generate a horizontal grouped bar chart for Job Roles, applying a dark theme
    fig_job = px.histogram(filtered_df, y='JobRole', color='Attrition', barmode='group', orientation='h', template='plotly_dark')
    # Render the plot inside the Streamlit app, forcing it to fill the column width
    st.plotly_chart(fig_job, use_container_width=True) 

# Open the second chart column context
with chart_col2:
    # Add a title above the chart
    st.subheader("Monthly Income vs. Attrition") 
    # Generate a box plot mapping Income distribution against Attrition, applying a dark theme
    fig_income = px.box(filtered_df, x='Attrition', y='MonthlyIncome', color='Attrition', template='plotly_dark')
    # Render the plot inside the Streamlit app, forcing it to fill the column width
    st.plotly_chart(fig_income, use_container_width=True) 

# Draw another horizontal separator line
st.markdown("---") 

# Add a title for a full-width chart at the bottom of the dashboard
st.subheader("OverTime and Attrition Impact") 
# Generate a grouped bar chart to analyze OverTime against Attrition
fig_ot = px.histogram(filtered_df, x='OverTime', color='Attrition', barmode='group', template='plotly_dark')
# Render the OverTime chart to span the entire width of the application
st.plotly_chart(fig_ot, use_container_width=True)