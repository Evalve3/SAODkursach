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


def main():
    search_func = InSearch
    tree = AvlTree
    hash_table = HashTableLine
    lst = List
    client_repo = ClientRepo(tree=tree(), search_in_text=search_func())
    sim_repo = SimRepo(hash_table=hash_table(1000))
    sim_issue_refund_repo = SimClientIssueRefundRepo(lst=lst())
    sim_cleint_presenter = SimByClientfPresenter()
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
        print("9. Просмотр всех имеющихся SIM-карт")
        print("10. Очистка данных о SIM-картах")
        print("11. Поиск SIM-карты по номеру SIM-карты")
        print("12. Поиск SIM-карты по тарифу")
        print("13. Регистрация выдачи клиенту SIM-карты")
        print("14. Регистрация возврата SIM-карты от клиента")
        print("0. Выйти из программы")

        choice = input("Введите номер выбранного действия: ")

        if choice == "1":
            # вызов функции регистрации нового клиента
            usecase = RegisterNewClientUC(client_repo=client_repo)
            try:
                client = Client.input_client()
            except Exception as e:
                print(e)
                continue
            usecase.execute(client)
        elif choice == "2":
            # вызов функции снятия с обслуживания клиента
            usecase = RemoveClientUC(client_repo=client_repo, sim_client_repo=sim_issue_refund_repo, sim_repo=sim_repo)
            try:
                client = Client.input_client()
            except Exception as e:
                print(e.__traceback__)
                continue
            usecase.execute(client)
        elif choice == "3":
            # вызов функции просмотра всех зарегистрированных клиентов
            usecase = GetAllClientsUC(client_repo=client_repo)
            print(usecase.execute())
        elif choice == "4":
            # вызов функции очистки данных о клиентах
            usecase = RemoveAllClientsUC(client_repo=client_repo)
            usecase.execute()
        elif choice == "5":
            # вызов функции поиска клиента по номеру паспорта
            usecase = FindByPassportUC(client_repo=client_repo)
            passport_number = input("Введите номер паспорта: ")
            print(usecase.execute(passport_number))
        elif choice == "6":
            # вызов функции поиска клиента по фрагментам ФИО или адреса
            usecase = FindByTextUC(client_repo=client_repo)
            text = input("Введите фрагмент ФИО или адреса: ")
            print(usecase.execute(text))
        elif choice == "7":
            # вызов функции добавления новой SIM-карты
            usecase = AddNewSimUC(sim_repo=sim_repo)
            try:
                sim = Sim.input_sim()
            except Exception as e:
                print(e)
                continue
            usecase.execute(sim)
        elif choice == "8":
            # вызов функции удаления сведений о SIM-карте
            usecase = RemoveSimUC(sim_repo=sim_repo, sim_client_repo=sim_issue_refund_repo)
            try:
                sim = Sim.input_sim()
            except Exception as e:
                print(e)
                continue
            if usecase.execute(sim):
                print("SIM-карта успешно удалена")
            else:
                print("SIM-карта кому-то принадлежит")
        elif choice == "9":
            # вызов функции просмотра всех имеющихся SIM-карт
            usecase = GetAllSimUC(sim_repo=sim_repo)
            print(usecase.execute())
        elif choice == "10":
            # вызов функции очистки данных о SIM-картах
            usecase = RemoveAllSimUC(sim_repo=sim_repo)
            usecase.execute()
        elif choice == "11":
            # вызов функции поиска SIM-карты по номеру SIM-карты
            # sim_clients_repo: ClientSimsABC, client_repo: ClientRepoABC, presenter: PresenterABC
            usecase = ClientBySimNumber(sim_clients_repo=sim_issue_refund_repo, client_repo=client_repo,
                                        presenter=sim_cleint_presenter)
            sim_number = input("Введите номер SIM-карты: ")
            print(usecase.execute(sim_number))
        elif choice == "12":
            # вызов функции поиска SIM-карты по тарифу
            usecase = FindSimByTariffUC(sim_repo=sim_repo, presenter=sim_tariff_presenter)
            tariff = input("Введите тариф: ")
            print(usecase.execute(tariff))
        elif choice == "13":
            # вызов функции регистрации выдачи клиенту SIM-карты
            pass
        elif choice == "14":
            # вызов функции регистрации возврата SIM-карты от клиента
            pass
        elif choice == "0":
            # выход из программы
            print("Выход из программы")
            break


if __name__ == "__main__":
    main()
