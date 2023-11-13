def main():
    from src.API_getters.api_hh import APIHeadhunter
    from src.API_getters.api_sj import APISuperJob
    from src.file_handlers.handler_json import JSONHandler

    api_hh = APIHeadhunter
    api_sj = APISuperJob
    handler = JSONHandler

    api_hh.save_data()
    api_sj.save_data()

    handler.save_vacancies_hh()
    handler.save_vacancies_sj()

    hh_or_sj = input("Откуда интересуют вакансии #1 Superjob или #2 Headhunter? ")
    keyword = input("Какую профессию ищем? ")
    salary_min = input("напишите минимальную зп для фильтрации ")
    top = input("сколько вывести вакансий? ")

    if hh_or_sj == "1":
        professions = handler.get_sorted_vacancies_hh(top, int(salary_min), keyword)
        for profession in professions:
            print(profession['profession'])
            print(profession['requirement'])
            print(f"{profession['salary_min']} {profession['salary_max']} {profession['currency']}")
            print(f"Ссылка: {profession['url']}")

    elif hh_or_sj == "2":
        professions = handler.get_sorted_vacancies_sj(top, int(salary_min), keyword)
        for profession in professions:
            print(f"Профессия: {profession['profession']}")
            print(f"Требования {profession['requirement']}")
            print(f"{profession['salary_min']} {profession['salary_max']} {profession['currency']}")
            print(f"Ссылка: {profession['url']}")


if __name__ == "__main__":
    main()
