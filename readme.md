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

---
## Interpretation of Results
Two geovisualizations were analyzed:

1. Population Density Map: Highlights areas of Berlin with varying population densities.
2. Charging Station Map: Displays the density and distribution of electric vehicle (EV) charging stations across the city.

### Observations from the Maps

1. Population Density :

   High-density areas (red zones) are predominantly located in central Berlin, such as neighborhoods in Mitte and Friedrichshain-Kreuzberg.
   Moderate-density areas (orange zones) extend outward to parts of Neukölln, Wedding, and the southern parts of Lichtenberg.
   Low-density areas (yellow zones) are in the outer regions, particularly to the north and southwest of the city.

2. Charging Station Coverage :

   High charging station density is concentrated in central urban areas, such as Mitte and Charlottenburg-Wilmersdorf.
   Lower station density is seen in the peripheral areas, such as Marzahn-Hellersdorf, Falkenberg, and parts of Spandau.

### Analysis
Using the maps, we identified areas with high population density but insufficient EV charging infrastructure.


**Central Berlin**: Areas with high population density already have a good number of charging stations. More stations could be added to prevent the population growth. 

**Outer areas with moderate density**: Areas such as Neukölln, Kreuzberg, and eastern parts of Lichtenberg and Friedrichshain are underserved despite their moderate to high population density.

**Peripheral regions**: While some low-density areas might rely on private charging solutions, regions with detached housing and moderate density show potential for public charging stations.

### Suggestions : 
1. High Priority Areas:

   * Neukölln, Kreuzberg :
     * High population density.
   Low to moderate station coverage—expansion here could address a significant portion of unmet demand.

   * Friedrichshain:
     * High population density and is home to many environmentally conscious residents, increasing the demand for electric vehicles. While the area has some charging stations, they are insufficient to meet the growing need.

   * Mitte:

      * High-density area with significant commuter and residential activity. Expansion of existing infrastructure can future-proof demand.

   
   


---

## Data Sources `(/Datasets)`
The project utilizes the following publicly available datasets:

1. **Charging Station Infrastructure by Postal Code**  
   Source: [Federal Network Agency](https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/E-Mobilitaet/start.html)  
   - File: `Ladesaeulenregister.csv`

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
