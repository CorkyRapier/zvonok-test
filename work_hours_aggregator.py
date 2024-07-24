from collections import defaultdict
from typing import List

class WorkHoursAggregator:
    def aggregate(self, records: List[str]) -> dict[list]:
        """
        Считает рабочие часы каждого сотрудника.

        :param records: Список записей, где каждая запись содержит имя сотрудника и отработанные часы.
        """
        work_hours = defaultdict(list)
        
        for record in records:
            name, hours = record.rsplit(' ', 1)
            hours = int(hours)
            work_hours[name].append(hours)

        return work_hours

    def print(self, aggregate_records: dict[list]) -> None:
        """
        Выводит рабочие часы каждого сотрудника в консоль.

        :param aggregate_records: Список агрегированных записей.
        """
        for name, hours in aggregate_records.items():
            hours_str = ', '.join(map(str, hours))
            total_hours = sum(hours)
            print(f"{name}: {hours_str}; sum: {total_hours}")



def main():
    data = [
        "Андрей 9",
        "Василий 11",
        "Роман 7",
        "X Æ A-12 45",
        "Иван Петров 3",
        "Андрей 6",
        "Роман 11",
    ]
    
    aggregator = WorkHoursAggregator()
    aggregate_records = aggregator.aggregate(data)
    aggregator.print(aggregate_records)

if __name__ == "__main__":
    main()