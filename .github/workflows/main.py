import pandas as pd
from scorer import score_description

def main():
    # Update this path to your actual Excel file
    input_file = "../input.xlsx"
    output_file = "../output.xlsx"

    # Read the Excel file (assuming all vendor data is in one sheet for simplicity)
    df = pd.read_excel(input_file)

    # Columns: 'Company Name', 'Internal Format', 'D&B', 'UCC', 'Livesight', 'Creditsafe'
    vendor_cols = ['D&B', 'UCC', 'Livesight', 'Creditsafe']
    results = []

    for idx, row in df.iterrows():
        internal_format = row['Internal Format']
        company_name = row['Company Name']
        vendor_scores = []
        for vendor in vendor_cols:
            desc = row[vendor]
            score = score_description(str(desc), str(internal_format))
            vendor_scores.append((vendor, desc, score))
        # Sort by score descending, break ties randomly
        vendor_scores.sort(key=lambda x: x[2], reverse=True)
        top_score = vendor_scores[0][2]
        top_vendors = [v for v in vendor_scores if v[2] == top_score]
        import random
        winner = random.choice(top_vendors)
        results.append({
            'Company Name': company_name,
            'Vendor': winner[0],
            'Business Description': winner[1],
            'Score': winner[2],
            'Rank': 1
        })

    # Output to new sheet
    result_df = pd.DataFrame(results)
    with pd.ExcelWriter(output_file, engine='openpyxl', mode='w') as writer:
        df.to_excel(writer, sheet_name='All Data', index=False)
        result_df.to_excel(writer, sheet_name='Top Ranked', index=False)

if __name__ == "__main__":
    main()