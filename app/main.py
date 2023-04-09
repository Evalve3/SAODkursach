from src.core.dto.client_dto import Client
from src.core.dto.sim_dto import Sim
from src.data.algorithms.search_in_text.in_search import InSearch
from src.data.client_repo.client_repo import ClientRepo
from src.data.data_structures.hash_table.hash_table_line import HashTableLine
from src.data.data_structures.my_list.cycled_list import List
from src.data.data_structures.tree.AVL import AvlTree
from src.data.sim_clients_repo.sim_clients_repo import SimClientIssueRefundRepo
from src.data.sim_repo.sim_repo import SimRepo
from src.data.usecase.client.find_by_passport import FindByPassportUC
from src.data.usecase.client.find_client_by_text import FindByTextUC
from src.data.usecase.client.get_all_clients import GetAllClientsUC
from src.data.usecase.client.new_client import RegisterNewClientUC
from src.data.usecase.client.remo_all_clients import RemoveAllClientsUC
from src.data.usecase.client.remove_client import RemoveClientUC
from src.data.usecase.sim.add_new_sim import AddNewSimUC
from src.data.usecase.sim.find_by_tariff import FindSimByTariffUC
from src.data.usecase.sim.get_all_sims import GetAllSimUC
from src.data.usecase.sim.presenters.sim_by_tariff_presenter import SimByTariffPresenter
from src.data.usecase.sim.remove_all_sim import RemoveAllSimUC
from src.data.usecase.sim.remove_sim import RemoveSimUC
from src.data.usecase.sim_clients.client_by_sim_number import ClientBySimNumber
from src.data.usecase.sim_clients.presenters.client_by_sim_numer import SimByClientfPresenter
from src.data.usecase.sim_clients.register_sim import RegisterSimNumber
from src.data.usecase.sim_clients.regitster_sim_return import RegisterSimReturnNumber


def add_test_data(client_repo: ClientRepo, sim_repo: SimRepo, sim_client_repo: SimClientIssueRefundRepo):
    client1 = Client('1234-567890', 'Moscow, 01.01.2020', 'John Smith', 1985, 'Moscow, 01.01.2020')
    client2 = Client('9876-543210', 'Saint Petersburg, 01.01.2020', 'Jane Doe', 1990, 'Saint Petersburg, 01.01.2020')
    sim1 = Sim('123-4567890', 'Tariff 1', 2000, False)
    sim2 = Sim('098-7654321', 'Tariff 2', 2000, False)
    sim3 = Sim('123-4567891', 'Tariff 1', 2000, False)
    sim4 = Sim('098-7654322', 'Tariff 2', 2000, False)
    sim_repo.add(sim1)
    sim_repo.add(sim2)
    sim_repo.add(sim3)
    sim_repo.add(sim4)
    client_repo.add(client1)
    client_repo.add(client2)
    sim_client_repo.register_sim_number(client1, sim1, date_end='12.12.2030')
    sim_client_repo.register_sim_number(client1, sim2, date_end='12.12.2030')
    sim_client_repo.register_sim_number(client2, sim3, date_end='12.12.2030')
    sim_client_repo.register_sim_number(client2, sim4, date_end='12.12.2030')


def main():
    search_func = InSearch
    tree = AvlTree
    hash_table = HashTableLine
    lst = List
    client_repo = ClientRepo(tree=tree(), search_in_text=search_func())
    sim_repo = SimRepo(hash_table=hash_table(1000))
    sim_issue_refund_repo = SimClientIssueRefundRepo(lst=lst())
    sim_client_presenter = SimByClientfPresenter()
    sim_tariff_presenter = SimByTariffPresenter()
    while True:
        print("Выберите действие:")
        print("1. Регистрация нового клиента")
        print("2. Снятие с обслуживания клиента")
        print("3. Просмотр всех зарегистрированных клиентов")
        print("4. Очистка данных о клиентах")
        print("5. Поиск клиента по номеру паспорта")
        print("6. Поиск клиента по фрагментам ФИО или адреса")
        print("7. Добавление новой SIM-карты")
        print("8. Удаление сведений о SIM-карте")
        print("9. Просмотр всех SIM-карт")
        print("10. Очистка данных о SIM-картах")
        print("11. Поиск SIM-карты по номеру SIM-карты")
        print("12. Поиск SIM-карты по тарифу")
        print("13. Регистрация выдачи клиенту SIM-карты")
        print("14. Регистрация возврата SIM-карты от клиента")
        print("15. Напихать тестовых данных")
        print("0. Выйти из программы")

        choice = input("Введите номер выбранного действия: ")
        match choice:
            case "1":
                # вызов функции регистрации нового клиента
                use_case = RegisterNewClientUC(client_repo=client_repo)
                try:
                    client = Client.input_client()
                    use_case.execute(client)
                    print("Клиент успешно зарегистрирован")
                except Exception as e:
                    print(e)
                    continue
            case "2":
                # вызов функции снятия с обслуживания клиента
                use_case = RemoveClientUC(client_repo=client_repo, sim_client_repo=sim_issue_refund_repo,
                                          sim_repo=sim_repo)
                try:
                    client = Client.input_client()
                    use_case.execute(client)
                    print("Клиент успешно снят с обслуживания")
                except Exception as e:
                    print(e)
                    continue
            case "3":
                # вызов функции просмотра всех зарегистрированных клиентов
                use_case = GetAllClientsUC(client_repo=client_repo)
                print(*use_case.execute(), sep='\n')
            case "4":
                # вызов функции очистки данных о клиентах
                use_case = RemoveAllClientsUC(client_repo=client_repo, client_sims_repo=sim_issue_refund_repo,
                                              sim_repo=sim_repo)
                use_case.execute()
                print("Данные о клиентах успешно очищены")
            case "5":
                # вызов функции поиска клиента по номеру паспорта
                use_case = FindByPassportUC(client_repo=client_repo)
                passport_number = input("Введите номер паспорта: ")
                try:
                    result = use_case.execute(passport_number)
                    print(result, sep='\n')
                except Exception as e:
                    print(e)
                    continue
            case "6":
                # вызов функции поиска клиента по фрагментам ФИО или адреса
                use_case = FindByTextUC(client_repo=client_repo)
                text = input("Введите фрагмент ФИО или адреса: ")
                result = use_case.execute(text)
                if result:
                    print(*result, sep='\n')
                else:
                    print("Клиент с такими данными не найден")
            case "7":
                # вызов функции добавления новой SIM-карты
                use_case = AddNewSimUC(sim_repo=sim_repo)
                try:
                    sim = Sim.input_sim()
                    use_case.execute(sim)
                    print("SIM-карта успешно добавлена")
                except Exception as e:
                    print(e)
                    continue
            case "8":
                # вызов функции удаления сведений о SIM-карте
                use_case = RemoveSimUC(sim_repo=sim_repo, sim_client_repo=sim_issue_refund_repo)
                try:
                    sim = Sim.input_sim()
                except Exception as e:
                    print(e)
                    continue
                if use_case.execute(sim):
                    print("SIM-карта успешно удалена")
                else:
                    print("SIM-карта кому-то принадлежит")
            case "9":
                # вызов функции просмотра всех имеющихся SIM-карт
                use_case = GetAllSimUC(sim_repo=sim_repo)
                print(*use_case.execute(), sep='\n')
            case "10":
                # вызов функции очистки данных о SIM-картах
                use_case = RemoveAllSimUC(sim_repo=sim_repo, sim_client_repo=sim_issue_refund_repo)
                use_case.execute()
            case "11":
                # вызов функции поиска SIM-карты по номеру SIM-карты
                use_case = ClientBySimNumber(sim_clients_repo=sim_issue_refund_repo, client_repo=client_repo,
                                             presenter=sim_client_presenter, sim_repo=sim_repo)
                sim_number = input("Введите номер SIM-карты: ")
                try:
                    print(use_case.execute(sim_number))
                except Exception as e:
                    print(e)
            case "12":
                # вызов функции поиска SIM-карты по тарифу
                use_case = FindSimByTariffUC(sim_repo=sim_repo, presenter=sim_tariff_presenter)
                tariff = input("Введите тариф: ")
                print(*use_case.execute(tariff), sep='\n')
            case "13":
                # вызов функции регистрации выдачи клиенту SIM-карты
                use_case = RegisterSimNumber(sim_clients_repo=sim_issue_refund_repo, sim_repo=sim_repo,
                                             client_repo=client_repo)
                uc_result = use_case.execute(client=Client.input_client(),
                                             sim=Sim.input_sim(),
                                             date_end=input("Введите дату окончания действия SIM-карты: "))
                if not uc_result:
                    print("Сим карта уже выдана какому-то клиенту или не существует")
            case "14":
                # вызов функции регистрации возврата SIM-карты от клиента
                use_case = RegisterSimReturnNumber(sim_clients_repo=sim_issue_refund_repo, sim_repo=sim_repo)
                try:
                    use_case.execute(sim=Sim.input_sim())
                    print("Сим карта успешно возвращена")
                except Exception:
                    print("Сим карта принадлежит никому или не существует")
            case "15":
                # напихать тестовых данных
                try:
                    add_test_data(client_repo=client_repo, sim_repo=sim_repo, sim_client_repo=sim_issue_refund_repo)
                except Exception:
                    print("Тестовые данные уже добавлены")
            case "0":
                # выход из программы
                print("Выход из программы")
                break


if __name__ == "__main__":
    main()
