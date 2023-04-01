from src.core.repo.search_in_text.search_text_repo import SearchInTextABC


class InSearch(SearchInTextABC):
    def search(self, text, pattern) -> bool:
        """
           Есть ли строка в тексте
        """
        n = len(text)
        m = len(pattern)

        for i in range(n - m + 1):
            if text[i:i + m] == pattern:
                return True

        return False
