import csv
import json
import subprocess
import sys
import tempfile
from pathlib import Path


def test_csv_to_json_stdout():
    with tempfile.TemporaryDirectory() as tmp:
        csv_path = Path(tmp) / "data.csv"
        csv_path.write_text("name,age\nAli,25\nSara,30\n", encoding="utf-8")

        result = subprocess.run(
            [sys.executable, "csv2json.py", str(csv_path)],
            capture_output=True,
            text=True,
            check=True,
        )

        data = json.loads(result.stdout)
        assert data == [{"name": "Ali", "age": "25"}, {"name": "Sara", "age": "30"}]
