from datetime import datetime, timedelta
from collections import defaultdict


employees = [{'name': 'Bill', 'birthdate': datetime(2004, 7, 27)},
             {'name': 'Jill', 'birthdate': datetime(1985, 6, 18)},
             {'name': 'Kim', 'birthdate': datetime(2000, 7, 25)},
             {'name': 'Jan', 'birthdate': datetime(2005, 7, 22)}]


def get_period():
    current_date = datetime.now()
    start_period = current_date + timedelta(days=5-current_date.weekday())
    return start_period.date(), (start_period + timedelta(6)).date()


def check_epl(list_of_emp: list) -> None:
    result = defaultdict(list)
    current_year = datetime.now().year
    for employee in list_of_emp:
        bd = employee["birthdate"]
        if isinstance(bd, datetime):
            bd = bd.date()
        else:
            bd = datetime.strptime(bd, "%d.%m.%Y").date()
        bd = bd.replace(year=current_year)

        start, end = get_period()

        if start <= bd <= end:
            if bd.weekday() in (5, 6):
                #result["Monday"].append(employee["name"])
                result[bd].append(employee["name"])
            else:
                #result[bd.strftime("%A")].append(bd) 
                result[bd].append(employee["name"])
    return result


if __name__ == "__main__":
    for key, value in check_epl(employees).items():
        if key.strftime("%A") in ["Saturday", "Sunday"]:
            print(f"Monday {value}")
        else:
            print(key.strftime("%A"), value)
        #print(key, [v.strftime("%A") for v in value])
    # for key, value in check_epl(employees).items():
    #     print(key.strftime("%A"), value)
    #print(get_period())
