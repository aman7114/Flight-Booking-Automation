# Flight Booking Automation

Pytest and Playwright end-to-end tests for the flight booking scenarios on [QAPractice](https://www.qapractice.com/). The suite uses the Page Object Model to keep browser interactions separate from test scenarios.

## Tech Stack

- Python
- pytest
- Playwright for Python
- `pytest-playwright` for the pytest browser fixture
- `pytest-html` for HTML reports

## Project Structure

```text
.
|-- pages/                 # Page Object Model classes
|-- test_data/             # Reusable flight and passenger data
|-- tests/                 # pytest test scenarios
|-- reports/               # Generated HTML test report
|-- utils/                 # Project utilities and configuration
|-- pytest.ini             # pytest paths, base URL, and default options
|-- requirements.txt       # Python dependencies
```

## Prerequisites

- Python 3.9 or later
- Internet access to reach `https://www.qapractice.com`

## Installation

Create and activate a virtual environment from the project root.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
playwright install
```

### macOS or Linux

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
playwright install
```

`playwright install` downloads the browser binaries used by the tests. If PowerShell blocks script activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Running the Tests

Run the complete suite from the project root:

```bash
pytest
```

The default configuration in `pytest.ini`:

- Discovers tests in `tests/`.
- Uses `https://www.qapractice.com` as the Playwright `base_url`.
- Opens the booking flow at `/flight-booking-scenarios`.
- Runs in verbose mode.
- Writes a self-contained report to `reports/report.html`.

Run a specific test module:

```bash
pytest tests/test_flight_booking.py
```

Run a single test by name:

```bash
pytest -k test_one_way_flight_booking
```

Run with a visible browser for troubleshooting:

```bash
pytest --headed
```

Run with a slower browser interaction speed:

```bash
pytest --headed --slowmo 500
```

## Test Coverage

- One-way and round-trip flight booking through confirmation.
- Flight search validation for empty cities and identical origin/destination.
- Return-date visibility for one-way searches.
- Flight sorting by ascending price.
- Nonstop flight filtering.
- Continue-button state before and after selecting a flight.
- Invalid passenger email validation.

## Test Data

Reusable booking values are stored in `test_data/flight_data.py`. They are intended for the practice site only. Do not replace them with real passenger, payment-card, or other sensitive information.

## Reports

After a test run, open [`reports/report.html`](reports/report.html) in a browser to view the self-contained pytest HTML report.

## Troubleshooting

- **Browser executable missing:** run `playwright install` after activating the virtual environment.
- **Tests cannot reach the page:** verify internet access and that `https://www.qapractice.com` is available.
- **PowerShell activation fails:** use the temporary execution-policy command shown in the installation section, or activate the environment through Command Prompt with `.venv\\Scripts\\activate.bat`.
