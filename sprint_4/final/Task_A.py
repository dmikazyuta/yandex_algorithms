"""
ID: 68339306

Шаги для решения задачи:

** РАБОТАЕМ С ДОКУМЕНТАМИ **
1. Инициируем лист для хранения баллов релевантности и документов request_list.
Понадобится на последнем этапе
[ [КОЛ-ВО СОВПАДЕНИЙ СЛОВ НА ДОКУМЕНТ, -1 * ИД ДОКУМЕНТА], .. ]
-1 для сортировки в конце
2. Заполним вспомогательный справочник слов документов
{ СЛОВО: {ДОК ИД: КОЛ-ВО ИСПОЛЬЗОВАНИЙ} }

** ОБРАБОТКА ЗАПРОСА **
1. Построчно обрабатываем запросы
Если запрос не первый возвращаем в дефольтное состояние request_list
2. Идем от слова к слову в строке запроса.
Собираем слова в справочник уникальности, чтобы не искать повторно уже обработанное
3. Для новых слов запускаем обращение к справочнику слов документов.
Если нашлось, то забираем общее кол-во совпадений слов и добавляем плюсом к ранее сохраненным в лист релевантности
4. Сортируем лист релевантности обратным порядком
5. Вывод на печать

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

* Подготовка справочника документов:
O(n * k)
n - кол-во документов
k - кол-во уникальных слов

* Обработка запроса
O(m * k + nlogn + n)
m - кол-во документов
k - кол-во уникальных слов
n log n - сортировка массива релевантности python дефолтным алгоритмом tim-sort

* ИТОГО
O(n * k + m * k + nlogn)


-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

* Подготовка справочника документов:
O(n * k)
n - кол-во документов
k - кол-во уникальных слов

* Обработка запроса
O(n) - для листа релевантности
n - кол-во документов

* ИТОГО:
O(n * k + n)

"""


def search_system():
    class SearchEngine:
        def __init__(self):
            self.doc_dict = {}
            self.request_list = []

        """
        Функция для сброса списка баллов релевантности
        """
        def set_request_list_default(self, request_list: list):
            for l in range(0, len(request_list)):
                request_list[l] = [0, -1 * (l + 1)]

        """
        Функция для заполнения справочника документов
        """
        def populate(self, in_doc_str: str, doc_id: int):
            # Инициируем список баллов релевантности и ид документов
            # -1 на ид документа для корректной сортировки в конце
            self.request_list.append([0, -1 * doc_id])

            # Готовим справочник { СЛОВО: [ДОК ИД: КОЛ-ВО ИСПОЛЬЗОВАНИЙ] }
            doc_list = in_doc_str.split()
            for d_idx in range(0, len(doc_list)):
                d_word = doc_list[d_idx]
                doc_dict_val = self.doc_dict.get(d_word, 0)
                # Если слово нашлось добавляем к количеству + 1
                if bool(doc_dict_val):
                    doc_dict_val[doc_id] = doc_dict_val.get(doc_id, 0) + 1
                else:
                    self.doc_dict[d_word] = {doc_id: 1}

        """
        Функция подготовки результатов запроса
        """
        def process_request(self, in_req_str, m):
            # Сбрасываем лист релевантности на изначальное состояние
            if m > 0:
                self.set_request_list_default(self.request_list)

            req_list = in_req_str.split()
            # Справочник для хранения уникальных слов
            req_unq_word_dict = {}

            # Итеративно идем по словам запроса
            for req_idx in range(0, len(req_list)):
                req_word = req_list[req_idx]

                # Заполняем справочник уникальных слов
                # Если слово уже есть в справочнике его можно пропустить
                if req_word not in req_unq_word_dict:
                    req_unq_word_dict[req_word] = None

                    # Механизм подсчета баллов релевантности
                    # Идем в справочник документов за словом
                    req_word_dict = self.doc_dict.get(req_word, None)
                    # Если слово нашлось
                    if req_word_dict is not None:
                        # Пробегаем по всем документам, общее кол-во баллов на документ суммируем
                        for req_word_docid in req_word_dict:
                            request_rel_grade = self.request_list[req_word_docid - 1][0] + req_word_dict[req_word_docid]
                            # Сохраняем в лист релевантности
                            self.request_list[req_word_docid - 1][0] = request_rel_grade
                else:
                    pass

            # Сортируем по убыванию релевантности
            self.request_list.sort(reverse=True)

    s_engine = SearchEngine()

    # Вызов механизма работы с документами
    n = int(input())
    for d in range(1, n + 1):
        doc_str = input()

        s_engine.populate(doc_str, d)

    # Вызов механизма работы с запросами
    m = int(input())
    for rq in range(0, m):
        req_str = input()

        s_engine.process_request(req_str, m)

        # Собираем результат для вывода
        result_list = []
        # Первые 5 значений
        for i in range(0, len(s_engine.request_list[:5])):
            rel_result = s_engine.request_list[i][0]
            if rel_result > 0:
                # -1, чтобы вернуть оригинальный вид ид документа
                result_list.append(-1 * s_engine.request_list[i][1])
        print(*result_list)


if __name__ == "__main__":
    search_system()
