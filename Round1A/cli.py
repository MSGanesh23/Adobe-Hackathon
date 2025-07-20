from pathlib import Path
import json
from process_pdf import extract_outline  

def process_pdfs():
    input_dir = Path("/app/input")
    output_dir = Path("/app/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    for pdf_file in input_dir.glob("*.pdf"):
        print(f"Processing {pdf_file.name}")
        result = extract_outline(pdf_file)

        output_path = output_dir / f"{pdf_file.stem}.json"
        with open(output_path, "w") as f:
            json.dump(result, f, indent=2)

        print(f"Saved: {output_path.name}")

if __name__ == "__main__":
    process_pdfs()
