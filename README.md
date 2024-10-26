# Disaster Response System Simulation

This project is a simulation of a disaster response system that uses drones to handle various types of disaster alerts. Built using Python and Streamlit, this app provides an interactive dashboard to simulate disaster alerts and dispatch drones to respond to them.

## Project Overview
The Disaster Response System Simulation allows users to view simulated disaster alerts, including disaster type, location, and severity. Users can also select a disaster from the sidebar and dispatch a simulated drone to handle the selected disaster.

## Features
- **Simulated Disaster Alerts**: Displays a list of current disaster alerts with details on type, location, and severity.
- **Drone Dispatch Functionality**: Allows users to select a disaster from a dropdown and simulate the dispatch of a drone to that location.
- **Interactive Dashboard**: Built with Streamlit, offering a user-friendly interface.

## File Descriptions
- **app.py**: The main file for running the disaster response simulation app.
- **README.md**: Documentation file describing the project.

## Installation

### Prerequisites
1. Python 3.6 or higher
2. Install the required library by running:
   ```bash
   pip install streamlit


Running the Application
Open the terminal in the project directory.
Run the Streamlit app:
streamlit run app.py


Usage
Open the Streamlit web app in your browser.
View the disaster alerts on the main dashboard.
In the sidebar, select a disaster type and click "Send Drone" to simulate the dispatch of a drone to handle the selected disaster.
Project Structure
app.py: Main application file for the Streamlit app.
Example Usage
Disaster Alerts:

Type: Fire, Location: Forest Zone A, Severity: High
Type: Earthquake, Location: City Center, Severity: Critical
User Action:

Select "Earthquake" from the sidebar and click "Send Drone".
App Output:

Displays a message indicating that a drone has been successfully dispatched to handle the Earthquake in the City Center.
