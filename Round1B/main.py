import json
import os
from pipeline import run_pipeline
from datetime import datetime


def main():
    
    input_file = "data/challenge1b_input.json"
    with open(input_file, "r") as f:
        input_data = json.load(f)

    
    persona = input_data["persona"]["role"]
    task = input_data["job_to_be_done"]["task"]

    
    pdf_folder = "data/PDFs"
    pdf_paths = [os.path.join(pdf_folder, doc["filename"]) for doc in input_data["documents"]]

   
    result = run_pipeline(persona, task, pdf_paths)

   
    result["metadata"]["challenge_id"] = input_data["challenge_info"]["challenge_id"]
    result["metadata"]["test_case_name"] = input_data["challenge_info"]["test_case_name"]
    result["metadata"]["description"] = input_data["challenge_info"]["description"]
    result["metadata"]["processing_timestamp"] = str(datetime.now())

    
    with open("output.json", "w") as out_file:
        json.dump(result, out_file, indent=2)

    print("✅ Processing complete. Output written to output.json")


if __name__ == "__main__":
    main()
