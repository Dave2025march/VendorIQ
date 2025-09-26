# This file is the entry point of the application. It initializes the application, loads vendor data, and orchestrates the comparison, scoring, and ranking processes.

from vendors.dun_bradstreet import get_dun_bradstreet_data
from vendors.ucc import get_ucc_data
from vendors.livesight import get_livesight_data
from vendors.creditsafe import get_creditsafe_data
from comparator import Comparator
from scorer import Scorer
from ranker import Ranker
from excel_writer import ExcelWriter

def main():
    # Load vendor data
    dnb_data = get_dun_bradstreet_data()
    ucc_data = get_ucc_data()
    livesight_data = get_livesight_data()
    creditsafe_data = get_creditsafe_data()

    # Compare business descriptions
    comparator = Comparator()
    comparison_results = comparator.compare(dnb_data, ucc_data, livesight_data, creditsafe_data)

    # Score the comparisons
    scorer = Scorer()
    scores = scorer.score(comparison_results)

    # Rank the vendors based on scores
    ranker = Ranker()
    ranked_vendors = ranker.rank(scores)

    # Write the results to an Excel sheet
    excel_writer = ExcelWriter()
    excel_writer.write_to_excel(ranked_vendors)

if __name__ == "__main__":
    main()