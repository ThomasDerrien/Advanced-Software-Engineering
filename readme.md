# Electric Charging Stations Demand Analysis in Berlin
---
## Project Overview
This project analyzes the demand for additional electric vehicle charging stations in Berlin using geovisualization techniques. By examining datasets on population size and the current distribution of charging stations across postal code areas, the project identifies areas with high demand for additional charging infrastructure.

**Objective:**  
The main goal is to highlight areas with a high population density and low availability of charging stations, excluding housing type considerations due to data unavailability.

---
## Final Visualization
The final interactive geovisualization is hosted on Streamlit and can be viewed here:  
[Berlin Electric Charging Stations Heatmap](https://advanced-software-engineering-group6.streamlit.app/)
**Analysis:**

The neighborhoods of Berlin most likely to benefit from an increase in the number of charging stations, based on population density, are as follows:
- Mitte (east part)
- Friedrichshain-Kreuzberg (south and east)
- Pankow (Weißensee and outskirts)
- Neukölln (Britz and south)
- Treptow-Köpenick (Köpenick and Alt-Treptow)


---

## Data Sources `(/Datasets)`
The project utilizes the following publicly available datasets:

1. **Charging Station Infrastructure by Postal Code**  
   Source: [Federal Network Agency](https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/E-Mobilitaet/start.html)  
   - File: `/Ladesaeulenregister.csv`

2. **Population Size by Postal Code**  
   Source: [Postcode Population Size](https://www.suche-postleitzahl.org/downloads)  
   - File: `plz_einwohner.csv`

---


## Repository Structure
The project files and their roles are organized as follows:

- **`main.py`**: The primary script that integrates all functionalities to generate the geovisualization. It uses the functions in `core/methods.py`
- **`requirements.txt`**: Lists Python dependencies for the project environment.
- **`datasets/`**: Directory for storing downloaded datasets (`plz_einwohner.csv`, `ladesaeulen.csv`).
- **`core`**
    - **`core/methods.py`**: Contains methods and utilities for data processing and visualization.
      - **Data Preprocessing:**
        - `sort_by_plz_add_geometry`: Merges datasets by postal codes (PLZ) and geospatial geometries, ensuring proper sorting and filtering.
        - `preprop_lstat`: Prepares data from the *Ladesäulenregister.csv*, focusing on charging stations in Berlin within specific postal code ranges.
        - `preprop_resid`: Processes resident data to map population counts (`Einwohner`) by PLZ.
    
      - **Geospatial Aggregation:**
        - `count_plz_occurrences`: Counts charging stations per PLZ and retains geospatial information for visualization.
    
       - **Streamlit Visualization:**
         - `make_streamlit_electric_Charging_resid`: Generates an interactive heatmap in a Streamlit app, allowing users to toggle between layers:
           - **Residents**: Visualizes population density per postal code using a color gradient.
           - **Charging Stations**: Highlights the density of charging stations per postal code.
    - **`core/HelperTools.py`**
        -   The code provides utility functions for data processing, including serialization, DataFrame manipulation, mathematical operations, and random color generation. Key features include timing function execution, cleaning column names, counting frequencies, and sorting DataFrames.
---

## Local Installation Instructions
To set up the project environment and run the analysis:

1. Clone this repository to your local machine:
   ```bash
        git clone https://github.com/ThomasDerrien/Advanced-Software-Engineering.git
        cd Advanced-Software-Engineering
 2. Install required Python dependencies:

    ```bash
        python -m .venv 
        source .venv/bin/activate
        pip install -r requirements.txt
 3. Run the Streamlit app :

    ```bash
        streamlit run main.py
4. Access the app on [localhost:8051](https://localhost:8051)
