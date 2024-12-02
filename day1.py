class DayOne:

    def handler(self, input_name: str):
        lists = self.load_input_data(input_name)
        sorted_lists = [sorted(lists[0]), sorted(lists[1])]
        return self.get_total_of_differences(sorted_lists)

    def part2_handler(self, input_name: str):
        lists = self.load_input_data(input_name)
        sorted_lists = [sorted(lists[0]), sorted(lists[1])]
        number_counts = self.generate_number_count_dict(sorted_lists[1])
        return self.get_total_of_similarity(sorted_lists[0], number_counts)

    @staticmethod
    def load_input_data(file_name:str) -> list[list[int]]:
        list_one = []
        list_two = []
        with open(file_name, "r")  as f:
            input_data = f.readlines()
        for line in input_data:
            numbers = line.split()
            list_one.append(int(numbers[0]))
            list_two.append(int(numbers[1]))
        return [list_one, list_two]

    @staticmethod
    def get_total_of_differences(sorted_lists: list[list[int]]) -> int:
        total_difference = 0
        for item1, item2 in zip(sorted_lists[0], sorted_lists[1]):
            total_difference += abs(item1 - item2)
        return total_difference

    @staticmethod
    def generate_number_count_dict(list_of_numbers) -> dict[int, int]:
        number_count_dict = {}
        for number in list_of_numbers:
            if number in number_count_dict.keys():
                number_count_dict[number] += 1
            else:
                number_count_dict[number] = 1
        return number_count_dict

    def get_total_of_similarity(self, list_of_numbers: list[int], number_counts: dict[int, int]) -> int:
        total_similarity = 0
        for number in list_of_numbers:
            try:
                total_similarity += number * number_counts[number]
            except KeyError:
                continue
        return total_similarity