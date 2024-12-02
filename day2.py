class DayTwo:

    def part1_handler(self, input_file: str) -> int:
        number_of_valid_reports = 0
        list_of_rules = [self.are_all_increasing_or_decreasing, self.no_repeated_numbers, self.check_max_difference,
                         self.check_number_difference]
        list_of_reports = self.get_reports_from_input(input_file)
        for report in list_of_reports:
            have_not_removed_number = True
            if all(rule(report) for rule in list_of_rules):
                number_of_valid_reports += 1
            elif have_not_removed_number:
                full_report = [*report]
                for i in range(len(full_report)):
                    have_not_removed_number = False
                    original_report = [*report]
                    report.pop(i)
                    if all(rule(report) for rule in list_of_rules):
                        number_of_valid_reports += 1
                        break
                    else:
                        report = [*original_report]

        return number_of_valid_reports

    @staticmethod
    def get_reports_from_input(input_file) -> list[list[int]]:
        list_of_reports = []
        with open(input_file, "r") as f:
            reports = f.readlines()
        for report in reports:
            list_of_reports.append([int(x) for x in report.split()])
        return list_of_reports


    def are_all_increasing_or_decreasing(self, list_of_numbers) -> bool:
        if list_of_numbers == sorted(list_of_numbers) or list_of_numbers == sorted(list_of_numbers, reverse=True):
            return True
        return False


    def no_repeated_numbers(self, list_of_numbers) -> bool:
        return len(set(list_of_numbers)) == len(list_of_numbers)

    def check_max_difference(self, list_of_numbers) -> bool:
        list_length = len(list_of_numbers)
        max_diff = (list_length - 1) * 3
        actual_diff = abs(list_of_numbers[0] - list_of_numbers[list_length - 1])
        return actual_diff <= max_diff

    def check_number_difference(self, list_of_numbers) -> bool:
        for i in range(len(list_of_numbers) - 1):
            if abs(list_of_numbers[i] - list_of_numbers[i+1]) > 3:
                return False
        return True



