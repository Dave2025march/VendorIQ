from openpyxl import Workbook

class ExcelWriter:
    def write_to_excel(self, ranked_vendor_data, output_file):
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Vendor Rankings"

        # Write header
        sheet.append(["Vendor", "Score", "Rank"])

        # Write vendor data
        for vendor, score, rank in ranked_vendor_data:
            sheet.append([vendor, score, rank])

        # Save the workbook
        workbook.save(output_file)