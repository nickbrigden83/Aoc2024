import re

class DayThree:

    def handler(self, file_name):
        file_content = self.get_file_content(file_name)
        pairs = self.get_pairs(file_content)
        total = 0
        for pair in pairs:
            total += (pair[0]*pair[1])
        return total


    @staticmethod
    def get_file_content(file_name: str) -> str:
        with open(file_name, "r") as f:
            content = f.read()
        return content


    def get_pairs(self, content: str) -> list[tuple]:
        regex_expression = r"mul\((?P<num1>\d+),(?P<num2>\d+)\)"
        matches = re.finditer(regex_expression, content)
        match_list = []
        for match in matches:
            match_list.append((int(match.group(1)), int(match.group(2))))
        return match_list
