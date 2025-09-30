# UnicornServices
A platform to generate leads and fill last-minute cancellations for appointment-based businesses (hair salons, beauty centers, etc.).

## Project Structure
- `leads-by-zone/`: Landing page for zoned leads.
- `last-minute-appointments/`: Landing page for last-minute bookings.
- `app.py`: Navigation file.

## Setup
1. Clone the repo: `git clone git@github.com-hobby:unicorn-services/unicornservices.git`
2. Activate virtual env: `source unicornservices_venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `streamlit run app.py`

## Venv
deactivate
rm -rf unicornservices_venv/
python3 -m venv unicornservices_venv
source unicornservices_venv/bin/activate
pip install -r requirements.txt
cd app
streamlit run app.py
