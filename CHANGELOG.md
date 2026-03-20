# Changelog

All notable changes to this project following v1.0.6 will be documented in this file

## [v1.1.0] - 2026-03-23

### Added

- `amc.py`: Live log streaming during classification. Program polls `run.log.txt` every second and displays the last 5 lines in the UI
- `amc.py`: Cancel button now returns user to the start page immediately via `st.rerun()` instead of requiring a second interaction
- `amc.py`: Status indicators (running, complete, error) and a two-column layout for status and cancel button

### Changed

- `src/classification.py`: Arranged labels in alphabetical order to ensure XGBoost and MLP produce identical results when the script is run standalone and with Streamlit
- `src/utils.py`: Merged stderr into stdout in `start_classification` (`stderr=subprocess.PIPE` -> `stdout=subprocess.PIPE, stderr=subprocess.STDOUT`) so all subprocess output flows through a single pipe and is captured in `run.log.txt`

### Removed
