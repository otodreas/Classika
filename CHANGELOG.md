# Changelog

All notable changes to this project following v1.0.6 will be documented in this file

## [v1.1.0] - 2026-03-23

TODO:
- Reproducibility fix: DONE
- Parameter logging to output: DONE
- README rewrite
- Progress streaming to UI: DONE
- Advanced config panel: DONE
- Screenshots for README

### Added

1. `amc.py`: Improved app header for clarity
2. `amc.py`: Classification run timer implemented. Shows run time, updates each second
3. `amc.py`: Live log streaming during classification. Program polls `run.log.txt` every second and displays the last 5 lines in the UI
4. `amc.py`: Cancel button now returns user to the start page immediately via `st.rerun()` instead of requiring a second interaction
5. `amc.py`: Status indicators (running, complete, error) and a two-column layout for status and cancel button
6. `amc.py`: Placed advanced settings (voting grids, model-specific parameters) in their own dropdowns
7. `src/classification.py`: Added parsed arguments for all advanced settings
8. `src/utils.py`: Added arguments to `start_classification()` to account for advanced settings
9. `src/utils.py`: Update `start_classification()` to write all advanced model parameters to `run_parameters.json`

### Changed

1. `amc.py`: Crash message reflects the time after which `src/classification.py` crashed.
2. `src/classification.py`: Arranged labels in alphabetical order in `get_species()` to ensure XGBoost and MLP produce identical results when the script is run standalone and with Streamlit
3. `src/utils.py`: Merged stderr into stdout in `start_classification()` (`stderr=subprocess.PIPE` -> `stdout=subprocess.PIPE, stderr=subprocess.STDOUT`) so all subprocess output flows through a single pipe, accommodating `run.log.txt` to be streamed to the UI
4. `amc.py`: Changed parameter name in UI from "CV folds" to "Number of data splits" with a clarifying caption to help users understand that the parameter refers to a train/test split
5. `amc.py`: Moved importer to the top of the UI and placed file importer and general settings in pre-expanded dropdowns to clean UI when classification is running
6. `README.md`: Updated minimum Python version and confirmed that it works locally


### Removed

1. `amc.py`, `src/utils.py`, `src/classification.py`: Removed test size slider since the variable `TEST_SIZE` was not used anywhere in the classification script
