log_file = "sample.log"

search_id = input("Enter transaction ID: ")

total_records = 0
info_count = 0
warning_count = 0
error_count = 0

error_messages = []

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
