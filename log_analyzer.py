import os

log_file = "sample.log"

search_id = input("Enter transaction ID: ")

total_records = 0
info_count = 0
warning_count = 0
error_count = 0

error_messages = []

try:
    with open(log_file, "r") as file:

        for line in file:

            if f"ID={search_id}" in line:

                total_records += 1

                if "INFO" in line:
                    info_count += 1

                elif "WARNING" in line:
                    warning_count += 1

                elif "ERROR" in line:
                    error_count += 1

                    parts = line.split(" ", 4)

                    if len(parts) == 5:
                        error_messages.append(parts[4].strip())


    if total_records == 0:

        print("\nNo records found for ID:", search_id)

    else:

        print("\n--- Log Analysis Report ---")

        print("Transaction ID:", search_id)
        print("Total Records:", total_records)
        print("INFO:", info_count)
        print("WARNING:", warning_count)
        print("ERROR:", error_count)

        print("\nError Messages:")

        if error_messages:

            for message in error_messages:
                print("-", message)

        else:
            print("No errors found")


        os.makedirs("output", exist_ok=True)

        report_file = f"output/report_{search_id}.txt"

        with open(report_file, "w") as report:

            report.write("--- Log Analysis Report ---\n\n")

            report.write(f"Transaction ID: {search_id}\n")
            report.write(f"Total Records: {total_records}\n")
            report.write(f"INFO: {info_count}\n")
            report.write(f"WARNING: {warning_count}\n")
            report.write(f"ERROR: {error_count}\n")

            report.write("\nError Messages:\n")

            if error_messages:

                for message in error_messages:
                    report.write(f"- {message}\n")

            else:
                report.write("No errors found\n")


        print("\nReport saved:", report_file)


except FileNotFoundError:

    print("\nError: sample.log file was not found.")
